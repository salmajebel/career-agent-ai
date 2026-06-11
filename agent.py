import os
from google import genai

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(
    api_key=api_key
)

def ask_agent(message):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=message
    )
    return response.text
