from src.retrieval.query_processor import (
    QueryProcessor
)

from src.retrieval.hybrid.hybrid_retriever import (
    HybridRetriever
)

from src.retrieval.reranker.cross_encoder_reranker import (
    CrossEncoderReranker
)


class RetrievalPipeline:

    def __init__(self):

        self.query_processor = (
            QueryProcessor()
        )

        self.retriever = (
            HybridRetriever()
        )

        self.reranker = (
            CrossEncoderReranker()
        )

    # =====================================
    # Search Pipeline
    # =====================================

    def search(

        self,

        query
    ):

        # =====================================
        # Query Understanding
        # =====================================

        filters = (

            self.query_processor
            .extract_filters(query)
        )

        # =====================================
        # Hybrid Retrieval
        # =====================================

        retrieval_results = (

            self.retriever
            .retrieve(

                query=query,

                filters=filters
            )
        )

        print(

            f"✅ Retrieved "

            f"{len(retrieval_results)} candidates"
        )

        # =====================================
        # Reranking
        # =====================================

        reranked_results = (

            self.reranker
            .rerank(

                query=query,

                retrieval_results=(
                    retrieval_results
                ),

                top_k=5
            )
        )

        print(
            "✅ Reranking completed"
        )

        return {

            "query": query,

            "filters": filters,

            "results": reranked_results
        }