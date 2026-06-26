import re


def rerank(query, results):

    query_words = set(
        re.findall(
            r'\b\w+\b',
            query.lower()
        )
    )

    rescored=[]

    for r, original_score in results:

        content_words=set(
            re.findall(
                r'\b\w+\b',
                r.page_content.lower()
            )
        )

        overlap=len(
            query_words.intersection(
                content_words
            )
        )
        
        rerank_score=(overlap*2)+(1-original_score)

        if rerank_score > 2.75:
            confidence = "High"
        elif rerank_score > 0:
            confidence = "Medium"
        else:
            confidence = "Low"

        rescored.append(
            (r, original_score, rerank_score, confidence)
        )

    rescored.sort(
        key=lambda x: x[2],
        reverse=True
    )

    return rescored