from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from starlette import status

from api.assessment.dto import TestQuestionRead
from api.assessment.dto import TestQuestionResult
from api.assessment.dto import TestRead
from api.assessment.evaluation import TestEvaluationService
from api.assessment.recommendation import TherapistRecommendationService
from api.auth.guards import APIGuard
from api.errors import ErrorHandlingRoute
from api.profiles.dto import TherapistProfileView
from api.user.models import User

router = APIRouter(prefix='/assessment', route_class=ErrorHandlingRoute)


class AssessmentController:

    def __init__(
        self,
        evaluation_service: Annotated[TestEvaluationService, Depends()],
        recommendation_service: Annotated[TherapistRecommendationService, Depends()],
    ):
        self._evaluation_service = evaluation_service
        self._recommendation_service = recommendation_service

    async def get_test(self) -> TestRead:
        return TestRead(
            id=self._evaluation_service.test.id,
            questions=[TestQuestionRead(id=q.id, content=q.question) for q in self._evaluation_service.test.questions],
        )

    async def submit_test(self, results: list[TestQuestionResult], user: User) -> list[TherapistProfileView]:
        expertises = await self.evaluate_results(results, user)
        return await self.build_recommendation(expertises)

    async def evaluate_results(self, results: list[TestQuestionResult], user: User) -> list[int]:
        score, therapist_expertises = self._evaluation_service.run(results)
        self._evaluation_service.save_results(user.id, score, therapist_expertises, results)

        return therapist_expertises

    async def build_recommendation(self, expertises: list[int]) -> list[TherapistProfileView]:
        therapists = self._recommendation_service.run(expertises)

        return [TherapistProfileView.model_validate(t) for t in therapists]

    async def get_recommendations(self, user: User) -> list[TherapistProfileView]:
        test_result = self._evaluation_service.get_results(user.id)
        return await self.build_recommendation(test_result.expertise_codes)


@router.get("", status_code=status.HTTP_200_OK, response_model=TestRead)
async def get_entry_test(
    controller: Annotated[AssessmentController, Depends()]
) -> TestRead:
    return await controller.get_test()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=list[TherapistProfileView])
async def submit_entry_test(
    result: list[TestQuestionResult],
    user: APIGuard,
    controller: Annotated[AssessmentController, Depends()]
) -> list[TherapistProfileView]:
    response = await controller.submit_test(result, user)
    return response


@router.get("/results", status_code=status.HTTP_200_OK, response_model=list[TherapistProfileView])
async def get_recommendations(
    user: APIGuard,
    controller: Annotated[AssessmentController, Depends()]
) -> list[TherapistProfileView]:
    response = await controller.get_recommendations(user)
    return response
