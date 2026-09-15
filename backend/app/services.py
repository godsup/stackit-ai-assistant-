"""Application services for the StackIT documentation assistant."""

from typing import TypedDict

from chat import build_context, generate_answer, retrieve_documents


class AnswerResult(TypedDict):
    """Structured result returned by the question-answering service."""

    answer: str
    sources: list[str]


def answer_question(question: str) -> AnswerResult:
    """Retrieve documentation and generate an answer using the existing RAG flow."""
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be empty")

    results = retrieve_documents(question)
    context, sources = build_context(results)
    answer = generate_answer(question, context)
    return {"answer": answer, "sources": sources}