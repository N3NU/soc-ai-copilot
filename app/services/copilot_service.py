from app.retrieval.detect_category_service import detect_category
from app.retrieval.metadata_filter import metadata_filter
from app.retrieval.retriever_service import get_relevant_documents
from app.llm.rewrite import rewrite_query
from app.llm.generate import generate_response
from app.llm.context import context_builder
from app.llm.prompt import prompt_builder
from app.config import MAX_CHAT_HISTORY
from app.retrieval.detect_section_service import detect_section

def process_query(query, chat_history, current_topic):

    rewritten_query = rewrite_query(query, chat_history)
    print(f"{rewritten_query}\n")
    category = detect_category(rewritten_query)
    section = detect_section(rewritten_query)

    if category:
        current_topic = category
    elif current_topic:
        category = current_topic

    filters = metadata_filter(
        category,
        section
    )
    print(f"{filters}")
    safe_results = get_relevant_documents(
        rewritten_query,
        filters
    )

    top_doc, distance = safe_results[0]

    source = top_doc.metadata["source"]

    context = context_builder(safe_results)

    history = "\n".join(chat_history[-MAX_CHAT_HISTORY:])

    prompt = prompt_builder(history, context, rewritten_query)
    print(prompt)
    response = generate_response(prompt)

    return {
        "response": response.content,
        "rewritten_query": rewritten_query,
        "category": category,
        "current_topic": current_topic,
        "source": source,
        "distance": distance
    }