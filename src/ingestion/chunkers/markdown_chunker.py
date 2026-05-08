from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter
)

from src.config.settings import ChunkingConfig


class MarkdownChunker:

    def __init__(self):

        self.headers_to_split_on = [
            ("#", "header_1"),
            ("##", "header_2"),
            ("###", "header_3"),
        ]

        self.markdown_splitter = (
            MarkdownHeaderTextSplitter(
                headers_to_split_on=(
                    self.headers_to_split_on
                )
            )
        )

        self.recursive_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=(
                    ChunkingConfig
                    .REPORT_CHUNK_SIZE
                ),

                chunk_overlap=(
                    ChunkingConfig
                    .REPORT_CHUNK_OVERLAP
                )
            )
        )

    def chunk_documents(self, documents):

        final_chunks = []

        for doc in documents:

            markdown_chunks = (
                self.markdown_splitter
                .split_text(doc.page_content)
            )

            for chunk in markdown_chunks:

                chunk.metadata.update(doc.metadata)

                smaller_chunks = (
                    self.recursive_splitter
                    .split_documents([chunk])
                )

                final_chunks.extend(smaller_chunks)

        print(
            f"✅ Generated "
            f"{len(final_chunks)} "
            f"markdown chunks"
        )

        return final_chunks
    
    
