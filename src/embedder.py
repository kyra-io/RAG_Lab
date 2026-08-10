from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(texts)

        return embeddings.tolist()
