def detect_potential_inconsistency(question, response):
    """
    Prototype heuristic for identifying potential factual inconsistencies.

    IMPORTANT:
    This is NOT a reliable hallucination detector.
    It only checks a few known factual patterns.
    """

    question_lower = question.lower()
    response_lower = response.lower()

    warnings = []

    # Binary search complexity check
    if "binary search" in question_lower:
        if "o(n)" in response_lower:
            warnings.append(
                "Potential factual inconsistency: "
                "binary search is generally O(log n) for a sorted array, "
                "not O(n)."
            )

    # Python language check
    if "python" in question_lower:
        if "python is a database" in response_lower:
            warnings.append(
                "Potential factual inconsistency: "
                "Python is a programming language, not a database."
            )

    # Empty response
    if not response.strip():
        warnings.append(
            "The response is empty."
        )

    return warnings


def hallucination_risk(question, response):
    """
    Assign a simple heuristic risk level.

    This is a prototype and should not be treated
    as a factual verification system.
    """

    warnings = detect_potential_inconsistency(question, response)

    if len(warnings) == 0:
        return "Low"

    elif len(warnings) == 1:
        return "Medium"

    else:
        return "High"