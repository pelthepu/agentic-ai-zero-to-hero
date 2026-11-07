"""
Lesson 5, file 4: the brain forgets you after every call.
To make it "remember", we send the whole chat again, every time.

Run:  uv run 04_it_forgets.py
"""
from llm import ask

first = {"role": "user", "content": "Hi! My meeting in Tokyo is on 12 Nov at 2 PM."}
question = {"role": "user", "content": "What time is my meeting?"}

# Request 1: tell it the meeting time.
answer = ask([first])
print("Request 1:", answer, "\n")

# Request 2: ask again, in a new request. It does not know.
print("Request 2:", ask([question]), "\n")

# Request 3: send the whole chat again. Now it knows.
chat = [first, {"role": "assistant", "content": answer}, question]
print("Request 3:", ask(chat))
