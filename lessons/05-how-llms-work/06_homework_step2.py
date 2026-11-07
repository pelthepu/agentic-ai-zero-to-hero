"""
Lesson 5, homework: replay TripPilot's step 2.
Give the brain the rule and the two flights, 10 times. How often does it break the rule?

Run:  uv run 06_homework_step2.py
"""
from llm import ask

instructions = (
    "You are TripPilot. You fix travel plans. "
    "Rule: only book a flight that lands before the user's meeting."
)
situation = (
    "The user's meeting is in Tokyo on 12 Nov at 2 PM. Flights found:\n"
    "SK 209: leaves 12 Nov 06:00, lands 12 Nov 17:30\n"
    "JP 330: leaves 11 Nov 21:15, lands 12 Nov 08:45\n"
    "Which flight do you book? Reply with the flight number only."
)

picks = []
for _ in range(10):
    answer = ask(
        [{"role": "system", "content": instructions}, {"role": "user", "content": situation}],
        temperature=2,  # try 0 and 1 too
    )
    picks.append(answer.strip())

print(picks)
print("SK 209 (breaks the rule):", sum("209" in p for p in picks), "out of 10")
