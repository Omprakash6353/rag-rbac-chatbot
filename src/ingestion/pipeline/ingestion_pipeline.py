from src.ingestion.loaders.markdown_loader import (
    MarkdownLoader
)

from src.ingestion.loaders.csv_loader import (
    CSVLoader
)

from src.ingestion.normalizers.markdown_normalizer import (
    MarkdownNormalizer
)

from src.ingestion.normalizers.csv_normalizer import (
    CSVNormalizer
)

from src.ingestion.chunkers.markdown_chunker import (
    MarkdownChunker
)

from src.ingestion.chunkers.csv_chunker import (
    CSVChunker
)

from src.ingestion.metadata.metadata_enricher import (
    MetadataEnricher
)

from src.embeddings.embedding_model import (
    EmbeddingModel
)

from src.vectorstore.chroma_store import (
    ChromaVectorStore
)


class IngestionPipeline:

    def __init__(self):

        # =========================
        # Loaders
        # =========================

        self.markdown_loader = (
            MarkdownLoader(
                data_path="data/raw"
            )
        )

        self.csv_loader = (
            CSVLoader(
                data_path="data/raw"
            )
        )

        # =========================
        # Normalizers
        # =========================

        self.markdown_normalizer = (
            MarkdownNormalizer()
        )

        self.csv_normalizer = (
            CSVNormalizer()
        )

        # =========================
        # Chunkers
        # =========================

        self.markdown_chunker = (
            MarkdownChunker()
        )

        self.csv_chunker = (
            CSVChunker()
        )

        # =========================
        # Metadata
        # =========================

        self.metadata_enricher = (
            MetadataEnricher()
        )

        # =========================
        # Embeddings
        # =========================

        self.embedding_model = (
            EmbeddingModel()
        )

        # =========================
        # Vector Store
        # =========================

        self.vector_store = (
            ChromaVectorStore()
        )

    # =====================================
    # Unified Ingestion
    # =====================================

    def ingest(self):

        print(
            "\n🚀 Starting ingestion pipeline...\n"
        )

        # =====================================
        # LOAD
        # =====================================

        markdown_docs = (
            self.markdown_loader
            .load_documents()
        )

        csv_docs = (
            self.csv_loader
            .load_documents()
        )

        # =====================================
        # NORMALIZE
        # =====================================

        markdown_docs = (
            self.markdown_normalizer
            .normalize(markdown_docs)
        )

        csv_docs = (
            self.csv_normalizer
            .normalize(csv_docs)
        )

        # =====================================
        # CHUNK
        # =====================================

        markdown_chunks = (
            self.markdown_chunker
            .chunk_documents(markdown_docs)
        )

        csv_chunks = (
            self.csv_chunker
            .chunk_documents(csv_docs)
        )

        all_chunks = (
            markdown_chunks
            + csv_chunks
        )

        print(
            f"\n📦 Total chunks: "
            f"{len(all_chunks)}"
        )

        # =====================================
        # METADATA ENRICHMENT
        # =====================================

        enriched_chunks = (
            self.metadata_enricher
            .enrich(all_chunks)
        )

        # =====================================
        # EMBEDDINGS
        # =====================================

        chunk_texts = [

            chunk.page_content

            for chunk in enriched_chunks
        ]

        embeddings = (
            self.embedding_model
            .embed_documents(chunk_texts)
        )

        # =====================================
        # VECTOR STORAGE
        # =====================================

        self.vector_store.add_documents(
            documents=enriched_chunks,
            embeddings=embeddings
        )

        # =====================================
        # INGESTION SUMMARY
        # =====================================

        print(
            "\n✅ Ingestion pipeline completed"
        )

        print(
            f"\n📄 Total documents: "
            f"{len(markdown_docs) + len(csv_docs)}"
        )

        print(
            f"📦 Total chunks: "
            f"{len(enriched_chunks)}"
        )

        print(
            f"🧠 Total embeddings: "
            f"{len(embeddings)}"
        )

        return enriched_chunks