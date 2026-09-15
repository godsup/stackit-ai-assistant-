from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR.parent / "docs"
CHROMA_DIR = BASE_DIR.parent / "chroma_db"
COLLECTION_NAME = "stackit_docs"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


@dataclass(frozen=True)
class Document:
    """Markdown document and the metadata needed for its chunks."""

    content: str
    source_filename: str
    file_path: str


@dataclass(frozen=True)
class DocumentChunk:
    """Text chunk with metadata inherited from its source document."""

    text: str
    source_filename: str
    file_path: str
    chunk_index: int


def load_documents(docs_dir: Path = DOCS_DIR) -> list[Document]:
    """Load every Markdown file below ``docs_dir`` recursively."""
    documents: list[Document] = []

    for file_path in sorted(docs_dir.rglob("*.md")):
        if not file_path.is_file():
            continue

        print(f"Loading {file_path.name}")
        documents.append(
            Document(
                content=file_path.read_text(encoding="utf-8"),
                source_filename=file_path.name,
                file_path=str(file_path.resolve()),
            )
        )

    return documents


def chunk_documents(documents: Sequence[Document]) -> list[DocumentChunk]:
    """Split documents into overlapping chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks: list[DocumentChunk] = []

    for document in documents:
        document_chunks = splitter.split_text(document.content)
        print(f"Created {len(document_chunks)} chunks")
        chunks.extend(
            DocumentChunk(
                text=text,
                source_filename=document.source_filename,
                file_path=document.file_path,
                chunk_index=index,
            )
            for index, text in enumerate(document_chunks)
        )

    return chunks


def generate_embeddings(
    chunks: Sequence[DocumentChunk],
    model_name: str = EMBEDDING_MODEL_NAME,
) -> list[list[float]]:
    """Generate one Sentence Transformers embedding for each chunk."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode([chunk.text for chunk in chunks], show_progress_bar=False)
    return embeddings.tolist()


def store_embeddings(
    chunks: Sequence[DocumentChunk],
    embeddings: Sequence[Sequence[float]],
    chroma_dir: Path = CHROMA_DIR,
) -> None:
    """Persist chunks, embeddings, and source metadata in ChromaDB."""
    if len(chunks) != len(embeddings):
        raise ValueError("The number of chunks must match the number of embeddings")

    client = chromadb.PersistentClient(path=str(chroma_dir))
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    grouped_chunks: dict[str, list[tuple[DocumentChunk, Sequence[float]]]] = {}
    for chunk, embedding in zip(chunks, embeddings):
        grouped_chunks.setdefault(chunk.source_filename, []).append((chunk, embedding))

    for source_filename, source_chunks in grouped_chunks.items():
        collection.upsert(
            ids=[f"{chunk.file_path}:{chunk.chunk_index}" for chunk, _ in source_chunks],
            documents=[chunk.text for chunk, _ in source_chunks],
            embeddings=[list(embedding) for _, embedding in source_chunks],
            metadatas=[
                {
                    "source_filename": chunk.source_filename,
                    "file_path": chunk.file_path,
                }
                for chunk, _ in source_chunks
            ],
        )
        print(f"Stored {len(source_chunks)} embeddings")


def main() -> None:
    """Run the document ingestion pipeline."""
    documents = load_documents()
    if not documents:
        raise ValueError(f"No Markdown files found in: {DOCS_DIR}")

    chunks = chunk_documents(documents)
    embeddings = generate_embeddings(chunks)
    store_embeddings(chunks, embeddings)


if __name__ == "__main__":
    main()
