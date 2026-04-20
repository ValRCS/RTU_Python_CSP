from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "day4_pandas_full_workflow_working_examples.ipynb"
OUTPUT_NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "day4_pandas_full_worfklow_colab.ipynb"


def lines(text: str) -> list[str]:
    return [line + "\n" for line in dedent(text).strip("\n").split("\n")]


def main() -> None:
    notebook = json.loads(SOURCE_NOTEBOOK_PATH.read_text(encoding="utf-8"))

    markdown_by_id = {
        "intro": lines(
            """
            # Day 4 - Pandas Full Workflow Colab Examples

            This notebook is a Google Colab friendly worked example of a complete pandas workflow:
            `load -> inspect -> clean -> filter -> combine -> summarize -> reshape -> visualize -> export`.

            It keeps the same Day 4 theory and the same demo datasets as the local working notebook, but it loads the source files from this GitHub repository where appropriate:
            `https://github.com/ValRCS/RTU_Python_CSP`.

            Notebook behavior:
            - The setup cell prepares a Colab runtime folder for cached downloads and outputs.
            - CSV, JSON, and HTML inputs are loaded from GitHub raw URLs.
            - Binary files such as `SQLite` and `Excel` are first downloaded from GitHub raw URLs into the Colab runtime, then read locally.
            - The final cells generate exports inside the Colab runtime output folder.

            Important note:
            - The raw URLs target the `main` branch of this repository.
            - If you update the local `data/day4/raw/` files, push them to GitHub before relying on this Colab notebook.

            Recommended usage:
            1. Open the notebook in Google Colab.
            2. Run the notebook from top to bottom.
            3. Compare the code to the theory notes and adjust parameters interactively if needed.
            4. Inspect the generated files in the Colab runtime output folder.
            """
        )
    }

    code_by_id = {
        "setup": lines(
            """
            from __future__ import annotations

            import importlib.util
            import sqlite3
            import subprocess
            import sys
            from pathlib import Path
            from urllib.request import urlretrieve

            REQUIRED_PACKAGES = {
                "pandas": "pandas",
                "matplotlib": "matplotlib",
                "openpyxl": "openpyxl",
                "lxml": "lxml",
                "bs4": "beautifulsoup4",
                "html5lib": "html5lib",
            }
            missing_packages = sorted(
                {package for module_name, package in REQUIRED_PACKAGES.items() if importlib.util.find_spec(module_name) is None}
            )
            if missing_packages:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *missing_packages])

            from IPython.display import display
            import matplotlib.pyplot as plt
            import pandas as pd

            REPO_WEB_URL = "https://github.com/ValRCS/RTU_Python_CSP"
            RAW_BASE_URL = "https://raw.githubusercontent.com/ValRCS/RTU_Python_CSP/main/data/day4/raw"

            RUNTIME_ROOT = Path.cwd() / "day4_colab_runtime"
            RAW_CACHE_DIR = RUNTIME_ROOT / "raw_cache"
            INTERIM_DIR = RUNTIME_ROOT / "interim"
            OUTPUT_DIR = RUNTIME_ROOT / "outputs"

            for path in (RAW_CACHE_DIR, INTERIM_DIR, OUTPUT_DIR):
                path.mkdir(parents=True, exist_ok=True)

            pd.set_option("display.max_columns", 50)
            pd.set_option("display.width", 140)
            pd.set_option("display.precision", 2)

            EXCEL_ENGINE = "openpyxl"

            demo_files = {
                "sales_january_csv": f"{RAW_BASE_URL}/sales_january_raw.csv",
                "sales_february_csv": f"{RAW_BASE_URL}/sales_february_raw.csv",
                "products_json": f"{RAW_BASE_URL}/products_catalog.json",
                "stores_html": f"{RAW_BASE_URL}/stores.html",
                "stores_csv": f"{RAW_BASE_URL}/stores.csv",
                "targets_sqlite": f"{RAW_BASE_URL}/regional_targets.sqlite",
                "reference_excel": f"{RAW_BASE_URL}/reference_tables.xlsx",
            }
            demo_files
            """
        ),
        "load-code": lines(
            """
            january_csv_url = demo_files["sales_january_csv"]
            february_csv_url = demo_files["sales_february_csv"]
            products_json_url = demo_files["products_json"]
            stores_html_url = demo_files["stores_html"]
            stores_csv_url = demo_files["stores_csv"]
            sqlite_url = demo_files["targets_sqlite"]
            excel_url = demo_files["reference_excel"]

            sales_january_raw = pd.read_csv(january_csv_url)
            sales_february_raw = pd.read_csv(february_csv_url)
            products_df = pd.read_json(products_json_url)

            try:
                stores_df = pd.read_html(stores_html_url)[0]
                stores_source = "GitHub HTML table"
            except (ImportError, ValueError):
                stores_df = pd.read_csv(stores_csv_url)
                stores_source = "GitHub CSV fallback"

            sqlite_cache_path = RAW_CACHE_DIR / "regional_targets.sqlite"
            urlretrieve(sqlite_url, sqlite_cache_path)
            with sqlite3.connect(sqlite_cache_path) as connection:
                targets_df = pd.read_sql_query(
                    "SELECT month, region, target_revenue FROM regional_monthly_targets ORDER BY month, region",
                    connection,
                )

            excel_cache_path = RAW_CACHE_DIR / "reference_tables.xlsx"
            urlretrieve(excel_url, excel_cache_path)
            excel_tables = pd.read_excel(excel_cache_path, sheet_name=None)

            loaded_objects = pd.DataFrame(
                [
                    {"dataset": "sales_january_raw", "rows": len(sales_january_raw), "columns": sales_january_raw.shape[1]},
                    {"dataset": "sales_february_raw", "rows": len(sales_february_raw), "columns": sales_february_raw.shape[1]},
                    {"dataset": "products_df", "rows": len(products_df), "columns": products_df.shape[1]},
                    {"dataset": f"stores_df ({stores_source})", "rows": len(stores_df), "columns": stores_df.shape[1]},
                    {"dataset": "targets_df", "rows": len(targets_df), "columns": targets_df.shape[1]},
                    {"dataset": "excel_tables", "rows": len(excel_tables), "columns": len(excel_tables)},
                ]
            )
            loaded_objects
            """
        ),
    }

    for cell in notebook["cells"]:
        if cell.get("cell_type") == "markdown" and cell.get("id") in markdown_by_id:
            cell["source"] = markdown_by_id[cell["id"]]
        if cell.get("cell_type") == "code" and cell.get("id") in code_by_id:
            cell["source"] = code_by_id[cell["id"]]

    metadata = notebook.setdefault("metadata", {})
    metadata["colab"] = {
        "name": OUTPUT_NOTEBOOK_PATH.name,
        "provenance": [],
    }

    OUTPUT_NOTEBOOK_PATH.write_text(json.dumps(notebook, indent=2), encoding="utf-8")
    print(f"Created notebook: {OUTPUT_NOTEBOOK_PATH}")


if __name__ == "__main__":
    main()
