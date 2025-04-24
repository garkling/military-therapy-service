from typing import Annotated

from fastapi import Depends

from api.assessment.dto import TestQuestionResult
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
        total_score = sum(r.answer for r in results)
        score_range = self.test.get_score_range(total_score)
        codes = self.test.gradation[score_range]

        for r in results:
            if r.answer >= 4:
                question = self.test.get_question_by_id(r.id)
                codes.extend(question.codes)

        return total_score, codes

    def save_results(self, military_id: str, total_score: int, expertise_codes: list[int], results: list[TestQuestionResult]) -> TestAssessmentResult:
        db_result = TestAssessmentResult(
            test_id=self.test.id,
            military_id=military_id,
            answers=[r.model_dump(mode='json') for r in results],
            expertise_codes=expertise_codes,
            score=total_score,
        )
        saved = self._assessment_repo.create(db_result)
        return saved
