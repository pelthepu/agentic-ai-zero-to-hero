"""
TripPilot v0: your first AI agent, in plain Python. No framework.
Lesson 3 of Agentic AI Zero to Hero by Pavan Elthepu (@pavanelthepu)

How to run:
  1. Install Ollama from https://ollama.com
  2. ollama pull llama3.2
  3. pip install ollama
  4. python trippilot_v0.py
"""
import json

import ollama

MODEL = "llama3.2"  # free model that runs on your laptop
MAX_STEPS = 10      # stop rule: the agent can never loop forever


# ------------------------------------------------------------------
# 1. TOOLS: plain Python functions the agent is allowed to use.
#    They use fake data, so you need no API keys and pay nothing.
# ------------------------------------------------------------------
MEETING = "2026-11-12 14:00"  # the user's meeting in Tokyo

FLIGHTS = [
    {"flight": "SK 209", "departs": "2026-11-12 06:00", "lands": "2026-11-12 17:30", "seats": 9},
    {"flight": "JP 330", "departs": "2026-11-11 21:15", "lands": "2026-11-12 08:45", "seats": 4},
]


def search_flights(origin, destination):
    """Find flights that can replace the cancelled one."""
    return FLIGHTS


def book_flight(flight_no):
    """Book a seat, but only on a flight that lands before the meeting."""
    for flight in FLIGHTS:
        if flight["flight"] == flight_no:
            if flight["lands"] > MEETING:  # a hard rule lives in code, not only in the prompt
                return {"error": f"{flight_no} lands at {flight['lands']}, after the meeting at {MEETING}."}
            return {"status": "BOOKED", "flight": flight_no, "booking_id": "TP-7K2Q"}
    return {"error": f"No flight called {flight_no}."}


def update_hotel(check_in):
    """Move the hotel check-in to a new date."""
    return {"status": "UPDATED", "hotel": "Shinjuku Inn", "check_in": check_in}


def send_message(text):
    """Send a message to the user's phone."""
    return {"status": "SENT", "text": text}


TOOLS = {
    "search_flights": search_flights,
    "book_flight": book_flight,
    "update_hotel": update_hotel,
    "send_message": send_message,
}


# ------------------------------------------------------------------
# 2. INSTRUCTIONS: the LLM cannot see our Python code.
#    It only knows the tools we describe here.
# ------------------------------------------------------------------
INSTRUCTIONS = """
You are TripPilot, an assistant that fixes travel plans.
Work step by step. In each step, pick ONE tool, or finish.

Tools:
- search_flights(origin, destination): flights that can replace a cancelled one
- book_flight(flight_no): book a seat on a flight
- update_hotel(check_in): move the hotel check-in to the new arrival date
- send_message(text): send the user a short summary

Rules:
- Only book a flight that lands before the user's meeting.
- If a tool returns an error, read it and try another way.
- Message the user before you finish.
- When everything is done, use the tool "finish" with args {"answer": "<short summary>"}.

Reply with JSON only, in this shape:
{"thought": "what I learned and what I will do next", "tool": "<tool name>", "args": {}}
"""


# ------------------------------------------------------------------
# 3. THE AGENT LOOP: think -> act -> observe -> repeat until done.
# ------------------------------------------------------------------
def run_agent(goal):
    # MEMORY: everything the agent has done and seen so far
    memory = [
        {"role": "system", "content": INSTRUCTIONS},
        {"role": "user", "content": goal},
    ]

    for step in range(1, MAX_STEPS + 1):
        # THINK: the LLM reads the goal and its memory, then picks the next step
        reply = ollama.chat(model=MODEL, messages=memory, format="json", options={"temperature": 0})
        text = reply["message"]["content"]
        decision = json.loads(text)
        tool = decision.get("tool")
        args = decision.get("args") or {}
        print(f"\nStep {step}")
        print(f"  Think  : {decision.get('thought')}")

        # STOP: the LLM says the goal is done
        if tool == "finish":
            return args.get("answer", "Done.")

        # ACT: our code runs the tool. The LLM only asked for it.
        try:
            result = TOOLS[tool](**args)
        except Exception as error:  # wrong tool name or inputs: tell the LLM so it can fix it
            result = {"error": f"{type(error).__name__}: {error}"}
        print(f"  Act    : {tool}({args})")
        print(f"  Observe: {result}")

        # REMEMBER: save what we did and what happened, for the next step
        memory.append({"role": "assistant", "content": text})
        memory.append({"role": "user", "content": f"Result of {tool}: {json.dumps(result)}"})

    return "Stopped: hit the step limit before the goal was done."


if __name__ == "__main__":
    goal = ("My flight from Delhi to Tokyo got cancelled. "
            "I have a meeting in Tokyo on 12 Nov at 2 PM. Fix my trip.")
    print(f"Goal: {goal}")
    answer = run_agent(goal)
    print(f"\nTripPilot: {answer}")
