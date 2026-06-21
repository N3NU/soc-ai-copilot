

def category_classifier_prompt(query):
    prompt = f"""
    Classify the cybersecurity query into ONE category.
    For example, if the query says "What are mimikatz indicators?" you would response with "ransomware" because that is the category.

    Categories:

    ransomware
    phishing
    account_compromise
    credential_access
    lateral_movement
    beaconing
    network_intrusion
    data_exfiltration
    privilege_escalation
    suspicious_powershell
    impossible_travel
    suspicious_login
    web_shell
    insider_threat
    cloud_security
    identity
    incident_response

    Return ONLY the category name.

    Query:
    {query}
    """
    return prompt
