from __future__ import annotations

import os
from typing import Any

from openai import OpenAI
from dotenv import load_dotenv

from query import connect_db, search_documents


load_dotenv()

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")


def retrieve_documents(question: str) -> dict[str, Any]:
    """Retrieve the three most relevant chunks using query.py."""
    collection, embedding_model = connect_db()
    return search_documents(collection, embedding_model, question, n_results=3)


def build_context(results: dict[str, Any]) -> tuple[str, list[str]]:
    """Build the model context and collect the source filenames used."""
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    context = "\n\n---\n\n".join(documents)
    sources = list(
        dict.fromkeys(
            metadata.get("source_filename", "Unknown source")
            for metadata in metadatas
        )
    )
    return context, sources


def generate_answer(question: str, context: str) -> str:
    """Send the question and retrieved context to Gemini."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    prompt = f"""You are a documentation assistant.

Answer only using the provided documentation context.

If the answer is not contained in the context, respond:

I could not find sufficient information in the documentation.

Context:
{context}

Question:
{question}"""

    client = OpenAI(api_key=api_key, base_url=GEMINI_BASE_URL)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content
    if not answer:
        raise RuntimeError("The model returned an empty answer")
    return answer


def main() -> None:
    """Run the terminal RAG chatbot."""
    question = input("Ask a question: ").strip()
    if not question:
        raise ValueError("Question cannot be empty")

    results = retrieve_documents(question)
    context, sources = build_context(results)
    answer = generate_answer(question, context)

    print(f"\nGenerated answer:\n{answer}")
    print("\nSource documents used:")
    for source in sources:
        print(f"- {source}")


if __name__ == "__main__":
    main()
