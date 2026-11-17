"""
Exercise 05_02 - The tool-call round trip

Concepts: nested dicts/lists, loops, append, aliasing, type hints.

The model never runs anything. It ASKS: the assistant message carries tool_calls.
Your code executes them, appends one "tool" message per result, and sends the
WHOLE history back. An unknown tool is still a result - never leave a call unanswered,
or the next request is malformed.

Message shapes:
  {"role": "user", "content": "..."}
  {"role": "assistant", "content": "", "tool_calls": [{"name": ..., "args": {...}}, ...]}
  {"role": "tool", "name": "...", "content": "..."}

Task - implement the four functions; the demo at the bottom uses them:
  add_tool_calls(history, calls)  append ONE assistant message, content "",
                                  tool_calls = a COPY of calls (the caller keeps
                                  mutating their list afterwards - don't alias it)
  pending_calls(history)          the calls of the LAST message, but only if that
                                  message is an assistant asking for calls.
                                  Otherwise []. New list.
  run_tool(name, args)            fake executor:
                                    "get_weather" -> f"{args['city']}: 3C, rain"
                                    "add"         -> str(args["a"] + args["b"])
                                    anything else -> f"error: unknown tool '{name}'"
  run_tools(history)              append one tool message per pending call,
                                  return how many you appended

Run it: uv run python tools.py

--- EXPECTED OUTPUT ---
Pending: ['get_weather', 'add', 'launch_rocket']
Ran: 3
Pending now: []
user: Weather in Oslo, and 2 + 40?
assistant -> get_weather, add, launch_rocket
tool[get_weather]: Oslo: 3C, rain
tool[add]: 42
tool[launch_rocket]: error: unknown tool 'launch_rocket'
Messages: 5
"""


def render(history: list[dict]) -> list[str]:  # given
    lines: list[str] = []
    for m in history:
        if m["role"] == "assistant" and m.get("tool_calls"):
            lines.append(
                "assistant -> " + ", ".join(c["name"] for c in m["tool_calls"])
            )
        elif m["role"] == "tool":
            lines.append(f"tool[{m['name']}]: {m['content']}")
        else:
            lines.append(f"{m['role']}: {m['content']}")
    return lines


def add_tool_calls(history: list[dict], calls: list[dict]) -> None:
    history.append({"role": "assistant", "content": "", "tool_calls": list(calls)})
    print(history)


def pending_calls(history: list[dict]) -> list[dict]:
    if not history:
        return []
    last = history[-1]
    if last["role"] == "assistant" and last.get("tool_calls"):
        return list(last["tool_calls"])
    return []


def run_tool(name: str, args: dict) -> str:
    if name == "get_weather":
        value = args["city"]
        return f"{value}: 3C, rain"
    elif name == "add":
        a = int(args.get("a")) + int(args.get("b"))
        return f"{a}"
    else:
        return f"error: unknown tool 'launch_rocket'"


def run_tools(history: list[dict]) -> int:
    calls = pending_calls(history)
    for call in calls:
        result = run_tool(call["name"], call["args"])
        history.append({"role": "tool", "name": call["name"], "content": result})
    return len(calls)


if __name__ == "__main__":
    history: list[dict] = [{"role": "user", "content": "Weather in Oslo, and 2 + 40?"}]
    calls: list[dict] = [
        {"name": "get_weather", "args": {"city": "Oslo"}},
        {"name": "add", "args": {"a": 2, "b": 40}},
        {"name": "launch_rocket", "args": {}},
    ]
    add_tool_calls(history, calls)
    calls.append({"name": "sneaky", "args": {}})  # caller reuses their list

    print(f"Pending: {[c['name'] for c in pending_calls(history)]}")
    print(f"Ran: {run_tools(history)}")
    print(f"Pending now: {pending_calls(history)}")
    for line in render(history):
        print(line)
    print(f"Messages: {len(history)}")
