"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer, to /output/entry.txt (the sealed gate reads
that file: UTF-8, 1-199 characters) and prints the same text to stdout.
"""

import os
import sys

ENTRY = (
    "Have you tried turning it off and on again? I ask everyone \u2014 "
    "it's the one fix that's never failed me, "
    "except every single time I've tried it."
)


def resolve_output_path():
    """Pick the entry output path the grader expects.

    The harness runs the program with ENTRY_OUT (a file path) or
    ENTRY_OUT_DIR (a directory) set; fall back to /output/entry.txt.
    Either variable may name a file or a directory, so handle both.
    """
    for var in ("ENTRY_OUT", "ENTRY_OUT_DIR"):
        value = os.environ.get(var)
        if not value:
            continue
        if value.endswith(".txt"):
            return value
        return os.path.join(value, "entry.txt")
    return "/output/entry.txt"


def write_entry(path):
    """Write the entry text (no trailing newline) and return it."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    return ENTRY


def main():
    """Emit the entry to stdout and to the output file, then self-check."""
    text = write_entry(resolve_output_path())
    print(text)
    if not 1 <= len(text) <= 199:
        print(
            "ERROR: entry is %d characters, gate needs 1-199" % len(text),
            file=sys.stderr,
        )
        return 1
    if text != text.strip() or "\n" in text:
        print("ERROR: entry must be a single non-blank line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
