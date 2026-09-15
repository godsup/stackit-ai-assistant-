from __future__ import annotations

from pathlib import Path
from typing import Any

import chromadb
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent
CHROMA_DIR = BASE_DIR.parent / "chroma_db"
COLLECTION_NAME = "stackit_docs"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


def connect_db(
    chroma_dir: Path = CHROMA_DIR,
) -> tuple[Any, SentenceTransformer]:
    """Connect to the persisted collection and load its embedding model."""
    client = chromadb.PersistentClient(path=str(chroma_dir))
    collection = client.get_collection(name=COLLECTION_NAME)
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return collection, model


def search_documents(
    collection: Any,
    model: SentenceTransformer,
    question: str,
    n_results: int = 3,
) -> dict[str, Any]:
    """Embed a question and return the nearest document chunks."""
    question = question.strip()
    if not question:
        raise ValueError("Question cannot be empty")

    question_embedding = model.encode(question, show_progress_bar=False).tolist()
    return collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )


def display_results(results: dict[str, Any]) -> None:
    """Print ranked chunks, source metadata, and distance-based scores."""
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    if not documents:
        print("No matching documents found.")
        return

    for rank, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances), start=1
    ):
        relevance = 1 / (1 + distance)
        source = metadata.get("source_filename", "Unknown source")
        print(f"\nRank: {rank}")
        print(f"Source document: {source}")
        print(f"Distance: {distance:.6f}")
        print(f"Relevance score: {relevance:.6f}")
        print("Chunk content:")
        print(document)


if __name__ == "__main__":
    user_question = input("Ask a question: ")
    collection, embedding_model = connect_db()
    search_results = search_documents(collection, embedding_model, user_question)
    display_results(search_results)
