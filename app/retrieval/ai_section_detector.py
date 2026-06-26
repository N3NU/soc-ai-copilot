from langchain_ollama import ChatOllama
from app.config import ROUTING_MODEL
from app.prompts.section_classifier_prompt import section_classifier_prompt
from app.config import SECTION_KEYWORDS

llm = ChatOllama(
    model=ROUTING_MODEL,
    temperature=0
)


def ai_detect_section(query):
    response = llm.invoke(section_classifier_prompt(query))

    section =  response.content.strip().lower()

    if section in SECTION_KEYWORDS:
        return section
    
    return None