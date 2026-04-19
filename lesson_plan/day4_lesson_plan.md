# Day 4 Lesson Plan — Pandas Workflow: From Data Sources to Visual Output

## Day Focus
Day 4 is built around the full `Pandas` workflow rather than a disconnected list of features. Participants work through a realistic sequence: load data, inspect it, clean it, filter it, combine tables, summarize results, reshape output, visualize findings, and export final artifacts. The goal is not to cover all of `Pandas`, but to teach a practical analysis workflow that participants can reuse in real statistical and office data tasks.

## Objectives
- Read tabular data from `CSV`, `Excel`, `JSON`, `SQLite`, and HTML table sources with `Pandas`
- Inspect loaded data and identify structure, types, and quality issues
- Clean and standardize data before analysis
- Apply flexible filtering and selection patterns, including SQL-like syntax with `query()`
- Combine tables with `merge` and `concat`
- Summarize data with `groupby()`, `agg()`, and `pivot_table()`
- Reshape data for reporting with `pivot()` and `melt()`
- Create simple visual outputs with `Pandas` plotting and `matplotlib`
- Export cleaned data, summaries, and report-ready outputs

## Prerequisites
- Python basics from Day 1
- File reading and data cleaning ideas from Day 2
- `JSON`, `Series`, `DataFrame`, filtering, grouping, and basic joins from Day 3
- Basic familiarity with Excel tables and simple SQL concepts such as `SELECT`, `WHERE`, and `GROUP BY`

## Topic Sequence

### 1. Workflow overview and mental model
- The Day 4 workflow: `load -> inspect -> clean -> filter -> combine -> summarize -> reshape -> visualize -> export`
- Why this sequence is more useful than learning individual commands in isolation
- Short reminder of `Series`, `DataFrame`, `index`, columns, and `dtypes`
- Why vectorized `Pandas` operations are preferred over manual loops in most table operations

### 2. Loading data from multiple sources
- Reading `CSV` files with `pd.read_csv()`
- Reading `Excel` files with `pd.read_excel()`
- Loading one sheet or several sheets from the same workbook with `sheet_name`
- Brief recap of `JSON` loading with `pd.read_json()` and how it connects to Day 3
- Reading from a `SQLite` database with `pd.read_sql_query()`
- Using SQL results as another `DataFrame` source inside a `Pandas` workflow
- Reading HTML tables with `pd.read_html()`
- Useful parameters:
  - `usecols`
  - `sheet_name`
  - `dtype`
  - `parse_dates`
  - `index_col`
- Brief note on loading only the required columns, sheets, rows, and tables
- Framing idea:
  - not every source needs to be used later
  - some of these loaded `DataFrame` objects will later be inspected, cleaned, filtered, and combined

### 3. Inspecting loaded data
- Quick inspection with:
  - `.head()`
  - `.tail()`
  - `.sample()`
  - `.shape`
  - `.columns`
  - `.dtypes`
  - `.info()`
  - `.describe()`
- Using `.value_counts()` for quick frequency checks
- Identifying likely join keys, date fields, categorical columns, and numeric columns
- Detecting early warning signs:
  - missing values
  - inconsistent column names
  - unexpected data types
  - duplicate rows

### 4. Cleaning and preparing data
- Standardizing column names
- Renaming columns
- Handling missing values with:
  - `.isna()`
  - `.fillna()`
  - `.dropna()`
- Converting data types with `astype()` and parsing dates
- Cleaning text columns with:
  - `.str.strip()`
  - `.str.lower()`
  - `.str.replace()`
  - `.str.contains()`
- Detecting and removing duplicates with:
  - `.duplicated()`
  - `.drop_duplicates()`
- Creating calculated columns for later analysis

### 5. Filtering and selecting data
- Selecting one or more columns
- Selecting rows with boolean masks
- Using `.loc[]` and `.iloc[]`
- Building multi-condition filters with `&`, `|`, and `~`
- Common helper methods:
  - `.isin()`
  - `.between()`
  - `.str.contains()`
- Sorting results with `sort_values()`
- SQL-like syntax with `query()`
- Mapping familiar SQL ideas into `Pandas`:
  - `SELECT`
  - `WHERE`
  - `ORDER BY`
  - `LIMIT` via `.head()`

### 6. Combining multiple tables
- Vertical stacking with `pd.concat()`
- Joining related tables with `pd.merge()`
- Join types:
  - `left`
  - `inner`
  - `right`
  - `outer`
- Choosing appropriate join keys
- Validating merge results by checking row counts and unmatched values
- Common mistakes:
  - duplicate keys
  - mismatched column names
  - unexpected row multiplication
  - missing records after the join

### 7. Summarizing and aggregating
- Grouping with `groupby()`
- Common aggregations:
  - `count`
  - `sum`
  - `mean`
  - `min`
  - `max`
  - `nunique`
- Using `.agg()` with multiple summary functions
- Sorting aggregated results
- Connecting grouped summaries to typical Excel PivotTable thinking

### 8. Reshaping data for reporting
- When a table is easier to analyze in long form versus wide form
- `pivot_table()` for summary tables
- `pivot()` for reshaping when values are already unique
- `melt()` for wide-to-long conversion
- Preparing report-ready output for Excel-style reporting and charts

### 9. Visualization with `Pandas` and `matplotlib`
- Quick plots directly from `Series` and `DataFrame`
- Common chart types:
  - bar chart
  - line chart
  - histogram
  - scatter plot
  - box plot
- Choosing a chart based on the analytical question
- Basic chart improvements:
  - titles
  - axis labels
  - figure size
  - rotated category labels
- Understanding when `Pandas` plotting is enough and when `matplotlib` offers more control

### 10. Export and reproducibility
- Exporting cleaned data with:
  - `to_csv()`
  - `to_excel()`
  - `to_json()`
- Saving summary tables for reporting
- Keeping the workflow reproducible in a notebook or script
- Structuring work so that input, transformation, summary, and output steps are clear and repeatable

## Practical Part

### Exercise 1 — loading and inspecting multiple sources
- Read one `CSV` file
- Read an `Excel` workbook and load at least two different sheets
- Revisit one `JSON` source from Day 3 and load it into a `DataFrame`
- Load one table from a `SQLite` database query
- Load one table from HTML
- Compare their structure and identify which columns could later be used for joining
- Inspect data types and missing values

### Exercise 2 — cleaning and standardizing
- Standardize column names
- Convert one or more columns into numeric or datetime format
- Handle missing values and remove duplicates
- Create one calculated column

### Exercise 3 — filtering with SQL-like thinking
- Select only the needed columns
- Filter rows using multiple conditions
- Reproduce a simple SQL-style `WHERE` condition with both boolean masks and `query()`
- Sort and preview the final subset

### Exercise 4 — combining datasets after preparation
- Choose some of the previously loaded sources after inspection, cleaning, and filtering
- Combine two related tables with `merge()`
- Stack two similar extracts with `concat()`
- Check whether the combined result has the expected number of rows

### Exercise 5 — grouped summaries and pivot-style reporting
- Build a grouped summary with `groupby()`
- Create a `pivot_table()` summary for a manager-style report
- Compare the result to what would usually be done in Excel

### Exercise 6 — visualization and export
- Create one chart from a summary table
- Export the cleaned dataset and final summary
- Save outputs in a format that could be reused by another colleague or later script

## Recommended Time Allocation
- 15 min — Day 3 recap and Day 4 workflow overview
- 40 min — reading `CSV`, multi-sheet `Excel`, `JSON`, `SQLite`, and HTML table data with `Pandas`
- 20 min — inspection of structure, data types, and quality issues
- 30 min — cleaning, type conversion, missing values, and calculated columns
- 25 min — filtering, selection, sorting, and SQL-like `query()` syntax
- 20 min — combining tables with `merge` and `concat`
- 30 min — `groupby()`, `agg()`, and `pivot_table()`
- 15 min — reshaping with `pivot()` and `melt()`
- 20 min — visualization with `Pandas` and `matplotlib`
- 10 min — export, mini end-to-end workflow, and recap

## Day Outcome
After Day 4, participants can take several raw input files, inspect their structure, clean and standardize them, filter and combine them, create summaries and pivot-style outputs, visualize the main findings, and export results in a reproducible form. At this point, `Pandas` becomes not just a table library, but a practical end-to-end analysis workflow.

## Transition to Day 5
On Day 5, these prepared and summarized datasets can be used as input for basic machine learning workflows. The discipline learned on Day 4 around cleaning, selecting columns, and producing reliable analysis-ready tables becomes essential before any modeling step.
