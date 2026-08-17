# from src.llm_evaluator import evaluate_with_llm
from src.hybrid_evaluator import evaluate_hybrid
from src.history_manager import save_evaluation


def display_evaluation(question, response, evaluation):
    print("\n========== LLM EVALUATION ==========")

    print("\nQuestion:")
    print(question)

    print("\nAI Response:")
    print(response)

    print("\n------------------------------------")

    print(f"Correctness    : {evaluation['correctness']}/10")
    print(f"Relevance      : {evaluation['relevance']}/10")
    print(f"Clarity        : {evaluation['clarity']}/10")
    print(f"Completeness   : {evaluation['completeness']}/10")

    print(f"\nOverall Score  : {evaluation['overall_score']}/10")

    print("\nFeedback:")
    print(evaluation["feedback"])
    print("\nRule-Based Issues:")

    if evaluation["rule_issues"]:
        for issue in evaluation["rule_issues"]:
            print(f"- {issue}")
    else:
        print("No major rule-based issues detected.")

    print("\n====================================")



def evaluate_single_response():
    print("\n========== SINGLE RESPONSE EVALUATION ==========\n")

    question = input("Enter your question: ")
    response = input("\nEnter the AI response: ")

    print("\nEvaluating response using Gemini...")
    print("Please wait...")

    try:
        evaluation = evaluate_hybrid(question,response)

        display_evaluation(question,response,evaluation)

        file_path = save_evaluation(question,response,evaluation)

        print(f"\nEvaluation saved to: {file_path}")

    except Exception as e:
        print("\nAn error occurred while evaluating the response.")
        print(f"Error: {e}")


def main():
    while True:
        print("\n========================================")
        print("        AI RESPONSE EVALUATOR")
        print("========================================")

        print("\n1. Evaluate one response")
        print("2. Exit")

        choice = input("\nChoose an option (1 or 2): ")

        if choice == "1":
            evaluate_single_response()

        elif choice == "2":
            print("\nExiting AI Response Evaluator...")
            break

        else:
            print("\nInvalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()