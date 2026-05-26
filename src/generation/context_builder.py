from collections import defaultdict


class ContextBuilder:

    def __init__(

        self,

        max_chunks_per_document=3
    ):

        self.max_chunks_per_document = (
            max_chunks_per_document
        )

    # =====================================
    # Build Context
    # =====================================

    def build_context(

        self,

        retrieval_results
    ):

        # =====================================
        # Empty Protection
        # =====================================

        if len(retrieval_results) == 0:

            return None

        # =====================================
        # Group By Document
        # =====================================

        grouped_documents = defaultdict(list)

        for result in retrieval_results:

            document_id = (

                result["metadata"][
                    "document_id"
                ]
            )

            grouped_documents[
                document_id
            ].append(result)

        # =====================================
        # Build Structured Context
        # =====================================

        context_blocks = []

        for document_id, chunks in (

            grouped_documents.items()
        ):

            # =====================================
            # Limit Chunks
            # =====================================

            selected_chunks = chunks[
                :self.max_chunks_per_document
            ]

            # =====================================
            # Metadata
            # =====================================

            metadata = (

                selected_chunks[0][
                    "metadata"
                ]
            )

            source = metadata.get(
                "source",
                "unknown"
            )

            department = metadata.get(
                "department",
                "unknown"
            )

            quarter = metadata.get(
                "quarter",
                "unknown"
            )

            year = metadata.get(
                "year",
                "unknown"
            )

            # =====================================
            # Merge Content
            # =====================================

            merged_content = ""

            for chunk in selected_chunks:

                merged_content += (

                    chunk["content"]

                    + "\n\n"
                )

            # =====================================
            # Structured Document Block
            # =====================================

            document_block = f"""
<DOCUMENT>

<SOURCE>
{source}
</SOURCE>

<METADATA>
department: {department}
quarter: {quarter}
year: {year}
</METADATA>

<CONTENT>
{merged_content.strip()}
</CONTENT>

</DOCUMENT>
"""

            context_blocks.append(
                document_block
            )

        # =====================================
        # Final Context
        # =====================================

        final_context = "\n".join(
            context_blocks
        )

        print(
            f"✅ Context built with "
            f"{len(context_blocks)} "
            f"merged documents"
        )

        return final_context