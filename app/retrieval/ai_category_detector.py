from langchain_ollama import ChatOllama
from app.config import LLM_MODEL
from app.prompts.category_classifier_prompt import category_classifier_prompt

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)


def ai_detect_category(query):
    response = llm.invoke(category_classifier_prompt(query))

    return response.content.strip().lower()