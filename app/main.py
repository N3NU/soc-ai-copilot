from app.services.copilot_service import process_query

def print_rewritten_query(rewritten_query):
    print(
        f"\nRewritten query: {rewritten_query}"
    )

def print_routing_to_category(category):
    print(f"\nRouting to category: {category}")

def print_documents_retrieved_from_vector_db(results):
    print("\n--- Retrieved Documents ---")

    for r, score in results:
        print(
            f"""
    Source: {r.metadata.get('source')}
    Category: {r.metadata.get('category')}
    Score: {score}
    """
        )

def print_reranked_results(reranked_results):
        print("\n--- Reranked ---")

        for r, score in reranked_results:

            print(
                f"""
    Source: {r.metadata.get('source')}
    Rerank Score: {score}
        """
            )

def print_prompt(prompt):
    print("\n--- PROMPT ---\n")
    print(f"{prompt}")

def print_answer(response):
    print("\n--- ANSWER ---\n")
    print(response)

def run():

    current_topic = None
    chat_history = []

    while True:

        query = input("\nAsk a question (or 'exit'): ")

        if query.lower() == "exit":
            break

        result = process_query(
            query,
            chat_history,
            current_topic
        )

        print_answer(result["response"])
        print(f"Source: {result["source"]}")
        print(f"Distance: {result["distance"]}")

        chat_history.append(f"User: {result["rewritten_query"]}")
        chat_history.append(f"Assistant: {result["response"]}")
        chat_history.append(f"Topic: {result["category"]}")

        current_topic = result["current_topic"]

if __name__ == "__main__":

    run()