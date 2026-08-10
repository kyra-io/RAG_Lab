from loader import load_documents
from chunker import chunk_text
from embedder import Embedder
from indexer import insert_chunks

documents = load_documents("data/documents")

all_chunks = []

for document in documents:
    chunks = chunk_text(
        text=document["content"],
        source=document["source"],
        chunk_size=100,
    )

    all_chunks.extend(chunks)

print(f"Loaded {len(documents)} documents")
print(f"Created {len(all_chunks)} chunks")

embedder = Embedder()

texts = [chunk["content"] for chunk in all_chunks]

embeddings = embedder.embed(texts)

for chunk, embedding in zip(all_chunks, embeddings):
    chunk["embedding"] = embedding

inserted = insert_chunks(all_chunks)

print(f"Inserted {inserted} chunks")
