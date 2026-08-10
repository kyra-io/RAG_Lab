from embedder import Embedder
from retriever import search_chunks
from prompt import build_context, build_prompt
from llm import LLM


question = "Do I need to manage my database server?"


# ---------------------------------
# 1. EMBEDDING
# ---------------------------------

embedder = Embedder()

query_embedding = embedder.embed([question])[0]


# ---------------------------------
# 2. RETRIEVAL
# ---------------------------------

results = search_chunks(
    query_embedding=query_embedding,
    limit=5,
)


print("=" * 80)
print("QUESTION")
print("=" * 80)

print(question)


print("\n")
print("=" * 80)
print("RETRIEVED CHUNKS")
print("=" * 80)

for i, result in enumerate(results, start=1):
    print(
        f"\n#{i}"
        f" | distance={result['distance']:.4f}"
        f" | source={result['source']}"
        f" | chunk={result['chunk_id']}"
    )

    print(result["content"])


# ---------------------------------
# 3. CONTEXT
# ---------------------------------

context = build_context(results)


print("\n")
print("=" * 80)
print("CONTEXT")
print("=" * 80)

print(context)


# ---------------------------------
# 4. PROMPT
# ---------------------------------

prompt = build_prompt(
    question=question,
    context=context,
)


print("\n")
print("=" * 80)
print("PROMPT")
print("=" * 80)

print(prompt)


# ---------------------------------
# 5. LLM
# ---------------------------------

llm = LLM()

response = llm.generate(prompt)


print("\n")
print("=" * 80)
print("ANSWER")
print("=" * 80)

print(response["answer"])

print("\n")
print("=" * 80)
print("MODEL")
print("=" * 80)

print(response["model"])
