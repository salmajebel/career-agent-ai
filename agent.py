from google import genai
import os

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

chat = client.chats.create(model="gemini-3.5-flash")

def ask_agent(message):
    response = chat.send_message(message)
    return response.text
