from sentence_transformers import (
    CrossEncoder
)


class CrossEncoderReranker:

    def __init__(self):

        print(
            "\n🚀 Loading reranker model...\n"
        )

        self.model = CrossEncoder(
            "BAAI/bge-reranker-base"
        )

        print(
            "✅ Reranker model loaded"
        )

    # =====================================
    # Rerank Results
    # =====================================

    def rerank(

        self,

        query,

        retrieval_results,

        top_k=5
    ):

        # =====================================
        # Empty Protection
        # =====================================

        if len(retrieval_results) == 0:

            return []

        # =====================================
        # Query-Document Pairs
        # =====================================

        sentence_pairs = []

        for result in retrieval_results:

            sentence_pairs.append([

                query,

                result["content"]
            ])

        # =====================================
        # Predict Relevance Scores
        # =====================================

        scores = self.model.predict(
            sentence_pairs
        )

        # =====================================
        # Attach Scores
        # =====================================

        reranked_results = []

        for result, score in zip(

            retrieval_results,

            scores
        ):

            result["rerank_score"] = (
                round(float(score), 4)
            )

            reranked_results.append(
                result
            )

        # =====================================
        # Sort By Rerank Score
        # =====================================

        reranked_results.sort(

            key=lambda x: (
                x["rerank_score"]
            ),

            reverse=True
        )

        return reranked_results[:top_k]