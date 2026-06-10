from google import genai

client = genai.Client()

def career_agent(cv):

    prompt = f"""
You are CareerAgent, an AI career assistant.

TASKS:
1. Analyze CV
2. Extract skills
3. Suggest jobs
4. Create ATS improvement
5. Generate LaTeX CV (if possible)

CV:
{cv}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
