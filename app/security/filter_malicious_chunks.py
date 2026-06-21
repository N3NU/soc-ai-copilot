



# -------------------------
# BASIC PROMPT INJECTION FILTER
# -------------------------

BLOCKLIST = [
    "ignore previous instructions",
    "reveal sensitive information",
    "administrator passwords",
    "you are no longer"
]

def is_malicious(text):
    text = text.lower()

    for phrase in BLOCKLIST:
        if phrase in text:
            return True

    return False

def filter_malicious_chunks(reranked_results):

    safe_results = []

    for r, score in reranked_results:

        if is_malicious(r.page_content):
            print(f"\n[BLOCKED MALICIOUS CHUNK]: {r.metadata.get('source')}")
            print(f"[BLOCKED MALICIOUS CHUNK]: {r.page_content}")
            continue

        safe_results.append((r, score))
    
    return safe_results