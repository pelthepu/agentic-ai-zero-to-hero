# Lesson 8: Build Your First AI Agent in Python: TripPilot v0

**Video:** (coming 28 Nov) · **Code:** [trippilot_v0.py](trippilot_v0.py) · [plain_llm.py](plain_llm.py)

In this lesson we write our first agent in plain Python, with no framework: **TripPilot v0**. It is the same agent you watched in [lesson 3](../03-how-agentic-ai-works). Its flight from Delhi to Tokyo is cancelled, and it has to get you there before a 2 PM meeting.

## In one minute

An AI agent is an LLM in a loop. In each round, the LLM picks one step, your code runs it, and the result goes back to the LLM. It repeats until the goal is done.

| Part (from lesson 4) | What it is in TripPilot |
|---|---|
| Brain | The LLM picks one tool and its inputs, as JSON |
| Instructions | `INSTRUCTIONS`, the system prompt |
| Tools | `search_flights`, `book_flight`, and more. Your Python code runs them |
| Memory | The `memory` list keeps every step and result |
| Orchestrator | The `while` loop: next step, and when to stop. `MAX_STEPS` stops endless loops |
| Guardrails | `book_flight` rejects a flight that lands after the meeting |

```python
while not done:
    step = llm(goal, history)
    result = run(step)
    history.append(result)
```

## Run it

1. Install Ollama: [ollama.com](https://ollama.com)
2. Get a free model (about 2 GB):
   ```bash
   ollama pull llama3.2
   ```
3. Install the Python package:
   ```bash
   pip install ollama
   ```
4. Run a plain LLM call first, then the agent:
   ```bash
   python plain_llm.py
   python trippilot_v0.py
   ```

Your steps may differ a little from the video. That's normal.

## What to look for

- **The plain LLM** only gives advice. It can't search, book or message.
- **Step 2 of the agent:** the model tries to book SK 209, which lands after the meeting. The `book_flight` check rejects it, and the agent books JP 330 instead. Hard rules belong in code.
- **Break it:** comment out the two `memory.append(...)` lines and run again. The agent searches again and again until `MAX_STEPS` stops it.

## Homework

Add a tool `check_weather(city)` that returns fake weather. Describe it in `INSTRUCTIONS`, add it to `TOOLS`, and add the rule "Tell the user the weather in your message." Does the agent use it?

## Quick quiz

1. Who runs the tool: the LLM or your code?
2. What happens if you remove the memory?
3. Why does `book_flight` check the landing time when the prompt already says so?

<details><summary>Answers</summary>

1. Your code. The LLM only writes which tool to call and with what inputs.
2. The agent forgets every result and repeats the same step until the step limit stops it.
3. LLMs make mistakes. A rule that matters must be checked in code.

</details>

## Further reading

- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (2024)
- Ollama Python library: [github.com/ollama/ollama-python](https://github.com/ollama/ollama-python)

**Next:** Lesson 9: LangChain v1 for Beginners · **Previous:** Lesson 7: Prompt Engineering Essentials
