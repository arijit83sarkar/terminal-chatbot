"""Exercise 01 - Variables and f-strings

Concepts: variables, str/int/float/bool, f-strings and format specs.

Task
  1. Create these variables (names and values are fixed):
         bot_name     = "Sage"      (str)
         user_name    = "Arijit"    (str)
         turns        = 3           (int)
         tokens_used  = 2400        (int)
         usd_per_1k   = 0.003       (float, price per 1,000 tokens)
         is_streaming = False       (bool)
  2. Compute cost = tokens_used / 1000 * usd_per_1k
  3. Print the six lines in EXPECTED OUTPUT using f-strings only
     (no + concatenation, no .format()).

Hints
  {value:,}   thousands separator      {value:.4f}  four decimals
  {value!r}   the repr (adds quotes)   type(value).__name__  is the type's name

Run it:   uv run python check.py 1

--- EXPECTED OUTPUT ---
Sage: Hello, Arijit!
Turns: 3 | Tokens: 2,400
Cost: $0.0072
Streaming: False
Repr: 'Sage'
Types: str, int, float, bool
"""

# TODO 1: create the variables
bot_name = "Sage"
user_name = "Arijit"
turns = 3
tokens_used = 2400
usd_per_1k = 0.003
is_streaming = False
...

# TODO 2: compute the cost
computed_cost = tokens_used / 1000 * usd_per_1k
...

# TODO 3: print the six lines
print(f"{bot_name}: Hello, {user_name}!")
print(f"Turns: {turns} | Tokens: {tokens_used:,}")
print(f"Cost: ${computed_cost:.4f}")
print(f"Streaming: {is_streaming}")
print(f"Repr: {bot_name!r}")
print(
    f"Types: {type(bot_name).__name__}, {type(turns).__name__}, {type(computed_cost).__name__}, {type(is_streaming).__name__}"
)
...
