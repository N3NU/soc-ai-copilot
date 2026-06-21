def section_classifier_prompt(query):
    prompt = f"""
    Classify the cybersecurity query into ONE section.

    sections:

    purpose
    indicators
    initial_actions
    containment
    eradication
    recovery
    communication
    escalation
    references

    Return ONLY the section name.

    Query:
    {query}
    """
#   print(f"section:{prompt}")
    return prompt