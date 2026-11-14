"""Exercise 02 - while loops, break, continue

Concepts: while, a counter, break (stop), continue (skip), sentinel values.

Task
  Part A - walk through `scripted` with a while loop and an index (no `for`):
    * skip empty strings                     (continue)
    * stop when you reach "quit"             (break)
    * for every other message print "Turn N: <message>", N counting from 1
    * after the loop print "Stopped at 'quit' after N messages."
  Part B - a turn limit:
    * start with turns_left = 3
    * while turns_left > 0: print "Turns left: <n>" and count down
    * when the loop ends print "Out of turns."

Careful: a while loop whose condition never becomes False runs forever.
Stop it with Ctrl-C. Where do you increase your index? (Think about `continue`.)

Run it:   uv run python check.py 2

--- EXPECTED OUTPUT ---
Turn 1: hi
Turn 2: what's up
Stopped at 'quit' after 2 messages.
Turns left: 3
Turns left: 2
Turns left: 1
Out of turns.
"""

scripted = ["hi", "", "what's up", "quit", "never reached"]

# TODO Part A
count = 0
# print(f"Turn {count+1}: {scripted[count]}")
while count < 3:
    value = scripted[count]
    if value == "":
        continue
    elif value == "quit":
        print(f"Stopped at {value} after {count} messages.")
        break
    else:
        print(f"Turn {count+1}: {value}")
    print(f"Turn {count+1}: {value}")
    count = count + 1

...

# TODO Part B
turn_left = 3
while turn_left > 0:
    print(f"Turns left: {turn_left}")
    turn_left = turn_left - 1
print("Out of turns.")
...
