def section_classifier_prompt(query):
    prompt = f"""
    Classify the cybersecurity query into ONE section.

    If the query does not clearly match any section, return:
    none

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

    Return ONLY the section name or none.

    Query:
    {query}
    """
#   print(f"section:{prompt}")
    return prompt