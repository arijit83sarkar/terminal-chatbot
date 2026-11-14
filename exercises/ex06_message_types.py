"""Exercise 06 - LangChain message types

Concepts: SystemMessage, HumanMessage, AIMessage, .type, .content, isinstance.

LangChain wraps each chat turn in a typed object instead of a dict:
    dict role "system"    -> SystemMessage     .type == "system"
    dict role "user"      -> HumanMessage      .type == "human"
    dict role "assistant" -> AIMessage         .type == "ai"
Note the names differ from the dict roles you used in exercise 05.

Task
  1. Build one message of each type (texts are in the demo) - the demo prints
     "<type>: <content>" for each.
  2. Implement to_messages(history): turn a list of role/content dicts into the
     matching message objects, same order. Unknown role -> ValueError("Unknown role: <role>").

Run it:   uv run python check.py 6

--- EXPECTED OUTPUT ---
system: You are terse.
human: Hi
ai: Hello.
Converted 4 messages: SystemMessage, HumanMessage, AIMessage, HumanMessage
Last: What is 2+2?
Is human? True
Unknown role -> ValueError: Unknown role: robot
"""

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage


def to_messages(history: list[dict]) -> list[BaseMessage]:
    # TODO: map "system"/"user"/"assistant" to the three message classes
    raise NotImplementedError('TODO: map "system"/"user"/"assistant" to the three message classes')


if __name__ == "__main__":
    # TODO: create one of each type and print "<type>: <content>"
    ...

    history = [
        {"role": "system", "content": "You are terse."},
        {"role": "user", "content": "Hi"},
        {"role": "assistant", "content": "Hello."},
        {"role": "user", "content": "What is 2+2?"},
    ]
    messages = to_messages(history)
    print(f"Converted {len(messages)} messages: " + ", ".join(type(m).__name__ for m in messages))
    print(f"Last: {messages[-1].content}")
    print(f"Is human? {isinstance(messages[-1], HumanMessage)}")
    try:
        to_messages([{"role": "robot", "content": "beep"}])
    except ValueError as error:
        print(f"Unknown role -> ValueError: {error}")
