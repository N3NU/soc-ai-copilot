import re

from app.config import CATEGORY_KEYWORDS

def keyword_detect_category(query):

    query = query.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, query):
                return category

    return None