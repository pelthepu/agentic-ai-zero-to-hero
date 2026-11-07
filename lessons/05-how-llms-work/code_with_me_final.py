"""
Lesson 5: the file we write together in the video ("Code with me"), as it looks at the end.
Change the `question` line to try the other mysteries.

Run:  uv run code_with_me_final.py
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # read GEMINI_API_KEY from the .env file

client = OpenAI(  # connect to the brain (a free Gemini model)
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

question = "What time does flight SK 999 from Delhi land in Tokyo? Reply with the time only."

reply = client.chat.completions.create(  # send the message
    model="gemini-3.8-flash",
    messages=[{"role": "user", "content": question}],
    temperature=0,  # mystery 2: low = nearly the same answer every time
    stream=True,    # mystery 1: get each piece the moment it is written
)

for chunk in reply:  # print each piece as it arrives
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
