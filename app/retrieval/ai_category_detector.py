from langchain_ollama import ChatOllama

from app.config import ROUTING_MODEL
from app.prompts.category_classifier_prompt import category_classifier_prompt
from app.config import CATEGORIES

llm = ChatOllama(
    model=ROUTING_MODEL,
    temperature=0
)


def ai_detect_category(query):

    response = llm.invoke(
        category_classifier_prompt(query)
    )

    category = response.content.strip().lower()

    if category in CATEGORIES:
        return category

    return None