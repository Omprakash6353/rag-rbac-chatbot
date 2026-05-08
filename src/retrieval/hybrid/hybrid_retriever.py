from src.retrieval.retriever import (
    Retriever
)

from src.retrieval.hybrid.bm25_retriever import (
    BM25Retriever
)

from src.retrieval.hybrid.rrf_fusion import (
    RRFFusion
)


class HybridRetriever:

    def __init__(self):

        self.semantic_retriever = (
            Retriever()
        )

        self.bm25_retriever = (
            BM25Retriever()
        )

        self.rrf_fusion = (
            RRFFusion()
        )

    # =====================================
    # Hybrid Retrieval
    # =====================================

    def retrieve(

        self,

        query,

        filters=None
    ):

        # =====================================
        # Semantic Retrieval
        # =====================================

        semantic_results = (

            self.semantic_retriever
            .retrieve(

                query=query,

                filters=filters
            )
        )

        # =====================================
        # BM25 Retrieval
        # =====================================

        bm25_results = (

            self.bm25_retriever
            .retrieve(

                query=query,

                filters=filters
            )
        )

        # =====================================
        # RRF Fusion
        # =====================================

        fused_results = (

            self.rrf_fusion
            .fuse(

                semantic_results,

                bm25_results
            )
        )

        return fused_results