import os
from dotenv import load_dotenv

load_dotenv()


# =========================
# EMBEDDING CONFIG
# =========================

class EmbeddingConfig:

    MODEL_NAME = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-base-en-v1.5"
    )

    QUERY_PREFIX = "query: "
    PASSAGE_PREFIX = "passage: "

    NORMALIZE_EMBEDDINGS = True


# =========================
# VECTOR DATABASE CONFIG
# =========================

class VectorDBConfig:

    VECTOR_DB_PATH = os.getenv(
        "VECTOR_DB_PATH",
        "data/vectorstore/chroma_db"
    )

    COLLECTION_NAME = os.getenv(
        "COLLECTION_NAME",
        "company_knowledge_base"
    )


# =========================
# CHUNKING CONFIG
# =========================

class ChunkingConfig:

    REPORT_CHUNK_SIZE = int(
        os.getenv("REPORT_CHUNK_SIZE", 900)
    )

    REPORT_CHUNK_OVERLAP = int(
        os.getenv("REPORT_CHUNK_OVERLAP", 120)
    )

    POLICY_CHUNK_SIZE = int(
        os.getenv("POLICY_CHUNK_SIZE", 700)
    )

    POLICY_CHUNK_OVERLAP = int(
        os.getenv("POLICY_CHUNK_OVERLAP", 100)
    )


# =========================
# RETRIEVAL CONFIG
# =========================

class RetrievalConfig:

    TOP_K = int(
        os.getenv("TOP_K", 5)
    )

    INITIAL_RETRIEVAL_K = int(
        os.getenv("INITIAL_RETRIEVAL_K", 20)
    )

    CONFIDENCE_THRESHOLD = float(
        os.getenv("CONFIDENCE_THRESHOLD", 60)
    )


# =========================
# DEBUG CONFIG
# =========================

class DebugConfig:

    SHOW_RETRIEVAL_DEBUG = os.getenv(
        "SHOW_RETRIEVAL_DEBUG",
        "True"
    ) == "True"

    SHOW_METADATA = os.getenv(
        "SHOW_METADATA",
        "True"
    ) == "True"
    
    