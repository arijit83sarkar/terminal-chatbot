"""Run exercises and compare their output with the EXPECTED OUTPUT in each docstring.

    uv run python check.py          # progress table for every exercise
    uv run python check.py 3        # run exercise 03 and show a full diff / traceback
    uv run python check.py exercises/ex03_input_loop.py

How it works
- The exercise's module docstring may contain these sections:
      --- INPUT ---            lines fed to input(), one per call
      --- ENV ---              NAME=value lines set as environment variables
      --- EXPECTED OUTPUT ---  exactly what the program should print
- input() is replaced so the transcript looks like a real terminal session:
  the prompt AND the line that was "typed" both appear in the output.
- Before each run, every CHATBOT_* and ANTHROPIC_* variable is removed from the
  environment, so only the variables in the ENV section exist.
- Trailing whitespace at the end of a line is ignored.
"""

from __future__ import annotations

import ast
import builtins
import contextlib
import difflib
import io
import os
import re
import runpy
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISES = ROOT / "exercises"
HEADER = re.compile(r"^--- (INPUT|ENV|EXPECTED OUTPUT) ---$")


def parse_sections(path: Path) -> dict[str, list[str]]:
    doc = ast.get_docstring(ast.parse(path.read_text()), clean=False) or ""
    sections: dict[str, list[str]] = {}
    current: list[str] | None = None
    for line in doc.splitlines():
        match = HEADER.match(line)
        if match:
            current = sections.setdefault(match.group(1), [])
        elif current is not None:
            current.append(line)
    for lines in sections.values():
        while lines and not lines[-1].strip():
            lines.pop()
    return sections


def run_exercise(path: Path, inputs: list[str], env: dict[str, str]) -> tuple[str, BaseException | None]:
    """Run the file as a script. Returns (stdout, exception-or-None)."""
    pending = iter(inputs)

    def fake_input(prompt: object = "") -> str:
        try:
            line = next(pending)
        except StopIteration:
            raise EOFError("ran out of INPUT lines (your program asked for more input than expected)") from None
        print(f"{prompt}{line}")
        return line

    saved_env = dict(os.environ)
    for name in list(os.environ):
        if name.startswith(("CHATBOT_", "ANTHROPIC_")):
            del os.environ[name]
    os.environ.update(env)
    real_input = builtins.input
    builtins.input = fake_input
    sys.path.insert(0, str(ROOT))
    buffer = io.StringIO()
    error: BaseException | None = None
    try:
        with contextlib.redirect_stdout(buffer):
            runpy.run_path(str(path), run_name="__main__")
    except SystemExit as exc:  # sys.exit() is a normal way to stop a script
        if exc.code not in (None, 0):
            error = exc
    except BaseException as exc:  # noqa: BLE001 - we want to report everything
        error = exc
    finally:
        builtins.input = real_input
        sys.path.remove(str(ROOT))
        os.environ.clear()
        os.environ.update(saved_env)
    return buffer.getvalue(), error


def print_trace(error: BaseException, path: Path) -> None:
    """Print the traceback starting at the exercise file, hiding check.py/runpy frames."""
    tb = error.__traceback__
    while tb is not None and tb.tb_frame.f_code.co_filename != str(path):
        tb = tb.tb_next
    traceback.print_exception(type(error), error, tb or error.__traceback__)


def check(path: Path, verbose: bool) -> str:
    sections = parse_sections(path)
    if "EXPECTED OUTPUT" not in sections:
        return "SKIP"
    env = dict(line.split("=", 1) for line in sections.get("ENV", []) if "=" in line)
    output, error = run_exercise(path, sections.get("INPUT", []), env)

    if isinstance(error, NotImplementedError):
        if verbose:
            print_trace(error, path)
            print("\nThat traceback is your to-do list: the last line says what is missing,")
            print("the lines above it show where. Read it bottom-up.")
        return "TODO"
    if error is not None:
        if verbose:
            print("Your program printed:\n" + output)
            print_trace(error, path)
        return f"ERROR  {type(error).__name__}: {error}"

    expected = [line.rstrip() for line in sections["EXPECTED OUTPUT"]]
    actual = [line.rstrip() for line in output.rstrip().splitlines()]
    if expected == actual:
        return "PASS"
    if not actual:
        if verbose:
            print("Nothing printed yet. Expected output:\n" + "\n".join(expected))
        return "TODO"
    if verbose:
        diff = difflib.unified_diff(expected, actual, "expected", "actual", lineterm="")
        print("\n".join(diff))
    return "FAIL"


def resolve(arg: str) -> Path:
    if arg.isdigit():
        matches = sorted(EXERCISES.glob(f"ex{int(arg):02d}_*.py"))
        if not matches:
            sys.exit(f"No exercise numbered {arg} in {EXERCISES}")
        return matches[0]
    return Path(arg).resolve()


def main(argv: list[str]) -> int:
    if argv:
        paths = [resolve(arg) for arg in argv]
    else:
        paths = sorted(EXERCISES.glob("ex*.py"))
    verbose = len(paths) == 1
    failed = False
    for path in paths:
        label, _, detail = check(path, verbose).partition("  ")
        failed |= label not in ("PASS", "SKIP")
        print(f"{label:<6} {path.name}" + (f"  <- {detail}" if detail else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
