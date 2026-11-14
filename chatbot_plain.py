"""Terminal chatbot v1 - plain Anthropic SDK, no framework.

Write this BEFORE the LangChain version: seeing the raw API call is what makes the
framework make sense later. Run it (needs ANTHROPIC_API_KEY in .env or your shell):

    uv run python chatbot_plain.py

Behaviour
  * keeps the whole conversation in a list of {"role", "content"} dicts (exercise 05)
  * 'quit' exits, '/clear' empties the history, Ctrl-D / Ctrl-C exit cleanly
  * the system prompt is NOT in the list: the Anthropic API takes it as a separate
    `system=` argument. (LangChain's SystemMessage, exercise 06, is the framework's
    way of putting it back into the list - compare the two designs.)

This file can't be auto-checked (it needs the network), so test it by chatting.
Ask it your name, then ask "what's my name?" - the answer proves the list works.
"""

import os
import sys

import anthropic
from dotenv import load_dotenv

SYSTEM_PROMPT = "You are a concise, friendly assistant. Answer in at most three sentences."


def main() -> None:
    load_dotenv()  # copies the variables in .env into os.environ

    # TODO 1: settings from the environment (exercise 04): the model name from CHATBOT_MODEL
    #         (default "claude-sonnet-5-5") and max_tokens from CHATBOT_MAX_TOKENS
    #         (default 1024 - remember it arrives as a str)
    raise NotImplementedError('TODO 1: settings from the environment (exercise 04): the model name from CHATBOT_MODEL')

    # TODO 2: if ANTHROPIC_API_KEY is unset, exit early with
    #         sys.exit("Setup problem: missing ANTHROPIC_API_KEY (see .env.example)").
    #         Then create the client with anthropic.Anthropic() - it reads the key itself.
    raise NotImplementedError('TODO 2: if ANTHROPIC_API_KEY is unset, exit early with')

    history: list[dict] = []
    print(f"Chatting with {model}. Type 'quit' to exit, '/clear' to start over.")

    while True:
        # TODO 3: read input("You: "), strip it. Skip blank lines, stop on "quit",
        #         "/clear" empties history and prints "(history cleared)".
        #         Treat EOFError / KeyboardInterrupt like "quit" (print an empty line first).
        raise NotImplementedError('TODO 3: read input("You: "), strip it. Skip blank lines, stop on "quit",')

        # TODO 4: append the user's message to history
        raise NotImplementedError("TODO 4: append the user's message to history")

        # TODO 5: call client.messages.create(model=model, max_tokens=max_tokens,
        #         system=SYSTEM_PROMPT, messages=history). If it raises anthropic.APIError,
        #         print "Error: <error>", REMOVE the user message you just appended
        #         (otherwise the history is left in a broken state), and `continue`.
        raise NotImplementedError('TODO 5: call client.messages.create(model=model, max_tokens=max_tokens,')

        # TODO 6: the reply text is response.content[0].text. Print "Bot: <text>" and
        #         append {"role": "assistant", "content": text} to history.
        raise NotImplementedError('TODO 6: the reply text is response.content[0].text. Print "Bot: <text>" and')

        # BONUS (not required): print the token usage after each reply using
        # response.usage.input_tokens / response.usage.output_tokens and an f-string
        # such as  [in: 25 | out: 18]  (exercise 01).


if __name__ == "__main__":
    main()
