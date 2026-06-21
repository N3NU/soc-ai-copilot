from langchain_ollama import ChatOllama
from app.config import LLM_MODEL

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)

def generate_response(prompt):

    response = llm.invoke(prompt)

    return response