from pathlib import Path

from langchain_community.document_loaders import TextLoader


class MarkdownLoader:

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_documents(self):

        markdown_files = list(
            self.data_path.rglob("*.md")
        )

        all_documents = []

        for file_path in markdown_files:

            try:
                loader = TextLoader(
                    str(file_path),
                    encoding="utf-8"
                )

                documents = loader.load()

                for doc in documents:

                    doc.metadata["source"] = file_path.name

                    doc.metadata["file_path"] = str(file_path)

                    doc.metadata["file_type"] = "markdown"

                all_documents.extend(documents)

                print(f"✅ Loaded: {file_path.name}")

            except Exception as e:

                print(
                    f"❌ Failed loading "
                    f"{file_path.name}: {e}"
                )

        print(
            f"\n📄 Total markdown documents loaded: "
            f"{len(all_documents)}"
        )

        return all_documents
    