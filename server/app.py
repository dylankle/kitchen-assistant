from google import genai
from dotenv import find_dotenv, load_dotenv
import os

def main():
    env_path = find_dotenv()
    load_dotenv(env_path)
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Is tarragon and vanilla a good flavor combination for butter poached lobster?"
    )

    print(response.text)

main()
