"""Exercise 09 - The chat loop (offline, with a fake model)

Concepts: everything so far - while loop, input(), history list, message types,
          model.invoke(). This is the heart of the chatbot.

Task - implement chat_loop(model, system_prompt) -> list[BaseMessage]:
  * history starts as [SystemMessage(system_prompt)]
  * loop:
      text = input("You: ").strip()
      - empty    -> ask again
      - "quit"   -> stop
      - "/clear" -> reset history to just the SystemMessage, print "(history cleared)"
      - else     -> append HumanMessage, reply = model.invoke(history),
                    print "Bot: <reply.content>", append the reply
  * Ctrl-D (EOFError) or Ctrl-C (KeyboardInterrupt) also end the loop cleanly:
    print an empty line first, so the shell prompt starts on a fresh line
  * return the final history

The demo below runs your loop against a fake model. chatbot_langchain.py will import
chat_loop from this file and plug in the real model - so this one is worth getting right.

Run it:   uv run python check.py 9

--- INPUT ---
hi
/clear

what is 2+2?
quit
--- EXPECTED OUTPUT ---
You: hi
Bot: Hello! I'm a fake model.
You: /clear
(history cleared)
You:
You: what is 2+2?
Bot: 4.
You: quit
Final history: 3 messages
"""

from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage


def chat_loop(model, system_prompt: str) -> list[BaseMessage]:
    # TODO: implement the chat loop (rules in the docstring)
    raise NotImplementedError('TODO: implement the chat loop (rules in the docstring)')


if __name__ == "__main__":
    fake = GenericFakeChatModel(messages=iter(["Hello! I'm a fake model.", "4."]))
    final = chat_loop(fake, "You are terse.")
    print(f"Final history: {len(final)} messages")
