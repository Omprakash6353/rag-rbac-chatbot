from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader as LangChainCSVLoader
)


class CSVLoader:

    def __init__(self, data_path: str):

        self.data_path = Path(data_path)

    def load_documents(self):

        csv_files = list(
            self.data_path.rglob("*.csv")
        )

        all_documents = []

        for file_path in csv_files:

            try:

                loader = (
                    LangChainCSVLoader(
                        file_path=str(file_path),
                        encoding="utf-8"
                    )
                )

                documents = loader.load()

                for index, doc in enumerate(
                    documents
                ):

                    doc.metadata["source"] = (
                        file_path.name
                    )

                    doc.metadata["file_path"] = (
                        str(file_path)
                    )

                    doc.metadata["file_type"] = (
                        "csv"
                    )

                    doc.metadata["row_index"] = (
                        index
                    )

                all_documents.extend(
                    documents
                )

                print(
                    f"✅ Loaded: "
                    f"{file_path.name}"
                )

            except Exception as e:

                print(
                    f"❌ Failed loading "
                    f"{file_path.name}: {e}"
                )

        print(
            f"\n📄 Total CSV documents loaded: "
            f"{len(all_documents)}"
        )

        return all_documents