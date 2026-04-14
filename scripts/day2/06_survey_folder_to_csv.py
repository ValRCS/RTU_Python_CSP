"""
Day 2 Session 6

Read a folder of Latvian survey text files, extract structured data with
regular expressions, remove stopwords from longer text answers, and save the
result as a CSV table.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


STOPWORDS_PATH = Path("data/day2/stopwords_lv.txt")
DEFAULT_OUTPUT_NAME = "survey_responses_summary.csv"

QUESTION_FIELD_MAP = {
    1: "name",
    2: "age_answer",
    3: "gender",
    4: "contact_answer",
    5: "employment_answer",
    6: "education_answer",
    7: "household_answer",
    8: "income_answer",
    9: "economic_pressures_answer",
    10: "drive_answer",
    11: "bike_answer",
    12: "inflation_impact_answer",
    13: "job_finance_security_answer",
    14: "riga_economy_view_answer",
    15: "improvements_answer",
}

TEXT_FIELDS_FOR_KEYWORDS = [
    "employment_answer",
    "education_answer",
    "household_answer",
    "income_answer",
    "economic_pressures_answer",
    "inflation_impact_answer",
    "job_finance_security_answer",
    "riga_economy_view_answer",
    "improvements_answer",
]

CSV_COLUMNS = [
    "source_file",
    "name",
    "age",
    "age_answer",
    "gender",
    "email",
    "phone",
    "employment_type",
    "occupation",
    "years_in_profession",
    "employment_answer",
    "employment_answer_keywords",
    "education_answer",
    "education_answer_keywords",
    "household_answer",
    "household_answer_keywords",
    "income_min_eur",
    "income_max_eur",
    "income_answer",
    "income_answer_keywords",
    "economic_pressures_answer",
    "economic_pressures_answer_keywords",
    "drive_km_week",
    "bike_km_week",
    "inflation_impact_answer",
    "inflation_impact_answer_keywords",
    "job_finance_security_answer",
    "job_finance_security_answer_keywords",
    "riga_economy_view_answer",
    "riga_economy_view_answer_keywords",
    "improvements_answer",
    "improvements_answer_keywords",
]


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert a folder of Latvian survey .txt files into a CSV summary."
    )
    parser.add_argument(
        "-i",
        "--input-folder",
        required=True,
        help="Folder that contains the survey .txt files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output CSV path. Default: <input-folder>/survey_responses_summary.csv",
    )
    return parser.parse_args()


def load_stopwords(path: Path, encoding: str = "utf-8") -> set[str]:
    """Load stopwords from a UTF-8 text file."""
    with path.open("r", encoding=encoding) as file:
        return {line.strip().lower() for line in file if line.strip() != ""}


def read_text(path: Path, encoding: str = "utf-8") -> str:
    """Read a UTF-8 text file."""
    with path.open("r", encoding=encoding) as file:
        return file.read()


def parse_survey_blocks(text: str) -> dict[int, str]:
    """Extract numbered question-answer blocks with regex."""
    pattern = re.compile(r"(?ms)^\s*(\d+)\.\s+.*?\n(.*?)(?=^\s*\d+\.\s+|\Z)")
    answers: dict[int, str] = {}

    for match in pattern.finditer(text):
        question_number = int(match.group(1))
        answer = match.group(2).strip()
        answers[question_number] = answer

    return answers


def normalize_text(text: str) -> str:
    """Lowercase text and keep word-like tokens for keyword extraction."""
    lowered = text.lower()
    cleaned = re.sub(r"[^\w\s]", " ", lowered, flags=re.UNICODE)
    return " ".join(cleaned.split())


def keyword_text(text: str, stopwords: set[str]) -> str:
    """Remove stopwords from text and return normalized keywords."""
    tokens = normalize_text(text).split()
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return " ".join(filtered_tokens)


def compact_value(text: str) -> str:
    """Strip extra whitespace and trailing sentence punctuation."""
    return text.strip().rstrip(".")


def first_int(text: str) -> int | None:
    """Return the first integer found in text."""
    match = re.search(r"\d+", text)
    return int(match.group()) if match else None


def income_range(text: str) -> tuple[int | None, int | None]:
    """Extract minimum and maximum income values from Latvian survey text."""
    numbers = [int(number) for number in re.findall(r"\d+", text)]
    if not numbers:
        return None, None
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    return numbers[0], numbers[1]


def extract_email(text: str) -> str:
    """Extract an email address from text if present."""
    match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", text, flags=re.UNICODE)
    return match.group(0) if match else ""


def extract_phone(text: str) -> str:
    """Extract a Latvian-style phone number from text if present."""
    match = re.search(r"\+371\s?\d{8}", text)
    return match.group(0) if match else ""


def employment_type(text: str) -> str:
    """Return a compact employment type label from the employment answer."""
    lowered = text.lower()
    if "nepilnu slodzi" in lowered:
        return "nepilna slodze"
    if "pilnu slodzi" in lowered:
        return "pilna slodze"
    if "pensionār" in lowered:
        return "pensionārs/pensionāre"
    return ""


def occupation(text: str) -> str:
    """Extract the occupation phrase from the employment answer."""
    match = re.search(r"\bpar (.+?)(?=,|\sun\b|$)", text, flags=re.IGNORECASE | re.UNICODE)
    if match:
        return compact_value(match.group(1))

    lowered = text.lower()
    if "pensionāre" in lowered:
        return "pensionāre"
    if "pensionārs" in lowered:
        return "pensionārs"
    return ""


def survey_row(path: Path, stopwords: set[str]) -> dict[str, str | int | None]:
    """Parse one survey text file into a flat CSV row."""
    answers = parse_survey_blocks(read_text(path))
    parsed_answers = {
        field_name: answers.get(question_number, "")
        for question_number, field_name in QUESTION_FIELD_MAP.items()
    }

    row: dict[str, str | int | None] = {column: "" for column in CSV_COLUMNS}
    row["source_file"] = path.name

    row["name"] = compact_value(str(parsed_answers["name"]))
    row["age_answer"] = str(parsed_answers["age_answer"])
    row["gender"] = compact_value(str(parsed_answers["gender"]))
    row["employment_answer"] = str(parsed_answers["employment_answer"])
    row["education_answer"] = str(parsed_answers["education_answer"])
    row["household_answer"] = str(parsed_answers["household_answer"])
    row["income_answer"] = str(parsed_answers["income_answer"])
    row["economic_pressures_answer"] = str(parsed_answers["economic_pressures_answer"])
    row["inflation_impact_answer"] = str(parsed_answers["inflation_impact_answer"])
    row["job_finance_security_answer"] = str(parsed_answers["job_finance_security_answer"])
    row["riga_economy_view_answer"] = str(parsed_answers["riga_economy_view_answer"])
    row["improvements_answer"] = str(parsed_answers["improvements_answer"])

    row["age"] = first_int(str(parsed_answers["age_answer"]))
    row["email"] = extract_email(str(parsed_answers["contact_answer"]))
    row["phone"] = extract_phone(str(parsed_answers["contact_answer"]))
    row["employment_type"] = employment_type(str(parsed_answers["employment_answer"]))
    row["occupation"] = occupation(str(parsed_answers["employment_answer"]))
    row["years_in_profession"] = first_int(str(parsed_answers["employment_answer"]))
    income_min, income_max = income_range(str(parsed_answers["income_answer"]))
    row["income_min_eur"] = income_min
    row["income_max_eur"] = income_max
    row["drive_km_week"] = first_int(str(parsed_answers["drive_answer"]))
    row["bike_km_week"] = first_int(str(parsed_answers["bike_answer"]))

    for field_name in TEXT_FIELDS_FOR_KEYWORDS:
        row[f"{field_name}_keywords"] = keyword_text(str(row[field_name]), stopwords)

    return row


def write_csv(path: Path, rows: list[dict[str, str | int | None]], encoding: str = "utf-8") -> None:
    """Write survey rows to CSV."""
    with path.open("w", encoding=encoding, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Run the survey folder to CSV pipeline."""
    args = parse_args()
    input_folder = Path(args.input_folder)
    output_path = Path(args.output) if args.output else input_folder / DEFAULT_OUTPUT_NAME

    if not input_folder.exists() or not input_folder.is_dir():
        raise FileNotFoundError(f"Input folder not found: {input_folder}")

    stopwords = load_stopwords(STOPWORDS_PATH)
    survey_paths = sorted(input_folder.glob("*.txt"))
    rows = [survey_row(path, stopwords) for path in survey_paths]

    write_csv(output_path, rows)

    print(f"Input folder: {input_folder}")
    print(f"Survey files processed: {len(rows)}")
    print(f"Saved CSV to: {output_path}")

    # TODO: Add validation for missing question numbers inside a file.
    # TODO: Add derived columns for household size when the wording allows it.
    # TODO: Add an option to save cleaned keyword text to a separate report.


if __name__ == "__main__":
    main()
