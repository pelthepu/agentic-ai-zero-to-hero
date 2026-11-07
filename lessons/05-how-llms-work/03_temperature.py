"""
Lesson 5, file 3: temperature. Same question, 3 times, at two settings.

Run:  uv run 03_temperature.py
"""
from llm import ask

question = "Suggest one name for a travel app. Reply with the name only."

for temperature in [0, 2]:
    print(f"Temperature {temperature}:")
    for _ in range(3):
        print("  ", ask(question, temperature=temperature).strip())
    print()
