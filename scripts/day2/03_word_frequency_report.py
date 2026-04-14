"""
Day 2 Session 3

Read cleaned text, remove stopwords, count word frequencies, and save
a frequency report as a UTF-8 tab-separated text file.
"""


CLEANED_PATH = "data/day2/generated_cleaned_responses.txt"
STOPWORDS_PATH = "data/day2/stopwords_lv.txt"
OUTPUT_FREQ_PATH = "data/day2/generated_word_frequencies.txt"


def read_lines(path: str, encoding: str = "utf-8") -> list[str]:
    """Read a text file and return non-newline-stripped lines."""
    with open(path, "r", encoding=encoding) as f:
        return f.read().splitlines()


def load_stopwords(path: str, encoding: str = "utf-8") -> set[str]:
    """Load stopwords from a text file into a set."""
    lines = read_lines(path, encoding=encoding)
    return {line.strip() for line in lines if line.strip() != ""}


def tokenize_lines(lines: list[str]) -> list[str]:
    """Split cleaned lines into a flat list of tokens."""
    tokens = []
    for line in lines:
        tokens.extend(line.split())
    return tokens


def remove_stopwords(tokens: list[str], stopwords: set[str]) -> list[str]:
    """Remove stopwords from a token list."""
    return [token for token in tokens if token not in stopwords]


def count_words(tokens: list[str]) -> dict[str, int]:
    """Count token frequencies with a dictionary."""
    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    return counts


def sort_word_counts(word_counts: dict[str, int]) -> list[tuple[str, int]]:
    """Sort word counts by descending frequency and then alphabetically."""
    return sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))


def write_word_frequencies(path: str, word_counts: list[tuple[str, int]], encoding: str = "utf-8") -> None:
    """Write word frequencies as tab-separated lines."""
    with open(path, "w", encoding=encoding) as f:
        for word, count in word_counts:
            f.write(f"{word}\t{count}\n")


def main() -> None:
    """Build and save a word frequency report from cleaned text."""
    cleaned_lines = read_lines(CLEANED_PATH)
    stopwords = load_stopwords(STOPWORDS_PATH)
    tokens = tokenize_lines(cleaned_lines)
    filtered_tokens = remove_stopwords(tokens, stopwords)
    word_counts = count_words(filtered_tokens)
    sorted_counts = sort_word_counts(word_counts)
    write_word_frequencies(OUTPUT_FREQ_PATH, sorted_counts)

    print(f"Saved frequency report to: {OUTPUT_FREQ_PATH}")
    print(f"Token count: {len(tokens)}")
    print(f"Filtered token count: {len(filtered_tokens)}")
    print("Top 10 words:")
    for word, count in sorted_counts[:10]:
        print(f"{word}\t{count}")

    # TODO: Compare counts before and after stopword removal.
    # TODO: Add a unique-word count to the report.
    # TODO: Add an option to skip very short words such as length < 3.


if __name__ == "__main__":
    main()
