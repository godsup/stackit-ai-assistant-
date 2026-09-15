import chromadb

client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_collection("stackit_docs")

print(f"Documents stored: {collection.count()}")

results = collection.peek(limit=3)

print(results)