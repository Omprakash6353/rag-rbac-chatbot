from rank_bm25 import BM25Okapi

from src.vectorstore.chroma_store import (
    ChromaVectorStore
)

from src.config.settings import (
    RetrievalConfig
)


class BM25Retriever:

    def __init__(self):

        self.vector_store = (
            ChromaVectorStore()
        )

        self.top_k = (
            RetrievalConfig.TOP_K
        )

        # =====================================
        # Load Collection
        # =====================================

        collection_data = (

            self.vector_store
            .collection
            .get()
        )

        self.documents = (
            collection_data["documents"]
        )

        self.metadatas = (
            collection_data["metadatas"]
        )

        print(

            f"✅ BM25 initialized with "

            f"{len(self.documents)} documents"
        )

    # =====================================
    # Metadata Filter Matching
    # =====================================

    def matches_filters(

        self,

        metadata,

        filters
    ):

        if filters is None:

            return True

        # =====================================
        # AND Filters
        # =====================================

        if "$and" in filters:

            for condition in (
                filters["$and"]
            ):

                for key, value in (
                    condition.items()
                ):

                    if metadata.get(key) != value:

                        return False

            return True

        # =====================================
        # Single Filter
        # =====================================

        for key, value in (
            filters.items()
        ):

            if metadata.get(key) != value:

                return False

        return True

    # =====================================
    # BM25 Retrieval
    # =====================================

    def retrieve(

        self,

        query,

        filters=None
    ):

        filtered_documents = []

        filtered_metadatas = []

        # =====================================
        # Apply Metadata Filters
        # =====================================

        for doc, metadata in zip(

            self.documents,

            self.metadatas
        ):

            if self.matches_filters(

                metadata,

                filters
            ):

                filtered_documents.append(doc)

                filtered_metadatas.append(
                    metadata
                )

        # =====================================
        # Empty Result Protection
        # =====================================

        if len(filtered_documents) == 0:

            return []

        # =====================================
        # Build BM25 Index
        # =====================================

        tokenized_documents = [

            document.lower().split()

            for document in (
                filtered_documents
            )
        ]

        bm25 = BM25Okapi(
            tokenized_documents
        )

        tokenized_query = (
            query.lower().split()
        )

        scores = bm25.get_scores(
            tokenized_query
        )

        scored_results = list(

            zip(

                filtered_documents,

                filtered_metadatas,

                scores
            )
        )

        # =====================================
        # Sort By Score
        # =====================================

        scored_results.sort(

            key=lambda x: x[2],

            reverse=True
        )

        top_results = scored_results[
            :self.top_k
        ]

        formatted_results = []

        # =====================================
        # Format Results
        # =====================================

        for doc, metadata, score in (
            top_results
        ):

            formatted_results.append({

                "content": doc,

                "metadata": metadata,

                "confidence": round(
                    float(score),
                    4
                ),

                "retriever": "bm25"
            })

        return formatted_results