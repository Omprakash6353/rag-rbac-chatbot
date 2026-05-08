class ContextBuilder:

    def build_context(
        self,
        retrieval_results,
        max_context_chars=4000
    ):

        context_sections = []

        used_chunk_ids = set()

        current_size = 0

        for result in retrieval_results:

            metadata = result["metadata"]

            chunk_id = (
                metadata["chunk_id"]
            )

            # =========================
            # Deduplication
            # =========================

            if chunk_id in used_chunk_ids:
                continue

            used_chunk_ids.add(
                chunk_id
            )

            content = result["content"]

            confidence = (
                result["confidence"]
            )

            source = metadata.get(
                "source",
                "unknown"
            )

            section_title = metadata.get(
                "header_2",
                "General Section"
            )

            # =========================
            # Structured Context
            # =========================

            formatted_chunk = f"""
SOURCE: {source}

SECTION: {section_title}

CONFIDENCE: {confidence}%

CONTENT:
{content}

==================================================
"""

            # =========================
            # Context Limit
            # =========================

            if (
                current_size
                + len(formatted_chunk)
                > max_context_chars
            ):

                break

            context_sections.append(
                formatted_chunk
            )

            current_size += len(
                formatted_chunk
            )

        final_context = "\n".join(
            context_sections
        )

        print(
            f"✅ Context built: "
            f"{len(context_sections)} "
            f"chunks included"
        )

        return final_context