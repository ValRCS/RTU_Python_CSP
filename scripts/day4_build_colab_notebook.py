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

            It keeps the same Day 4 theory and the same demo datasets as the local working notebook, but it is now hybrid:
            - if local `data/day4/raw/` files exist, it uses them directly;
            - otherwise it loads the source files from this GitHub repository where appropriate:
            `https://github.com/ValRCS/RTU_Python_CSP`.

            Notebook behavior:
            - The setup cell detects whether local Day 4 data is available.
            - In local mode, inputs are read from the repository and outputs are written into `data/day4/outputs/`.
            - In remote mode, CSV, JSON, and HTML inputs are loaded from GitHub raw URLs.
            - In remote mode, binary files such as `SQLite` and `Excel` are first downloaded into a runtime cache, then read locally.
            - The final cells generate exports in the active output folder.

            Important note:
            - The raw URLs target the `main` branch of this repository.
            - If you update the local `data/day4/raw/` files, push them to GitHub before relying on this Colab notebook.

            Recommended usage:
            1. Open the notebook in Google Colab.
            2. Or run it locally in Jupyter from the repository.
            3. Run the notebook from top to bottom.
            4. Compare the code to the theory notes and adjust parameters interactively if needed.
            5. Inspect the generated files in the active output folder.
            """
        )
    }

    markdown_by_id["visualize-guide"] = lines(
        """
        ## 8. Visualize

        Goal: communicate an answer, not just produce a chart.

        Visualization should come after the table is trustworthy enough to support a claim. In a pandas workflow, charts are usually based on cleaned and summarized data rather than directly on the raw source. This makes the visual easier to explain and much easier to validate.

        Useful chart families to discuss:
        - Line charts for trends over time.
        - Bar charts for category comparison.
        - Stacked or grouped bars for composition comparisons.
        - Histograms for distribution shape.
        - Box plots for spread and outliers.
        - Scatter plots for relationships between two numeric fields.
        - Heatmaps built from pivoted summaries.
        - Small multiples or faceted views when one chart becomes too crowded.

        Visualization tool choices:
        - `DataFrame.plot()` and `Series.plot()` for quick pandas-native plots.
        - `matplotlib` when you need fine control over axes, annotations, layouts, and styling.
        - `seaborn` when a tidy long-format table is available and statistical defaults are helpful.

        Chart selection cheat sheet:
        - Use a bar chart when the question is "which category is larger?"
        - Use a line chart when the question is "how did this change over time?"
        - Use a histogram when the question is "how are values distributed?"
        - Use a box plot when the question is "how do spread and outliers compare across groups?"
        - Use a scatter plot when the question is "do two numeric variables move together?"
        - Use a heatmap when the question is "where are the high and low pockets in a matrix?"

        Preparation tips before plotting:
        - Decide whether the chart should use raw rows, grouped summaries, or reshaped data.
        - Sort the categories before plotting if order helps the message.
        - Keep only the columns needed for the chart to reduce accidental confusion.
        - Round or format values for labels after the calculation stage, not before it.
        - Check whether missing values or filtered-out rows change the story.

        Readability and design tips:
        - Write titles that answer a business question rather than repeating the axis names.
        - Use axis labels and units consistently.
        - Keep legends short and place them where they do not block the data.
        - Rotate labels only when necessary; if too many labels need rotation, reconsider the chart design.
        - Use one highlight color intentionally and keep supporting colors quieter.
        - Prefer direct value labels for short bar charts when exact numbers matter.
        - Start bar charts from zero unless you have a very specific analytical reason not to.
        - Use grids lightly; they should support reading, not dominate the figure.

        Notebook workflow tips:
        - Save important figures to files so the notebook produces reusable artifacts.
        - Keep chart code close to the summary table it visualizes.
        - In Colab, use explicit output paths because the runtime is temporary.
        - In local mode, use repository output folders so exports stay versionable and easy to inspect.

        Common pitfalls:
        - Plotting too many categories in one chart.
        - Using pie charts when bars or lines explain the comparison more clearly.
        - Mixing incompatible scales without explanation.
        - Spending too much time styling before the underlying summary is correct.
        - Showing a chart without also checking the table behind it.
        - Forgetting that the plotting stage can reveal mistakes in earlier cleaning or grouping logic.

        Documentation references:
        - [pandas chart visualization guide](https://pandas.pydata.org/docs/user_guide/visualization.html)
        - [pandas.DataFrame.plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)
        - [Matplotlib plot types](https://matplotlib.org/stable/plot_types/index.html)
        - [Matplotlib annotated heatmap example](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)
        - [Matplotlib subplots guide](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)
        - [Seaborn plotting function overview](https://seaborn.pydata.org/tutorial/function_overview.html)
        """
    )

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

            def find_repo_root() -> Path | None:
                candidates: list[Path] = []

                try:
                    candidates.append(Path(__file__).resolve().parents[1])
                except NameError:
                    pass

                cwd = Path.cwd().resolve()
                candidates.extend([cwd, cwd.parent, cwd.parent.parent if len(cwd.parents) >= 2 else cwd])

                for candidate in candidates:
                    if (candidate / "data" / "day4" / "raw").exists() and (candidate / "notebooks").exists():
                        return candidate

                return None


            LOCAL_REPO_ROOT = find_repo_root()
            USE_LOCAL_DATA = LOCAL_REPO_ROOT is not None
            IN_COLAB = "google.colab" in sys.modules

            if USE_LOCAL_DATA:
                DATA_DIR = LOCAL_REPO_ROOT / "data" / "day4"
                RAW_DIR = DATA_DIR / "raw"
                INTERIM_DIR = DATA_DIR / "interim"
                OUTPUT_DIR = DATA_DIR / "outputs"
                RAW_CACHE_DIR = RAW_DIR
                DATA_SOURCE_MODE = "local"
            else:
                RUNTIME_ROOT = Path.cwd() / "day4_colab_runtime"
                RAW_CACHE_DIR = RUNTIME_ROOT / "raw_cache"
                INTERIM_DIR = RUNTIME_ROOT / "interim"
                OUTPUT_DIR = RUNTIME_ROOT / "outputs"
                DATA_SOURCE_MODE = "remote"

            for path in (RAW_CACHE_DIR, INTERIM_DIR, OUTPUT_DIR):
                path.mkdir(parents=True, exist_ok=True)

            pd.set_option("display.max_columns", 50)
            pd.set_option("display.width", 140)
            pd.set_option("display.precision", 2)

            EXCEL_ENGINE = "openpyxl"

            if USE_LOCAL_DATA:
                demo_files = {
                    "sales_january_csv": RAW_DIR / "sales_january_raw.csv",
                    "sales_february_csv": RAW_DIR / "sales_february_raw.csv",
                    "products_json": RAW_DIR / "products_catalog.json",
                    "stores_html": RAW_DIR / "stores.html",
                    "stores_csv": RAW_DIR / "stores.csv",
                    "targets_sqlite": RAW_DIR / "regional_targets.sqlite",
                    "reference_excel": RAW_DIR / "reference_tables.xlsx",
                }
            else:
                demo_files = {
                    "sales_january_csv": f"{RAW_BASE_URL}/sales_january_raw.csv",
                    "sales_february_csv": f"{RAW_BASE_URL}/sales_february_raw.csv",
                    "products_json": f"{RAW_BASE_URL}/products_catalog.json",
                    "stores_html": f"{RAW_BASE_URL}/stores.html",
                    "stores_csv": f"{RAW_BASE_URL}/stores.csv",
                    "targets_sqlite": f"{RAW_BASE_URL}/regional_targets.sqlite",
                    "reference_excel": f"{RAW_BASE_URL}/reference_tables.xlsx",
                }

            {
                "data_source_mode": DATA_SOURCE_MODE,
                "in_colab": IN_COLAB,
                "output_dir": OUTPUT_DIR,
                "demo_files": demo_files,
            }
            """
        ),
        "load-code": lines(
            """
            def ensure_local_binary(source: str | Path, filename: str) -> Path:
                if isinstance(source, Path):
                    return source
                destination = RAW_CACHE_DIR / filename
                urlretrieve(source, destination)
                return destination


            january_csv_source = demo_files["sales_january_csv"]
            february_csv_source = demo_files["sales_february_csv"]
            products_json_source = demo_files["products_json"]
            stores_html_source = demo_files["stores_html"]
            stores_csv_source = demo_files["stores_csv"]
            sqlite_source = demo_files["targets_sqlite"]
            excel_source = demo_files["reference_excel"]

            sales_january_raw = pd.read_csv(january_csv_source)
            sales_february_raw = pd.read_csv(february_csv_source)
            products_df = pd.read_json(products_json_source)

            try:
                stores_df = pd.read_html(stores_html_source)[0]
                stores_source = "HTML table"
            except (ImportError, ValueError):
                stores_df = pd.read_csv(stores_csv_source)
                stores_source = "CSV fallback"

            sqlite_cache_path = ensure_local_binary(sqlite_source, "regional_targets.sqlite")
            with sqlite3.connect(sqlite_cache_path) as connection:
                targets_df = pd.read_sql_query(
                    "SELECT month, region, target_revenue FROM regional_monthly_targets ORDER BY month, region",
                    connection,
                )

            excel_cache_path = ensure_local_binary(excel_source, "reference_tables.xlsx")
            excel_tables = pd.read_excel(excel_cache_path, sheet_name=None)

            loaded_objects = pd.DataFrame(
                [
                    {"dataset": "sales_january_raw", "rows": len(sales_january_raw), "columns": sales_january_raw.shape[1], "source_mode": DATA_SOURCE_MODE},
                    {"dataset": "sales_february_raw", "rows": len(sales_february_raw), "columns": sales_february_raw.shape[1], "source_mode": DATA_SOURCE_MODE},
                    {"dataset": "products_df", "rows": len(products_df), "columns": products_df.shape[1], "source_mode": DATA_SOURCE_MODE},
                    {"dataset": f"stores_df ({stores_source})", "rows": len(stores_df), "columns": stores_df.shape[1], "source_mode": DATA_SOURCE_MODE},
                    {"dataset": "targets_df", "rows": len(targets_df), "columns": targets_df.shape[1], "source_mode": DATA_SOURCE_MODE},
                    {"dataset": "excel_tables", "rows": len(excel_tables), "columns": len(excel_tables), "source_mode": DATA_SOURCE_MODE},
                ]
            )
            loaded_objects
            """
        ),
        "visualize-code": lines(
            """
            monthly_totals = region_target_summary.groupby("month")[["revenue", "target_revenue"]].sum().round(2)
            category_totals = (
                sales_analysis.groupby("category")["net_revenue"].sum().sort_values(ascending=False).round(2)
            )
            channel_month = (
                sales_analysis.groupby(["month", "sales_channel"])["net_revenue"]
                .sum()
                .unstack(fill_value=0)
                .round(2)
            )
            achievement_heatmap = (
                region_target_summary.pivot(index="region", columns="month", values="achievement_pct")
                .fillna(0)
                .round(1)
            )

            category_colors = {
                "Electronics": "#4C78A8",
                "Office": "#F58518",
                "Breakroom": "#54A24B",
            }

            fig1, axes1 = plt.subplots(2, 2, figsize=(15, 10))

            monthly_totals.plot(kind="bar", ax=axes1[0, 0], title="Actual Revenue vs Target by Month")
            axes1[0, 0].set_xlabel("Month")
            axes1[0, 0].set_ylabel("Revenue")
            axes1[0, 0].tick_params(axis="x", rotation=0)
            axes1[0, 0].grid(axis="y", alpha=0.25)

            category_totals.plot(
                kind="bar",
                ax=axes1[0, 1],
                color=[category_colors.get(category, "#999999") for category in category_totals.index],
                title="Revenue by Product Category",
            )
            axes1[0, 1].set_xlabel("Category")
            axes1[0, 1].set_ylabel("Revenue")
            axes1[0, 1].tick_params(axis="x", rotation=20)
            axes1[0, 1].grid(axis="y", alpha=0.25)
            for patch in axes1[0, 1].patches:
                height = patch.get_height()
                axes1[0, 1].annotate(
                    f"{height:.0f}",
                    (patch.get_x() + patch.get_width() / 2, height),
                    ha="center",
                    va="bottom",
                    xytext=(0, 4),
                    textcoords="offset points",
                    fontsize=9,
                )

            channel_month.plot(
                kind="line",
                marker="o",
                linewidth=2,
                ax=axes1[1, 0],
                title="Monthly Revenue by Sales Channel",
            )
            axes1[1, 0].set_xlabel("Month")
            axes1[1, 0].set_ylabel("Revenue")
            axes1[1, 0].tick_params(axis="x", rotation=0)
            axes1[1, 0].grid(axis="y", alpha=0.25)

            sales_analysis.boxplot(column="net_revenue", by="sales_channel", ax=axes1[1, 1])
            axes1[1, 1].set_title("Order Revenue Distribution by Channel")
            axes1[1, 1].set_xlabel("Sales Channel")
            axes1[1, 1].set_ylabel("Net Revenue")
            axes1[1, 1].grid(axis="y", alpha=0.25)
            fig1.suptitle("")

            plt.tight_layout()
            dashboard_path = OUTPUT_DIR / "day4_visualization_dashboard.png"
            fig1.savefig(dashboard_path, dpi=150, bbox_inches="tight")
            plt.show()

            fig2, axes2 = plt.subplots(1, 2, figsize=(15, 5.5))

            for category, subset in sales_analysis.groupby("category"):
                axes2[0].scatter(
                    subset["units"],
                    subset["net_revenue"],
                    s=90,
                    alpha=0.8,
                    label=category,
                    color=category_colors.get(category, "#999999"),
                )
            axes2[0].set_title("Units vs Net Revenue")
            axes2[0].set_xlabel("Units")
            axes2[0].set_ylabel("Net Revenue")
            axes2[0].grid(alpha=0.25)
            axes2[0].legend(title="Category")

            heatmap = axes2[1].imshow(achievement_heatmap.values, aspect="auto", cmap="YlGnBu")
            axes2[1].set_title("Target Achievement Heatmap (%)")
            axes2[1].set_xticks(range(len(achievement_heatmap.columns)))
            axes2[1].set_xticklabels(achievement_heatmap.columns)
            axes2[1].set_yticks(range(len(achievement_heatmap.index)))
            axes2[1].set_yticklabels(achievement_heatmap.index)
            for row_index in range(len(achievement_heatmap.index)):
                for col_index in range(len(achievement_heatmap.columns)):
                    value = achievement_heatmap.iloc[row_index, col_index]
                    axes2[1].text(
                        col_index,
                        row_index,
                        f"{value:.0f}",
                        ha="center",
                        va="center",
                        color="black",
                        fontsize=9,
                    )
            fig2.colorbar(heatmap, ax=axes2[1], label="Achievement %")

            plt.tight_layout()
            examples_path = OUTPUT_DIR / "day4_visualization_examples.png"
            fig2.savefig(examples_path, dpi=150, bbox_inches="tight")
            plt.show()

            visualization_outputs = pd.DataFrame(
                [
                    {"artifact": "visual dashboard", "path": str(dashboard_path)},
                    {"artifact": "extra examples", "path": str(examples_path)},
                ]
            )
            visualization_outputs
            """
        ),
        "export-code": lines(
            """
            clean_output_path = OUTPUT_DIR / "sales_analysis_clean.csv"
            summary_output_path = OUTPUT_DIR / "regional_target_summary.csv"
            metrics_output_path = OUTPUT_DIR / "regional_metrics_long.json"
            html_output_path = OUTPUT_DIR / "regional_revenue_report.html"

            sales_analysis.to_csv(clean_output_path, index=False)
            region_target_summary.to_csv(summary_output_path, index=False)
            metrics_long.to_json(metrics_output_path, orient="records", indent=2)
            report_wide.to_html(html_output_path)

            if EXCEL_ENGINE:
                excel_output_path = OUTPUT_DIR / "day4_reporting_pack.xlsx"
                with pd.ExcelWriter(excel_output_path, engine=EXCEL_ENGINE) as writer:
                    sales_analysis.to_excel(writer, index=False, sheet_name="sales_analysis")
                    region_target_summary.to_excel(writer, index=False, sheet_name="region_targets")
                    report_wide.reset_index().to_excel(writer, index=False, sheet_name="revenue_wide")
            else:
                excel_output_path = None

            artifact_rows = [
                {"artifact": "clean sales data", "path": str(clean_output_path)},
                {"artifact": "regional target summary", "path": str(summary_output_path)},
                {"artifact": "long metrics json", "path": str(metrics_output_path)},
                {"artifact": "html report", "path": str(html_output_path)},
                {"artifact": "excel pack", "path": str(excel_output_path) if excel_output_path else "skipped: no Excel engine installed"},
            ]

            if "visualization_outputs" in globals():
                artifact_rows.extend(visualization_outputs.to_dict(orient="records"))

            pd.DataFrame(artifact_rows)
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
