from src.config.settings import (
    RetrievalConfig
)


class RetrievalValidator:

    def validate(
        self,
        retrieval_results
    ):

        validated_results = []

        for result in retrieval_results:

            content = result["content"]

            confidence = (
                result["confidence"]
            )

            # =========================
            # Confidence Threshold
            # =========================

            if confidence < (
                RetrievalConfig
                .CONFIDENCE_THRESHOLD
            ):

                continue

            # =========================
            # Remove TOC Chunks
            # =========================

            if self.is_table_of_contents(
                content
            ):

                continue

            # =========================
            # Remove Very Short Chunks
            # =========================

            if len(content.strip()) < 120:

                continue

            # =========================
            # Remove Navigation Noise
            # =========================

            if self.is_navigation_heavy(
                content
            ):

                continue

            validated_results.append(
                result
            )

        print(
            f"✅ Validation complete: "
            f"{len(validated_results)} "
            f"high-quality results"
        )

        return validated_results

    # =====================================
    # TOC Detection
    # =====================================

    def is_table_of_contents(
        self,
        content
    ):

        content_lower = (
            content.lower()
        )

        toc_patterns = [

            "table of contents",

            "welcome & introduction",

            "leave policies",

            "performance & feedback",

            "miscellaneous"
        ]

        matches = sum(
            pattern in content_lower
            for pattern in toc_patterns
        )

        return matches >= 3

    # =====================================
    # Navigation Detection
    # =====================================

    def is_navigation_heavy(
        self,
        content
    ):

        lines = content.splitlines()

        short_lines = sum(
            len(line.strip()) < 40
            for line in lines
        )

        if len(lines) == 0:
            return False

        ratio = short_lines / len(lines)

        return ratio > 0.7