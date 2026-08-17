import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

client = genai.Client(api_key=api_key)


def validate_evaluation(evaluation):
    """Validate the structure and values returned by Gemini."""

    required_fields = [
        "correctness",
        "relevance",
        "clarity",
        "completeness",
        "overall_score",
        "feedback"
    ]

    # Check that all required fields exist
    for field in required_fields:
        if field not in evaluation:
            raise ValueError(
                f"Gemini response is missing required field: {field}"
            )

    # Check score fields
    score_fields = [
        "correctness",
        "relevance",
        "clarity",
        "completeness",
        "overall_score"
    ]

    for field in score_fields:
        score = evaluation[field]

        if not isinstance(score, (int, float)):
            raise ValueError(
                f"{field} must be a number."
            )

        if not 0 <= score <= 10:
            raise ValueError(
                f"{field} must be between 0 and 10."
            )

    # Check feedback
    if not isinstance(evaluation["feedback"], str):
        raise ValueError("feedback must be a string.")

    return evaluation


def evaluate_with_llm(question, response):

    prompt = f"""
You are an AI response evaluator.

Evaluate the following AI response.

QUESTION:
{question}

AI RESPONSE:
{response}

Evaluate the response on these criteria:

1. correctness
2. relevance
3. clarity
4. completeness

Give each score from 0 to 10.

Calculate an overall score from 0 to 10.

Return ONLY valid JSON in exactly this format:

{{
    "correctness": 0,
    "relevance": 0,
    "clarity": 0,
    "completeness": 0,
    "overall_score": 0,
    "feedback": ""
}}

Rules:

- All scores must be numbers between 0 and 10.
- feedback must be a string.
- Do not use markdown.
- Do not use ```json.
- Return only JSON.
"""

    try:
        result = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        text = result.text.strip()

        # Remove markdown code fences if Gemini accidentally adds them
        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        evaluation = json.loads(text)

        # Validate Gemini's response
        evaluation = validate_evaluation(evaluation)

        return evaluation

    except json.JSONDecodeError:
        raise ValueError(
            "Gemini returned invalid JSON."
        )

    except Exception as e:
        raise RuntimeError(
            f"Gemini evaluation failed: {e}"
        )