from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import field_validator
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field

from api.base.model import Base


class TestAssessmentResult(Base, table=True):
    __tablename__ = "assessment_test_results"
    test_id: str = Field(primary_key=True)
    military_id: str = Field(foreign_key="military.id", primary_key=True)
    answers: list[dict] = Field(sa_type=JSONB, nullable=False)
    expertise_codes: list[int] = Field(sa_type=JSONB, nullable=False)
    score: int


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
        return {
            range(*map(int, range_.split("-"))): scores
            for range_, scores in gradation.items()
        }

    def get_question_by_id(self, q_id: int):
        for question in self.questions:
            if question.id == q_id:
                return question

    def get_score_range(self, score: int):
        for range_ in self.gradation:
            if score in range_:
                return range_
