from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from api.assessment.dto import TestQuestionRead
from api.assessment.dto import TestQuestionResult
from api.assessment.dto import TestRead
from api.assessment.evaluation import TestEvaluationService
from api.assessment.recommendation import TherapistRecommendationService
from api.auth.guards import APIGuard
from api.profiles.dto import TherapistProfileView
from api.user.models import User

router = APIRouter(prefix='/assessment')


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


@router.get("")
async def get_entry_test(
    controller: Annotated[AssessmentController, Depends()]
) -> TestRead:
    return await controller.get_test()


@router.post("")
async def submit_entry_test(
    result: list[TestQuestionResult],
    user: APIGuard,
    controller: Annotated[AssessmentController, Depends()]
):
    response = await controller.submit_test(result, user)
    return response
