from app.retrieval.detect_category_service import detect_category
from app.retrieval.detect_section_service import detect_section

TEST_CASES = [

    {
        "query": "What are ransomware indicators?",
        "expected_category": "ransomware",
        "expected_section": "indicators"
    },

    {
        "query": "How do I contain a phishing attack?",
        "expected_category": "phishing",
        "expected_section": "containment"
    },

    {
        "query": "What are signs of credential dumping?",
        "expected_category": "credential_access",
        "expected_section": "indicators"
    },

    {
        "query": "How do I recover from ransomware?",
        "expected_category": "ransomware",
        "expected_section": "recovery"
    },

    {
        "query": "What are psexec indicators?",
        "expected_category": "lateral_movement",
        "expected_section": "indicators"
    }
]

def run_tests():

    passed = 0

    for test in TEST_CASES:

        category = detect_category(
            test["query"]
        )

        section = detect_section(
            test["query"]
        )

        category_pass = (
            category ==
            test["expected_category"]
        )

        section_pass = (
            section ==
            test["expected_section"]
        )

        if category_pass and section_pass:
            passed += 1

        print(
            f"""
Query: {test['query']}
Expected Category: {test['expected_category']}
Actual Category: {category}

Expected Section: {test['expected_section']}
Actual Section: {section}

PASS: {category_pass and section_pass}
"""
        )

    print(
        f"\nPassed {passed}/{len(TEST_CASES)}"
    )


if __name__ == "__main__":
    run_tests()
