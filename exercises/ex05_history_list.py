"""Exercise 05 - The conversation is a list

Concepts: lists, dicts, append, slicing, loops, functions, type hints.

A chat history is just a list of {"role": ..., "content": ...} dicts, oldest first.
Every request to a model sends the WHOLE list - the model itself remembers nothing.

Task - implement the four functions; the demo at the bottom uses them:
  add_message(history, role, content)  append one dict to the list (return nothing)
  last_n(history, n)                   the last n messages as a NEW list.
                                       Watch out: history[-0:] is the whole list!
                                       last_n(history, 0) must be [].
  render(history)                      one "role: content" string per message
                                       (a list of str, same order)
  count_by_role(history)               a plain dict such as {"user": 2, "assistant": 1}

Run it:   uv run python check.py 5

--- EXPECTED OUTPUT ---
Messages: 5
assistant: Hello! How can I help?
user: What is a list?
assistant: An ordered, mutable collection.
Last 0: []
Counts: {'assistant': 2, 'system': 1, 'user': 2}
"""


def add_message(history: list[dict], role: str, content: str) -> None:
    history.append({"role": role, "content": content})


def last_n(history: list[dict], n: int) -> list[dict]:
    if n == 0:
        return []
    return history[-n:]


def render(history: list[dict]) -> list[str]:
    return [f"{message['role']}: {message['content']}" for message in history]


def count_by_role(history: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for message in history:
        counts[message["role"]] = counts.get(message["role"], 0) + 1
    return counts


if __name__ == "__main__":
    history: list[dict] = []
    add_message(history, "system", "You are a helpful assistant.")
    add_message(history, "user", "Hi!")
    add_message(history, "assistant", "Hello! How can I help?")
    add_message(history, "user", "What is a list?")
    add_message(history, "assistant", "An ordered, mutable collection.")

    print(f"Messages: {len(history)}")
    for line in render(last_n(history, 3)):
        print(line)
    print(f"Last 0: {last_n(history, 0)}")
    print(f"Counts: {dict(sorted(count_by_role(history).items()))}")
