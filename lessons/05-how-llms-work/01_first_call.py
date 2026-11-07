"""
Lesson 5, file 1: your first AI code. One call to an LLM.

Run:  uv run 01_first_call.py
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 1. read your secret key from the .env file

client = OpenAI(  # 2. connect to the brain (a free Gemini model)
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

reply = client.chat.completions.create(  # 3. send it a message
    model="gemini-3.8-flash",
    messages=[{"role": "user",
               "content": "Plan a 5-day trip to Japan in 3 short lines."}],
)

print(reply.choices[0].message.content)  # 4. print what it says back
