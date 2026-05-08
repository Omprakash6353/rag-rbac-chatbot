import re


class CSVNormalizer:

    def normalize(self, documents):

        normalized_documents = []

        for doc in documents:

            content = doc.page_content

            # =========================
            # Normalize line endings
            # =========================

            content = content.replace("\r\n", "\n")

            # =========================
            # Remove excessive spaces
            # =========================

            content = re.sub(
                r"[ \t]+",
                " ",
                content
            )

            # =========================
            # Remove excessive blank lines
            # =========================

            content = re.sub(
                r"\n{3,}",
                "\n\n",
                content
            )

            # =========================
            # Normalize NaN-like values
            # =========================

            content = content.replace("nan", "N/A")

            # =========================
            # Update document
            # =========================

            doc.page_content = content.strip()

            normalized_documents.append(doc)

        print(
            f"✅ Normalized "
            f"{len(normalized_documents)} "
            f"CSV documents"
        )

        return normalized_documents