


def context_builder(safe_results):
    context = "\n\n".join([
        f"""SOURCE: {r.metadata.get('source')}

DOCUMENT_TYPE: {r.metadata.get('document_type')}

CATEGORY: {r.metadata.get('category')}

DEPARTMENT: {r.metadata.get('department')}

CONFIDENCE: {confidence}

CONTENT:
{r.page_content}
"""
        for r, original_score, rerank_score, confidence in safe_results
    ])
#    print(f"+" * 50)
#    print(f"{context}")
    return context