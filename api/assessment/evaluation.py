from typing import Annotated

from fastapi import Depends

from api.assessment.dto import TestQuestionResult
from api.assessment.errors import InvalidTestResult
from api.assessment.models import AssessmentTest
from api.assessment.models import TestAssessmentResult
from api.assessment.repository import TestAssessmentRepository
from api.assessment.utils import load_entry_test


class TestEvaluationService:

    def __init__(
        self,
        assessment_repo: Annotated[TestAssessmentRepository, Depends()]
    ):
        self._assessment_repo = assessment_repo
        self.test: AssessmentTest = load_entry_test()

    def run(self, results: list[TestQuestionResult]) -> tuple[int, list[int]]:
        self.validate_results(results)

        total_score = sum(r.answer for r in results)
        score_range = self.test.get_score_range(total_score)
        codes = self.test.gradation[score_range]

        for r in results:
            if r.answer >= 4:
                question = self.test.get_question_by_id(r.id)
                codes.extend(question.codes)

        return total_score, codes

    def save_results(self, military_id: str, total_score: int, expertise_codes: list[int], results: list[TestQuestionResult]) -> TestAssessmentResult:
        if db_result := self.get_results(military_id):
            self._assessment_repo.delete(db_result)

        db_result = TestAssessmentResult(
            test_id=self.test.id,
            military_id=military_id,
            answers=[r.model_dump(mode='json') for r in results],
            expertise_codes=expertise_codes,
            score=total_score,
        )
        saved = self._assessment_repo.create(db_result)
        return saved

    def get_results(self, military_id: str) -> TestAssessmentResult:
        test_result = self._assessment_repo.get((self.test.id, military_id))
        return test_result

    def validate_results(self, results: list[TestQuestionResult]):
        unique_questions = set(r.id for r in results)
        if len(unique_questions) != len(results):
            raise InvalidTestResult()

        if not unique_questions.issubset(q.id for q in self.test.questions):
            raise InvalidTestResult()
