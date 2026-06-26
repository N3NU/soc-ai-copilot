from app.retrieval.retriever import retrieve
from app.retrieval.reranker import rerank
from app.security.filter_malicious_chunks import filter_malicious_chunks

def get_relevant_documents(query, filters=None):
    # Step 1: vector search
    results = retrieve(query, filters, k=None)
#    for r, original_score in results:
#        print(f"TEXT: {r}")
#        print(f"SCORE: {original_score}")
#        print(f"=" * 50)
    # Step 2: rerank
    reranked = rerank(query, results)

    # Step 3: safety filter
    safe = filter_malicious_chunks(results)
    print(f"Chuck: {safe[0]}")
    return safe