from datetime import datetime, timezone

from src.ingestion.loader import load_markdown_files, load_csv_files
from src.ingestion.chunker import chunk_markdown
from src.ingestion.csv_handler import transform_csv
from src.embedding.embedding_model import EmbeddingModel
from src.vectorstore.chroma_store import reset_collection


def run_pipeline():
    print("🚀 Starting ingestion pipeline...")

    # Load
    md_docs = load_markdown_files()
    csv_docs = load_csv_files()

    # Transform
    md_chunks = chunk_markdown(md_docs)
    csv_chunks = transform_csv(csv_docs)

    all_chunks = md_chunks + csv_chunks
    print(f"Total chunks: {len(all_chunks)}")

    # Prepare metadata
    documents = []
    metadatas = []
    ids = []

    ingestion_time = datetime.now(timezone.utc).isoformat()

    for i, item in enumerate(all_chunks):
        doc_id = item["source"].split(".")[0]
        chunk_id = f"{doc_id}_{i}"

        documents.append(item["content"])

        metadatas.append({
            "department": item["department"],
            "type": item["type"],
            "source": item["source"],
            "section": item.get("section", "none"),
            "access_level": "department",
            "ingestion_timestamp": ingestion_time,
            "document_id": doc_id,
            "chunk_id": chunk_id
        })

        ids.append(chunk_id)

    # Embedding
    model = EmbeddingModel()
    embeddings = model.embed_documents(documents)

    # Store
    collection = reset_collection()

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print("✅ Ingestion complete!")