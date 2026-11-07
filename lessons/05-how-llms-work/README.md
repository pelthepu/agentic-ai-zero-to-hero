# Lesson 5: How LLMs Work for Developers

**Part on the map:** the brain (LLM). **First code of the course.**

In this lesson you make your first LLM call in Python, then open the brain: tokens, next-token guessing, training vs use, attention, temperature, the context window and made-up answers.

## Set up (once, about 3 minutes)

1. Install [VS Code](https://code.visualstudio.com).
2. Install [uv](https://docs.astral.sh/uv/). It installs Python and the packages for you.
   - Mac or Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
3. Download this repo (green **Code** button, then **Download ZIP**) and open this folder in VS Code.
4. Get a free API key at [Google AI Studio](https://aistudio.google.com): **Get API key**, then **Create API key**. No card needed.
5. Copy `.env.example` to a new file called `.env` and paste your key after `GEMINI_API_KEY=`.
6. In the VS Code terminal, run `uv run 01_first_call.py`. The first run takes about a minute.

> Keep your key secret. Never share `.env` or push it to GitHub. On the free plan, Google may use what you send to improve its models, so don't send private data.

## The files

| File | What it shows |
|---|---|
| `01_first_call.py` | Your first LLM call: connect, send, print |
| `code_with_me_final.py` | The file we write together in the video, finished: temperature, streaming, and a made-up answer |
| `llm.py` | The same connection in one place. Change the brain here |
| `02_tokens.py` | How text splits into tokens, and how many tokens a call uses |
| `03_temperature.py` | The same question at temperature 0 and 2 |
| `04_it_forgets.py` | The brain forgets you after each call, until you send the whole chat |
| `05_fake_flight.py` | A made-up answer about flight SK 999, which does not exist |
| `06_homework_step2.py` | Homework: replay TripPilot's step 2, ten times |

Run any file with `uv run <file>`.

## If something goes wrong

| You see | Do this |
|---|---|
| `No API key found` | Check that the file is named `.env` (not `.env.txt`) and has your key |
| `model not found` | Open AI Studio, pick any free "Flash" model, and paste its name into `MODEL` in `llm.py` (and in `01_first_call.py`) |
| `429` or `quota` | You hit the free limit. Wait a minute and run it again |

## Homework

Run `06_homework_step2.py`. How many times out of 10 does the brain pick SK 209, the flight that breaks the rule? Try temperature 0, 1 and 2. Post your numbers and your model name in the video comments.

## Key ideas

| Idea | In one line |
|---|---|
| LLM | A next-token guesser that has read most of the internet |
| Token | A small piece of text. About 75 English words = 100 tokens |
| Training vs use | It learns in training. When you use it, it is frozen |
| Attention | Each token looks at the others to find what matters |
| Temperature | Low = same safe answer. High = more random |
| Context window | How many tokens it can see in one call. It forgets everything else |
| Made-up answers | It writes what is likely, not what is true. Give it facts with tools |
