from src.retrieval.query_processor import (
    QueryProcessor
)

from src.retrieval.retriever import (
    Retriever
)

from src.retrieval.retrieval_validator import (
    RetrievalValidator
)


class RetrievalPipeline:

    def __init__(self):

        self.query_processor = (
            QueryProcessor()
        )

        self.retriever = (
            Retriever()
        )

        self.validator = (
            RetrievalValidator()
        )

    # =====================================
    # Unified Search
    # =====================================

    def search(
        self,
        query
    ):

        # =========================
        # Query Understanding
        # =========================

        processed_query = (
            self.query_processor
            .process_query(query)
        )

        filters = (
            processed_query["filters"]
        )

        # =========================
        # Semantic Retrieval
        # =========================

        retrieval_results = (
            self.retriever.retrieve(
                query=query,
                filters=filters
            )
        )

        # =========================
        # Validation
        # =========================

        validated_results = (
            self.validator.validate(
                retrieval_results
            )
        )

        return {

            "query": query,

            "filters": filters,

            "results": validated_results
        }