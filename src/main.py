# from loader import load_documents
# from chunker import chunk_text


# documents = load_documents("data/documents")

# all_chunks = []

# for document in documents:
#     chunks = chunk_text(
#         text=document["content"],
#         source=document["source"],
#         chunk_size=100,
#     )

#     all_chunks.extend(chunks)


# print(f"Loaded {len(documents)} documents")
# print(f"Created {len(all_chunks)} chunks\n")

# for chunk in all_chunks:
#     print(f"--- {chunk['source']} | chunk {chunk['chunk_id']} ---")
#     print(chunk["content"])
#     print()

from embedder import Embedder
from retriever import cosine_similarity


embedder = Embedder()

query = "Do I need to manage my database server?"

texts = [
    "Acme Database is a managed PostgreSQL service.",
    "Customers do not need to manage database servers.",
    "Acme Cloud is headquartered in Lisbon.",
]

query_embedding = embedder.embed([query])[0]
text_embeddings = embedder.embed(texts)

for text, embedding in zip(texts, text_embeddings):
    similarity = cosine_similarity(
        query_embedding,
        embedding,
    )

    print(f"{similarity:.4f}  {text}")
