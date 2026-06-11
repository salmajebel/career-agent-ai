import os
from google.genai import Client

client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_agent(message):
    return client.models.generate_content(
        model="models/gemini-1.5-flash",
        contents=message
    ).text
