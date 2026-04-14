"""
Day 2 Session 5

Package the full text-processing workflow into a simple reusable class.
The script loads raw text, cleans it, tokenizes it, counts words,
writes outputs, and prints a compact report.
"""

import string


RAW_PATH = "data/day2/responses_raw.txt"
STOPWORDS_PATH = "data/day2/stopwords_lv.txt"
OUTPUT_CLEANED_PATH = "data/day2/generated_cleaned_responses_final.txt"
OUTPUT_FREQ_PATH = "data/day2/generated_word_frequencies_final.txt"


def clean_line(line: str) -> str:
    """Normalize one line of raw text."""
    line = line.lower().strip()
    line = line.translate(str.maketrans("", "", string.punctuation))
    return " ".join(line.split())


class TextCorpus:
    """A small reusable object for loading, cleaning, and analyzing text files."""

    def __init__(self, raw_path: str, stopwords_path: str, encoding: str = "utf-8"):
        self.raw_path = raw_path
        self.stopwords_path = stopwords_path
        self.encoding = encoding
        self.raw_lines: list[str] = []
        self.stopwords: set[str] = set()
        self.cleaned_lines: list[str] = []
        self.tokens: list[str] = []

    def load(self) -> None:
        """Load raw lines and stopwords from disk."""
        with open(self.raw_path, "r", encoding=self.encoding) as f:
            self.raw_lines = f.read().splitlines()

        with open(self.stopwords_path, "r", encoding=self.encoding) as f:
            self.stopwords = {line.strip() for line in f if line.strip() != ""}

    def clean(self) -> None:
        """Clean raw lines and store the cleaned result."""
        self.cleaned_lines = [clean_line(line) for line in self.raw_lines if clean_line(line) != ""]

    def tokenize(self) -> None:
        """Split cleaned lines into tokens."""
        self.tokens = [token for line in self.cleaned_lines for token in line.split()]

    def filtered_tokens(self) -> list[str]:
        """Return tokens with stopwords removed."""
        return [token for token in self.tokens if token not in self.stopwords]

    def word_counts(self) -> dict[str, int]:
        """Return token frequencies for filtered tokens."""
        counts: dict[str, int] = {}
        for token in self.filtered_tokens():
            counts[token] = counts.get(token, 0) + 1
        return counts

    def top_words(self, n: int = 10) -> list[tuple[str, int]]:
        """Return the top N words by frequency."""
        counts = self.word_counts()
        return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]

    def save_cleaned(self, path: str) -> None:
        """Save cleaned lines to a text file."""
        with open(path, "w", encoding=self.encoding) as f:
            for line in self.cleaned_lines:
                f.write(line + "\n")

    def save_word_frequencies(self, path: str) -> None:
        """Save sorted word frequencies to a tab-separated text file."""
        with open(path, "w", encoding=self.encoding) as f:
            for word, count in sorted(self.word_counts().items(), key=lambda item: (-item[1], item[0])):
                f.write(f"{word}\t{count}\n")

    def summary(self) -> dict[str, int]:
        """Return a compact numeric summary of the corpus."""
        filtered = self.filtered_tokens()
        return {
            "raw_line_count": len(self.raw_lines),
            "cleaned_line_count": len(self.cleaned_lines),
            "token_count": len(self.tokens),
            "filtered_token_count": len(filtered),
            "unique_word_count": len(set(filtered)),
        }


def main() -> None:
    """Run the full class-based text processing workflow."""
    corpus = TextCorpus(RAW_PATH, STOPWORDS_PATH)
    corpus.load()
    corpus.clean()
    corpus.tokenize()
    corpus.save_cleaned(OUTPUT_CLEANED_PATH)
    corpus.save_word_frequencies(OUTPUT_FREQ_PATH)

    print(f"Saved cleaned output to: {OUTPUT_CLEANED_PATH}")
    print(f"Saved frequency output to: {OUTPUT_FREQ_PATH}")

    print("\nSummary")
    for key, value in corpus.summary().items():
        print(f"- {key}: {value}")

    print("\nTop 10 words")
    for word, count in corpus.top_words(10):
        print(f"{word}\t{count}")

    # TODO: Add basic error handling for missing files.
    # TODO: Add an option to ignore very short words.
    # TODO: Add a method that returns the longest words in the corpus.


if __name__ == "__main__":
    main()
