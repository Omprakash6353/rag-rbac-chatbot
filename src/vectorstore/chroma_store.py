import chromadb

from src.config.settings import (
    VectorDBConfig
)


class ChromaVectorStore:

    def __init__(self):

        print(
            "\n🚀 Initializing ChromaDB...\n"
        )

        self.client = (
            chromadb.PersistentClient(
                path=(
                    VectorDBConfig
                    .VECTOR_DB_PATH
                )
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=(
                    VectorDBConfig
                    .COLLECTION_NAME
                )
            )
        )

        print(
            f"✅ Connected to collection: "
            f"{VectorDBConfig.COLLECTION_NAME}"
        )

    # =====================================
    # Add Documents
    # =====================================

    def add_documents(
        self,
        documents,
        embeddings
    ):

        ids = [

            doc.metadata["chunk_id"]

            for doc in documents
        ]

        texts = [

            doc.page_content

            for doc in documents
        ]

        metadatas = [

            doc.metadata

            for doc in documents
        ]

        self.collection.add(

            ids=ids,

            documents=texts,

            metadatas=metadatas,

            embeddings=embeddings
        )

        print(
            f"✅ Stored "
            f"{len(documents)} "
            f"documents in ChromaDB"
        )

    # =====================================
    # Similarity Search
    # =====================================

    def similarity_search(
        self,
        query_embedding,
        top_k=5,
        filters=None
    ):

        results = (
            self.collection.query(

                query_embeddings=[
                    query_embedding
                ],

                n_results=top_k,

                where=filters
            )
        )

        return results