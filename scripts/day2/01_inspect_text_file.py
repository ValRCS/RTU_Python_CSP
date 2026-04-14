"""
Day 2 Session 1

Read a UTF-8 text file and inspect its contents before cleaning.
This script helps identify blank lines, lines with digits, repeated spaces,
and possible encoding problems in raw survey-style text.
"""

from collections import Counter


RAW_PATH = "data/day2/responses_raw.txt"


def read_text_file(path: str, encoding: str = "utf-8") -> str:
    """Read a text file and return its full contents as one string."""
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def split_into_lines(text: str) -> list[str]:
    """Split text into lines without keeping trailing newline characters."""
    return text.splitlines()


def find_blank_lines(lines: list[str]) -> list[int]:
    """Return 1-based line numbers for blank or whitespace-only lines."""
    return [i for i, line in enumerate(lines, start=1) if line.strip() == ""]


def find_digit_lines(lines: list[str]) -> list[int]:
    """Return 1-based line numbers for lines containing any digit."""
    return [i for i, line in enumerate(lines, start=1) if any(ch.isdigit() for ch in line)]


def find_lines_with_extra_spaces(lines: list[str]) -> list[int]:
    """Return 1-based line numbers for lines containing double spaces."""
    return [i for i, line in enumerate(lines, start=1) if "  " in line]


def find_duplicate_lines(lines: list[str]) -> list[tuple[str, int]]:
    """Return duplicate non-empty lines and how many times they appear."""
    counts = Counter(line.strip() for line in lines if line.strip() != "")
    return [(line, count) for line, count in counts.items() if count > 1]


def print_inspection_report(lines: list[str]) -> None:
    """Print a compact inspection report for the raw text."""
    blank_lines = find_blank_lines(lines)
    digit_lines = find_digit_lines(lines)
    extra_space_lines = find_lines_with_extra_spaces(lines)
    duplicate_lines = find_duplicate_lines(lines)

    print("Raw text inspection")
    print(f"- Total lines: {len(lines)}")
    print(f"- Blank lines: {blank_lines}")
    print(f"- Lines with digits: {digit_lines}")
    print(f"- Lines with repeated spaces: {extra_space_lines}")
    print(f"- Duplicate non-empty lines: {len(duplicate_lines)}")

    print("\nFirst 5 lines")
    for i, line in enumerate(lines[:5], start=1):
        print(f"{i}: {line}")

    if duplicate_lines:
        print("\nDuplicate line examples")
        for line, count in duplicate_lines[:3]:
            print(f"{count}x | {line}")


def main() -> None:
    """Run the raw text inspection workflow."""
    text = read_text_file(RAW_PATH)
    lines = split_into_lines(text)
    print_inspection_report(lines)

    # TODO: Add a simple encoding warning if suspicious mojibake patterns appear.
    # TODO: Add detection for very long lines that may indicate malformed exports.
    # TODO: Extend the report with counts for uppercase-heavy or punctuation-heavy lines.


if __name__ == "__main__":
    main()
