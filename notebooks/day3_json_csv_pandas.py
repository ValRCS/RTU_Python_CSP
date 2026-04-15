# %% [markdown]
# # Day 3 - JSON, CSV, and Pandas Basics
#
# ## Notebook goal
#
# In this notebook we will learn how to:
# - read simple JSON files with Python's standard library
# - inspect JSON structure
# - work with nested JSON data
# - load CSV files with pandas
# - inspect a DataFrame
# - select, filter, sort, and transform data
# - combine tables with `concat()` and `merge()`
# - export results to CSV and JSON
#
# ## Files used in this lesson
#
# We will use the sample files created in `data/day3/`:
# - `products_basic.json`
# - `orders_nested.json`
# - `products.csv`
# - `sales_january.csv`
# - `sales_february.csv`
#
# ## Important
#
# Run the notebook from top to bottom. Later cells depend on variables created
# earlier.

# %%
from __future__ import annotations

import json
from pathlib import Path

try:
    import pandas as pd
except ModuleNotFoundError as exc:
    raise SystemExit(
        "This notebook requires pandas. Install it first, for example with: pip install pandas"
    ) from exc


def find_repo_root() -> Path:
    """Return a sensible project root for script and Jupyter execution."""
    candidates: list[Path] = []

    try:
        candidates.append(Path(__file__).resolve().parents[1])
    except NameError:
        pass

    cwd = Path.cwd().resolve()
    candidates.extend([cwd, cwd.parent])

    for candidate in candidates:
        if (candidate / "data" / "day3").exists():
            return candidate

    return cwd


REPO_ROOT = find_repo_root()
DATA_DIR = REPO_ROOT / "data" / "day3"

# %% [markdown]
# ## 1. Check that the data files exist
#
# It is good practice to confirm file paths before reading data.

# %%
data_files = sorted(DATA_DIR.glob("*"))
print("Data directory:", DATA_DIR.resolve())
print("Files found:")
for path in data_files:
    print("-", path.name)

# %% [markdown]
# ## 2. Read a simple JSON file
#
# `products_basic.json` is a flat JSON file.
# It contains a list of product objects.
# This is the easiest JSON shape to convert into a table.

# %%
products_json_path = DATA_DIR / "products_basic.json"

with products_json_path.open("r", encoding="utf-8") as file:
    products_data = json.load(file)

print("Python type:", type(products_data))
print("Number of records:", len(products_data))

# %% [markdown]
# We can inspect one element from the list.

# %%
products_data[0]

# %% [markdown]
# Each item is a Python dictionary.

# %%
print("Type of first item:", type(products_data[0]))
print("Keys in first item:", list(products_data[0].keys()))

# %% [markdown]
# ## 3. Loop through JSON records
#
# Before using pandas, it is useful to see the raw data directly in Python.

# %%
for product in products_data[:3]:
    print(product["product_id"], "-", product["name"], "-", product["price"])

# %% [markdown]
# ## 4. Convert simple JSON into a DataFrame
#
# A list of dictionaries can usually be converted directly into a pandas
# `DataFrame`.

# %%
products_df = pd.DataFrame(products_data)
products_df

# %% [markdown]
# ## 5. Inspect the DataFrame
#
# These are the first commands students should get comfortable with.

# %%
products_df.head()

# %%
products_df.shape

# %%
products_df.columns

# %%
products_df.dtypes

# %%
products_df.info()

# %% [markdown]
# ## 6. Simple selections
#
# We can select one column or a few columns.

# %%
products_df["name"]

# %%
products_df[["product_id", "name", "category", "price"]]

# %% [markdown]
# ## 7. Filter rows
#
# Here we keep only electronics products.

# %%
products_df[products_df["category"] == "Electronics"]

# %% [markdown]
# We can also combine conditions.

# %%
products_df[(products_df["category"] == "Electronics") & (products_df["price"] > 10)]

# %% [markdown]
# ## 8. Sort values
#
# Sorting is often one of the first real data analysis tasks.

# %%
products_df.sort_values("price")

# %%
products_df.sort_values("price", ascending=False)

# %% [markdown]
# ## 9. Create new columns
#
# We can derive new values from existing columns.

# %%
products_df["price_with_vat"] = (products_df["price"] * 1.21).round(2)
products_df["name_upper"] = products_df["name"].str.upper()
products_df

# %% [markdown]
# ## 10. Group and summarize
#
# This is similar to a simple Excel PivotTable.

# %%
products_df.groupby("category")["price"].mean().sort_values(ascending=False)

# %%
products_summary = (
    products_df.groupby("category")
    .agg(
        product_count=("product_id", "count"),
        average_price=("price", "mean"),
        max_price=("price", "max"),
    )
    .round(2)
)
products_summary

# %% [markdown]
# ## 11. Read a nested JSON file
#
# `orders_nested.json` is more complex.
# The file is not just a list. It is a dictionary with metadata and an `orders`
# list inside it.

# %%
orders_json_path = DATA_DIR / "orders_nested.json"

with orders_json_path.open("r", encoding="utf-8") as file:
    orders_document = json.load(file)

print("Top-level type:", type(orders_document))
print("Top-level keys:", list(orders_document.keys()))

# %% [markdown]
# Let us inspect the report metadata.

# %%
print("Report name:", orders_document["report_name"])
print("Generated at:", orders_document["generated_at"])
print("Currency:", orders_document["currency"])

# %% [markdown]
# The actual records are inside `orders`.

# %%
orders_list = orders_document["orders"]
print("Number of orders:", len(orders_list))
orders_list[0]

# %% [markdown]
# ## 12. Access nested values manually
#
# This is useful when students are still learning JSON structure.

# %%
first_order = orders_list[0]

print("Order ID:", first_order["order_id"])
print("Customer name:", first_order["customer"]["name"])
print("Customer city:", first_order["customer"]["city"])
print("Payment status:", first_order["payment"]["status"])
print("First ordered product:", first_order["items"][0]["product_id"])

# %% [markdown]
# ## 13. Flatten nested JSON with a manual loop
#
# Here we create one row per order.
# We intentionally use `.get()` for some fields because not every order has the
# same structure.

# %%
order_rows = []

for order in orders_list:
    items = order.get("items", [])
    total_quantity = sum(item["quantity"] for item in items)
    items_total = sum(item["quantity"] * item["unit_price"] for item in items)
    delivery_cost = order.get("delivery", {}).get("cost", 0)
    total_amount = round(items_total + delivery_cost, 2)

    order_rows.append(
        {
            "order_id": order["order_id"],
            "customer_id": order["customer"]["customer_id"],
            "customer_name": order["customer"]["name"],
            "city": order["customer"]["city"],
            "loyalty_tier": order["customer"].get("loyalty_tier"),
            "item_count": len(items),
            "total_quantity": total_quantity,
            "items_total": round(items_total, 2),
            "delivery_type": order.get("delivery", {}).get("type"),
            "delivery_cost": delivery_cost,
            "payment_method": order.get("payment", {}).get("method"),
            "payment_status": order.get("payment", {}).get("status"),
            "coupon_code": order.get("coupon_code"),
            "total_amount": total_amount,
        }
    )

orders_df = pd.DataFrame(order_rows)
orders_df

# %% [markdown]
# ## 14. Inspect missing values
#
# Nested JSON often leads to missing values after flattening.

# %%
orders_df.isna().sum()

# %% [markdown]
# For example, some orders do not have `coupon_code` or `loyalty_tier`.

# %%
orders_df[["order_id", "loyalty_tier", "coupon_code", "delivery_cost"]]

# %% [markdown]
# ## 15. Filter nested JSON results
#
# Here we keep only paid orders with at least one item.

# %%
paid_orders_df = orders_df[
    (orders_df["payment_status"] == "paid") & (orders_df["item_count"] > 0)
]
paid_orders_df

# %% [markdown]
# ## 16. Read CSV files with pandas
#
# CSV is tabular data, so pandas can load it directly.

# %%
sales_january_path = DATA_DIR / "sales_january.csv"
sales_february_path = DATA_DIR / "sales_february.csv"
products_csv_path = DATA_DIR / "products.csv"

sales_january_df = pd.read_csv(sales_january_path)
sales_february_df = pd.read_csv(sales_february_path)
products_lookup_df = pd.read_csv(products_csv_path)

# %%
sales_january_df.head()

# %%
sales_january_df.shape

# %%
sales_january_df.dtypes

# %%
sales_january_df.info()

# %% [markdown]
# ## 17. Convert column types
#
# Dates usually need conversion.

# %%
sales_january_df["date"] = pd.to_datetime(sales_january_df["date"])
sales_february_df["date"] = pd.to_datetime(sales_february_df["date"])

sales_january_df.dtypes

# %% [markdown]
# ## 18. Missing values in CSV
#
# Notice that `discount_pct` has missing values.

# %%
sales_january_df.isna().sum()

# %%
sales_january_df[sales_january_df["discount_pct"].isna()]

# %% [markdown]
# We can fill missing discount values with `0`.

# %%
sales_january_df["discount_pct"] = sales_january_df["discount_pct"].fillna(0)
sales_february_df["discount_pct"] = sales_february_df["discount_pct"].fillna(0)

sales_january_df.isna().sum()

# %% [markdown]
# ## 19. Select and filter CSV data

# %%
sales_january_df[["sale_id", "date", "product_id", "store", "units_sold"]]

# %%
sales_january_df[sales_january_df["units_sold"] >= 10]

# %%
sales_january_df[sales_january_df["store"] == "Riga-Center"]

# %% [markdown]
# ## 20. Create calculated columns
#
# First we merge product prices into the sales table.

# %%
sales_january_enriched_df = sales_january_df.merge(
    products_lookup_df[["product_id", "name", "category", "price"]],
    on="product_id",
    how="left",
)

sales_january_enriched_df.head()

# %% [markdown]
# Now we can calculate gross revenue and discounted revenue.

# %%
sales_january_enriched_df["gross_revenue"] = (
    sales_january_enriched_df["units_sold"] * sales_january_enriched_df["price"]
).round(2)

sales_january_enriched_df["net_revenue"] = (
    sales_january_enriched_df["gross_revenue"]
    * (1 - sales_january_enriched_df["discount_pct"] / 100)
).round(2)

sales_january_enriched_df.head()

# %% [markdown]
# ## 21. Sort and summarize sales

# %%
sales_january_enriched_df.sort_values("net_revenue", ascending=False)

# %%
sales_by_store_df = (
    sales_january_enriched_df.groupby("store")
    .agg(
        total_units=("units_sold", "sum"),
        total_revenue=("net_revenue", "sum"),
        average_discount=("discount_pct", "mean"),
    )
    .round(2)
    .sort_values("total_revenue", ascending=False)
)
sales_by_store_df

# %%
sales_by_category_df = (
    sales_january_enriched_df.groupby("category")
    .agg(
        total_units=("units_sold", "sum"),
        total_revenue=("net_revenue", "sum"),
    )
    .round(2)
    .sort_values("total_revenue", ascending=False)
)
sales_by_category_df

# %% [markdown]
# ## 22. Combine monthly tables with `concat()`
#
# The January and February files have the same columns, so vertical combination
# is straightforward.

# %%
all_sales_df = pd.concat([sales_january_df, sales_february_df], ignore_index=True)
all_sales_df

# %%
all_sales_df.shape

# %% [markdown]
# ## 23. Merge combined sales with product data
#
# `merge()` combines two tables by a shared key.

# %%
all_sales_enriched_df = all_sales_df.merge(products_lookup_df, on="product_id", how="left")
all_sales_enriched_df.head()

# %% [markdown]
# Let us add calculated revenue columns to the combined data too.

# %%
all_sales_enriched_df["gross_revenue"] = (
    all_sales_enriched_df["units_sold"] * all_sales_enriched_df["price"]
).round(2)

all_sales_enriched_df["net_revenue"] = (
    all_sales_enriched_df["gross_revenue"]
    * (1 - all_sales_enriched_df["discount_pct"] / 100)
).round(2)

all_sales_enriched_df.head()

# %% [markdown]
# ## 24. Combined analysis
#
# Now we can summarize across both months.

# %%
monthly_store_summary_df = (
    all_sales_enriched_df.groupby("store")
    .agg(
        total_units=("units_sold", "sum"),
        total_revenue=("net_revenue", "sum"),
        row_count=("sale_id", "count"),
    )
    .round(2)
    .sort_values("total_revenue", ascending=False)
)
monthly_store_summary_df

# %%
product_summary_df = (
    all_sales_enriched_df.groupby(["category", "name"])
    .agg(
        total_units=("units_sold", "sum"),
        total_revenue=("net_revenue", "sum"),
    )
    .round(2)
    .sort_values(["category", "total_revenue"], ascending=[True, False])
)
product_summary_df

# %% [markdown]
# ## 25. A simple pivot table
#
# This is one of the most common patterns for Excel users moving into pandas.

# %%
pivot_table_df = pd.pivot_table(
    all_sales_enriched_df,
    index="store",
    columns="category",
    values="net_revenue",
    aggfunc="sum",
    fill_value=0,
).round(2)

pivot_table_df

# %% [markdown]
# ## 26. Compare JSON and CSV
#
# A quick comparison:
# - CSV is easier for already tabular data
# - simple JSON can often be converted directly into a table
# - nested JSON needs inspection and flattening first
#
# Below we compare the structure of the three main tables we created.

# %%
print("products_df shape:", products_df.shape)
print("orders_df shape:", orders_df.shape)
print("all_sales_enriched_df shape:", all_sales_enriched_df.shape)

# %% [markdown]
# ## 27. Export results
#
# In real workflows we often save cleaned or summarized data.

# %%
output_dir = DATA_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

sales_by_store_df.to_csv(output_dir / "sales_by_store_january.csv")
monthly_store_summary_df.to_csv(output_dir / "sales_by_store_all_months.csv")
orders_df.to_json(output_dir / "orders_flattened.json", orient="records", indent=2)

print("Saved files to:", output_dir.resolve())

# %% [markdown]
# ## 28. Practice ideas
#
# Try these tasks on your own:
# - filter only `Office` products
# - find the most expensive product
# - calculate total January revenue by product
# - find orders with missing `loyalty_tier`
# - sort all sales by `units_sold`
# - export only Electronics sales into a separate CSV file
#
# You can add your own cells below this point.

# %%
# Write your own practice code here.
