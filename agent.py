import os
from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def ask_agent(message):

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=message
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
