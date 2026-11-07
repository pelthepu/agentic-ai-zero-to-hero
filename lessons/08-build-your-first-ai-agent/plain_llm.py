"""
Before the agent: one plain LLM call with the same goal.
It can only reply with text. It cannot search, book or message anyone.
"""
import ollama

goal = ("My flight from Delhi to Tokyo got cancelled. "
        "I have a meeting in Tokyo on 12 Nov at 2 PM. Fix my trip.")

reply = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": goal}])
print(reply["message"]["content"])
