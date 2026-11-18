"""
Exercise 05_03 - Streaming chunks -> one message

Concepts: slicing, loops, string building, dicts, type hints.

A streamed reply arrives as many small deltas. The history does NOT get one entry
per chunk: you accumulate the text and append exactly ONE assistant message at the
end. Usage numbers usually ride along with the final chunk.

Chunk shapes:
  {"type": "start", "model": "demo-1"}
  {"type": "delta", "text": "Hel"}
  {"type": "stop", "usage": {"prompt": 12, "completion": 8}}

Task - implement the four functions; the demo at the bottom uses them:
  chunk_text(text, size)      slice text into delta chunks of exactly size characters
                              (the last one may be shorter). size >= 1.
                              Empty text -> []. Watch your range step.
  collect_text(chunks)        concatenate the delta texts in order, ignore other types
  final_usage(chunks)         usage from the LAST stop chunk, or {} if there is none
  finish(history, chunks)     append ONE assistant message with the collected text,
                              return the usage

Run it: uv run python stream.py

--- EXPECTED OUTPUT ---
Chunks: 7
Deltas: ['An orde', 'red, mu', 'table, ', 'collect', 'ion.']
Text: An ordered, mutable collection.
Usage: {'prompt': 12, 'completion': 8}
Messages: 2
user: What is a list?
assistant: An ordered, mutable collection.
No chunks: '' {}
"""


# fake the stream
def chunk_text(text: str, size: int) -> list[dict]:
    count = 0
    chunks: list[dict] = []
    while count < len(text):
        txt = text[count : count + size]
        chunks.append({"type": "delta", "text": txt})
        count += size
    return chunks
    # return [
    #     {"type": "delta", "text": text[i : i + size]} for i in range(0, len(text), size)
    # ]


# glue the pieces back
def collect_text(chunks: list[dict]) -> str:
    result: list[str] = []
    for chunk in chunks:
        if chunk["type"] == "delta":
            # print(f"{chunk}")
            result.append(chunk["text"])
    return "".join(result)
    # return "".join(c["text"] for c in chunks if c["type"] == "delta")


# find the token counts
def final_usage(chunks: list[dict]) -> dict[str, int]:
    usage: dict[str, int] = {}
    for c in chunks:
        if c["type"] == "stop":
            usage = c["usage"]
    return usage


# the one that matters
def finish(history: list[dict], chunks: list[dict]) -> dict[str, int]:
    history.append({"role": "assistannt", "content": collect_text(chunks)})
    return final_usage(chunks)


if __name__ == "__main__":
    text = "An ordered, mutable collection."
    chunks: list[dict] = [{"type": "start", "model": "demo-1"}]
    chunks += chunk_text(text, 7)
    chunks.append({"type": "stop", "usage": {"prompt": 12, "completion": 8}})

    print(f"Chunks: {len(chunks)}")
    print(f"Deltas: {[c['text'] for c in chunks if c['type'] == 'delta']}")
    print(f"Text: {collect_text(chunks)}")

    history: list[dict] = [{"role": "user", "content": "What is a list?"}]
    usage = finish(history, chunks)
    print(f"Usage: {usage}")
    print(f"Messages: {len(history)}")
    for m in history:
        print(f"{m['role']}: {m['content']}")
    print(f"No chunks: {collect_text([])!r} {final_usage([])}")
