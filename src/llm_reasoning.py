from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_clause(clause_text, risk_name):
    prompt = f"""
You are a legal assistant for Indian small businesses.

Clause:
{clause_text}

Task:
1. Explain this clause in very simple business English
2. Why is this clause risky for an SME?
3. Suggest a safer alternative clause wording

Keep response short and clear.
"""

    #response = client.ChatCompletion.create(
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
