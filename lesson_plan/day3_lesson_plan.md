# Day 3 Lesson Plan — JSON Basics and Introduction to Pandas

## Day Focus
On Day 3, participants begin with basic work with `JSON` using Python's standard library and then move on to structured data processing with `Pandas`. This sequence helps them first understand semi-structured data and only then see how to convert it into `DataFrame` form for further analysis and Excel-style workflows.

## Objectives
- Understand how to read and interpret simple `JSON` without external libraries
- Understand what external libraries are and why `Pandas` is used in data work
- Get familiar with the basic structures of `Series` and `DataFrame`
- Read data from `CSV` and simple `JSON`
- Perform `filtering`, `selection`, `sorting`, `grouping`, and `aggregation`
- Combine multiple datasets with `merge` and `concat`
- Show how typical Excel operations can be replaced with a `Pandas` approach

## Prerequisites
- Python basics from Day 1
- File reading, string processing, and data cleaning from Day 2
- Basic understanding of table structure: rows, columns, headers

## Topic Sequence

### 1. Introduction to `JSON`
- What `JSON` is and where it appears in real workflows
- `JSON` as a nested data structure
- Working with Python's `json` module
- Simple `JSON` reading in Python
- The difference between `JSON`, `CSV`, and Python dictionaries/lists

### 2. Moving from `JSON` to tabular data
- When `JSON` can be analyzed directly in Python structures
- When it is more convenient to convert it into a `DataFrame`
- Converting `list of dicts` into tabular data
- Limitations: nested structures, uneven fields, missing keys

### 3. Introduction to external libraries
- What an external library is and how it differs from the standard library
- `import pandas as pd`
- Brief reminder about `pip install`
- Why `Pandas` is useful in statistical and office data workflows

### 4. First look at `DataFrame`
- What `Series` is
- What `DataFrame` is
- Rows, columns, and `index`
- Inspecting data with:
  - `.head()`
  - `.shape`
  - `.columns`
  - `.dtypes`
  - `.info()`

### 5. Loading data into `Pandas`
- Reading a `CSV` file with `pd.read_csv()`
- Creating a `DataFrame` from Python lists and dictionaries
- The difference between structured and semi-structured data

### 6. Selecting columns and rows
- Selecting a single column
- Selecting multiple columns
- Selecting rows by condition
- Common comparisons and logical operators
- Basic work with missing values

### 7. Transforming data
- Renaming columns
- Creating a new column
- Changing data types
- Simple text operations on columns
- Preparing data for further analysis

### 8. Sorting, grouping, and summarizing
- `sort_values()`
- `groupby()`
- Most common `aggregation` operations:
  - `count`
  - `sum`
  - `mean`
  - `min`
  - `max`
- Interpreting results and linking them to typical Excel PivotTable operations

### 9. Combining datasets
- Vertical combination with `concat`
- Joining by key with `merge`
- Simple examples with two tables
- Common mistakes: mismatched column names, missing keys, duplicates

### 10. Exporting
- Saving results to `CSV`
- Basic export to `JSON`
- Brief emphasis on reproducibility: from input file to finished result with a script or notebook

## Practical Part

### Exercise 1 — basic work with `JSON`
- Read a simple `JSON` file
- Inspect its structure in Python
- Understand which parts are ready to be converted into a table

### Exercise 2 — first analysis with `Pandas`
- Convert simple `JSON` or read a `CSV` file as a `DataFrame`
- Inspect the data structure
- Identify the most important columns

### Exercise 3 — recreating Excel operations
- Select only the needed rows and columns
- Sort data by a chosen field
- Create a new calculated column

### Exercise 4 — grouping and summary
- Group data by category
- Calculate frequency or average value
- Interpret the resulting summary

### Exercise 5 — combining datasets
- Combine two tables using a shared key
- Check whether all rows were joined correctly

### Exercise 6 — comparing `JSON` and `CSV`
- Compare how `CSV` and `JSON` input differ
- Evaluate which format is more convenient for a specific task
- Convert `JSON` data into a `DataFrame` for further analysis

## Recommended Time Allocation
- 20 min — review from Day 2 and introduction to `JSON`
- 25 min — Python `json` module and inspecting `JSON` structures
- 25 min — moving from `JSON` to `DataFrame` and introduction to `Pandas`
- 35 min — `DataFrame` basics and data loading
- 35 min — `filtering`, `selection`, and data transformation
- 30 min — `sorting`, `grouping`, and `aggregation`
- 20 min — `merge`, `concat`, and working with multiple tables
- 30 min — practical exercises and discussion

## Day Outcome
After Day 3, participants can read basic `JSON` data with Python's standard library, understand when it makes sense to convert it into a tabular structure, and then use `Pandas` to select and transform columns and rows, build summaries, and combine datasets.

## Transition to Day 4
On Day 4, this foundation can be extended with multiple data sources, `Excel` files, more complex `JSON`, basic `SQL` integration, and visualization with `matplotlib`.
