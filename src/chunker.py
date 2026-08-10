def chunk_text(
    text: str,
    source: str,
    chunk_size: int = 100,
) -> list[dict]:
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])

        chunks.append(
            {
                "content": chunk,
                "source": source,
                "chunk_id": len(chunks),
            }
        )

    return chunks
