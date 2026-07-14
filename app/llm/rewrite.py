from langchain_ollama import  ChatOllama

from app.config import ROUTING_MODEL

llm = ChatOllama(
    model=ROUTING_MODEL,
    temperature=0
)

def rewrite_query(query, current_topic):

    if not current_topic:
        return query
    
    print(f"\nHistory TEXT:\n{current_topic}\n")
    rewrite_prompt = f"""
You are a query rewriting system.

Your ONLY job is to rewrite follow-up questions into standalone questions.

You are NOT an assistant.
You are NOT allowed to answer questions.
You are NOT allowed to explain anything.

Rules:

- Preserve the user's intent exactly.
- Replace ambiguous references only when necessary:
    - it
    - that
    - this
    - they
    - them
    - these
    - those

- Use the conversation only to resolve those references.
- If the question is already standalone, return it unchanged.
- Never summarize previous messages.
- Never introduce new information.
- Never add investigation steps.
- Never answer the question.

Examples:

Conversation:
User: What are ransomware indicators?
Assistant: ...

Question:
How do I recover from it?

Output:
How do I recover from ransomware?

Conversation:
User: Explain Mimikatz.
Assistant: ...

Question:
What MITRE technique does it use?

Output:
What MITRE technique does Mimikatz use?

Conversation:
User: What are phishing indicators?
Assistant: ...

Question:
What are phishing indicators?

Output:
What are phishing indicators?

Conversation:
{current_topic}

Question:
{query}

Return ONLY the rewritten question.
"""

    rewritten=llm.invoke(
        rewrite_prompt
    )

    return rewritten.content.strip()