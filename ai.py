from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def get_response(command):

    response = client.responses.create(
        model="gpt-5",
        instructions=(
            "You are Jarvis, a helpful virtual assistant. "
            "Give concise and useful answers."
        ),
        input=command
    )

    return response.output_text