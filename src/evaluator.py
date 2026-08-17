def evaluate_correctness(question, response):
    """
    Evaluate the correctness of an AI response.

    This is a simple rule-based prototype.
    It is NOT a general-purpose fact checker.
    """

    question_lower = question.lower()
    response_lower = response.lower()

    # Simple example rule for binary search
    if "binary search" in question_lower:
        if "o(log n)" in response_lower:
            return 10
        elif "o(n)" in response_lower:
            return 3
        else:
            return 5

    # Default score when we don't have a specific rule
    return 5


def evaluate_relevance(question, response):
    """
    Check whether the response is related to the question.
    """

    question_words = set(question.lower().split())
    response_words = set(response.lower().split())

    common_words = question_words.intersection(response_words)

    if len(common_words) >= 2:
        return 8
    elif len(common_words) == 1:
        return 6
    else:
        return 3


def evaluate_completeness(question, response):
    """
    Estimate completeness based on response length.

    This is only a simple prototype.
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
    Estimate clarity using simple sentence/length rules.
    """

    word_count = len(response.split())

    if word_count <= 50:
        return 8
    elif word_count <= 100:
        return 6
    else:
        return 4


def calculate_overall_score(scores):
    """
    Calculate the average score across all evaluation criteria.
    """

    total = (
        scores["correctness"]
        + scores["relevance"]
        + scores["completeness"]
        + scores["clarity"]
    )

    return round(total / 4, 2)


def generate_feedback(scores):
    """
    Generate simple feedback based on evaluation scores.

    This is rule-based feedback, not an LLM-generated explanation.
    """

    feedback = []

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
    Evaluate an AI-generated response using all criteria.
    """

    correctness = evaluate_correctness(question, response)
    relevance = evaluate_relevance(question, response)
    completeness = evaluate_completeness(question, response)
    clarity = evaluate_clarity(response)

    overall = (
        correctness
        + relevance
        + completeness
        + clarity
    ) / 4

    scores = {
        "correctness": correctness,
        "relevance": relevance,
        "completeness": completeness,
        "clarity": clarity,
        "overall": round(overall, 2)
    }

    scores["feedback"] = generate_feedback(scores)

    return scores