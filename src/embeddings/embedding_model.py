from sentence_transformers import (
    SentenceTransformer
)

from src.config.settings import (
    EmbeddingConfig
)


class EmbeddingModel:

    def __init__(self):

        print(
            "\n🚀 Loading embedding model...\n"
        )

        self.model_name = (
            EmbeddingConfig.MODEL_NAME
        )

        self.query_prefix = (
            EmbeddingConfig.QUERY_PREFIX
        )

        self.passage_prefix = (
            EmbeddingConfig.PASSAGE_PREFIX
        )

        self.normalize_embeddings = (
            EmbeddingConfig.NORMALIZE_EMBEDDINGS
        )

        self.model = SentenceTransformer(
            self.model_name
        )

        print(
            f"✅ Embedding model loaded: "
            f"{self.model_name}"
        )

    # =====================================
    # Document Embeddings
    # =====================================

    def embed_documents(
        self,
        texts
    ):

        formatted_texts = [

            self.passage_prefix + text

            for text in texts
        ]

        embeddings = self.model.encode(

            formatted_texts,

            normalize_embeddings=(
                self.normalize_embeddings
            ),

            show_progress_bar=True
        )

        return embeddings.tolist()

    # =====================================
    # Query Embedding
    # =====================================

    def embed_query(
        self,
        query
    ):

        formatted_query = (
            self.query_prefix + query
        )

        embedding = self.model.encode(

            formatted_query,

            normalize_embeddings=(
                self.normalize_embeddings
            )
        )

        return embedding.tolist()