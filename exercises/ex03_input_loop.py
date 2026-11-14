"""Exercise 03 - input()

Concepts: input(), str.strip(), str.lower(), a while True loop with break.

Task - an echo bot:
  1. Ask for a name:  input("Your name: ")  and strip surrounding whitespace.
  2. Print "Nice to meet you, <name>!"
  3. Loop forever:
       text = input("You: ") stripped
       * empty            -> ask again, count nothing
       * "quit" (any case) -> leave the loop
       * anything else    -> count it and print  Bot: you said <repr of text>
  4. After the loop print "Bye <name>! (<count> messages)"

check.py feeds the INPUT lines below to input() (the third one is an empty answer)
and shows them in the transcript the way a terminal would. To try it by hand, run the file directly:
    uv run python exercises/ex03_input_loop.py

Run the check:   uv run python check.py 3

--- INPUT ---
Arijit
hello

How are you?
  QUIT
--- EXPECTED OUTPUT ---
Your name: Arijit
Nice to meet you, Arijit!
You: hello
Bot: you said 'hello'
You:
You: How are you?
Bot: you said 'How are you?'
You:   QUIT
Bye Arijit! (2 messages)
"""

# TODO: write the whole program
name = input("Your name: ")
print(f"Nice to meet you, {name.strip()}!")

count = 0
while True:
    text = input("You: ").strip()
    if not text:
        continue
    if text.lower() == "quit":
        break
    count += 1
    print(f"Bot: you said {text!r}")

print(f"Bye {name}! ({count} messages)")
...
