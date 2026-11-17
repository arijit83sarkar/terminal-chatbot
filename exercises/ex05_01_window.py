"""
Exercise 05_01 - Trimming the context window

Concepts: slicing, loops, dicts, copies, type hints.

A model has a context window: send too much and the request is rejected.
So you trim. Two rules people learn the hard way:
  - the system prompt is not "just another message" - it stays.
  - trimming must NOT mutate the caller's history; they still own it.

Task - implement the four functions; the demo at the bottom uses them:
  estimate_tokens(history)              crude tokenizer: 3 per message + 1 per word
  system_prefix(history)                the leading run of system messages (a NEW list)
  trim_messages(history, max_messages)  the newest messages, but the system prefix
                                        always stays - even if it alone fills the
                                        limit. max_messages 0 -> just the prefix.
  fit_tokens(history, budget)           drop the OLDEST non-system messages one at a
                                        time until estimate_tokens <= budget.
                                        The system prefix survives no matter what.
Every function that returns a list returns a NEW list. history is never modified.

Run it: uv run python window.py

--- EXPECTED OUTPUT ---
Messages: 6
Tokens: 36
Trim 3:
system: You are a terse assistant.
assistant: Two, three, five.
user: Now three even numbers.
Trim 0: ['system']
Fit 20:
system: You are a terse assistant.
user: Now three even numbers.
Fit 20 tokens: 15
Original unchanged: 6
"""


def render(history: list[dict]) -> list[str]:  # given, from the last exercise
    return [f"{m['role']}: {m['content']}" for m in history]


def estimate_tokens(history: list[dict]) -> int:
    token = 0
    for message in history:
        token += len(message["content"].split()) + 3
    return token


def system_prefix(history: list[dict]) -> list[dict]:
    result: list[dict] = []
    for message in history:
        if message["role"] != "system":
            break
        result.append(message)
    return result


def trim_messages(history: list[dict], max_messages: int) -> list[dict]:
    prefix = system_prefix(history)
    rest = history[len(prefix) :]
    # slots left for non-system messages
    room = max(0, max_messages - len(prefix))
    # index of the oldest message we keep
    start = max(0, len(rest) - room)
    return prefix + rest[start:]


def fit_tokens(history: list[dict], budget: int) -> list[dict]:
    prefix = system_prefix(history)
    # a slice is a new list, so mutating it is safe
    rest = history[len(prefix) :]
    while rest and estimate_tokens(prefix + rest) > budget:
        rest.pop(0)
    return prefix + rest


if __name__ == "__main__":
    history: list[dict] = []
    for role, content in [
        ("system", "You are a terse assistant."),
        ("user", "Hi"),
        ("assistant", "Hello."),
        ("user", "Name three prime numbers."),
        ("assistant", "Two, three, five."),
        ("user", "Now three even numbers."),
    ]:
        history.append({"role": role, "content": content})

    print(f"Messages: {len(history)}")
    print(f"Tokens: {estimate_tokens(history)}")
    print("Trim 3:")
    for line in render(trim_messages(history, 3)):
        print(line)
    print(f"Trim 0: {[m['role'] for m in trim_messages(history, 0)]}")
    print("Fit 20:")
    trimmed = fit_tokens(history, 20)
    for line in render(trimmed):
        print(line)
    print(f"Fit 20 tokens: {estimate_tokens(trimmed)}")
    print(f"Original unchanged: {len(history)}")
