import os
import time
from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# 🧠 Model priority list (fallback chain)
MODELS = [
    "gemini-1.5-flash",   # fastest + most stable
    "gemini-1.5-pro",     # smarter fallback
]

def ask_agent(message, max_retries=2):

    last_error = None

    # 🔁 Try multiple models
    for model in MODELS:

        # 🔁 Retry per model
        for attempt in range(max_retries):

            try:
                response = client.models.generate_content(
                    model=model,
                    contents=message
                )

                if response and response.text:
                    return response.text

            except Exception as e:
                last_error = str(e)

                # ⏳ wait before retry (avoid rate limit)
                time.sleep(2 * (attempt + 1))

                continue

    # 🛑 Final fallback (never crash UI)
    return f"""
⚠️ Agent temporarily unavailable.

Technical info:
{last_error}

Please try again in a few seconds.
"""
