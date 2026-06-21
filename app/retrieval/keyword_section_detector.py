def keyword_section_detector(query):

    query = query.lower()

    if "purpose" in query:
        return "purpose"
    
    elif "indicator" in query:
        return "indicators"

    elif "initial action" in query:
        return "initial_actions"

    elif "containment" in query:
        return "containment"

    elif "eradication" in query:
        return "eradication"

    elif "recovery" in query:
        return "recovery"

    elif "communication" in query:
        return "communication"

    elif "escalation" in query:
        return "escalation"

    elif "reference" in query:
        return "references"

    return None