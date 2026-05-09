from src.evaluation.golden_set import (
    GOLDEN_SET
)

from src.retrieval.retrieval_pipeline import (
    RetrievalPipeline
)


class MRREvaluator:

    def __init__(self):

        self.pipeline = (
            RetrievalPipeline()
        )

    # =====================================
    # Evaluate MRR
    # =====================================

    def evaluate(self):

        print(
            "\n🚀 Running MRR Evaluation...\n"
        )

        total_queries = len(
            GOLDEN_SET
        )

        reciprocal_ranks = []

        # =====================================
        # Run Queries
        # =====================================

        for index, test_case in enumerate(
            GOLDEN_SET,
            start=1
        ):

            query = (
                test_case["query"]
            )

            expected_document = (
                test_case[
                    "expected_document"
                ]
            )

            print("=" * 80)

            print(
                f"\nTest Case {index}\n"
            )

            print(
                f"Query: {query}\n"
            )

            print(
                f"Expected Document: "
                f"{expected_document}"
            )

            # =====================================
            # Search
            # =====================================

            response = (
                self.pipeline.search(query)
            )

            results = (
                response["results"]
            )

            retrieved_documents = []

            for result in results:

                retrieved_documents.append(

                    result["metadata"][
                        "document_id"
                    ]
                )

            print(
                "\nRetrieved Documents:"
            )

            for rank, document_id in enumerate(

                retrieved_documents,

                start=1
            ):

                print(
                    f"{rank}. {document_id}"
                )

            # =====================================
            # Compute Reciprocal Rank
            # =====================================

            reciprocal_rank = 0

            for rank, document_id in enumerate(

                retrieved_documents,

                start=1
            ):

                if (
                    document_id
                    ==
                    expected_document
                ):

                    reciprocal_rank = (
                        1 / rank
                    )

                    break

            reciprocal_ranks.append(
                reciprocal_rank
            )

            print(
                f"\nReciprocal Rank: "
                f"{round(reciprocal_rank, 4)}"
            )

            print(
                "\n" + "=" * 80
            )

        # =====================================
        # Final MRR
        # =====================================

        mrr_score = (

            sum(reciprocal_ranks)

            /

            total_queries
        )

        print(
            "\n🎯 FINAL MRR RESULTS\n"
        )

        print(
            f"Total Queries: "
            f"{total_queries}"
        )

        print(
            f"MRR Score: "
            f"{round(mrr_score, 4)}"
        )