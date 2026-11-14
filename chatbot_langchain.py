"""Terminal chatbot v2 - the same chatbot, with LangChain.

Compare with chatbot_plain.py: the loop now lives in exercises/ex09_chat_loop.py
(your code), the model comes from exercises/ex08_build_model.py (your code), and the
history holds message objects instead of dicts.

    uv run python chatbot_langchain.py

Finish exercises 08 and 09 first - this file only wires them together.

BONUS ideas (write them as NEW functions so exercise 09 keeps passing)
  A. Streaming: use `for chunk in model.stream(history): print(chunk.content, end="", flush=True)`.
     Chunks can be added together with + to rebuild the full AIMessage for the history.
  B. Print `reply.usage_metadata` (input_tokens / output_tokens / total_tokens) after each reply.
  C. Keep the history bounded: send the SystemMessage plus only the last 10 messages
     (the idea behind last_n in exercise 05).
  D. Survive API errors: if model.invoke raises, print the error, remove the HumanMessage
     you just appended, and keep going (the same trap chatbot_plain.py handles).
"""

import sys

from dotenv import load_dotenv

from exercises.ex08_build_model import build_model
from exercises.ex09_chat_loop import chat_loop

SYSTEM_PROMPT = "You are a concise, friendly assistant. Answer in at most three sentences."


def main() -> None:
    load_dotenv()

    # TODO 1: model = build_model(). It raises RuntimeError when the key is missing:
    #         catch that and exit with sys.exit(f"Setup problem: {error}").
    raise NotImplementedError('TODO 1: model = build_model(). It raises RuntimeError when the key is missing:')

    print(f"Chatting with {model.model}. Type 'quit' to exit, '/clear' to start over.")

    # TODO 2: run chat_loop(model, SYSTEM_PROMPT)
    raise NotImplementedError('TODO 2: run chat_loop(model, SYSTEM_PROMPT)')


if __name__ == "__main__":
    main()
