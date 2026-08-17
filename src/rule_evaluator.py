def evaluate_with_rules(question, response):
    """
    Perform basic rule-based evaluation of an AI response.
    """

    evaluation = {
        "relevance": 0,
        "clarity": 0,
        "completeness": 0,
        "issues": []
    }

    question = question.strip()
    response = response.strip()

    # -----------------------------------
    # 1. Check whether response is empty
    # -----------------------------------

    if not response:
        evaluation["issues"].append("Response is empty.")
        return evaluation

    # -----------------------------------
    # 2. Response length
    # -----------------------------------

    word_count = len(response.split())

    if word_count < 5:
        evaluation["completeness"] = 2
        evaluation["issues"].append(
            "Response is too short."
        )

    elif word_count < 15:
        evaluation["completeness"] = 5

    elif word_count < 40:
        evaluation["completeness"] = 7

    else:
        evaluation["completeness"] = 9

    # -----------------------------------
    # 3. Basic relevance check
    # -----------------------------------

    question_words = set(question.lower().split())
    response_words = set(response.lower().split())

    # Remove very common words
    stop_words = {
        "what", "is", "a", "an", "the",
        "of", "to", "in", "for", "and",
        "how", "why", "are", "on"
    }

    meaningful_question_words = (
        question_words - stop_words
    )

    if meaningful_question_words:
        overlap = (
            meaningful_question_words
            & response_words
        )

        overlap_ratio = (
            len(overlap)
            / len(meaningful_question_words)
        )

        if overlap_ratio >= 0.6:
            evaluation["relevance"] = 9

        elif overlap_ratio >= 0.3:
            evaluation["relevance"] = 6

        else:
            evaluation["relevance"] = 3

    else:
        evaluation["relevance"] = 5

    # -----------------------------------
    # 4. Basic clarity check
    # -----------------------------------

    sentences = [
        sentence.strip()
        for sentence in response.split(".")
        if sentence.strip()
    ]

    if len(sentences) == 0:
        evaluation["clarity"] = 3

    else:
        average_sentence_length = (
            word_count / len(sentences)
        )

        if average_sentence_length <= 25:
            evaluation["clarity"] = 9

        elif average_sentence_length <= 40:
            evaluation["clarity"] = 7

        else:
            evaluation["clarity"] = 5
            evaluation["issues"].append(
                "Some sentences may be too long."
            )

    return evaluation