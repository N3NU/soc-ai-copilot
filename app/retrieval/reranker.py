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
        
        final_score=(overlap*2)+(1-original_score)

        rescored.append(
            (r, final_score)
        )

    rescored.sort(
        key=lambda x:x[1],
        reverse=True
    )

    return rescored