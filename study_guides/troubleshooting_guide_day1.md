# Troubleshooting Guide: Day 1 Foundations and Setup

This guide is for the Day 1 material in:

- `lesson_plan/README.md`
- `study_guides/study_guide_day1.md`
- `notebooks/python_basics.ipynb`
- `python_vscode_setup/README.md`

Reference links in this guide were verified on April 14, 2026.

## What This Guide Covers

Day 1 problems usually fall into one of four groups:

1. The code is invalid Python.
2. The code is valid, but it fails at runtime.
3. VS Code or Jupyter is using the wrong environment.
4. The notebook is in an unexpected state because of earlier cells, `input()`, or an interrupted run.

The fastest way to recover is to identify which group you are in before changing random things.

## Fast Triage Checklist

When something fails, check these in order:

1. Read the last line of the error message. It usually names the actual problem, such as `SyntaxError`, `NameError`, or `TypeError`.
2. Check the file or cell number and line number.
3. If you are in a notebook, ask whether the needed earlier cells were run.
4. If imports or packages fail, confirm the correct VS Code `interpreter` or notebook `kernel`.
5. If a cell looks stuck, check whether it is waiting for `input()` or whether the kernel is busy.
6. Change one thing at a time and run again.

## How To Read a Python Error

A Python error usually has three useful parts:

- the location
- the traceback or context
- the exception type and message

Example:

```python
age = int("abc")
```

Typical result:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

How to interpret it:

- `ValueError` means Python received the right kind of operation, but the value itself was not acceptable.
- `int("abc")` failed because `"abc"` is not a valid integer.

For syntax errors, Python often points to where it detected the problem, not always where the real mistake began. For example, a missing colon may be detected at the next token.

## The Most Common Day 1 Errors

### `SyntaxError`

What it means:

- Python could not parse the code at all.

Common causes:

- missing colon after `if`, `for`, `while`, or `def`
- missing or mismatched quotes
- missing closing parenthesis
- using `=` where `==` was intended
- trying to write plain English inside a code cell

Example:

```python
if age > 18
    print("Adult")
```

How to fix it:

- inspect the line shown by Python
- inspect the line just above it
- check colons, parentheses, commas, and quotes

Useful habit:

- when you get `SyntaxError`, stop and fix structure first before thinking about logic

### `IndentationError`

What it means:

- Python expected a correctly indented block and did not get one.

Common causes:

- forgetting to indent the code inside `if`, `for`, `while`, or `def`
- indenting one line too little or too much

Example:

```python
if age > 18:
print("Adult")
```

Fix:

- indent the body consistently, usually by 4 spaces

Correct version:

```python
if age > 18:
    print("Adult")
```

### `TabError`

What it means:

- the code mixes tabs and spaces in indentation.

Fix:

- convert indentation to spaces only
- in VS Code, select the indentation style from the lower status bar if needed

Even experienced users hit this when pasting code from different sources.

### `NameError`

What it means:

- you used a variable or function name that does not exist in the current state.

Common causes:

- typo in a variable name
- trying to use a variable before defining it
- notebook cell with the definition was never run
- kernel was restarted and variables were cleared

Example:

```python
print(total_amount)
```

Fix:

- check spelling exactly
- define the variable before using it
- in notebooks, rerun earlier setup cells

### `TypeError`

What it means:

- the operation is not valid for the given types.

Common causes:

- adding text and a number directly
- calling something that is not a function
- trying to index a value that is not a sequence

Example:

```python
"Age: " + 25
```

Fix:

- convert types intentionally

Correct version:

```python
"Age: " + str(25)
```

### `ValueError`

What it means:

- the type is acceptable, but the specific value is not.

Common causes:

- `int()` or `float()` on invalid text
- unpacking the wrong number of values

Example:

```python
age = int("twenty")
```

Fix:

- print the value before converting it
- strip extra spaces if needed
- validate user input before conversion

Safer pattern:

```python
raw = input("Enter age: ").strip()
age = int(raw)
```

### `ZeroDivisionError`

What it means:

- code attempted division by zero.

Example:

```python
10 / 0
```

Fix:

- inspect the denominator before dividing

Example:

```python
if count != 0:
    average = total / count
```

### `ModuleNotFoundError`

What it means:

- Python cannot find the package you are trying to import.

Common causes on Day 1:

- the package was not installed
- it was installed into a different Python environment
- VS Code is using the wrong `interpreter`
- the notebook is using the wrong `kernel`

Example:

```python
import pandas
```

Fix:

1. Confirm the selected `interpreter` in VS Code for `.py` files.
2. Confirm the selected `kernel` in notebooks.
3. Install packages into that exact environment:

```powershell
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

### `AttributeError`

What it means:

- you asked an object to do something that type does not support.

Common causes:

- calling string methods on numbers
- calling list methods on strings
- mistyping a method name

Example:

```python
age = 25
age.strip()
```

Fix:

- check the actual type with `type(age)`
- verify that the method belongs to that type

### `EOFError`

What it means:

- `input()` expected data but none was provided.

Where it appears:

- sometimes in notebooks or interactive environments when input is interrupted or unavailable

Fix:

- rerun the cell
- provide the requested value
- if the environment is not suitable for input, replace `input()` temporarily with a fixed test value

Example:

```python
name = "Test User"
```

### `KeyboardInterrupt`

What it means:

- execution was manually interrupted.

Common causes:

- you clicked interrupt
- the kernel was stopped because a cell was hanging
- code was waiting on `input()` and you canceled it

Fix:

- this is not always a bug
- identify whether the code was slow, stuck in a loop, or waiting for input

## Notebook-Specific Problems

### Problem: `input()` blocks the notebook

Symptoms:

- the cell shows it is still running
- later cells cannot run
- the notebook appears frozen
- a prompt is waiting for typed input

What is happening:

- `input()` pauses execution until something is entered

How to recover:

1. Look for the active input box or prompt and enter a value.
2. Press Enter to continue execution.
3. If you do not want to continue, interrupt the kernel.
4. Rerun the cell after deciding what test value to use.

Good debugging strategy:

- when teaching or testing notebook logic, replace `input()` temporarily with a fixed value

Example:

```python
name = "Anna"
```

Instead of:

```python
name = input("Enter your name: ")
```

This removes interaction and makes debugging easier.

### Problem: The notebook remembers old values

Symptoms:

- you changed code, but output seems inconsistent
- a variable exists even though the defining cell is no longer visible
- one student gets a different result from another

What is happening:

- notebook kernels keep variables in memory until restarted

Fix:

1. Restart the kernel.
2. Run cells from top to bottom.
3. Avoid jumping randomly through the notebook during early exercises.

### Problem: The notebook does not know a variable that definitely exists

Symptoms:

- `NameError` in a later cell

What is happening:

- the earlier cell that defines the variable was not run in the current kernel session

Fix:

- rerun the notebook in order from the beginning

### Problem: The cell never finishes

Possible causes:

- waiting for `input()`
- infinite or very long `while` loop
- kernel got stuck

How to debug:

1. Check whether the code contains `input()`.
2. Check whether loop variables actually change.
3. Interrupt the kernel.
4. Simplify the cell and rerun smaller pieces.

Example of a bad loop:

```python
count = 1
while count <= 3:
    print(count)
```

Why it hangs:

- `count` never changes

Fix:

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

### Problem: A Markdown explanation was run as Python code

Symptoms:

- `SyntaxError` on text that looks like a sentence

Fix:

- make sure the cell type is `Markdown`, not `Code`

This is common in notebooks and wastes time because the error message looks unrelated at first.

## VS Code and Environment Problems

### Problem: `python` or `py` is not found

Check:

```powershell
python --version
py --version
```

If these fail:

- reopen the terminal
- verify Python is installed
- on Windows, verify the Python launcher is available

### Problem: PowerShell will not activate `.venv`

Typical fix:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Problem: `pip` behaves inconsistently

Fix:

- prefer `python -m pip` instead of plain `pip`

Example:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

This reduces the chance of installing into the wrong Python.

### Problem: VS Code is using the wrong Python

Symptoms:

- code runs in terminal but not in VS Code
- imports work in one file but fail in another
- packages seem installed but still cannot be imported

Fix:

1. Open the Command Palette.
2. Run `Python: Select Interpreter`.
3. Select the project `.venv`.
4. Open a new terminal after switching.

### Problem: Notebook kernel is wrong

Symptoms:

- notebook imports fail
- notebook behavior differs from `.py` files

Fix:

1. Open the notebook.
2. Click the kernel picker in the top right.
3. Select the environment matching `.venv`.
4. If needed, install `ipykernel` into that environment.

### Problem: Notebook execution is disabled

Possible cause:

- the workspace is in Restricted Mode or not trusted

Fix:

- trust the workspace if it is your own course folder

## Logic Bugs That Do Not Always Raise Errors

Some mistakes produce wrong results without throwing exceptions.

### Reusing an old variable by accident

Example:

```python
count = 5
count = 2
```

This is valid Python. It may still be a logic mistake if the second assignment was accidental.

Debug it by:

- printing values after important steps
- using descriptive variable names

### Comparing when you meant to assign, or assigning when you meant to compare

Examples:

```python
x = 5
```

versus:

```python
x == 5
```

The first assigns. The second compares.

If code "does nothing useful", check whether the right operator was used.

### Running cells out of order

This is one of the biggest notebook-specific logic problems.

Fix:

- restart the kernel
- run all cells from the top

### Shadowing built-in names

Example:

```python
list = [1, 2, 3]
```

This works, but later it can break code like:

```python
list("abc")
```

because `list` now refers to your variable, not the built-in function.

Avoid using names like:

- `list`
- `str`
- `int`
- `input`
- `type`

## A Practical Debugging Workflow

Use this process instead of guessing:

1. Reproduce the problem with the smallest possible code example.
2. Read the exact error type and message.
3. Check variable values with `print(...)`.
4. Check types with `type(...)`.
5. In notebooks, rerun earlier cells or restart the kernel.
6. If imports fail, verify `interpreter` or `kernel`.
7. After each fix, rerun and confirm the exact symptom changed.

## Useful Debug Prints for Day 1

When the problem is unclear, print intermediate values.

```python
raw_age = input("Enter age: ")
print("raw_age =", raw_age)
print("type(raw_age) =", type(raw_age))
age = int(raw_age)
print("age =", age)
```

For loops:

```python
for value in [1, 2, 3]:
    print("value =", value)
```

For conditions:

```python
score = 78
print("score >= 60:", score >= 60)
```

These are simple, but they remove guesswork.

## When To Restart, Rerun, or Rebuild

Restart the notebook kernel when:

- variables seem inconsistent
- cells were run out of order
- the notebook is stuck

Rerun the current cell when:

- you fixed a local syntax or logic issue
- you changed only one line in that cell

Rerun the whole notebook from the top when:

- one cell depends on earlier state
- you changed variable definitions used later
- you are not sure the current kernel state is clean

Rebuild the environment only when:

- imports fail because packages truly are missing
- the wrong interpreter or kernel keeps being selected

## Minimal Recovery Commands

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

Basic checks:

```powershell
python --version
python -m pip --version
```

## Authoritative References

- Python tutorial on errors and exceptions: <https://docs.python.org/3/tutorial/errors.html>
- Built-in exceptions: <https://docs.python.org/3/library/exceptions.html>
- Built-in `input()` documentation: <https://docs.python.org/3/library/functions.html#input>
- Built-in `int()` documentation: <https://docs.python.org/3/library/functions.html#int>
- Python in VS Code: <https://code.visualstudio.com/docs/languages/python>
- Jupyter notebooks in VS Code: <https://code.visualstudio.com/docs/datascience/jupyter-notebooks>
- Jupyter kernel management in VS Code: <https://code.visualstudio.com/docs/datascience/jupyter-kernel-management>
- VS Code Workspace Trust: <https://code.visualstudio.com/docs/editing/workspaces/workspace-trust>
