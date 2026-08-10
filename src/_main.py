from embedder import Embedder
from retriever import search_chunks
from prompt import build_context, build_prompt


embedder = Embedder()

question = "Do I need to manage my database server?"

query_embedding = embedder.embed([question])[0]

results = search_chunks(
    query_embedding=query_embedding,
    limit=5,
)

context = build_context(results)

prompt = build_prompt(
    question=question,
    context=context,
)

print(prompt)
