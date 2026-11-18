"""
Exercise 05_03 - Regenerate/edit without corrupting the other branch

Concepts: copying, slicing, loops, dicts, type hints.

"Regenerate" and "edit & resend" both fork the conversation. Here is the trap:
list(history) and history[:] copy the LIST, but both lists still point at the SAME
dicts. Edit a message in one branch and the other branch changes too. Copy one
level deeper. (Values here are plain strings, so one level is enough.)

Task - implement the four functions; the demo at the bottom uses them:
  clone(history)                    new list AND new dicts
  edit_message(history, i, content) new history with message[i]["content"] replaced
  regenerate(history, answer)       new history: drop the trailing assistant
                                    message(s), then append
                                    {"role": "assistant", "content": answer}
  common_prefix_len(a, b)           how many leading messages match on BOTH
                                    role and content (stop at the first difference)
Nothing here may modify its arguments.

Run it: uv run python branch.py

--- EXPECTED OUTPUT ---
base: ['Hi', 'Hello!', 'Tell me a joke.', 'Joke v1.']
branch: ['Hi', 'Hello!', 'Tell me a joke.', 'Joke v2.']
edited: ['Hi', 'Hello!', 'Tell me a dad joke.', 'Joke v2.']
branch still: ['Hi', 'Hello!', 'Tell me a joke.', 'Joke v2.']
Shared prefix: 2
Shares dicts: False
Clone equals: True
Fresh: ['Ping', 'Pong']
"""


def clone(history: list[dict]) -> list[dict]:
    result: list[dict] = []
    for h in history:
        result.append(dict(h))
    return result
    # return [dict(h) for h in history]


def edit_message(history: list[dict], index: int, content: str) -> list[dict]:
    cloned = clone(history)
    cloned[index]["content"] = content
    return cloned


def regenerate(history: list[dict], answer: str) -> list[dict]:
    cloned = clone(history)

    while cloned and cloned[-1]["role"] == "assistant":
        cloned.pop()

    cloned.append({"role": "assistant", "content": answer})
    return cloned


def common_prefix_len(a: list[dict], b: list[dict]) -> int:
    count = 0
    while a and b:
        if a[count]["content"] != b[count]["content"]:
            break
        count += 1
    return count


if __name__ == "__main__":
    base: list[dict] = [
        {"role": "user", "content": "Hi"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Tell me a joke."},
        {"role": "assistant", "content": "Joke v1."},
    ]
    branch = regenerate(base, "Joke v2.")
    edited = edit_message(branch, 2, "Tell me a dad joke.")

    print(f"base: {[m['content'] for m in base]}")
    print(f"branch: {[m['content'] for m in branch]}")
    print(f"edited: {[m['content'] for m in edited]}")
    print(f"branch still: {[m['content'] for m in branch]}")
    print(f"Shared prefix: {common_prefix_len(branch, edited)}")
    print(f"Shares dicts: {branch[0] is edited[0]}")
    print(f"Clone equals: {clone(base) == base}")
    fresh = regenerate([{"role": "user", "content": "Ping"}], "Pong")
    print(f"Fresh: {[m['content'] for m in fresh]}")
