import re
from datetime import datetime, timezone


class MetadataEnricher:

    def enrich(self, documents):

        enriched_documents = []

        for index, doc in enumerate(documents):

            source = doc.metadata.get(
                "source",
                ""
            )

            file_path = doc.metadata.get(
                "file_path",
                ""
            )

            # =========================
            # Department Detection
            # =========================

            department = self.detect_department(
                file_path
            )

            # =========================
            # Document Type Detection
            # =========================

            doc_type = self.detect_doc_type(
                source
            )

            # =========================
            # Quarter Detection
            # =========================

            quarter = self.detect_quarter(
                source
            )

            # =========================
            # Year Detection
            # =========================

            year = self.detect_year(
                source
            )

            # =========================
            # Period Detection
            # =========================

            period = (
                "quarterly"
                if quarter != "unknown"
                else "annual"
            )

            # =========================
            # Document ID
            # =========================

            document_id = (
                source.replace(".md", "")
                .replace(".csv", "")
            )

            # =========================
            # Chunk ID
            # =========================

            chunk_id = (
                f"{document_id}_{index}"
            )

            # =========================
            # Timestamp
            # =========================

            ingestion_timestamp = (
                datetime.now(timezone.utc)
                .isoformat()
            )

            # =========================
            # Access Level
            # =========================

            access_level = "department"

            # =========================
            # Metadata Update
            # =========================

            doc.metadata.update({

                "department": department,

                "doc_type": doc_type,

                "quarter": quarter,

                "year": year,

                "period": period,

                "document_id": document_id,

                "chunk_id": chunk_id,

                "access_level": access_level,

                "ingestion_timestamp":
                    ingestion_timestamp
            })

            enriched_documents.append(doc)

        print(
            f"✅ Enriched metadata for "
            f"{len(enriched_documents)} chunks"
        )

        return enriched_documents

    # =====================================
    # Department Detection
    # =====================================

    def detect_department(
        self,
        file_path
    ):

        path = file_path.lower()

        if "marketing" in path:
            return "marketing"

        if "finance" in path:
            return "finance"

        if "hr" in path:
            return "hr"

        if "engineering" in path:
            return "engineering"

        return "general"

    # =====================================
    # Document Type Detection
    # =====================================

    def detect_doc_type(
        self,
        source
    ):

        source = source.lower()

        if "report" in source:
            return "report"

        if "handbook" in source:
            return "policy"

        if ".csv" in source:
            return "dataset"

        return "document"

    # =====================================
    # Quarter Detection
    # =====================================

    def detect_quarter(
        self,
        source
    ):

        match = re.search(
            r"(q[1-4])",
            source.lower()
        )

        if match:
            return match.group(1).upper()

        return "unknown"

    # =====================================
    # Year Detection
    # =====================================

    def detect_year(
        self,
        source
    ):

        match = re.search(
            r"(20\d{2})",
            source
        )

        if match:
            return match.group(1)

        return "unknown"