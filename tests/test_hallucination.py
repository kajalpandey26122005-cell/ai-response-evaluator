from src.hallucination import (
    detect_potential_inconsistency,
    hallucination_risk
)


def test_binary_search_inconsistency():
    question = "What is binary search?"

    response = (
        "Binary search is a searching algorithm "
        "with O(n) time complexity."
    )

    warnings = detect_potential_inconsistency(
        question,
        response
    )

    assert len(warnings) == 1


def test_correct_binary_search():
    question = "What is binary search?"

    response = (
        "Binary search is a searching algorithm "
        "with O(log n) time complexity."
    )

    warnings = detect_potential_inconsistency(
        question,
        response
    )

    assert len(warnings) == 0


def test_low_hallucination_risk():
    question = "What is binary search?"

    response = (
        "Binary search works on sorted data "
        "and has O(log n) time complexity."
    )

    assert hallucination_risk(
        question,
        response
    ) == "Low"


def test_medium_hallucination_risk():
    question = "What is binary search?"

    response = (
        "Binary search has O(n) time complexity."
    )

    assert hallucination_risk(
        question,
        response
    ) == "Medium"