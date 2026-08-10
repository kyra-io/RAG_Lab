def build_context(results: list[dict]) -> str:
    sections = []

    for result in results:
        sections.append(
            f"[Source: {result['source']}]\n"
            f"{result['content']}"
        )

    return "\n\n".join(sections)

def build_prompt(
    question: str,
    context: str,
) -> str:
    return f"""
        You are a helpful assistant.

        Answer the question using only the information provided in the context.

        If the answer cannot be found in the context, say that you do not have enough information.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """.strip()
