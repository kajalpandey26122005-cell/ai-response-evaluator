from src.llm_evaluator import evaluate_with_llm
from src.rule_evaluator import evaluate_with_rules


def evaluate_hybrid(question, response):
    """
    Combine rule-based evaluation with Gemini evaluation.
    """

    # Get rule-based evaluation
    rule_result = evaluate_with_rules(
        question,
        response
    )

    # Get Gemini evaluation
    llm_result = evaluate_with_llm(
        question,
        response
    )

    # Combine scores
    final_evaluation = {
        "correctness": llm_result["correctness"],

        "relevance": (
            llm_result["relevance"] * 0.7
            + rule_result["relevance"] * 0.3
        ),

        "clarity": (
            llm_result["clarity"] * 0.7
            + rule_result["clarity"] * 0.3
        ),

        "completeness": (
            llm_result["completeness"] * 0.7
            + rule_result["completeness"] * 0.3
        ),

        "feedback": llm_result["feedback"],

        "rule_issues": rule_result["issues"]
    }

    # Calculate final overall score
    final_evaluation["overall_score"] = round(
        (
            final_evaluation["correctness"]
            + final_evaluation["relevance"]
            + final_evaluation["clarity"]
            + final_evaluation["completeness"]
        ) / 4,
        2
    )

    # Round individual scores
    final_evaluation["relevance"] = round(
        final_evaluation["relevance"], 2
    )

    final_evaluation["clarity"] = round(
        final_evaluation["clarity"], 2
    )

    final_evaluation["completeness"] = round(
        final_evaluation["completeness"], 2
    )

    return final_evaluation