"""Exercise 07 - Chat models: list of messages in, AIMessage out

Concepts: model.invoke(), AIMessage, a growing history, a fake model for offline practice.

A chat model is a function: invoke(list_of_messages) -> AIMessage.
GenericFakeChatModel returns canned replies in order, so you can practise with no
API key and no network. (Real models are covered in exercise 08.)

Task
  1. In the demo, call the model once directly with [HumanMessage("Hi")] and print
     "<class name of the reply>: <reply content>".
  2. Implement ask(model, history, text):
       - append HumanMessage(text) to history
       - reply = model.invoke(history)
       - append the reply (an AIMessage) to history
       - return reply.content
  3. The demo then asks two questions and prints the history length and the
     message types in order.

Run it:   uv run python check.py 7

--- EXPECTED OUTPUT ---
AIMessage: Hello!
Q: Who are you? -> I am a fake model.
Q: Say it again -> Still fake.
History length: 5
Types: system, human, ai, human, ai
"""

from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage


def ask(model: GenericFakeChatModel, history: list[BaseMessage], text: str) -> str:
    # TODO: append HumanMessage, invoke the model, append the reply, return reply.content
    raise NotImplementedError('TODO: append HumanMessage, invoke the model, append the reply, return reply.content')


if __name__ == "__main__":
    model = GenericFakeChatModel(messages=iter(["Hello!", "I am a fake model.", "Still fake."]))

    # TODO 1: one direct call
    ...

    history: list[BaseMessage] = [SystemMessage("You are a fake.")]
    for question in ("Who are you?", "Say it again"):
        print(f"Q: {question} -> {ask(model, history, question)}")

    # TODO 3: length and types
    ...
