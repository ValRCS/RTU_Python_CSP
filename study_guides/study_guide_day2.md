# Study Guide: Day 2 Text Processing and Cleaning

This guide matches the Day 2 lesson plan in `lesson_plan/README.md`, the Day 2 notebook in `notebooks/python_intermediate_text_processing.ipynb`, and the sample files in `data/day2/`.

Reference links in this guide were verified on April 14, 2026.

## Day 2 Goals

By the end of Day 2, learners should be able to:

- read text and CSV-style data from files
- recognize and handle common encoding issues
- clean strings into a more usable form
- use regular expressions for simple pattern matching
- build a small, repeatable cleaning pipeline

## 1. Text Processing Workflow

A practical text-cleaning workflow usually looks like this:

1. Read raw input.
2. Normalize line endings and whitespace.
3. Remove or repair invalid values.
4. Standardize text format.
5. Extract useful parts.
6. Save cleaned output.

This pattern matters more than any single function. The course uses it repeatedly.

## 2. Reading Files Safely

The most common pattern is `with open(...)` because it closes the file automatically.

```python
with open("data/day2/responses_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

To read lines:

```python
with open("data/day2/responses_raw.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
```

Why `encoding="utf-8"` matters:

- it makes the expected encoding explicit
- it avoids relying on platform defaults
- it reduces confusion when files move between systems

## 3. Encoding Problems

Typical signs of bad decoding:

- unexpected extra symbols appearing inside words
- one letter turning into two or more characters
- text that looked correct in one program but broken in another

Those patterns usually mean the bytes were decoded using the wrong encoding.

Common rule for this course:

- if a text file was saved as UTF-8, open it with `encoding="utf-8"`

If text already looks corrupted, check:

- how the file was saved
- which encoding Python used to open it
- whether a previous system exported the data incorrectly

## 4. Core String Cleaning Techniques

Start with simple string methods before reaching for regex.

```python
line = "  Python, Excel, and CSV files!  "

cleaned = line.strip()
lowered = cleaned.lower()
replaced = lowered.replace("csv", "comma-separated values")
parts = replaced.split(",")
```

Useful string methods for Day 2:

- `strip()`
- `lower()`
- `upper()`
- `replace()`
- `split()`
- `splitlines()`
- `startswith()`
- `endswith()`

These are often enough for:

- trimming whitespace
- normalizing case
- standardizing repeated labels
- splitting a line into pieces

## 5. Lists, Dictionaries, Sets, and Tuples in Text Work

The Day 2 notebook goes beyond plain strings because text cleaning usually needs a few core data structures.

### Lists

Use lists for ordered collections of lines or tokens.

```python
cleaned_lines = []

for line in lines:
    line = line.strip()
    if line:
        cleaned_lines.append(line)
```

### Dictionaries

Use dictionaries for counts and grouped results.

```python
counts = {}

for word in ["python", "data", "python"]:
    counts[word] = counts.get(word, 0) + 1
```

### Sets

Use sets for uniqueness and fast membership checks.

```python
stopwords = {"un", "ar", "bet"}
unique_words = set(["python", "data", "python"])
```

### Tuples

Use tuples for small fixed records, such as `(word, count)`.

```python
pair = ("python", 3)
```

## 6. Basic Regular Expressions

Regular expressions help when plain string methods are not enough.

Example: remove digits.

```python
import re

text = "report_2026_version_2"
result = re.sub(r"\d+", "", text)
print(result)
```

Example: keep only letters and spaces.

```python
import re

line = "Python 3.14 is useful!"
clean = re.sub(r"[^A-Za-z ]+", "", line)
print(clean)
```

Important Day 2 regex ideas:

- `\d` matches digits
- `\s` matches whitespace
- `+` means one or more
- `[]` defines a character class
- `^` inside `[]` means "not these characters"
- raw strings like `r"\d+"` are preferred for regex patterns

Use regex when you need patterns. Do not use it for every string problem.

## 7. Building a Cleaning Function

A cleaning pipeline becomes easier to test and reuse when it is wrapped in a function.

```python
import re

def clean_line(line):
    line = line.strip().lower()
    line = re.sub(r"\d+", "", line)
    line = re.sub(r"\s+", " ", line)
    return line
```

Benefits:

- one place to maintain logic
- easier testing
- easier reuse across multiple files

## 8. Comprehensions and Generators

The Day 2 notebook introduces concise ways to transform data.

### List comprehension

```python
cleaned_lines = [line.strip() for line in lines if line.strip()]
```

### Generator expression

```python
words = (word for line in cleaned_lines for word in line.split())
```

Why it matters:

- comprehensions are compact and readable for simple transformations
- generators help process items one at a time instead of building large intermediate lists

## 9. Word Frequencies

Counting words is a common first text-analysis task.

```python
counts = {}

for line in cleaned_lines:
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1

top_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
print(top_items[:5])
```

This combines several Day 2 concepts:

- file reading
- string splitting
- loops
- dictionaries
- sorting

## 10. Saving Cleaned Results

Write cleaned output back to disk explicitly.

```python
with open("data/day2/cleaned_responses.txt", "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")
```

This keeps the workflow reproducible:

- raw data stays separate
- cleaned data can be regenerated
- outputs are easy to inspect

## 11. CSV Awareness

Day 2 includes file reading with `.txt` and `.csv`.

For true CSV data, prefer Python's `csv` module instead of manual string splitting when:

- values may contain commas
- quoting rules matter
- rows need structured reading or writing

Example:

```python
import csv

with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## 12. Common Cleaning Decisions

Before cleaning, decide:

- which rows should be removed completely
- which missing values are acceptable
- whether text should be lowercase
- whether punctuation should be kept
- whether numbers are meaningful or noise
- how duplicates should be handled

These are data decisions, not only code decisions.

## 13. Common Day 2 Errors

Typical mistakes:

- forgetting `encoding="utf-8"`
- using regex when `strip()` or `replace()` would be simpler
- splitting CSV data with plain `split(",")` when quoting may exist
- accidentally deleting useful characters during cleaning
- mixing raw and cleaned data in the same file

## 14. How This Connects to the Rest of the Course

Day 2 builds the preprocessing mindset used later for:

- cleaning tabular data in Pandas
- standardizing columns before analysis
- preparing model-ready input for later machine learning examples

## Suggested Practice

- clean `data/day2/responses_raw.txt` into a list of non-empty normalized lines
- count the five most common words after cleaning
- compare the original and cleaned outputs
- test two regex patterns and explain exactly what each one matches

## Course Files

- Day 2 lesson plan: `lesson_plan/README.md`
- Day 2 notebook: `notebooks/python_intermediate_text_processing.ipynb`
- Sample raw data: `data/day2/responses_raw.txt`
- Sample cleaned data: `data/day2/cleaned_responses.txt`
- Stopwords: `data/day2/stopwords_lv.txt`
- Word frequencies: `data/day2/word_frequencies.txt`

## Authoritative References

- Python input and output tutorial: <https://docs.python.org/3/tutorial/inputoutput.html>
- Built-in `open()` documentation: <https://docs.python.org/3/library/functions.html#open>
- String methods (`str`): <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>
- `re` regular expression module: <https://docs.python.org/3/library/re.html>
- Regular Expression HOWTO: <https://docs.python.org/3/howto/regex.html>
- Unicode HOWTO: <https://docs.python.org/3/howto/unicode.html>
- `csv` module: <https://docs.python.org/3/library/csv.html>
