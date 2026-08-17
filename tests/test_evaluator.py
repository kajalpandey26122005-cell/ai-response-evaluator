from src.evaluator import evaluate_response


def test_correct_binary_search_response():

    question = "What is binary search?"

    response = (
        "Binary search is a searching algorithm that works "
        "on a sorted array. Its time complexity is O(log n)."
    )

    result = evaluate_response(question, response)

    assert result["correctness"] == 10


def test_incorrect_binary_search_complexity():

    question = "What is binary search?"

    response = (
        "Binary search is a searching algorithm. "
        "Its time complexity is O(n)."
    )

    result = evaluate_response(question, response)

    assert result["correctness"] == 3
def test_binary_search_correct_answer():
    result = evaluate_response(
        "What is binary search?",
        "Binary search works on a sorted array and has O(log n) time complexity."
    )

    assert result["correctness"] == 10


def test_binary_search_wrong_answer():
    result = evaluate_response(
        "What is binary search?",
        "Binary search works on a sorted array and has O(n) time complexity."
    )

    assert result["correctness"] == 3


def test_overall_score_exists():
    result = evaluate_response(
        "What is binary search?",
        "Binary search works on a sorted array and has O(log n) time complexity."
    )

    assert "overall" in result
    assert 0 <= result["overall"] <= 10