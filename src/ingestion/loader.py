import os
from langchain_community.document_loaders import TextLoader, CSVLoader
from src.utils.config import BASE_DATA_PATH


def load_markdown_files():
    md_docs = []

    for department in os.listdir(BASE_DATA_PATH):
        dept_path = os.path.join(BASE_DATA_PATH, department)

        if not os.path.isdir(dept_path):
            continue

        for file in os.listdir(dept_path):
            if file.endswith(".md"):
                file_path = os.path.join(dept_path, file)

                loader = TextLoader(file_path, encoding="utf-8")
                documents = loader.load()

                for doc in documents:
                    md_docs.append({
                        "content": doc.page_content,
                        "department": department,
                        "source": file
                    })

    return md_docs


def load_csv_files():
    csv_docs = []

    for department in os.listdir(BASE_DATA_PATH):
        dept_path = os.path.join(BASE_DATA_PATH, department)

        if not os.path.isdir(dept_path):
            continue

        for file in os.listdir(dept_path):
            if file.endswith(".csv"):
                file_path = os.path.join(dept_path, file)

                loader = CSVLoader(file_path=file_path, encoding="utf-8")
                documents = loader.load()

                for doc in documents:
                    csv_docs.append({
                        "content": doc.page_content,
                        "department": department,
                        "source": file
                    })

    return csv_docs