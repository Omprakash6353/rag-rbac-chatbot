import chromadb
from src.utils.config import CHROMA_PATH, COLLECTION_NAME


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def reset_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass

    return client.get_or_create_collection(name=COLLECTION_NAME)