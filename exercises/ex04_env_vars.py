"""Exercise 04 - Environment variables

Concepts: os.environ, .get() with a default, KeyError, env vars are always str,
          never printing a full secret.

Why: API keys and settings live outside your code. In the real chatbots they come
from a .env file (see .env.example) loaded with python-dotenv. Never commit .env.

Task - implement three helpers, then run the demo at the bottom:
  get_setting(name, default)  -> the variable's value, or `default` if it is not set
  require_env(name)           -> the value, or raise RuntimeError("Missing environment
                                 variable: <name>") if it is unset OR empty
  mask(secret)                -> first 7 characters + "..." + last 2 characters.
                                 Secrets shorter than 12 characters become "***".

The demo converts CHATBOT_MAX_TOKENS to an int: os.environ only holds strings.
check.py sets exactly the variables in the ENV section below (and removes any other
CHATBOT_* / ANTHROPIC_* ones), so CHATBOT_MODEL is deliberately NOT set.

Run it:   uv run python check.py 4

--- ENV ---
CHATBOT_NAME=Sage
CHATBOT_MAX_TOKENS=512
ANTHROPIC_API_KEY=sk-ant-test-key-1234
--- EXPECTED OUTPUT ---
Name: Sage
Model: claude-sonnet-5-5
Max tokens: 512 (int)
Key: sk-ant-...34
Short key: ***
Error: Missing environment variable: CHATBOT_MISSING
"""

import os


def get_setting(name: str, default: str) -> str:
    # TODO: return os.environ's value for `name`, or `default`
    raise NotImplementedError("TODO: return os.environ's value for `name`, or `default`")


def require_env(name: str) -> str:
    # TODO: raise RuntimeError(f"Missing environment variable: {name}") when unset/empty
    raise NotImplementedError('TODO: raise RuntimeError(f"Missing environment variable: {name}") when unset/empty')


def mask(secret: str) -> str:
    # TODO: mask the secret (rules in the docstring)
    raise NotImplementedError('TODO: mask the secret (rules in the docstring)')


if __name__ == "__main__":
    print(f"Name: {get_setting('CHATBOT_NAME', 'Assistant')}")
    print(f"Model: {get_setting('CHATBOT_MODEL', 'claude-sonnet-5-5')}")
    max_tokens = int(get_setting("CHATBOT_MAX_TOKENS", "1024"))
    print(f"Max tokens: {max_tokens} ({type(max_tokens).__name__})")
    print(f"Key: {mask(require_env('ANTHROPIC_API_KEY'))}")
    print(f"Short key: {mask('abc123')}")
    try:
        require_env("CHATBOT_MISSING")
    except RuntimeError as error:
        print(f"Error: {error}")
