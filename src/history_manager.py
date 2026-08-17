import json
from pathlib import Path
from datetime import datetime


HISTORY_DIR = Path("evaluation_history")


def save_evaluation(question, response, evaluation):
    """
    Save an evaluation as a JSON file.
    """

    HISTORY_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = HISTORY_DIR / f"evaluation_{timestamp}.json"

    data = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "response": response,
        "evaluation": evaluation
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    return file_path