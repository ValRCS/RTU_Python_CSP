"""
Day 2 Session 4

Refactor the text cleaning and counting workflow using comprehensions
and generators to make the pipeline shorter and more expressive.
"""

import string


RAW_PATH = "data/day2/responses_raw.txt"
STOPWORDS_PATH = "data/day2/stopwords_lv.txt"
OUTPUT_CLEANED_PATH = "data/day2/generated_cleaned_responses_v2.txt"
OUTPUT_FREQ_PATH = "data/day2/generated_word_frequencies_v2.txt"


def clean_line(line: str) -> str:
    """Normalize one line of text."""
    line = line.lower().strip()
    line = line.translate(str.maketrans("", "", string.punctuation))
    return " ".join(line.split())


def read_lines(path: str, encoding: str = "utf-8") -> list[str]:
    """Read a UTF-8 text file into a list of lines."""
    with open(path, "r", encoding=encoding) as f:
        return f.read().splitlines()


def load_stopwords(path: str, encoding: str = "utf-8") -> set[str]:
    """Load stopwords into a set."""
    return {line.strip() for line in read_lines(path, encoding=encoding) if line.strip() != ""}


def cleaned_lines_from_file(path: str, encoding: str = "utf-8") -> list[str]:
    """Read and clean lines using a list comprehension."""
    lines = read_lines(path, encoding=encoding)
    return [clean_line(line) for line in lines if clean_line(line) != ""]


def cleaned_line_generator(path: str, encoding: str = "utf-8"):
    """Yield cleaned non-empty lines one by one."""
    for line in read_lines(path, encoding=encoding):
        cleaned = clean_line(line)
        if cleaned != "":
            yield cleaned


def token_generator(lines: list[str]):
    """Yield tokens one by one from cleaned lines."""
    for line in lines:
        for token in line.split():
            yield token


def build_word_counts(tokens: list[str], stopwords: set[str]) -> dict[str, int]:
    """Build a frequency dictionary from filtered tokens."""
    filtered_tokens = [token for token in tokens if token not in stopwords]
    unique_tokens = {token for token in filtered_tokens}
    return {token: filtered_tokens.count(token) for token in unique_tokens}


def summarize_counts(word_counts: dict[str, int], top_n: int = 10) -> list[tuple[str, int]]:
    """Return the top N word counts."""
    return sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))[:top_n]


def write_lines(path: str, lines: list[str], encoding: str = "utf-8") -> None:
    """Write plain text lines to a file."""
    with open(path, "w", encoding=encoding) as f:
        for line in lines:
            f.write(line + "\n")


def write_word_frequencies(path: str, pairs: list[tuple[str, int]], encoding: str = "utf-8") -> None:
    """Write word frequency pairs to a file."""
    with open(path, "w", encoding=encoding) as f:
        for word, count in pairs:
            f.write(f"{word}\t{count}\n")


def main() -> None:
    """Run the text pipeline in a more compact intermediate-Python style."""
    stopwords = load_stopwords(STOPWORDS_PATH)
    cleaned_lines = cleaned_lines_from_file(RAW_PATH)
    tokens = list(token_generator(cleaned_lines))
    word_counts = build_word_counts(tokens, stopwords)
    top_words = summarize_counts(word_counts, top_n=10)

    write_lines(OUTPUT_CLEANED_PATH, cleaned_lines)
    write_word_frequencies(OUTPUT_FREQ_PATH, sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    print(f"Saved cleaned output to: {OUTPUT_CLEANED_PATH}")
    print(f"Saved frequency output to: {OUTPUT_FREQ_PATH}")
    print(f"Cleaned line count: {len(cleaned_lines)}")
    print(f"Token count: {len(tokens)}")
    print("Top 10 words:")
    for word, count in top_words:
        print(f"{word}\t{count}")

    # TODO: Replace the dict-comprehension counting approach with a more efficient one.
    # TODO: Add a generator-based version that avoids building the full token list.
    # TODO: Compare readability between this script and Session 3.


if __name__ == "__main__":
    main()
