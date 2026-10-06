import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(API_KEY))

if not API_KEY:
    print("ERROR: GEMINI_API_KEY not found in .env")
    exit()

try:
    client = genai.Client(api_key=API_KEY)

    print("Sending test question to Gemini...")

    response = client.interactions.create(
        model="gemini-3.5-flash",
        input="What is Python? Answer in 2 simple sentences."
    )

    print("\nGemini response:")
    print(response.output_text)

except Exception as e:
    print("\nGemini Error:")
    print(type(e).__name__)
    print(e)