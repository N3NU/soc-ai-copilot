from app.retrieval.keyword_section_detector import keyword_section_detector
from app.retrieval.ai_section_detector import ai_detect_section

def detect_section(rewritten_query):
    
    section = keyword_section_detector(rewritten_query)

    if section:
        return section
    
    return ai_detect_section(rewritten_query)