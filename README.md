# Project 1 - Terminal chatbot

A chatbot in your terminal that keeps the whole conversation in a list.

| Python | LangChain |
|---|---|
| variables, `while` loops, `input()`, f-strings, env vars | chat models, message types |

## Setup

```bash
uv sync                      # creates .venv from pyproject.toml / uv.lock
cp .env.example .env         # then put your ANTHROPIC_API_KEY in .env
uv run python check.py       # progress table - every stub starts as TODO
```

Exercises 01-05, 06-09 need **no API key and no network**. Only the two chatbots at the
root talk to the real API.

## Order

| # | File | Practises |
|---|---|---|
| 01 | `exercises/ex01_variables_fstrings.py` | variables, types, f-strings |
| 02 | `exercises/ex02_while_loops.py` | `while`, `break`, `continue` |
| 03 | `exercises/ex03_input_loop.py` | `input()`, `strip()`, a chat-shaped loop |
| 04 | `exercises/ex04_env_vars.py` | `os.environ`, defaults, secrets |
| 05 | `exercises/ex05_history_list.py` | the conversation as a list of dicts |
| v1 | `chatbot_plain.py` | **plain Anthropic SDK, no framework** (live) |
| 06 | `exercises/ex06_message_types.py` | `SystemMessage` / `HumanMessage` / `AIMessage` |
| 07 | `exercises/ex07_fake_chat_model.py` | `model.invoke(list) -> AIMessage` |
| 08 | `exercises/ex08_build_model.py` | `ChatAnthropic` from env vars |
| 09 | `exercises/ex09_chat_loop.py` | the full loop against a fake model |
| v2 | `chatbot_langchain.py` | the same chatbot with LangChain (live) |

## How the stubs work

Each exercise is a stub: the docstring has the task and an `EXPECTED OUTPUT` block,
the code has `# TODO`s that raise `NotImplementedError`.

```bash
uv run python check.py 3     # run exercise 03: PASS, or a diff, or a traceback
uv run python check.py       # table for all exercises
```

`check.py` replaces `input()` with scripted answers from the docstring's `INPUT`
section and shows them in the transcript like a real terminal. You can also run any
exercise directly (`uv run python exercises/ex03_input_loop.py`) and type the answers yourself.

## Three tips

1. **Framework-free first.** Finish `chatbot_plain.py` (plain SDK call) before touching
   `chatbot_langchain.py`. That is when the Python sticks.
2. **Read every traceback before pasting it anywhere.** Bottom line = what went wrong,
   the lines above = where. A stub's `NotImplementedError` is practice for this.
3. **Tests come later.** From project 3 on, add one `pytest` test per project
   (extractors and routers are easy to test). Here `check.py` plays that role.
