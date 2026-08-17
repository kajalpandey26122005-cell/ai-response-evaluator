from src.evaluator import evaluate_response, compare_responses


def print_evaluation(result):
    """
    Display evaluation results in a readable format.
    """

    print("\n========== EVALUATION ==========")

    print(f"\nCorrectness:        {result['correctness']}/10")
    print(f"Relevance:          {result['relevance']}/10")
    print(f"Completeness:       {result['completeness']}/10")
    print(f"Clarity:            {result['clarity']}/10")
    print(f"Overall Score:      {result['overall']}/10")
    print(f"Hallucination Risk: {result['hallucination_risk']}")

    print("\n========== FEEDBACK ==========")

    for feedback in result["feedback"]:
        print(f"- {feedback}")


def evaluate_single_response():
    """
    Evaluate one AI-generated response.
    """

    print("\n========== SINGLE RESPONSE EVALUATION ==========")

    question = input("\nEnter your question: ")
    response = input("\nEnter the AI response: ")

    result = evaluate_response(question, response)

    print_evaluation(result)


def compare_two_responses():
    """
    Compare two AI-generated responses to the same question.
    """

    print("\n========== RESPONSE COMPARISON ==========")

    question = input("\nEnter your question: ")

    response_a = input("\nEnter Response A: ")

    response_b = input("\nEnter Response B: ")

    result = compare_responses(
        question,
        response_a,
        response_b
    )

    print("\n========== RESPONSE A ==========")
    print_evaluation(result["response_a"])

    print("\n========== RESPONSE B ==========")
    print_evaluation(result["response_b"])

    print("\n========== COMPARISON ==========")
    print(f"Winner: {result['winner']}")


def main():
    """
    Main program.
    """

    print("========================================")
    print("        AI RESPONSE EVALUATOR")
    print("========================================")

    print("\n1. Evaluate one response")
    print("2. Compare two responses")

    choice = input("\nChoose an option (1 or 2): ")

    if choice == "1":
        evaluate_single_response()

    elif choice == "2":
        compare_two_responses()

    else:
        print("\nInvalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()