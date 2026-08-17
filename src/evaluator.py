from src.hallucination import hallucination_risk


def evaluate_correctness(question, response):
    """
    Evaluate the correctness of an AI response.

    This is a simple rule-based prototype.
    It is NOT a general-purpose fact checker.
    """

    question_lower = question.lower()
    response_lower = response.lower()

    # Binary search rule
    if "binary search" in question_lower:
        if "o(log n)" in response_lower:
            return 10
        elif "o(n)" in response_lower:
            return 3
        else:
            return 5

    # Python rule
    if "python" in question_lower:
        if "programming language" in response_lower:
            return 10
        elif "database" in response_lower:
            return 3
        else:
            return 5

    # Default prototype score
    if not response.strip():
        return 0

    return 5


def evaluate_relevance(question, response):
    """
    Estimate whether the response is related to the question.

    This is a simple keyword-overlap prototype.
    """

    question_words = set(question.lower().split())
    response_words = set(response.lower().split())

    common_words = question_words.intersection(response_words)

    if len(common_words) >= 3:
        return 10
    elif len(common_words) >= 2:
        return 8
    elif len(common_words) == 1:
        return 6
    else:
        return 3


def evaluate_completeness(question, response):
    """
    Estimate completeness based on response length.

    This is only a prototype.
    """

    word_count = len(response.split())

    if word_count >= 30:
        return 9
    elif word_count >= 15:
        return 7
    elif word_count >= 5:
        return 5
    else:
        return 3


def evaluate_clarity(response):
    """
    Estimate clarity using simple response-length rules.
    """

    word_count = len(response.split())

    if word_count == 0:
        return 0
    elif word_count <= 50:
        return 8
    elif word_count <= 100:
        return 6
    else:
        return 4


def calculate_overall_score(scores):
    """
    Calculate the average score of all evaluation criteria.
    """

    criteria = [
        "correctness",
        "relevance",
        "completeness",
        "clarity"
    ]

    total = sum(scores[criterion] for criterion in criteria)

    return round(total / len(criteria), 2)


def generate_feedback(scores):
    """
    Generate feedback based on the evaluation scores.
    """

    feedback = []

    # Correctness
    if scores["correctness"] < 5:
        feedback.append(
            "The response may contain a factual or technical error."
        )
    elif scores["correctness"] < 8:
        feedback.append(
            "The response is partially correct but could be more accurate."
        )
    else:
        feedback.append(
            "The response appears technically correct."
        )

    # Relevance
    if scores["relevance"] < 5:
        feedback.append(
            "The response is not sufficiently related to the question."
        )
    elif scores["relevance"] < 8:
        feedback.append(
            "The response is relevant but could focus more directly on the question."
        )
    else:
        feedback.append(
            "The response is relevant to the question."
        )

    # Completeness
    if scores["completeness"] < 5:
        feedback.append(
            "The response is too short and misses important information."
        )
    elif scores["completeness"] < 8:
        feedback.append(
            "The response covers the basic idea but could provide more detail."
        )
    else:
        feedback.append(
            "The response provides a reasonably complete explanation."
        )

    # Clarity
    if scores["clarity"] < 5:
        feedback.append(
            "The response could be clearer and easier to understand."
        )
    else:
        feedback.append(
            "The response is reasonably clear."
        )

    return feedback


def evaluate_response(question, response):
    """
    Evaluate an AI-generated response on all criteria.
    """

    # Input validation
    if not isinstance(question, str):
        raise TypeError("Question must be a string.")

    if not isinstance(response, str):
        raise TypeError("Response must be a string.")

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if not response.strip():
        raise ValueError("Response cannot be empty.")

    # Evaluate each criterion
    scores = {
        "correctness": evaluate_correctness(question, response),
        "relevance": evaluate_relevance(question, response),
        "completeness": evaluate_completeness(question, response),
        "clarity": evaluate_clarity(response)
    }

    # Overall score
    scores["overall"] = calculate_overall_score(scores)

    # Hallucination risk
    scores["hallucination_risk"] = hallucination_risk(
        question,
        response
    )

    # Feedback
    scores["feedback"] = generate_feedback(scores)

    return scores


def compare_responses(question, response_a, response_b):
    """
    Evaluate two AI responses and determine which one is better.
    """

    result_a = evaluate_response(question, response_a)
    result_b = evaluate_response(question, response_b)

    if result_a["overall"] > result_b["overall"]:
        winner = "Response A"
    elif result_b["overall"] > result_a["overall"]:
        winner = "Response B"
    else:
        winner = "Tie"

    return {
        "response_a": result_a,
        "response_b": result_b,
        "winner": winner
    }