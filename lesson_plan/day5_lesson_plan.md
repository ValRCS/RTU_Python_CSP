# Day 5 Lesson Plan - From Summary Tables to Introductory Machine Learning

## Day Focus
Day 5 begins by finishing the Day 4 work that was not completed: summarizing cleaned data and turning those summaries into clear visual outputs. That is not a detour from machine learning; it is the necessary bridge into it. Participants first make sure they can produce analysis-ready tables, grouped summaries, and charts from the prepared dataset, and only then move into the basics of supervised learning. The emphasis is practical: understand how a cleaned dataset becomes a model input, how a target variable is chosen, how training and testing are separated, and how simple predictions are evaluated.

## Objectives
- Complete grouped summaries and visual outputs that remained unfinished on Day 4
- Connect descriptive analysis work to the first steps of predictive modeling
- Understand the basic supervised machine learning workflow
- Prepare features and a target column from an already cleaned dataset
- Build one simple regression example and one simple classification example
- Evaluate model outputs with basic metrics and discuss limitations

## Prerequisites
- Python basics from Day 1
- Cleaning and transformation ideas from Day 2
- `Pandas` filtering, grouping, joins, and reshaping from Days 3 and 4
- A cleaned Day 4 dataset that can be summarized and then reused for modeling
- Comfort with simple charts, tables, and the idea of a business or statistical question

## Topic Sequence

### 1. Finish the missing Day 4 work
- Brief recap of the Day 4 workflow: `load -> inspect -> clean -> filter -> combine -> summarize -> reshape -> visualize -> export`
- Reopen the prepared Day 4 dataset and identify what was left unfinished
- Complete one or two grouped summaries with `groupby()`, `agg()`, or `pivot_table()`
- Turn the summary into a usable chart with `Pandas` plotting or `matplotlib`
- Use this review to reinforce that modeling starts only after the data pipeline is stable

### 2. Bridge from analysis to machine learning
- Descriptive question versus predictive question
- Why summaries and charts still matter before any model is built
- Examples:
  - analysis: "Which region had the highest sales last month?"
  - prediction: "What sales value might we expect next month?"
- The role of features, target, and historical examples

### 3. Machine learning workflow overview
- Problem framing
- Selecting the target column
- Choosing input features
- Separating training data from evaluation data
- Fitting a model
- Generating predictions
- Evaluating whether the model is useful
- Warning that machine learning does not replace cleaning, validation, or domain judgment

### 4. Preparing model-ready data
- Reuse the Day 4 cleaned and enriched table instead of returning to raw files
- Select candidate columns for modeling
- Handle missing values or remove unusable rows
- Convert categorical columns into model-usable form
- Separate:
  - `X` for features
  - `y` for target
- Avoid data leakage by not using columns that already contain the answer

### 5. Simple regression
- When regression is the right choice
- Numeric target example such as sales amount, revenue, or units sold
- `train_test_split`
- Fitting a simple regression model
- Comparing predicted and actual values
- Basic metrics:
  - `MAE`
  - `RMSE`
  - `R^2`
- Interpreting model output carefully instead of treating it as certain truth

### 6. Simple classification
- When classification is the right choice
- Turning a practical question into classes, for example:
  - high vs low sales
  - target met vs target not met
- Fitting a simple classification model
- Generating class predictions
- Basic metrics:
  - accuracy
  - precision
  - recall
- Understanding that different mistakes have different costs

### 7. Evaluation, interpretation, and limits
- Why a train score alone is not enough
- Overfitting in simple terms
- The difference between a usable baseline and a production-quality model
- Reading metrics together with charts and grouped summaries
- When a simple grouped report is more useful than a model

### 8. Wrap-up and transition to final work
- Review the full flow:
  - cleaned data
  - summary table
  - chart
  - model input
  - prediction
  - evaluation
- Decide which parts are ready for reuse in a final mini-project or future lesson extension

## Practical Part

### Exercise 1 - finish the missing summary and chart
- Use the Day 4 prepared dataset
- Build at least one grouped summary table
- Create one chart that answers a clear question from that summary
- Export or save the result in the existing workflow

### Exercise 2 - prepare data for modeling
- Choose one target column
- Choose a small set of useful feature columns
- Remove or fix missing values needed for the model
- Split the data into `X` and `y`
- Create training and test sets

### Exercise 3 - build a simple regression model
- Use a numeric target
- Fit the model on the training set
- Predict on the test set
- Inspect a few predicted versus actual values
- Report one or two evaluation metrics

### Exercise 4 - build a simple classification model
- Create or choose a categorical target
- Fit the classifier
- Predict on the test set
- Check basic classification metrics
- Discuss which errors matter most

### Exercise 5 - reflect on whether ML adds value
- Compare the model output with the grouped summaries and charts
- Identify one case where descriptive analysis is enough
- Identify one case where prediction could be useful
- List one limitation in the current dataset or workflow

## Recommended Time Allocation
- 20 min - recap of Day 4 status and completion of unfinished summary work
- 25 min - visualization completion and discussion of chart choice
- 20 min - bridge from descriptive analysis to machine learning thinking
- 20 min - machine learning workflow overview and terminology
- 25 min - preparing features, target, and train/test split
- 30 min - simple regression example
- 30 min - simple classification example
- 20 min - evaluation, interpretation, and common pitfalls
- 35 min - guided practical work, review, and wrap-up

## Day Outcome
After Day 5, participants can finish a small reporting workflow from cleaned data, create a summary table and chart, and then reuse the same prepared dataset in a basic supervised learning example. They understand that machine learning sits on top of good data preparation, not instead of it, and they can distinguish between descriptive reporting tasks and simple predictive tasks.

## Connection to Final Project
The final project can remain primarily a data pipeline and reporting task, with machine learning added only where it clarifies a realistic predictive question. Participants should leave Day 5 understanding that a clean, well-documented workflow with trustworthy summaries is already a strong outcome, and that a basic model is an optional extension when the question truly requires prediction.
