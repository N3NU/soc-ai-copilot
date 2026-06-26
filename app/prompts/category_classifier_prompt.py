
def category_classifier_prompt(query):
    return f"""
Classify the cybersecurity query into ONE category.

Valid categories:

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

If the query:
- is unrelated to cybersecurity,
- is gibberish,
- is too vague,
- or cannot confidently be assigned to exactly one category,

return ONLY:

none

Otherwise return ONLY the category name.

Query:
{query}
"""