from pydantic import BaseModel, Field


class TestQuestionRead(BaseModel):
    id: int
    content: str


class TestQuestionResult(BaseModel):
    id: int
    answer: int = Field(ge=1, le=5)
