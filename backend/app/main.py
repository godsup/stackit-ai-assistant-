"""FastAPI application for the StackIT documentation assistant."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import ChatRequest, ChatResponse
from app.services import answer_question


app = FastAPI(
    title="STACKIT Documentation Assistant",
    description="RAG-powered answers from STACKIT documentation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    """Report whether the API process is running."""
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Answer a question using the persisted documentation index."""
    try:
        result = answer_question(request.question)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unable to generate an answer",
        ) from exc

    return ChatResponse(**result)