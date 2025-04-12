from pydantic import BaseModel, model_validator, field_validator, ConfigDict
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field

from api.base.model import Base


class AssessmentTestResults(Base, table=True):
    __tablename__ = "assessment_test_results"
    test_id: str = Field(primary_key=True)
    military_id: str = Field(foreign_key="military.id", primary_key=True)
    answers: dict = Field(sa_type=JSONB, nullable=False)
    score: float


class TestQuestion(BaseModel):
    id: int
    question: str
    codes: list[int]


class AssessmentTest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: str
    questions: list[TestQuestion]
    gradation: dict[range, list[int]]

    @field_validator('gradation', mode='before')
    def validate_gradation(cls, gradation: dict[str, str], values):
        gradation = {
            range(*map(int, range_.split("-"))): scores
            for range_, scores in gradation.items()
        }

        return gradation

    def get_question_by_id(self, q_id: int):
        for question in self.questions:
            if question.id == q_id:
                return question

    def get_score_range(self, score: int):
        for range_ in self.gradation:
            if score in range_:
                return range_
