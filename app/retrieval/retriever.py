from app.retrieval.vector_store import db
from app.config import RETRIEVAL_K

def retrieve(query, filters=None, k=None):

    if k is None:
        k = RETRIEVAL_K
        
    results = db.similarity_search_with_score(
        query,
        k=k,
        filter=filters
    )

    return results