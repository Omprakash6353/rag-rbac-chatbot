class RRFFusion:

    def __init__(
        self,
        k=60
    ):

        self.k = k

    # =====================================
    # Fuse Rankings
    # =====================================

    def fuse(

        self,

        semantic_results,

        bm25_results
    ):

        fused_scores = {}

        # =====================================
        # Semantic Rankings
        # =====================================

        for rank, result in enumerate(

            semantic_results,

            start=1
        ):

            document_id = (

                result["metadata"][
                    "chunk_id"
                ]
            )

            score = 1 / (
                self.k + rank
            )

            if document_id not in (
                fused_scores
            ):

                fused_scores[
                    document_id
                ] = {

                    "result": result,

                    "score": 0
                }

            fused_scores[
                document_id
            ]["score"] += score

        # =====================================
        # BM25 Rankings
        # =====================================

        for rank, result in enumerate(

            bm25_results,

            start=1
        ):

            document_id = (

                result["metadata"][
                    "chunk_id"
                ]
            )

            score = 1 / (
                self.k + rank
            )

            if document_id not in (
                fused_scores
            ):

                fused_scores[
                    document_id
                ] = {

                    "result": result,

                    "score": 0
                }

            fused_scores[
                document_id
            ]["score"] += score

        # =====================================
        # Final Ranking
        # =====================================

        reranked_results = sorted(

            fused_scores.values(),

            key=lambda x: x["score"],

            reverse=True
        )

        return [

            item["result"]

            for item in reranked_results
        ]