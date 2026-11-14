"""Exercise 08 - Build a real chat model from environment variables

Concepts: ChatAnthropic, constructor arguments, env vars, no network until invoke().

Creating a model object does NOT call the API - only .invoke() does. That is why this
exercise can run with a fake key.

Task - implement build_model():
  * refuse to continue without a key: if ANTHROPIC_API_KEY is unset or empty raise
    RuntimeError("Missing environment variable: ANTHROPIC_API_KEY")
  * model name from CHATBOT_MODEL, default "claude-sonnet-5-5"
  * max tokens from CHATBOT_MAX_TOKENS (a str!), default 1024, passed as an int
  * temperature from CHATBOT_TEMPERATURE: pass a float when the variable is set,
    otherwise pass None (do NOT invent a default)
  * return ChatAnthropic(model=..., max_tokens=..., temperature=...)

Gotcha (read this before you chat): claude-sonnet-5-5 only accepts the default
temperature. Set CHATBOT_TEMPERATURE=0.3 and ChatAnthropic raises
"ValueError: `temperature` is not supported for claude-sonnet-5-5 at non-default values"
on the first .invoke() - not when the object is created. That is why unset means None.

Bonus (not checked): build the same model with
    from langchain.chat_models import init_chat_model
    init_chat_model("anthropic:<model name>", max_tokens=...)
and compare the two objects' types.

Run it:   uv run python check.py 8

--- ENV ---
ANTHROPIC_API_KEY=sk-ant-test-key-1234
CHATBOT_MAX_TOKENS=512
--- EXPECTED OUTPUT ---
Type: ChatAnthropic
Model: claude-sonnet-5-5
Max tokens: 512
Temperature: None
With CHATBOT_TEMPERATURE=1.0 -> Temperature: 1.0
Without a key -> RuntimeError: Missing environment variable: ANTHROPIC_API_KEY
"""

import os

from langchain_anthropic import ChatAnthropic


def build_model() -> ChatAnthropic:
    # TODO: build ChatAnthropic from the environment variables (rules in the docstring)
    raise NotImplementedError('TODO: build ChatAnthropic from the environment variables (rules in the docstring)')


if __name__ == "__main__":
    model = build_model()
    print(f"Type: {type(model).__name__}")
    print(f"Model: {model.model}")
    print(f"Max tokens: {model.max_tokens}")
    print(f"Temperature: {model.temperature}")

    os.environ["CHATBOT_TEMPERATURE"] = "1.0"
    print(f"With CHATBOT_TEMPERATURE=1.0 -> Temperature: {build_model().temperature}")

    del os.environ["ANTHROPIC_API_KEY"]
    try:
        build_model()
    except RuntimeError as error:
        print(f"Without a key -> RuntimeError: {error}")
