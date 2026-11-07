"""
The brain for lesson 5. Every file here uses it.
Want a different brain? Change it here, in one place. (We do that in lesson 6.)

Agentic AI Zero to Hero by Pavan Elthepu (@pavanelthepu)
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads GEMINI_API_KEY from your .env file

# A free Gemini model. If you get "model not found", open aistudio.google.com,
# pick any free "Flash" model, and paste its name here.
MODEL = "gemini-3.8-flash"

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit(
        "No API key found.\n"
        "1. Copy .env.example to a new file called .env\n"
        "2. Paste your free key from aistudio.google.com after GEMINI_API_KEY=\n"
        "3. Run the file again."
    )

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def ask(messages, temperature=None):
    """Send a message (or a list of messages) to the brain. Get its reply text back."""
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    extra = {} if temperature is None else {"temperature": temperature}
    reply = client.chat.completions.create(model=MODEL, messages=messages, **extra)
    return reply.choices[0].message.content
