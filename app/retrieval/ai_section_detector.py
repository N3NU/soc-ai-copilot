from langchain_ollama import ChatOllama
from app.config import LLM_MODEL
from app.prompts.section_classifier_prompt import section_classifier_prompt

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)


def ai_detect_section(query):
    response = llm.invoke(section_classifier_prompt(query))

    return response.content.strip().lower()