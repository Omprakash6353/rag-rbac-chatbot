from src.retrieval.retrieval_pipeline import (
    RetrievalPipeline
)

from src.evaluation.golden_set import (
    GOLDEN_SET
)


class HitRateEvaluator:

    def __init__(self):

        self.pipeline = (
            RetrievalPipeline()
        )

    # =====================================
    # Evaluate Hit Rate
    # =====================================

    def evaluate(self):

        print(
            "\n🚀 Running Hit Rate Evaluation...\n"
        )

        total_queries = len(GOLDEN_SET)

        hits = 0

        for index, test_case in enumerate(
            GOLDEN_SET
        ):

            query = test_case["query"]

            expected_document = (
                test_case["expected_document"]
            )

            print("=" * 80)

            print(
                f"\nTest Case {index + 1}"
            )

            print(
                f"\nQuery: {query}"
            )

            print(
                f"\nExpected Document: "
                f"{expected_document}"
            )

            response = (
                self.pipeline.search(query)
            )

            retrieved_documents = [

                result["metadata"][
                    "document_id"
                ]

                for result in (
                    response["results"]
                )
            ]

            print(
                f"\nRetrieved Documents:"
            )

            for doc in retrieved_documents:

                print(f"- {doc}")

            # =====================================
            # Hit Detection
            # =====================================

            if expected_document in (
                retrieved_documents
            ):

                print(
                    "\n✅ HIT"
                )

                hits += 1

            else:

                print(
                    "\n❌ MISS"
                )

        # =====================================
        # Final Hit Rate
        # =====================================

        hit_rate = round(

            (hits / total_queries) * 100,

            2
        )

        print("\n" + "=" * 80)

        print(
            "\n🎯 FINAL HIT RATE RESULTS\n"
        )

        print(
            f"Total Queries: "
            f"{total_queries}"
        )

        print(
            f"Hits: {hits}"
        )

        print(
            f"Misses: "
            f"{total_queries - hits}"
        )

        print(
            f"\n✅ Hit Rate: "
            f"{hit_rate}%"
        )