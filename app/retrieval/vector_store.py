from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from app.config import (
    EMBED_MODEL,
    DB_PATH,
    COLLECTION_NAME
)

embeddings = OllamaEmbeddings(
    model=EMBED_MODEL
    )

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings,
    collection_name=COLLECTION_NAME
)