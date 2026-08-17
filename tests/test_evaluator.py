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