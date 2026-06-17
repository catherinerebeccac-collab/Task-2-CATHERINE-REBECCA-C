import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llama3.2:1b"


def generate_response(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        return result["response"]

    except Exception as e:

        return f"ERROR: {str(e)}"