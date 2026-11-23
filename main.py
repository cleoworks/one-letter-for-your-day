"""v1.1: Write the one-letter entry for make.fun's "One Letter for Your Day".

The entry is a single letter: the letter of the word that describes the
day. Behind P sits "procrastinating" — the whole day spent putting
everything off until tomorrow, a confession everyone recognises at once.
The program writes that letter to /output/entry.txt (the program/v1
harness contract) and prints it to stdout. Exactly one character, no
newline, nothing else.
"""

from pathlib import Path

LETTER = "P"


def output_path() -> Path:
    """The harness output location, with a local fallback for testing."""
    system_output = Path("/output")
    if system_output.is_dir():
        return system_output / "entry.txt"
    local_output = Path(__file__).parent / "output"
    local_output.mkdir(parents=True, exist_ok=True)
    return local_output / "entry.txt"


def main() -> None:
    path = output_path()
    path.write_text(LETTER, encoding="utf-8")
    assert path.read_text(encoding="utf-8") == LETTER, "entry.txt round-trip mismatch"
    print(LETTER)


if __name__ == "__main__":
    main()
