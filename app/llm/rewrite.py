from langchain_ollama import OllamaEmbeddings, ChatOllama
from app.config import LLM_MODEL

# -------------------------
# LOAD LLM
# -------------------------

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)

# -------------------------
# REWRITE FUNCTION
# -------------------------

def rewrite_query(query, history):

    if len(history) == 0:
        return query

    history_text="\n".join(
        history[-6:]
    )
    print(f"\nHistory TEXT:\n{history_text}\n")
    rewrite_prompt=f"""
You rewrite follow-up questions into standalone questions.

STRICT RULES:

1. Preserve intent exactly.
2. Never answer the question.
3. Never summarize.
4. Never introduce new actions.
5. Never replace:
   "next"
   "before"
   "after"
   "then"

6. Only replace ambiguous references:
   "it"
   "that"
   "this"
   "they"

7. If no ambiguity exists, return the original question unchanged.

Conversation:
{history_text}

Question:
{query}

Standalone question:
"""

    rewritten=llm.invoke(
        rewrite_prompt
    )

    return rewritten.content.strip()