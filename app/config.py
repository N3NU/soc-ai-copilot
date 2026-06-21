DOCS_PATH = "./docs"

DB_PATH = "./chroma_db"
COLLECTION_NAME = "secure_rag"

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3"

RETRIEVAL_K = 4
MAX_CHAT_HISTORY = 30

META_KEYS = [
    "TITLE",
    "DOCUMENT_TYPE",
    "CATEGORY",
    "DEPARTMENT",
    "SEVERITY",
    "VERSION",
    "CLASSIFICATION",
    "LAST_UPDATED"
]

CATEGORY_KEYWORDS = {

    "ransomware": [
        "ransomware",
        "ransom note",
        "encrypted files",
        "file encryption",
        "mass encryption",
        "crypto locker",
        "locker malware"
    ],

    "phishing": [
        "phishing",
        "malicious email",
        "suspicious email",
        "email attachment",
        "email link",
        "credential harvesting",
        "fake login page"
    ],

    "account_compromise": [
        "account compromise",
        "compromised account",
        "hijacked account",
        "stolen account",
        "account takeover",
        "ato"
    ],

    "credential_access": [
        "credential dumping",
        "dumped credentials",
        "mimikatz",
        "lsass",
        "sekurlsa",
        "password hashes",
        "credential theft"
    ],

    "lateral_movement": [
        "lateral movement",
        "psexec",
        "remote execution",
        "pivoting",
        "wmic",
        "smb movement"
    ],

    "beaconing": [
        "beaconing",
        "c2",
        "command and control",
        "periodic traffic",
        "callback traffic",
        "check-in traffic"
    ],

    "network_intrusion": [
        "network intrusion",
        "intrusion",
        "unauthorized access",
        "network breach",
        "network compromise"
    ],

    "data_exfiltration": [
        "data exfiltration",
        "data theft",
        "large upload",
        "sensitive data transfer",
        "unauthorized transfer",
        "exfiltration"
    ],

    "privilege_escalation": [
        "privilege escalation",
        "elevated privileges",
        "administrator access",
        "root access",
        "token manipulation"
    ],

    "suspicious_powershell": [
        "powershell",
        "encodedcommand",
        "invoke-expression",
        "iex",
        "suspicious powershell"
    ],

    "impossible_travel": [
        "geographic anomaly",
        "multiple login locations",
        "login from different countries",
  #      "travel alert"
    ],

    "suspicious_login": [
        "suspicious login",
        "failed login",
        "brute force",
        "password spray",
        "unusual authentication"
    ],

    "web_shell": [
        "web shell",
        "webshell",
        "cmd.aspx",
        "shell upload",
        "shell access"
    ],

    "insider_threat": [
        "insider threat",
        "malicious insider",
        "employee misuse",
        "data theft by employee",
        "rogue employee"
    ],

    "cloud_security": [
        "cloud security",
        "aws",
        "azure",
        "gcp",
        "cloud compromise",
        "public bucket",
        "cloud incident"
    ],

    "identity": [
        "impossible travel",
        "password",
        "credential",
        "authentication",
        "identity",
        "mfa",
        "login",
        "access control"
    ],

    "incident_response": [
        "incident",
        "security incident",
        "incident response",
        "ir process",
        "containment",
        "eradication",
        "recovery"
    ]
}

SECTION_KEYWORDS = [
    "purpose",
    "indicators",
    "initial_actions",
    "containment",
    "eradication",
    "recovery",
    "communication",
    "escalation",
    "references"
]