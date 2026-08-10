from pathlib import Path

def load_documents(directory: str) -> list[dict]:
    documents = []

    for path in Path(directory).glob("*.md"):
        content = path.read_text(encoding="utf-8")

        documents.append(
            {
                "source": path.name,
                "content": content,
            }
        )

    return documents
