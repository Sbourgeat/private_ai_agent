import argparse
import os

from dotenv import load_dotenv
from google import genai

MODEL = "gemini-2.5-flash"

load_dotenv()
try:
    api_key = os.environ.get("GEMINI_APIKEY")
except Exception as e:
    raise RuntimeError(f"Error loading API key: {e}")


if __name__ == "__main__":
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response = client.models.generate_content(
        model=MODEL,
        contents=args.user_prompt,
    )
    if response:
        print(f"User prompt: {args.user_prompt}")
        if response.usage_metadata:
            prompt_token = response.usage_metadata.prompt_token_count
            response_token = response.usage_metadata.candidates_token_count
            print(f"Prompt tokens: {prompt_token}")
            print(f"Response tokens: {response_token}")
            print(f"Response: {response.text}")

        else:
            raise RuntimeError("Usage metadata not found")
    else:
        raise RuntimeError("Response not found")
