from src.embeddings.embedding_model import (
    EmbeddingModel
)

from src.vectorstore.chroma_store import (
    ChromaVectorStore
)

from src.config.settings import (
    RetrievalConfig
)


class Retriever:

    def __init__(self):

        self.embedding_model = (
            EmbeddingModel()
        )

        self.vector_store = (
            ChromaVectorStore()
        )

        self.top_k = (
            RetrievalConfig.TOP_K
        )

    # =====================================
    # Semantic Retrieval
    # =====================================

    def retrieve(
        self,
        query,
        filters=None
    ):

        # =========================
        # Query Embedding
        # =========================

        query_embedding = (
            self.embedding_model
            .embed_query(query)
        )

        # =========================
        # Vector Search
        # =========================

        results = (
            self.vector_store
            .similarity_search(

                query_embedding=query_embedding,

                top_k=self.top_k,

                filters=filters
            )
        )

        retrieved_results = []

        documents = results["documents"][0]

        metadatas = results["metadatas"][0]

        distances = results["distances"][0]

        # =========================
        # Result Formatting
        # =========================

        for doc, metadata, distance in zip(

            documents,

            metadatas,

            distances
        ):

            confidence = round(

                (1 - distance) * 100,

                2
            )

            retrieved_results.append({

                "content": doc,

                "metadata": metadata,

                "confidence": confidence
            })

        return retrieved_results