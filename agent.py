import os
from google import genai

# =========================
# INIT CLIENT
# =========================
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Missing GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

# =========================
# CHAT MEMORY (simple in RAM)
# =========================
chat = client.chats.create(
    model="gemini-1.5-flash"
)

# =========================
# MAIN CHAT FUNCTION
# =========================
def ask_agent(message):
    """
    Free chat agent:
    - user can ask anything
    - CV, jobs, roadmap, LaTeX, etc.
    """

    try:
        response = chat.send_message(message)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
