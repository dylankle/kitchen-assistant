from google import genai
from dotenv import find_dotenv, load_dotenv
import os

resources = ["tarragon and vanilla is disgusting",
             "tarragon does not taste good with lobster",
             "vanilla does not emulsify with butter well"]

def prompt_builder(user_prompt: str) -> str:
    context = "\n".join(resources)

    return (
        f"Your job is to evaluate the flavor compatibility of ingredients."
        f"Do NOT include phrases like based on the context according to the above or provided information"
        f"Context:\n{context}\n"
        f"Question:\n{user_prompt}\n"
    )

def main():
    env_path = find_dotenv()
    load_dotenv(env_path)
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt_builder("Is tarragon and vanilla a good flavor combination for butter poached lobster?"),
    )

    print(response.text)

main()
