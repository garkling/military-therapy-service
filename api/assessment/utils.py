import json

from api.assessment.models import AssessmentTest


def load_entry_test(path: str = "entry_test.json") -> AssessmentTest:
    with open(path) as f:
        return AssessmentTest.model_validate(json.load(f))
