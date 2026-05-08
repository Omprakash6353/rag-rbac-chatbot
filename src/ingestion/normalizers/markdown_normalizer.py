import re


class MarkdownNormalizer:

    def normalize(self, documents):

        normalized_documents = []

        for doc in documents:

            content = doc.page_content

            # =========================
            # Normalize line endings
            # =========================

            content = content.replace("\r\n", "\n")

            # =========================
            # Remove excessive blank lines
            # =========================

            content = re.sub(
                r"\n{3,}",
                "\n\n",
                content
            )

            # =========================
            # Remove trailing spaces
            # =========================

            content = "\n".join(
                line.rstrip()
                for line in content.splitlines()
            )

            # =========================
            # Normalize multiple spaces
            # =========================

            content = re.sub(
                r"[ \t]+",
                " ",
                content
            )

            # =========================
            # Update document
            # =========================

            doc.page_content = content.strip()

            normalized_documents.append(doc)

        print(
            f"✅ Normalized "
            f"{len(normalized_documents)} "
            f"markdown documents"
        )

        return normalized_documents