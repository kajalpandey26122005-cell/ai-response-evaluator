from src.evaluator import evaluate_response


def main():
    print("=================================")
    print("       AI RESPONSE EVALUATOR")
    print("=================================")

    question = input("\nEnter your question: ")

    response = input("\nEnter the AI response: ")

    result = evaluate_response(question, response)

    print("\n========== EVALUATION ==========")

    print(f"\nCorrectness:    {result['correctness']}/10")
    print(f"Relevance:      {result['relevance']}/10")
    print(f"Completeness:   {result['completeness']}/10")
    print(f"Clarity:        {result['clarity']}/10")

    print("\n========== FEEDBACK ==========")

    for feedback in result["feedback"]:
        print(f"- {feedback}")


if __name__ == "__main__":
    main()