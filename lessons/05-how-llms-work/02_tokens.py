"""
Lesson 5, file 2: the brain reads tokens, not words.

Run:  uv run 02_tokens.py
"""
import tiktoken

# Part 1: see the pieces. This part needs no API key.
# Every model family splits text its own way. The idea is the same for all.
enc = tiktoken.get_encoding("o200k_base")

texts = [
    "Hello",
    "TripPilot",
    "Get me to Tokyo before my 2 PM meeting.",
    "నా ఫ్లైట్ రద్దయింది",  # "My flight got cancelled" in Telugu
]

for text in texts:
    ids = enc.encode(text)
    pieces = [enc.decode_single_token_bytes(i).decode("utf-8", errors="replace") for i in ids]
    print(f"{len(ids):>2} tokens | {text}")
    print("          " + " | ".join(pieces))
    print()

# Part 2: the brain tells you how many tokens each call used.
# You pay, and you hit limits, per token.
from llm import MODEL, client  # noqa: E402

reply = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Plan a 5-day trip to Japan in 3 short lines."}],
)
print(reply.choices[0].message.content)
print()
print("Tokens in (your message):", reply.usage.prompt_tokens)
print("Tokens out (its reply):  ", reply.usage.completion_tokens)
print("Total:                   ", reply.usage.total_tokens)
