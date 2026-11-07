# Lesson 3: How Agentic AI Works, Step by Step

**Video:** (link coming) · **Code:** none today. We build this agent in [lesson 8](../08-build-your-first-ai-agent)

In this lesson we follow one goal through the loop that every agent runs. Then we watch **TripPilot**, the travel assistant we build later in this series, fix a cancelled trip on its own.

## In one minute

An AI agent is an LLM in a loop. In each round, the LLM looks at the goal and everything that has happened so far, and picks the next step. The step runs, the result comes back, and it decides again, until the goal is done.

**The loop:** Goal → Perceive → Remember → Reason → Plan → Act → Check, with guardrails around it.

| Step | What it means | Trip example |
|---|---|---|
| Goal | What you want done | "Fix my trip. Meeting in Tokyo on 12 Nov at 2 PM." |
| Perceive | Look at the world | Search for flights |
| Remember | Use what it knows and has done | SK 209 already failed |
| Reason | Weigh the options | SK 209 lands too late |
| Plan | Pick the steps and their order | Book a flight, then move the hotel |
| Act | Use a tool | Book JP 330 |
| Check | Did it work? Is the goal done? | Yes, so stop |
| Guardrails | Rules that keep it safe | Ask before paying |

## Priya, the everyday example

| Priya | AI agent |
|---|---|
| Your request | The goal |
| Her brain | The LLM |
| Website and phone | Tools |
| Her notepad | Memory |
| "Is it done yet?" | The loop |
| Calls you before paying | Guardrails |

## What to look for in the TripPilot run

- **Step 2:** TripPilot tries to book SK 209, which lands after the meeting. A rule in the booking tool rejects it. Real agents make mistakes, so the Check step and guardrails matter.
- **The notepad:** after every step, TripPilot writes down what happened. That's how it knew SK 209 had already failed.

## Quick quiz

1. Which step decides the order of the work?
2. Where does the agent's memory show up in the TripPilot run?
3. Why does the booking tool check the landing time?

<details><summary>Answers</summary>

1. Plan.
2. In the notepad. It keeps every step and result.
3. LLMs make mistakes. A rule that matters is checked in code, as a guardrail.

</details>

## Further reading

- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (2024)

**Next:** Lesson 4: Inside an Agentic AI System · **Previous:** [Lesson 2](../02-genai-vs-ai-agents-vs-agentic-ai)
