from api.assessment.dto import TestQuestionResult
from api.assessment.models import AssessmentTest
from api.assessment.utils import load_entry_test


class TestEvaluationService:

    def __init__(self):
        self.test: AssessmentTest = load_entry_test()

    def run(self, results: list[TestQuestionResult]):
        total_score = sum(r.answer for r in results)
        score_range = self.test.get_score_range(total_score)
        codes = set(self.test.gradation[score_range])

        for r in results:
            if r.answer >= 4:
                question = self.test.get_question_by_id(r.id)
                codes.update(question.codes)

        return list(codes)
