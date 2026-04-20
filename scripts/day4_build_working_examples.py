from __future__ import annotations

import csv
import html
import json
import sqlite3
import zipfile
from pathlib import Path
from textwrap import dedent


REPO_ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD_PATH = REPO_ROOT / "notebooks" / "day4_pandas_full_workflow_workbook.ipynb"
OUTPUT_NOTEBOOK_PATH = REPO_ROOT / "notebooks" / "day4_pandas_full_workflow_working_examples.ipynb"

DATA_DIR = REPO_ROOT / "data" / "day4"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
OUTPUT_DIR = DATA_DIR / "outputs"


SALES_JANUARY_RECORDS = [
    {
        "Order ID": 1001,
        "Order Date": "2026-01-03",
        "Store Code": "S001",
        "Product Code": "P100",
        "Customer Segment ": "Consumer",
        "Units": 4,
        "Unit Price": 12.50,
        "Discount %": 0.00,
        "Sales Channel": "Online",
        "Promo Flag": "yes",
    },
    {
        "Order ID": 1002,
        "Order Date": "2026-01-05",
        "Store Code": "S002",
        "Product Code": "P200",
        "Customer Segment ": "Corporate",
        "Units": 2,
        "Unit Price": 85.00,
        "Discount %": 0.10,
        "Sales Channel": "Retail ",
        "Promo Flag": "no",
    },
    {
        "Order ID": 1003,
        "Order Date": "2026-01-07",
        "Store Code": "S003",
        "Product Code": "P400",
        "Customer Segment ": "Consumer",
        "Units": 1,
        "Unit Price": 210.00,
        "Discount %": "",
        "Sales Channel": "Online",
        "Promo Flag": "yes",
    },
    {
        "Order ID": 1004,
        "Order Date": "2026/01/10",
        "Store Code": "S004",
        "Product Code": "P300",
        "Customer Segment ": "Home Office",
        "Units": 3,
        "Unit Price": 42.00,
        "Discount %": 0.05,
        "Sales Channel": "Retail",
        "Promo Flag": "No",
    },
    {
        "Order ID": 1005,
        "Order Date": "15-01-2026",
        "Store Code": "S001",
        "Product Code": "P100",
        "Customer Segment ": "consumer",
        "Units": 5,
        "Unit Price": 12.50,
        "Discount %": 0.15,
        "Sales Channel": "Online",
        "Promo Flag": "YES",
    },
    {
        "Order ID": 1006,
        "Order Date": "2026-01-18",
        "Store Code": "S005",
        "Product Code": "P500",
        "Customer Segment ": "Corporate",
        "Units": 2,
        "Unit Price": 15.00,
        "Discount %": 0.00,
        "Sales Channel": "Wholesale",
        "Promo Flag": "no",
    },
    {
        "Order ID": 1006,
        "Order Date": "2026-01-18",
        "Store Code": "S005",
        "Product Code": "P500",
        "Customer Segment ": "Corporate",
        "Units": 2,
        "Unit Price": 15.00,
        "Discount %": 0.00,
        "Sales Channel": "Wholesale",
        "Promo Flag": "no",
    },
    {
        "Order ID": 1007,
        "Order Date": "2026-01-22",
        "Store Code": "S002",
        "Product Code": "P999",
        "Customer Segment ": "Consumer",
        "Units": 1,
        "Unit Price": 30.00,
        "Discount %": 0.00,
        "Sales Channel": "Online",
        "Promo Flag": "yes",
    },
    {
        "Order ID": 1008,
        "Order Date": "2026-01-28",
        "Store Code": "S006",
        "Product Code": "P200",
        "Customer Segment ": "",
        "Units": 2,
        "Unit Price": 85.00,
        "Discount %": 0.20,
        "Sales Channel": "Retail",
        "Promo Flag": "yes",
    },
]


SALES_FEBRUARY_RECORDS = [
    {
        "Order ID": 2001,
        "Order Date": "2026-02-02",
        "Store Code": "S001",
        "Product Code": "P200",
        "Customer Segment ": "Corporate",
        "Units": 1,
        "Unit Price": 85.00,
        "Discount %": 0.00,
        "Sales Channel": "Online",
        "Promo Flag": "no",
    },
    {
        "Order ID": 2002,
        "Order Date": "2026-02-05",
        "Store Code": "S003",
        "Product Code": "p300",
        "Customer Segment ": "Consumer",
        "Units": 4,
        "Unit Price": 42.00,
        "Discount %": 0.10,
        "Sales Channel": "Retail",
        "Promo Flag": "yes",
    },
    {
        "Order ID": 2003,
        "Order Date": "2026-02-09",
        "Store Code": "S004",
        "Product Code": "P400",
        "Customer Segment ": "Home Office",
        "Units": 1,
        "Unit Price": 210.00,
        "Discount %": 0.15,
        "Sales Channel": "Retail",
        "Promo Flag": "no",
    },
    {
        "Order ID": 2004,
        "Order Date": "2026/02/11",
        "Store Code": "S002",
        "Product Code": "P100",
        "Customer Segment ": "Consumer",
        "Units": 6,
        "Unit Price": 12.50,
        "Discount %": 0.05,
        "Sales Channel": "Online",
        "Promo Flag": "yes",
    },
    {
        "Order ID": 2005,
        "Order Date": "18-02-2026",
        "Store Code": "S005",
        "Product Code": "P500",
        "Customer Segment ": "Corporate",
        "Units": "",
        "Unit Price": 15.00,
        "Discount %": 0.00,
        "Sales Channel": "Wholesale",
        "Promo Flag": "no",
    },
    {
        "Order ID": 2006,
        "Order Date": "2026-02-20",
        "Store Code": "S001",
        "Product Code": "P300",
        "Customer Segment ": "Consumer",
        "Units": 2,
        "Unit Price": 42.00,
        "Discount %": "invalid",
        "Sales Channel": "Online",
        "Promo Flag": "no",
    },
    {
        "Order ID": 2007,
        "Order Date": "2026-02-23",
        "Store Code": "S003",
        "Product Code": "P400",
        "Customer Segment ": "Consumer",
        "Units": 1,
        "Unit Price": 210.00,
        "Discount %": 0.20,
        "Sales Channel": "Online",
        "Promo Flag": "yes",
    },
    {
        "Order ID": 2008,
        "Order Date": "2026-02-27",
        "Store Code": "S002",
        "Product Code": "P200",
        "Customer Segment ": " Corporate ",
        "Units": 3,
        "Unit Price": 85.00,
        "Discount %": 0.05,
        "Sales Channel": "Retail",
        "Promo Flag": " yes ",
    },
    {
        "Order ID": 2009,
        "Order Date": "2026-02-28",
        "Store Code": "S001",
        "Product Code": "P100",
        "Customer Segment ": "Consumer",
        "Units": 2,
        "Unit Price": 12.50,
        "Discount %": 0.00,
        "Sales Channel": "Online",
        "Promo Flag": "no",
    },
]


PRODUCT_RECORDS = [
    {
        "product_code": "P100",
        "product_name": "Notebook Set",
        "category": "Office",
        "subcategory": "Paper",
        "base_price": 12.50,
    },
    {
        "product_code": "P200",
        "product_name": "Wireless Keyboard",
        "category": "Electronics",
        "subcategory": "Accessories",
        "base_price": 85.00,
    },
    {
        "product_code": "P300",
        "product_name": "Desk Lamp",
        "category": "Office",
        "subcategory": "Lighting",
        "base_price": 42.00,
    },
    {
        "product_code": "P400",
        "product_name": "Monitor 24",
        "category": "Electronics",
        "subcategory": "Display",
        "base_price": 210.00,
    },
    {
        "product_code": "P500",
        "product_name": "Coffee Beans Pack",
        "category": "Breakroom",
        "subcategory": "Supplies",
        "base_price": 15.00,
    },
]


STORE_RECORDS = [
    {
        "store_code": "S001",
        "store_name": "Riga Central",
        "region": "Riga",
        "city": "Riga",
        "opened_year": 2018,
        "store_type": "Flagship",
    },
    {
        "store_code": "S002",
        "store_name": "Liepaja Coast",
        "region": "Kurzeme",
        "city": "Liepaja",
        "opened_year": 2020,
        "store_type": "Retail",
    },
    {
        "store_code": "S003",
        "store_name": "Daugavpils East",
        "region": "Latgale",
        "city": "Daugavpils",
        "opened_year": 2019,
        "store_type": "Retail",
    },
    {
        "store_code": "S004",
        "store_name": "Cesis North",
        "region": "Vidzeme",
        "city": "Cesis",
        "opened_year": 2021,
        "store_type": "Outlet",
    },
    {
        "store_code": "S005",
        "store_name": "Jelgava South",
        "region": "Zemgale",
        "city": "Jelgava",
        "opened_year": 2017,
        "store_type": "Warehouse",
    },
]


TARGET_RECORDS = [
    ("2026-01", "Riga", 110.0),
    ("2026-01", "Kurzeme", 160.0),
    ("2026-01", "Latgale", 200.0),
    ("2026-01", "Vidzeme", 130.0),
    ("2026-01", "Zemgale", 40.0),
    ("2026-02", "Riga", 190.0),
    ("2026-02", "Kurzeme", 300.0),
    ("2026-02", "Latgale", 310.0),
    ("2026-02", "Vidzeme", 190.0),
    ("2026-02", "Zemgale", 35.0),
]


def lines(text: str) -> list[str]:
    return [line + "\n" for line in dedent(text).strip("\n").split("\n")]


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def column_letter(index: int) -> str:
    letters: list[str] = []
    while index > 0:
        index, remainder = divmod(index - 1, 26)
        letters.append(chr(65 + remainder))
    return "".join(reversed(letters))


def excel_cell_reference(row_number: int, column_number: int) -> str:
    return f"{column_letter(column_number)}{row_number}"


def xml_cell(value: object, row_number: int, column_number: int) -> str:
    cell_ref = excel_cell_reference(row_number, column_number)
    if isinstance(value, bool):
        numeric = "1" if value else "0"
        return f'<c r="{cell_ref}" t="b"><v>{numeric}</v></c>'
    if isinstance(value, (int, float)):
        return f'<c r="{cell_ref}"><v>{value}</v></c>'

    escaped = html.escape("" if value is None else str(value))
    return f'<c r="{cell_ref}" t="inlineStr"><is><t>{escaped}</t></is></c>'


def worksheet_xml(rows: list[dict]) -> str:
    headers = list(rows[0].keys())
    xml_rows: list[str] = []

    header_cells = [
        xml_cell(header, row_number=1, column_number=index + 1)
        for index, header in enumerate(headers)
    ]
    xml_rows.append(f'<row r="1">{"".join(header_cells)}</row>')

    for row_number, row in enumerate(rows, start=2):
        row_cells = [
            xml_cell(row.get(header), row_number=row_number, column_number=index + 1)
            for index, header in enumerate(headers)
        ]
        xml_rows.append(f'<row r="{row_number}">{"".join(row_cells)}</row>')

    last_cell = excel_cell_reference(len(rows) + 1, len(headers))
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f"<dimension ref=\"A1:{last_cell}\"/>"
        "<sheetViews><sheetView workbookViewId=\"0\"/></sheetViews>"
        "<sheetFormatPr defaultRowHeight=\"15\"/>"
        f"<sheetData>{''.join(xml_rows)}</sheetData>"
        "</worksheet>"
    )


def write_simple_xlsx(path: Path, sheets: dict[str, list[dict]]) -> None:
    content_types = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>',
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
    ]
    for index in range(1, len(sheets) + 1):
        content_types.append(
            f'<Override PartName="/xl/worksheets/sheet{index}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        )
    content_types.append("</Types>")

    workbook_sheets = []
    workbook_relationships = []
    app_titles = []
    for index, sheet_name in enumerate(sheets.keys(), start=1):
        escaped_name = html.escape(sheet_name)
        workbook_sheets.append(
            f'<sheet name="{escaped_name}" sheetId="{index}" r:id="rId{index}"/>'
        )
        workbook_relationships.append(
            f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{index}.xml"/>'
        )
        app_titles.append(f"<vt:lpstr>{escaped_name}</vt:lpstr>")

    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f"<sheets>{''.join(workbook_sheets)}</sheets>"
        "</workbook>"
    )

    workbook_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        f"{''.join(workbook_relationships)}"
        '<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        "</Relationships>"
    )

    package_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
        '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
        "</Relationships>"
    )

    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
        '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
        '<borders count="1"><border/></borders>'
        '<cellStyleXfs count="1"><xf/></cellStyleXfs>'
        '<cellXfs count="1"><xf xfId="0"/></cellXfs>'
        '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
        "</styleSheet>"
    )

    core_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:dcmitype="http://purl.org/dc/dcmitype/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<dc:creator>Codex</dc:creator>"
        "<cp:lastModifiedBy>Codex</cp:lastModifiedBy>"
        "</cp:coreProperties>"
    )

    app_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        "<Application>Codex</Application>"
        f"<TitlesOfParts><vt:vector size=\"{len(sheets)}\" baseType=\"lpstr\">{''.join(app_titles)}</vt:vector></TitlesOfParts>"
        f"<HeadingPairs><vt:vector size=\"2\" baseType=\"variant\"><vt:variant><vt:lpstr>Worksheets</vt:lpstr></vt:variant><vt:variant><vt:i4>{len(sheets)}</vt:i4></vt:variant></vt:vector></HeadingPairs>"
        "</Properties>"
    )

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", "".join(content_types))
        archive.writestr("_rels/.rels", package_rels_xml)
        archive.writestr("docProps/core.xml", core_xml)
        archive.writestr("docProps/app.xml", app_xml)
        archive.writestr("xl/workbook.xml", workbook_xml)
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml)
        archive.writestr("xl/styles.xml", styles_xml)
        for index, rows in enumerate(sheets.values(), start=1):
            archive.writestr(f"xl/worksheets/sheet{index}.xml", worksheet_xml(rows))


def build_data_files() -> None:
    for path in (RAW_DIR, INTERIM_DIR, OUTPUT_DIR):
        path.mkdir(parents=True, exist_ok=True)

    write_csv(RAW_DIR / "sales_january_raw.csv", SALES_JANUARY_RECORDS)
    write_csv(RAW_DIR / "sales_february_raw.csv", SALES_FEBRUARY_RECORDS)
    write_csv(RAW_DIR / "stores.csv", STORE_RECORDS)

    with (RAW_DIR / "products_catalog.json").open("w", encoding="utf-8") as handle:
        json.dump(PRODUCT_RECORDS, handle, indent=2)

    html_lines = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        '<head><meta charset="utf-8"><title>Stores Lookup</title></head>',
        "<body>",
        "<h1>Stores Lookup</h1>",
        '<table border="1">',
        "  <thead>",
        "    <tr><th>store_code</th><th>store_name</th><th>region</th><th>city</th><th>opened_year</th><th>store_type</th></tr>",
        "  </thead>",
        "  <tbody>",
    ]
    for row in STORE_RECORDS:
        html_lines.append(
            "    <tr>"
            f"<td>{row['store_code']}</td>"
            f"<td>{row['store_name']}</td>"
            f"<td>{row['region']}</td>"
            f"<td>{row['city']}</td>"
            f"<td>{row['opened_year']}</td>"
            f"<td>{row['store_type']}</td>"
            "</tr>"
        )
    html_lines.extend(["  </tbody>", "</table>", "</body>", "</html>"])
    (RAW_DIR / "stores.html").write_text("\n".join(html_lines), encoding="utf-8")

    sqlite_path = RAW_DIR / "regional_targets.sqlite"
    if sqlite_path.exists():
        sqlite_path.unlink()
    with sqlite3.connect(sqlite_path) as connection:
        connection.execute(
            "CREATE TABLE regional_monthly_targets (month TEXT NOT NULL, region TEXT NOT NULL, target_revenue REAL NOT NULL)"
        )
        connection.executemany(
            "INSERT INTO regional_monthly_targets (month, region, target_revenue) VALUES (?, ?, ?)",
            TARGET_RECORDS,
        )
        connection.commit()

    write_simple_xlsx(
        RAW_DIR / "reference_tables.xlsx",
        {"products": PRODUCT_RECORDS, "stores": STORE_RECORDS},
    )


def build_notebook() -> None:
    scaffold = json.loads(SCAFFOLD_PATH.read_text(encoding="utf-8"))

    markdown_by_id = {
        "intro": lines(
            """
            # Day 4 - Pandas Full Workflow Working Examples

            This notebook is a runnable worked example of a complete pandas workflow:
            `load -> inspect -> clean -> filter -> combine -> summarize -> reshape -> visualize -> export`.

            It keeps the detailed theory markdown from the scaffold workbook, but the code cells now use real local demo data stored in `data/day4/`.

            Notebook behavior:
            - The setup cell creates or refreshes the local demo files in `data/day4/raw/`.
            - The workflow then loads those files from multiple local sources and processes them end to end.
            - The final cells generate exports in `data/day4/outputs/`.

            Recommended usage:
            1. Run the notebook from top to bottom.
            2. Read the markdown for the current workflow stage.
            3. Compare the code to the theory notes and adjust parameters interactively if needed.
            4. Inspect the generated files in `data/day4/raw/` and `data/day4/outputs/`.
            """
        )
    }

    code_by_id = {
        "setup": lines(
            """
            from __future__ import annotations

            import csv
            import importlib.util
            import json
            import sqlite3
            from pathlib import Path

            try:
                from IPython.display import display
                import matplotlib.pyplot as plt
                import pandas as pd
            except ModuleNotFoundError as exc:
                raise SystemExit(
                    "This notebook requires pandas and matplotlib. Install them first, for example: pip install pandas matplotlib openpyxl"
                ) from exc


            def find_repo_root() -> Path:
                \"\"\"Return a sensible project root for notebook execution.\"\"\"
                candidates: list[Path] = []

                try:
                    candidates.append(Path(__file__).resolve().parents[1])
                except NameError:
                    pass

                cwd = Path.cwd().resolve()
                candidates.extend([cwd, cwd.parent])

                for candidate in candidates:
                    if (candidate / "data").exists() and (candidate / "notebooks").exists():
                        return candidate

                return cwd


            REPO_ROOT = find_repo_root()
            DATA_DIR = REPO_ROOT / "data" / "day4"
            RAW_DIR = DATA_DIR / "raw"
            INTERIM_DIR = DATA_DIR / "interim"
            OUTPUT_DIR = DATA_DIR / "outputs"

            for path in (RAW_DIR, INTERIM_DIR, OUTPUT_DIR):
                path.mkdir(parents=True, exist_ok=True)

            pd.set_option("display.max_columns", 50)
            pd.set_option("display.width", 140)
            pd.set_option("display.precision", 2)

            EXCEL_ENGINE = next(
                (engine for engine in ("openpyxl", "xlsxwriter") if importlib.util.find_spec(engine)),
                None,
            )

            sales_january_records = [
                {"Order ID": 1001, "Order Date": "2026-01-03", "Store Code": "S001", "Product Code": "P100", "Customer Segment ": "Consumer", "Units": 4, "Unit Price": 12.50, "Discount %": 0.00, "Sales Channel": "Online", "Promo Flag": "yes"},
                {"Order ID": 1002, "Order Date": "2026-01-05", "Store Code": "S002", "Product Code": "P200", "Customer Segment ": "Corporate", "Units": 2, "Unit Price": 85.00, "Discount %": 0.10, "Sales Channel": "Retail ", "Promo Flag": "no"},
                {"Order ID": 1003, "Order Date": "2026-01-07", "Store Code": "S003", "Product Code": "P400", "Customer Segment ": "Consumer", "Units": 1, "Unit Price": 210.00, "Discount %": "", "Sales Channel": "Online", "Promo Flag": "yes"},
                {"Order ID": 1004, "Order Date": "2026/01/10", "Store Code": "S004", "Product Code": "P300", "Customer Segment ": "Home Office", "Units": 3, "Unit Price": 42.00, "Discount %": 0.05, "Sales Channel": "Retail", "Promo Flag": "No"},
                {"Order ID": 1005, "Order Date": "15-01-2026", "Store Code": "S001", "Product Code": "P100", "Customer Segment ": "consumer", "Units": 5, "Unit Price": 12.50, "Discount %": 0.15, "Sales Channel": "Online", "Promo Flag": "YES"},
                {"Order ID": 1006, "Order Date": "2026-01-18", "Store Code": "S005", "Product Code": "P500", "Customer Segment ": "Corporate", "Units": 2, "Unit Price": 15.00, "Discount %": 0.00, "Sales Channel": "Wholesale", "Promo Flag": "no"},
                {"Order ID": 1006, "Order Date": "2026-01-18", "Store Code": "S005", "Product Code": "P500", "Customer Segment ": "Corporate", "Units": 2, "Unit Price": 15.00, "Discount %": 0.00, "Sales Channel": "Wholesale", "Promo Flag": "no"},
                {"Order ID": 1007, "Order Date": "2026-01-22", "Store Code": "S002", "Product Code": "P999", "Customer Segment ": "Consumer", "Units": 1, "Unit Price": 30.00, "Discount %": 0.00, "Sales Channel": "Online", "Promo Flag": "yes"},
                {"Order ID": 1008, "Order Date": "2026-01-28", "Store Code": "S006", "Product Code": "P200", "Customer Segment ": "", "Units": 2, "Unit Price": 85.00, "Discount %": 0.20, "Sales Channel": "Retail", "Promo Flag": "yes"},
            ]

            sales_february_records = [
                {"Order ID": 2001, "Order Date": "2026-02-02", "Store Code": "S001", "Product Code": "P200", "Customer Segment ": "Corporate", "Units": 1, "Unit Price": 85.00, "Discount %": 0.00, "Sales Channel": "Online", "Promo Flag": "no"},
                {"Order ID": 2002, "Order Date": "2026-02-05", "Store Code": "S003", "Product Code": "p300", "Customer Segment ": "Consumer", "Units": 4, "Unit Price": 42.00, "Discount %": 0.10, "Sales Channel": "Retail", "Promo Flag": "yes"},
                {"Order ID": 2003, "Order Date": "2026-02-09", "Store Code": "S004", "Product Code": "P400", "Customer Segment ": "Home Office", "Units": 1, "Unit Price": 210.00, "Discount %": 0.15, "Sales Channel": "Retail", "Promo Flag": "no"},
                {"Order ID": 2004, "Order Date": "2026/02/11", "Store Code": "S002", "Product Code": "P100", "Customer Segment ": "Consumer", "Units": 6, "Unit Price": 12.50, "Discount %": 0.05, "Sales Channel": "Online", "Promo Flag": "yes"},
                {"Order ID": 2005, "Order Date": "18-02-2026", "Store Code": "S005", "Product Code": "P500", "Customer Segment ": "Corporate", "Units": "", "Unit Price": 15.00, "Discount %": 0.00, "Sales Channel": "Wholesale", "Promo Flag": "no"},
                {"Order ID": 2006, "Order Date": "2026-02-20", "Store Code": "S001", "Product Code": "P300", "Customer Segment ": "Consumer", "Units": 2, "Unit Price": 42.00, "Discount %": "invalid", "Sales Channel": "Online", "Promo Flag": "no"},
                {"Order ID": 2007, "Order Date": "2026-02-23", "Store Code": "S003", "Product Code": "P400", "Customer Segment ": "Consumer", "Units": 1, "Unit Price": 210.00, "Discount %": 0.20, "Sales Channel": "Online", "Promo Flag": "yes"},
                {"Order ID": 2008, "Order Date": "2026-02-27", "Store Code": "S002", "Product Code": "P200", "Customer Segment ": " Corporate ", "Units": 3, "Unit Price": 85.00, "Discount %": 0.05, "Sales Channel": "Retail", "Promo Flag": " yes "},
                {"Order ID": 2009, "Order Date": "2026-02-28", "Store Code": "S001", "Product Code": "P100", "Customer Segment ": "Consumer", "Units": 2, "Unit Price": 12.50, "Discount %": 0.00, "Sales Channel": "Online", "Promo Flag": "no"},
            ]

            product_records = [
                {"product_code": "P100", "product_name": "Notebook Set", "category": "Office", "subcategory": "Paper", "base_price": 12.50},
                {"product_code": "P200", "product_name": "Wireless Keyboard", "category": "Electronics", "subcategory": "Accessories", "base_price": 85.00},
                {"product_code": "P300", "product_name": "Desk Lamp", "category": "Office", "subcategory": "Lighting", "base_price": 42.00},
                {"product_code": "P400", "product_name": "Monitor 24", "category": "Electronics", "subcategory": "Display", "base_price": 210.00},
                {"product_code": "P500", "product_name": "Coffee Beans Pack", "category": "Breakroom", "subcategory": "Supplies", "base_price": 15.00},
            ]

            store_records = [
                {"store_code": "S001", "store_name": "Riga Central", "region": "Riga", "city": "Riga", "opened_year": 2018, "store_type": "Flagship"},
                {"store_code": "S002", "store_name": "Liepaja Coast", "region": "Kurzeme", "city": "Liepaja", "opened_year": 2020, "store_type": "Retail"},
                {"store_code": "S003", "store_name": "Daugavpils East", "region": "Latgale", "city": "Daugavpils", "opened_year": 2019, "store_type": "Retail"},
                {"store_code": "S004", "store_name": "Cesis North", "region": "Vidzeme", "city": "Cesis", "opened_year": 2021, "store_type": "Outlet"},
                {"store_code": "S005", "store_name": "Jelgava South", "region": "Zemgale", "city": "Jelgava", "opened_year": 2017, "store_type": "Warehouse"},
            ]

            target_records = [
                ("2026-01", "Riga", 110.0),
                ("2026-01", "Kurzeme", 160.0),
                ("2026-01", "Latgale", 200.0),
                ("2026-01", "Vidzeme", 130.0),
                ("2026-01", "Zemgale", 40.0),
                ("2026-02", "Riga", 190.0),
                ("2026-02", "Kurzeme", 300.0),
                ("2026-02", "Latgale", 310.0),
                ("2026-02", "Vidzeme", 190.0),
                ("2026-02", "Zemgale", 35.0),
            ]


            def write_csv(path: Path, rows: list[dict]) -> None:
                with path.open("w", newline="", encoding="utf-8") as handle:
                    writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
                    writer.writeheader()
                    writer.writerows(rows)


            def create_demo_day4_data() -> dict[str, Path]:
                january_csv_path = RAW_DIR / "sales_january_raw.csv"
                february_csv_path = RAW_DIR / "sales_february_raw.csv"
                products_json_path = RAW_DIR / "products_catalog.json"
                stores_html_path = RAW_DIR / "stores.html"
                stores_csv_path = RAW_DIR / "stores.csv"
                sqlite_path = RAW_DIR / "regional_targets.sqlite"
                excel_path = RAW_DIR / "reference_tables.xlsx"

                write_csv(january_csv_path, sales_january_records)
                write_csv(february_csv_path, sales_february_records)
                write_csv(stores_csv_path, store_records)

                with products_json_path.open("w", encoding="utf-8") as handle:
                    json.dump(product_records, handle, indent=2)

                html_lines = [
                    "<!DOCTYPE html>",
                    '<html lang="en">',
                    '<head><meta charset="utf-8"><title>Stores Lookup</title></head>',
                    "<body>",
                    "<h1>Stores Lookup</h1>",
                    '<table border="1">',
                    "  <thead>",
                    "    <tr><th>store_code</th><th>store_name</th><th>region</th><th>city</th><th>opened_year</th><th>store_type</th></tr>",
                    "  </thead>",
                    "  <tbody>",
                ]
                for row in store_records:
                    html_lines.append(
                        "    <tr>"
                        f"<td>{row['store_code']}</td>"
                        f"<td>{row['store_name']}</td>"
                        f"<td>{row['region']}</td>"
                        f"<td>{row['city']}</td>"
                        f"<td>{row['opened_year']}</td>"
                        f"<td>{row['store_type']}</td>"
                        "</tr>"
                    )
                html_lines.extend(["  </tbody>", "</table>", "</body>", "</html>"])
                stores_html_path.write_text("\\n".join(html_lines), encoding="utf-8")

                if sqlite_path.exists():
                    sqlite_path.unlink()
                with sqlite3.connect(sqlite_path) as connection:
                    connection.execute(
                        "CREATE TABLE regional_monthly_targets (month TEXT NOT NULL, region TEXT NOT NULL, target_revenue REAL NOT NULL)"
                    )
                    connection.executemany(
                        "INSERT INTO regional_monthly_targets (month, region, target_revenue) VALUES (?, ?, ?)",
                        target_records,
                    )
                    connection.commit()

                if EXCEL_ENGINE:
                    with pd.ExcelWriter(excel_path, engine=EXCEL_ENGINE) as writer:
                        pd.DataFrame(product_records).to_excel(writer, index=False, sheet_name="products")
                        pd.DataFrame(store_records).to_excel(writer, index=False, sheet_name="stores")

                return {
                    "sales_january_csv": january_csv_path,
                    "sales_february_csv": february_csv_path,
                    "products_json": products_json_path,
                    "stores_html": stores_html_path,
                    "stores_csv": stores_csv_path,
                    "targets_sqlite": sqlite_path,
                    "reference_excel": excel_path,
                }


            demo_files = create_demo_day4_data()
            demo_files
            """
        ),
        "load-code": lines(
            """
            january_csv_path = demo_files["sales_january_csv"]
            february_csv_path = demo_files["sales_february_csv"]
            products_json_path = demo_files["products_json"]
            stores_html_path = demo_files["stores_html"]
            stores_csv_path = demo_files["stores_csv"]
            sqlite_path = demo_files["targets_sqlite"]
            excel_path = demo_files["reference_excel"]

            sales_january_raw = pd.read_csv(january_csv_path)
            sales_february_raw = pd.read_csv(february_csv_path)
            products_df = pd.read_json(products_json_path)

            try:
                stores_df = pd.read_html(stores_html_path)[0]
                stores_source = "HTML table"
            except (ImportError, ValueError):
                stores_df = pd.read_csv(stores_csv_path)
                stores_source = "CSV fallback"

            with sqlite3.connect(sqlite_path) as connection:
                targets_df = pd.read_sql_query(
                    "SELECT month, region, target_revenue FROM regional_monthly_targets ORDER BY month, region",
                    connection,
                )

            if excel_path.exists():
                excel_tables = pd.read_excel(excel_path, sheet_name=None)
            else:
                excel_tables = {}

            loaded_objects = pd.DataFrame(
                [
                    {"dataset": "sales_january_raw", "rows": len(sales_january_raw), "columns": sales_january_raw.shape[1]},
                    {"dataset": "sales_february_raw", "rows": len(sales_february_raw), "columns": sales_february_raw.shape[1]},
                    {"dataset": "products_df", "rows": len(products_df), "columns": products_df.shape[1]},
                    {"dataset": f"stores_df ({stores_source})", "rows": len(stores_df), "columns": stores_df.shape[1]},
                    {"dataset": "targets_df", "rows": len(targets_df), "columns": targets_df.shape[1]},
                ]
            )
            loaded_objects
            """
        ),
        "inspect-code": lines(
            """
            display(sales_january_raw.head())
            display(sales_february_raw.head())

            inspection_summary = pd.DataFrame(
                [
                    {
                        "dataset": "sales_january_raw",
                        "rows": len(sales_january_raw),
                        "missing_values": int(sales_january_raw.isna().sum().sum()),
                        "duplicate_rows": int(sales_january_raw.duplicated().sum()),
                    },
                    {
                        "dataset": "sales_february_raw",
                        "rows": len(sales_february_raw),
                        "missing_values": int(sales_february_raw.isna().sum().sum()),
                        "duplicate_rows": int(sales_february_raw.duplicated().sum()),
                    },
                    {
                        "dataset": "products_df",
                        "rows": len(products_df),
                        "missing_values": int(products_df.isna().sum().sum()),
                        "duplicate_rows": int(products_df.duplicated().sum()),
                    },
                ]
            )

            january_missing = sales_january_raw.isna().sum().sort_values(ascending=False).rename("missing_count")
            january_dtypes = sales_january_raw.dtypes.astype(str).rename("dtype")

            display(inspection_summary)
            display(january_dtypes.to_frame())
            january_missing.to_frame()
            """
        ),
        "clean-code": lines(
            """
            def clean_sales_frame(frame: pd.DataFrame, source_month: str) -> pd.DataFrame:
                cleaned = frame.copy()
                cleaned.columns = (
                    cleaned.columns.str.strip()
                    .str.lower()
                    .str.replace("%", "pct", regex=False)
                    .str.replace(" ", "_", regex=False)
                )

                text_columns = ["store_code", "product_code", "customer_segment", "sales_channel", "promo_flag"]
                for column in text_columns:
                    cleaned[column] = cleaned[column].astype("string").str.strip()

                cleaned["store_code"] = cleaned["store_code"].str.upper()
                cleaned["product_code"] = cleaned["product_code"].str.upper()
                cleaned["customer_segment"] = cleaned["customer_segment"].replace({"": pd.NA}).str.title().fillna("Unknown")
                cleaned["sales_channel"] = cleaned["sales_channel"].str.title().fillna("Unknown")
                cleaned["promo_flag"] = cleaned["promo_flag"].str.lower().map({"yes": True, "no": False})

                parsed_dates = pd.to_datetime(cleaned["order_date"], errors="coerce", dayfirst=True)
                cleaned["order_date_invalid_flag"] = parsed_dates.isna()
                cleaned["order_date"] = parsed_dates

                units_numeric = pd.to_numeric(cleaned["units"], errors="coerce")
                cleaned["units_missing_flag"] = units_numeric.isna()
                cleaned["units"] = units_numeric.fillna(1).astype("Int64")

                cleaned["unit_price"] = pd.to_numeric(cleaned["unit_price"], errors="coerce")

                discounts = pd.to_numeric(cleaned["discount_pct"], errors="coerce")
                cleaned["discount_missing_flag"] = discounts.isna()
                cleaned["discount_pct"] = discounts.fillna(0)

                cleaned["source_month"] = source_month
                cleaned["gross_revenue"] = cleaned["units"].astype("float64") * cleaned["unit_price"]
                cleaned["net_revenue"] = (cleaned["gross_revenue"] * (1 - cleaned["discount_pct"])).round(2)
                cleaned["order_month"] = cleaned["order_date"].dt.strftime("%Y-%m")

                cleaned = cleaned.drop_duplicates(
                    subset=["order_id", "order_date", "store_code", "product_code", "sales_channel"]
                ).reset_index(drop=True)
                return cleaned


            sales_january_clean = clean_sales_frame(sales_january_raw, "2026-01")
            sales_february_clean = clean_sales_frame(sales_february_raw, "2026-02")

            cleaning_report = pd.DataFrame(
                [
                    {
                        "dataset": "sales_january_clean",
                        "raw_rows": len(sales_january_raw),
                        "clean_rows": len(sales_january_clean),
                        "duplicates_removed": len(sales_january_raw) - len(sales_january_clean),
                    },
                    {
                        "dataset": "sales_february_clean",
                        "raw_rows": len(sales_february_raw),
                        "clean_rows": len(sales_february_clean),
                        "duplicates_removed": len(sales_february_raw) - len(sales_february_clean),
                    },
                ]
            )

            display(cleaning_report)
            sales_january_clean.head()
            """
        ),
        "filter-code": lines(
            """
            analysis_columns = [
                "order_id",
                "order_date",
                "order_month",
                "store_code",
                "product_code",
                "customer_segment",
                "units",
                "unit_price",
                "discount_pct",
                "sales_channel",
                "promo_flag",
                "net_revenue",
                "source_month",
            ]


            def filter_sales_frame(frame: pd.DataFrame) -> pd.DataFrame:
                filtered = frame.loc[
                    frame["order_date"].notna()
                    & frame["units"].gt(0)
                    & frame["unit_price"].gt(0)
                    & frame["sales_channel"].isin(["Online", "Retail"]),
                    analysis_columns,
                ].copy()
                return filtered.sort_values(["order_date", "order_id"]).reset_index(drop=True)


            sales_january_filtered = filter_sales_frame(sales_january_clean)
            sales_february_filtered = filter_sales_frame(sales_february_clean)

            allowed_channels = ["Online", "Retail"]
            sql_style_preview = sales_february_clean.query(
                "sales_channel in @allowed_channels and unit_price > 0"
            )[["order_id", "sales_channel", "unit_price", "net_revenue"]].head()

            filter_report = pd.DataFrame(
                [
                    {"dataset": "sales_january_filtered", "rows_after_filter": len(sales_january_filtered)},
                    {"dataset": "sales_february_filtered", "rows_after_filter": len(sales_february_filtered)},
                ]
            )

            display(filter_report)
            display(sql_style_preview)
            sales_january_filtered.head()
            """
        ),
        "combine-code": lines(
            """
            products_lookup = products_df.copy()
            products_lookup["product_code"] = products_lookup["product_code"].astype("string").str.upper()

            stores_lookup = stores_df.copy()
            stores_lookup.columns = (
                stores_lookup.columns.astype("string")
                .str.strip()
                .str.lower()
                .str.replace(" ", "_", regex=False)
            )
            stores_lookup["store_code"] = stores_lookup["store_code"].astype("string").str.upper()

            sales_all = pd.concat([sales_january_filtered, sales_february_filtered], ignore_index=True)
            sales_with_products = sales_all.merge(
                products_lookup,
                on="product_code",
                how="left",
                validate="m:1",
                indicator="product_match",
            )
            sales_enriched = sales_with_products.merge(
                stores_lookup,
                on="store_code",
                how="left",
                validate="m:1",
                indicator="store_match",
            )
            sales_analysis = sales_enriched.query(
                "product_match == 'both' and store_match == 'both'"
            ).copy()
            sales_analysis["month"] = sales_analysis["order_date"].dt.strftime("%Y-%m")

            merge_report = pd.DataFrame(
                [
                    {"check": "rows_after_concat", "value": len(sales_all)},
                    {"check": "product_match_both", "value": int((sales_enriched["product_match"] == "both").sum())},
                    {"check": "product_match_left_only", "value": int((sales_enriched["product_match"] == "left_only").sum())},
                    {"check": "store_match_both", "value": int((sales_enriched["store_match"] == "both").sum())},
                    {"check": "store_match_left_only", "value": int((sales_enriched["store_match"] == "left_only").sum())},
                    {"check": "rows_for_analysis", "value": len(sales_analysis)},
                ]
            )

            display(merge_report)
            sales_analysis.head()
            """
        ),
        "summarize-code": lines(
            """
            targets_clean = targets_df.copy()
            targets_clean["month"] = targets_clean["month"].astype("string")
            targets_clean["region"] = targets_clean["region"].astype("string")

            category_summary = (
                sales_analysis.groupby(["month", "region", "category"], dropna=False)
                .agg(
                    orders=("order_id", "nunique"),
                    units_sold=("units", "sum"),
                    revenue=("net_revenue", "sum"),
                )
                .reset_index()
                .sort_values(["month", "revenue"], ascending=[True, False])
            )

            region_month_summary = (
                sales_analysis.groupby(["month", "region"], dropna=False)
                .agg(
                    orders=("order_id", "nunique"),
                    units_sold=("units", "sum"),
                    revenue=("net_revenue", "sum"),
                    average_order_value=("net_revenue", "mean"),
                )
                .reset_index()
                .round(2)
            )

            region_target_summary = region_month_summary.merge(
                targets_clean,
                on=["month", "region"],
                how="left",
                validate="1:1",
            )
            region_target_summary["achievement_pct"] = (
                region_target_summary["revenue"] / region_target_summary["target_revenue"] * 100
            ).round(1)

            revenue_pivot = pd.pivot_table(
                region_target_summary,
                index="region",
                columns="month",
                values="revenue",
                aggfunc="sum",
                fill_value=0,
            ).round(2)

            display(category_summary)
            display(region_target_summary)
            revenue_pivot
            """
        ),
        "reshape-code": lines(
            """
            report_wide = region_target_summary.pivot(index="region", columns="month", values="revenue").round(2)
            metrics_long = region_target_summary.melt(
                id_vars=["region", "month"],
                value_vars=["revenue", "target_revenue", "achievement_pct"],
                var_name="metric",
                value_name="value",
            ).sort_values(["region", "month", "metric"]).reset_index(drop=True)

            display(report_wide)
            metrics_long.head(12)
            """
        ),
        "visualize-code": lines(
            """
            monthly_totals = region_target_summary.groupby("month")[["revenue", "target_revenue"]].sum().round(2)
            category_totals = (
                sales_analysis.groupby("category")["net_revenue"].sum().sort_values(ascending=False).round(2)
            )

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            monthly_totals.plot(kind="bar", ax=axes[0], title="Actual Revenue vs Target by Month")
            axes[0].set_xlabel("Month")
            axes[0].set_ylabel("Revenue")
            axes[0].tick_params(axis="x", rotation=0)

            category_totals.plot(
                kind="bar",
                ax=axes[1],
                color=["#4C78A8", "#F58518", "#54A24B"],
                title="Revenue by Product Category",
            )
            axes[1].set_xlabel("Category")
            axes[1].set_ylabel("Revenue")
            axes[1].tick_params(axis="x", rotation=25)

            plt.tight_layout()
            chart_path = OUTPUT_DIR / "day4_revenue_overview.png"
            fig.savefig(chart_path, dpi=150, bbox_inches="tight")
            plt.show()
            chart_path
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

            pd.DataFrame(
                [
                    {"artifact": "clean sales data", "path": str(clean_output_path)},
                    {"artifact": "regional target summary", "path": str(summary_output_path)},
                    {"artifact": "long metrics json", "path": str(metrics_output_path)},
                    {"artifact": "html report", "path": str(html_output_path)},
                    {"artifact": "chart image", "path": str(OUTPUT_DIR / "day4_revenue_overview.png")},
                    {"artifact": "excel pack", "path": str(excel_output_path) if excel_output_path else "skipped: no Excel engine installed"},
                ]
            )
            """
        ),
    }

    for cell in scaffold["cells"]:
        if cell.get("cell_type") == "markdown" and cell.get("id") in markdown_by_id:
            cell["source"] = markdown_by_id[cell["id"]]
        if cell.get("cell_type") == "code" and cell.get("id") in code_by_id:
            cell["source"] = code_by_id[cell["id"]]

    OUTPUT_NOTEBOOK_PATH.write_text(json.dumps(scaffold, indent=2), encoding="utf-8")


def main() -> None:
    build_data_files()
    build_notebook()
    print(f"Created notebook: {OUTPUT_NOTEBOOK_PATH}")
    print("Created data files:")
    for path in sorted(RAW_DIR.iterdir()):
        print(f"- {path.name}")


if __name__ == "__main__":
    main()
