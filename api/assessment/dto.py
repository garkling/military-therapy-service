from pydantic import BaseModel
from pydantic import Field


class TestQuestionRead(BaseModel):
    id: int
    content: str


class TestRead(BaseModel):
    id: str
    questions: list[TestQuestionRead]


class TestQuestionResult(BaseModel):
    id: int
    answer: int = Field(ge=1, le=5)
