"""
Day 2 Session 2

Read raw text lines, normalize them, remove noise, and write cleaned text
to a new UTF-8 output file.
"""

import string


RAW_PATH = "data/day2/responses_raw.txt"
OUTPUT_CLEANED_PATH = "data/day2/generated_cleaned_responses.txt"


def read_lines(path: str, encoding: str = "utf-8") -> list[str]:
    """Read a text file and return its lines without trailing newline characters."""
    with open(path, "r", encoding=encoding) as f:
        return f.read().splitlines()


def clean_line(line: str) -> str:
    """Normalize a single line of text into a cleaner form."""
    line = line.lower().strip()
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = " ".join(line.split())
    return line


def clean_lines(lines: list[str]) -> list[str]:
    """Clean all lines and drop empty results."""
    cleaned = []
    for line in lines:
        cleaned_line = clean_line(line)
        if cleaned_line != "":
            cleaned.append(cleaned_line)
    return cleaned


def write_lines(path: str, lines: list[str], encoding: str = "utf-8") -> None:
    """Write lines to a UTF-8 text file, one line per output row."""
    with open(path, "w", encoding=encoding) as f:
        for line in lines:
            f.write(line + "\n")


def compare_raw_and_cleaned(raw_lines: list[str], cleaned_lines: list[str], limit: int = 5) -> None:
    """Print a small side-by-side sample of raw and cleaned lines."""
    print("Raw vs cleaned sample")
    for raw, cleaned in zip(raw_lines[:limit], cleaned_lines[:limit]):
        print(f"RAW   : {raw!r}")
        print(f"CLEAN : {cleaned!r}")
        print("---")


def main() -> None:
    """Run the line-cleaning workflow and save cleaned text."""
    raw_lines = read_lines(RAW_PATH)
    cleaned_lines = clean_lines(raw_lines)
    write_lines(OUTPUT_CLEANED_PATH, cleaned_lines)

    print(f"Saved cleaned lines to: {OUTPUT_CLEANED_PATH}")
    print(f"Raw line count: {len(raw_lines)}")
    print(f"Cleaned line count: {len(cleaned_lines)}")
    compare_raw_and_cleaned(raw_lines, cleaned_lines)

    # TODO: Decide whether digits should be kept or removed.
    # TODO: Add an optional regex-based cleaning variant.
    # TODO: Add a count of how many lines were dropped as empty after cleaning.


if __name__ == "__main__":
    main()
