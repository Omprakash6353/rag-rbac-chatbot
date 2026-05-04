from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    def __init__(self, model_name="BAAI/bge-base-en-v1.5"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        texts = [f"passage: {t}" for t in texts]
        return self.model.encode(texts, normalize_embeddings=True).tolist()

    def embed_query(self, query):
        query = f"query: {query}"
        return self.model.encode([query], normalize_embeddings=True)[0].tolist()