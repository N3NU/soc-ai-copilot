from app.retrieval.keyword_category_detector import keyword_detect_category
from app.retrieval.ai_category_detector import ai_detect_category

def detect_category(query):

    category = keyword_detect_category(query)
    print(f"category: {category}")
    if category:
        return category

    return ai_detect_category(query)



