# Lesson 4: What's Inside an AI Agent? Agentic AI Architecture Explained

**Video:** [Watch on YouTube](https://youtu.be/j-K575DRUS8) (15:05) · **Course:** [full playlist](https://www.youtube.com/playlist?list=PLExTFh0CQIwU) · **Code:** none today. Your first AI code is in [lesson 5](../05-how-llms-work)

[![What's Inside an AI Agent? Agentic AI Architecture Explained](https://img.youtube.com/vi/j-K575DRUS8/maxresdefault.jpg)](https://www.youtube.com/watch?v=j-K575DRUS8)

## Chapters

| Time | Chapter |
|---|---|
| [0:00](https://www.youtube.com/watch?v=j-K575DRUS8&t=0s) | What's inside an Agentic AI system? |
| [1:25](https://www.youtube.com/watch?v=j-K575DRUS8&t=85s) | Like a human body: you already met 2 parts |
| [1:47](https://www.youtube.com/watch?v=j-K575DRUS8&t=107s) | The parts map: 8 parts on the loop |
| [3:27](https://www.youtube.com/watch?v=j-K575DRUS8&t=207s) | Part 1: Brain (the LLM) |
| [4:23](https://www.youtube.com/watch?v=j-K575DRUS8&t=263s) | Part 2: Instructions |
| [5:05](https://www.youtube.com/watch?v=j-K575DRUS8&t=305s) | Part 3: Tools |
| [5:47](https://www.youtube.com/watch?v=j-K575DRUS8&t=347s) | Part 4: Memory and knowledge |
| [6:45](https://www.youtube.com/watch?v=j-K575DRUS8&t=405s) | Part 5: Planner |
| [7:23](https://www.youtube.com/watch?v=j-K575DRUS8&t=443s) | Part 6: Reflection |
| [8:06](https://www.youtube.com/watch?v=j-K575DRUS8&t=486s) | Part 7: Orchestrator |
| [9:00](https://www.youtube.com/watch?v=j-K575DRUS8&t=540s) | Part 8: Guardrails |
| [9:38](https://www.youtube.com/watch?v=j-K575DRUS8&t=578s) | Back to step 2: which part made the mistake? |
| [11:01](https://www.youtube.com/watch?v=j-K575DRUS8&t=661s) | Take one part away |
| [11:59](https://www.youtube.com/watch?v=j-K575DRUS8&t=719s) | Same parts, other agents (coding + support) |
| [13:13](https://www.youtube.com/watch?v=j-K575DRUS8&t=793s) | Tip: when an agent fails, find the part |
| [13:45](https://www.youtube.com/watch?v=j-K575DRUS8&t=825s) | Recap |
| [14:11](https://www.youtube.com/watch?v=j-K575DRUS8&t=851s) | Homework |
| [14:28](https://www.youtube.com/watch?v=j-K575DRUS8&t=868s) | Up next: How LLMs Work |

## In one minute

Lesson 3 showed what an agent **does**: the loop. This lesson shows what's **inside**: 8 parts, each doing one job on that loop.

An LLM alone is not Agentic AI. It's only the brain. A brain with no hands can't book a flight, and a brain with no notepad forgets what it just did.

These are jobs more than separate pieces of code. In a small agent like TripPilot v0, the LLM does the reasoning, planning and checking together. As agents grow, the jobs split into separate parts.

## The parts map

| Loop step | Part | Priya had | Job |
|---|---|---|---|
| Reason (in the middle) | 1. Brain (the LLM) | Her own head | Reads the goal, thinks, decides |
| Next to the brain | 2. Instructions | "Keep me on time, stay in budget" | Who it is, which tools it has, which rules to follow |
| Perceive + Act | 3. Tools | Her laptop and phone | Do the real work: APIs, databases, files, the web, code |
| Remember | 4. Memory | Her notepad | What it saved for itself |
| Plan | 5. Planner | Her to-do list | The steps, in order, changed when something fails |
| Check | 6. Reflection | "Did that work?" | Checks the result, learns from it |
| The loop itself | 7. Orchestrator | (none: the while loop) | Runs the loop. It isn't AI, it's normal code |
| Around it all | 8. Guardrails | Calling you before she pays | Keeps actions safe |

## Each part, in one line

| Part | Remember this |
|---|---|
| Brain | GPT, Claude, Gemini live here. It analyses, reads feedback, weighs options, decides what's next |
| Instructions | Clear instructions make a good agent. Vague ones make a confused one |
| Tools | Tools don't decide. The brain says "book JP 330". The booking tool books it |
| Memory | Short-term: "SK 209 failed" (this run). Long-term: "you prefer morning flights" (every trip) |
| Knowledge | Lives outside, in documents it can search, like the airline's baggage rules. More in the RAG lessons |
| Planner | The brain is the thinker. The planner is a job. The hotel can't move before the flight is booked |
| Reflection | Did this work? Why did it fail? What should I change next time? |
| Orchestrator | Passes the brain's choice to the right tool, tracks where it is, handles failures, asks a human, stops (say, after 10 rounds) |
| Guardrails | Some sit inside the tools and can't be skipped. Others sit around the loop, like a human's okay before paying |

## Back to step 2: which part did what?

TripPilot's run from lesson 3, part by part:

| # | Part | What happened |
|---|---|---|
| 1 | Instructions | Rule: only book a flight that lands before the user's meeting |
| 2 | Brain | Still chose SK 209. **The mistake** |
| 3 | Orchestrator | Passed that choice to the booking tool |
| 4 | Guardrail (in the tool) | Checked the landing time and said no. **Caught it** |
| 5 | Reflection | Read the error: SK 209 lands too late |
| 6 | Memory | Wrote it down, so it never tried SK 209 again |
| 7 | Planner | New plan: book JP 330, which is on time |

One part made the mistake. Another part caught it. But why did the brain break a rule it was clearly given? That's [lesson 5](../05-how-llms-work).

## Take one part away

| Without | What breaks |
|---|---|
| Brain | No thinking. Just a fixed script |
| Instructions | It doesn't know its job or its rules |
| Tools | It knows what to do, but can't do it |
| Memory | It forgets your preferences every time |
| Planner | It jumps between tasks |
| Reflection | It repeats the same mistakes |
| Orchestrator | It thinks once, then stops. No loop |
| Guardrails | It may do dangerous things |

## Same parts, other agents

| Part | AI coding agent (GitHub Copilot, Claude Code) | AI support agent |
|---|---|---|
| Brain | Writes the code | Reads the complaint |
| Tools | Editor, test runner, deploy pipeline | Order system, payments, email |
| Reflection / Knowledge | Why did the test fail? | The refund policy |
| Guardrails | A human's okay before deploy | Big refunds need a human |

## Tip from real projects

When an agent fails, don't just blame the model. First ask which part failed. Were the instructions vague? Was a guardrail missing? Did memory forget something? Most of the time, the fix is in a part around the model.

## FAQ

**What are the parts of an AI agent?**
Brain (the LLM), instructions, tools, memory, planner, reflection, orchestrator and guardrails.

**Is an LLM the same as Agentic AI?**
No. The LLM is the brain. Agentic AI is the whole system around it.

**What is the difference between memory and knowledge?**
Memory is what the agent saved for itself. Knowledge lives outside, in documents it can search.

**Is the orchestrator AI?**
No. It's normal code: a while loop in plain Python, or a framework like LangChain or LangGraph.

## Homework

Take the goal you picked in lesson 3, like "Plan my friend's birthday party." For each of the 8 parts, write one line. What are its tools? What should it remember? What needs a human's okay? Post it in the video's comments.

## Quick quiz

1. Which part of an agent is not AI?
2. In TripPilot's step 2, which part made the mistake, and which part caught it?
3. Airline baggage rules in a document the agent can search: memory or knowledge?
4. What is the difference between the brain and the planner?

<details><summary>Answers</summary>

1. The orchestrator. It's normal code.
2. The brain chose SK 209. The guardrail inside the booking tool caught it.
3. Knowledge. Memory is what the agent saved for itself.
4. The brain is the thinker. The planner is a job, which the brain can also do in a small agent.

</details>

## Further reading

- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (2024)

**Next:** [Lesson 5: How LLMs Work for Developers](../05-how-llms-work) · **Previous:** [Lesson 3](../03-how-agentic-ai-works)
