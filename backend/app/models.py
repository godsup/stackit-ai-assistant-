"""Request and response models for the StackIT documentation API."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Payload accepted by the chat endpoint."""

    question: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    """Answer and source documents returned by the chat endpoint."""

    answer: str
    sources: list[str]