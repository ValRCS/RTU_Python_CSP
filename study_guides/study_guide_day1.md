# Study Guide: Day 1 Foundations and Setup

This guide matches the Day 1 lesson plan in `lesson_plan/README.md`, the Day 1 notebook in `notebooks/python_basics.ipynb`, and the setup notes in `python_vscode_setup/README.md`.

Reference links in this guide were verified on April 14, 2026.

## Day 1 Goals

By the end of Day 1, learners should be able to:

- explain where Python fits in a modern data workflow
- set up a local Python environment in VS Code
- understand the difference between `.py` scripts and Jupyter notebooks
- write small Python programs with variables, types, conditions, loops, lists, and strings

## 1. Python in Data Workflows

For this course, Python is mainly used as a practical tool for:

- reading and transforming data
- automating repeated tasks
- making analysis steps reproducible
- moving from manual spreadsheet work toward reusable code

Typical workflow:

1. Read input data.
2. Clean or transform it.
3. Validate the result.
4. Save outputs for later analysis or reporting.

## 2. Local Environment Setup

The course uses a local setup so students can run the same code repeatedly on their own machine.

Core tools:

- Python
- VS Code
- Python extension for VS Code
- Jupyter extension for VS Code
- a project-specific virtual environment (`.venv`)

### Why use a virtual environment

A virtual environment keeps project dependencies isolated from the rest of the system. That makes the environment easier to reproduce and reduces version conflicts.

### Common setup commands

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

In VS Code, the selected interpreter should point to the `.venv` created for the project.

## 3. Scripts vs Notebooks

### `.py` scripts

Best for:

- repeatable tasks
- production-style workflows
- automation
- code that should run start to finish in one pass

Example:

```python
name = "Anna"
print(f"Hello, {name}")
```

### Jupyter notebooks

Best for:

- step-by-step exploration
- teaching and demonstrations
- mixing code, output, and notes
- testing ideas interactively

Important notebook habit:

- run cells from top to bottom so variables and results stay consistent

## 4. Variables and Core Types

A variable stores a value under a name.

```python
name = "Anna"
age = 32
height = 1.68
is_active = True
```

Common built-in types used on Day 1:

- `str`: text
- `int`: whole numbers
- `float`: decimal numbers
- `bool`: `True` or `False`

Check a value's type with:

```python
print(type(name))
```

## 5. Basic Operations and Type Conversion

Python lets you compute with numbers and compare values.

```python
a = 10
b = 3

print(a + b)
print(a / b)
print(a > b)
print(a == b)
```

Type conversion is common when data starts as text.

```python
text_number = "45"
number = int(text_number)
price = float("12.50")
label = str(99)
```

Use conversion carefully. `int("abc")` will raise an error because the text is not a valid integer.

## 6. Input, Output, and Strings

### Output with `print()`

```python
print("Python works")
```

### Input with `input()`

`input()` always returns text.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name, age)
```

### Common string operations

```python
text = "  Data Processing with Python  "

print(text.strip())
print(text.lower())
print(text.upper())
print(len(text))
print(text.replace("Python", "VS Code"))
```

These methods are used constantly in cleaning and validation tasks.

## 7. Conditions

Conditions allow code to branch.

```python
score = 78

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Review needed")
```

Key syntax rule:

- Python uses indentation as part of the language

## 8. Loops

### `for` loop

Use `for` when you want to process items from a collection.

```python
cities = ["Riga", "Liepaja", "Cesis"]

for city in cities:
    print(city)
```

### `while` loop

Use `while` when repetition depends on a condition.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

## 9. Lists

Lists store ordered collections of values.

```python
numbers = [10, 20, 30]

print(numbers[0])
numbers.append(40)
print(numbers)
```

List skills used early in data work:

- getting items by index
- looping through values
- adding new values
- building transformed lists

Example:

```python
values = [1, 2, 3, 4]
squared = []

for value in values:
    squared.append(value * value)

print(squared)
```

## 10. Functions

Functions make code reusable and easier to read.

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Anna"))
```

Day 1 only needs the core idea:

- define a function with `def`
- pass inputs as parameters
- return a result with `return`

## 11. Common Beginner Errors

Typical Day 1 mistakes:

- missing quotes around text
- mixing text and numbers without conversion
- forgetting a colon after `if`, `for`, `while`, or `def`
- incorrect indentation
- using a variable before assigning a value

These are normal. The important habit is to read the error message and check the exact line it points to.

## 12. How This Connects to the Rest of the Course

Day 1 builds the core habits used later:

- Day 2 uses strings, loops, lists, and functions for text cleaning
- Day 3 and Day 4 apply the same logic to tabular data in Pandas
- reproducible local setup becomes important once projects use multiple files and libraries

## Suggested Practice

- create a script that asks for a user's name and department, then prints a formatted greeting
- write a loop that filters numbers greater than `10`
- clean a text value with `strip()`, `lower()`, and `replace()`
- build a list of transformed values from another list

## Course Files

- Day 1 lesson plan: `lesson_plan/README.md`
- Day 1 notebook: `notebooks/python_basics.ipynb`
- Local setup notes: `python_vscode_setup/README.md`
- Intro script examples: `scripts/python_basics.py`

## Authoritative References

- Python tutorial overview: <https://docs.python.org/3/tutorial/>
- An informal introduction to Python: <https://docs.python.org/3/tutorial/introduction.html>
- More control flow tools: <https://docs.python.org/3/tutorial/controlflow.html>
- Data structures: <https://docs.python.org/3/tutorial/datastructures.html>
- Built-in types: <https://docs.python.org/3/library/stdtypes.html>
- Built-in functions: <https://docs.python.org/3/library/functions.html>
- `venv` virtual environments: <https://docs.python.org/3/library/venv.html>
- Python in VS Code: <https://code.visualstudio.com/docs/languages/python>
- Jupyter getting started: <https://docs.jupyter.org/en/stable/start/index.html>
