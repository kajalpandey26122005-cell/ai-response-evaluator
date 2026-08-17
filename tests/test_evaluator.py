import pytest

from src.evaluator import (
    evaluate_correctness,
    evaluate_relevance,
    evaluate_completeness,
    evaluate_clarity,
    calculate_overall_score,
    evaluate_response,
    compare_responses
)


def test_correct_binary_search():
    question = "What is binary search?"
    response = (
        "Binary search is a searching algorithm that works on "
        "a sorted array and has O(log n) time complexity."
    )

    assert evaluate_correctness(question, response) == 10


def test_incorrect_binary_search_complexity():
    question = "What is binary search?"
    response = (
        "Binary search searches a sorted array and has "
        "O(n) time complexity."
    )

    assert evaluate_correctness(question, response) == 3


def test_relevance():
    question = "What is binary search?"
    response = (
        "Binary search is an algorithm used to search "
        "a sorted array."
    )

    assert evaluate_relevance(question, response) >= 8


def test_completeness():
    question = "Explain binary search."

    response = (
        "Binary search is a searching algorithm used on sorted data. "
        "It repeatedly divides the search space into two halves. "
        "It compares the middle element with the target and eliminates "
        "the half that cannot contain the target. Its time complexity "
        "is O(log n)."
    )

    assert evaluate_completeness(question, response) == 9


def test_overall_score():
    scores = {
        "correctness": 10,
        "relevance": 8,
        "completeness": 6,
        "clarity": 8
    }

    assert calculate_overall_score(scores) == 8.0


def test_compare_responses():
    question = "What is binary search?"

    response_a = (
        "Binary search is a searching algorithm that works on "
        "a sorted array and has O(log n) time complexity."
    )

    response_b = (
        "Binary search searches an array using O(n) time."
    )

    result = compare_responses(
        question,
        response_a,
        response_b
    )

    assert result["response_a"]["correctness"] == 10
    assert result["response_b"]["correctness"] == 3
    assert result["winner"] == "Response A"
def test_evaluate_response_includes_hallucination_risk():
    question = "What is binary search?"

    response = (
        "Binary search is a searching algorithm "
        "with O(n) time complexity."
    )

    result = evaluate_response(question, response)

    assert "hallucination_risk" in result
    assert result["hallucination_risk"] == "Medium"


def test_correct_response_has_low_hallucination_risk():
    question = "What is binary search?"

    response = (
        "Binary search is a searching algorithm that works "
        "on a sorted array and has O(log n) time complexity."
    )

    result = evaluate_response(question, response)

    assert result["hallucination_risk"] == "Low"
def test_evaluation_contains_all_scores():
    result = evaluate_response(
        "What is binary search?",
        "Binary search works on a sorted array and has O(log n) time complexity."
    )

    expected_keys = {
        "correctness",
        "relevance",
        "completeness",
        "clarity",
        "overall",
        "hallucination_risk"
    }

    assert expected_keys.issubset(result.keys())


def test_overall_score_is_between_zero_and_ten():
    result = evaluate_response(
        "What is binary search?",
        "Binary search works on a sorted array and has O(log n) time complexity."
    )

    assert 0 <= result["overall"] <= 10