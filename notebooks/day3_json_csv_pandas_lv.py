# %% [markdown]
# # 3. diena - JSON, CSV un Pandas pamati
#
# ## Notebook mērķis
#
# Šajā notebook soli pa solim apskatīsim, kā:
# - nolasīt vienkāršu `JSON` failu ar Python standarta bibliotēku
# - apskatīt `JSON` struktūru
# - strādāt ar ligzdotu `JSON`
# - nolasīt `CSV` failus ar `pandas`
# - apskatīt `DataFrame`
# - atlasīt, filtrēt, kārtot un pārveidot datus
# - apvienot tabulas ar `concat()` un `merge()`
# - eksportēt rezultātus uz `CSV` un `JSON`
#
# ## Šajā nodarbībā izmantotie faili
#
# Mēs izmantosim paraugdatus no mapes `data/day3/`:
# - `products_basic.json`
# - `orders_nested.json`
# - `products.csv`
# - `sales_january.csv`
# - `sales_february.csv`
#
# ## Svarīgi
#
# Izpildiet notebook no augšas uz leju. Vēlākās šūnas izmanto mainīgos, kas
# izveidoti iepriekšējās šūnās.

# %%
from __future__ import annotations

import json
from pathlib import Path

try:
    import pandas as pd
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Šim notebook ir vajadzīgs pandas. Vispirms instalējiet to, piemēram: pip install pandas"
    ) from exc


def find_repo_root() -> Path:
    """Atrod projekta saknes mapi gan skripta, gan Jupyter izpildes gadījumā."""
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
# ## 1. Pārbaudām, vai datu faili eksistē
#
# Pirms datu nolasīšanas ir laba prakse pārbaudīt failu ceļus.

# %%
data_files = sorted(DATA_DIR.glob("*"))
print("Datu mape:", DATA_DIR.resolve())
print("Atrasti faili:")
for path in data_files:
    print("-", path.name)

# %% [markdown]
# ## 2. Nolasām vienkāršu JSON failu
#
# `products_basic.json` ir vienkāršs, plakans `JSON` fails.
# Tas satur produktu objektu sarakstu.
# Šādu struktūru ir visvieglāk pārveidot tabulā.

# %%
products_json_path = DATA_DIR / "products_basic.json"

with products_json_path.open("r", encoding="utf-8") as file:
    products_data = json.load(file)

print("Python tips:", type(products_data))
print("Ierakstu skaits:", len(products_data))

# %% [markdown]
# Apskatīsim vienu elementu no saraksta.

# %%
products_data[0]

# %% [markdown]
# Katrs elements ir Python vārdnīca.

# %%
print("Pirmā elementa tips:", type(products_data[0]))
print("Pirmā elementa atslēgas:", list(products_data[0].keys()))

# %% [markdown]
# ## 3. Ejam cauri JSON ierakstiem ar ciklu
#
# Pirms lietot `pandas`, ir vērts apskatīt neapstrādātos datus tieši Python
# struktūrās.

# %%
for product in products_data[:3]:
    print(product["product_id"], "-", product["name"], "-", product["price"])

# %% [markdown]
# ## 4. Pārveidojam vienkāršu JSON par DataFrame
#
# Sarakstu ar vārdnīcām bieži var uzreiz pārvērst par `pandas DataFrame`.

# %%
products_df = pd.DataFrame(products_data)
products_df

# %% [markdown]
# ## 5. Apskatām DataFrame
#
# Šīs ir pirmās komandas, ar kurām vajadzētu kļūt ērtāk strādāt.

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
# ## 6. Vienkārša kolonnu atlase
#
# Varam atlasīt vienu kolonnu vai vairākas kolonnas.

# %%
products_df["name"]

# %%
products_df[["product_id", "name", "category", "price"]]

# %% [markdown]
# ## 7. Filtrējam rindas
#
# Šeit atlasām tikai elektronikas produktus.

# %%
products_df[products_df["category"] == "Electronics"]

# %% [markdown]
# Varam kombinēt arī vairākus nosacījumus.

# %%
products_df[(products_df["category"] == "Electronics") & (products_df["price"] > 10)]

# %% [markdown]
# ## 8. Kārtojam vērtības
#
# Kārtošana ir viens no pirmajiem praktiskajiem datu analīzes uzdevumiem.

# %%
products_df.sort_values("price")

# %%
products_df.sort_values("price", ascending=False)

# %% [markdown]
# ## 9. Izveidojam jaunas kolonnas
#
# Jaunas vērtības varam aprēķināt no jau esošajām kolonnām.

# %%
products_df["price_with_vat"] = (products_df["price"] * 1.21).round(2)
products_df["name_upper"] = products_df["name"].str.upper()
products_df

# %% [markdown]
# ## 10. Grupējam un veidojam kopsavilkumu
#
# Šis ir līdzīgi vienkāršai Excel PivotTable pieejai.

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
# ## 11. Nolasām ligzdotu JSON failu
#
# `orders_nested.json` ir sarežģītāks piemērs.
# Šis fails nav tikai saraksts. Tas ir objekts ar metadatiem un ar `orders`
# sarakstu tā iekšpusē.

# %%
orders_json_path = DATA_DIR / "orders_nested.json"

with orders_json_path.open("r", encoding="utf-8") as file:
    orders_document = json.load(file)

print("Augšējā līmeņa tips:", type(orders_document))
print("Augšējā līmeņa atslēgas:", list(orders_document.keys()))

# %% [markdown]
# Apskatīsim atskaites metadatus.

# %%
print("Atskaites nosaukums:", orders_document["report_name"])
print("Izveidots:", orders_document["generated_at"])
print("Valūta:", orders_document["currency"])

# %% [markdown]
# Paši ieraksti atrodas laukā `orders`.

# %%
orders_list = orders_document["orders"]
print("Pasūtījumu skaits:", len(orders_list))
orders_list[0]

# %% [markdown]
# ## 12. Piekļuve ligzdotām vērtībām manuāli
#
# Tas ir noderīgi, kamēr vēl tikai mācāmies saprast `JSON` struktūras.

# %%
first_order = orders_list[0]

print("Pasūtījuma ID:", first_order["order_id"])
print("Klienta vārds:", first_order["customer"]["name"])
print("Klienta pilsēta:", first_order["customer"]["city"])
print("Maksājuma statuss:", first_order["payment"]["status"])
print("Pirmā pasūtītā prece:", first_order["items"][0]["product_id"])

# %% [markdown]
# ## 13. Izlīdzinām ligzdotu JSON ar ciklu
#
# Šeit veidojam vienu rindu katram pasūtījumam.
# Dažiem laukiem apzināti izmantojam `.get()`, jo ne visiem pasūtījumiem ir
# pilnīgi vienāda struktūra.

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
# ## 14. Apskatām trūkstošās vērtības
#
# Pēc ligzdota `JSON` izlīdzināšanas bieži parādās trūkstošas vērtības.

# %%
orders_df.isna().sum()

# %% [markdown]
# Piemēram, ne visiem pasūtījumiem ir `coupon_code` vai `loyalty_tier`.

# %%
orders_df[["order_id", "loyalty_tier", "coupon_code", "delivery_cost"]]

# %% [markdown]
# ## 15. Filtrējam rezultātu no ligzdotā JSON
#
# Šeit atstājam tikai apmaksātos pasūtījumus, kuros ir vismaz viena prece.

# %%
paid_orders_df = orders_df[
    (orders_df["payment_status"] == "paid") & (orders_df["item_count"] > 0)
]
paid_orders_df

# %% [markdown]
# ## 16. Nolasām CSV failus ar pandas
#
# `CSV` jau ir tabulveida formāts, tāpēc `pandas` to var nolasīt tieši.

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
# ## 17. Pārveidojam kolonnu datu tipus
#
# Datumu kolonnas parasti jāpārveido atbilstošā tipā.

# %%
sales_january_df["date"] = pd.to_datetime(sales_january_df["date"])
sales_february_df["date"] = pd.to_datetime(sales_february_df["date"])

sales_january_df.dtypes

# %% [markdown]
# ## 18. Trūkstošās vērtības CSV datos
#
# Pamaniet, ka kolonnā `discount_pct` ir trūkstošas vērtības.

# %%
sales_january_df.isna().sum()

# %%
sales_january_df[sales_january_df["discount_pct"].isna()]

# %% [markdown]
# Šīs trūkstošās atlaides varam aizpildīt ar `0`.

# %%
sales_january_df["discount_pct"] = sales_january_df["discount_pct"].fillna(0)
sales_february_df["discount_pct"] = sales_february_df["discount_pct"].fillna(0)

sales_january_df.isna().sum()

# %% [markdown]
# ## 19. Atlasām un filtrējam CSV datus

# %%
sales_january_df[["sale_id", "date", "product_id", "store", "units_sold"]]

# %%
sales_january_df[sales_january_df["units_sold"] >= 10]

# %%
sales_january_df[sales_january_df["store"] == "Riga-Center"]

# %% [markdown]
# ## 20. Veidojam aprēķinātās kolonnas
#
# Vispirms pievienojam produktu cenas pārdošanas tabulai ar `merge()`.

# %%
sales_january_enriched_df = sales_january_df.merge(
    products_lookup_df[["product_id", "name", "category", "price"]],
    on="product_id",
    how="left",
)

sales_january_enriched_df.head()

# %% [markdown]
# Tagad varam aprēķināt bruto ieņēmumus un ieņēmumus pēc atlaides.

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
# ## 21. Kārtojam un veidojam pārdošanas kopsavilkumus

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
# ## 22. Apvienojam mēnešu tabulas ar concat()
#
# Janvāra un februāra failiem ir vienādas kolonnas, tāpēc vertikāla
# apvienošana ir vienkārša.

# %%
all_sales_df = pd.concat([sales_january_df, sales_february_df], ignore_index=True)
all_sales_df

# %%
all_sales_df.shape

# %% [markdown]
# ## 23. Apvienojam pārdošanas datus ar produktu tabulu
#
# `merge()` apvieno divas tabulas pēc kopīgas atslēgas.

# %%
all_sales_enriched_df = all_sales_df.merge(products_lookup_df, on="product_id", how="left")
all_sales_enriched_df.head()

# %% [markdown]
# Pievienosim aprēķinātās ieņēmumu kolonnas arī apvienotajiem datiem.

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
# ## 24. Analīze pa abiem mēnešiem kopā
#
# Tagad varam veidot kopsavilkumus par abiem mēnešiem.

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
# ## 25. Vienkārša pivot tabula
#
# Šis ir viens no biežākajiem soļiem Excel lietotājiem, kuri sāk strādāt ar
# `pandas`.

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
# ## 26. JSON un CSV salīdzinājums
#
# Īss salīdzinājums:
# - `CSV` ir ērtāks, ja dati jau ir tabulas formā
# - vienkāršu `JSON` bieži var tieši pārveidot par tabulu
# - ligzdotu `JSON` parasti vispirms vajag apskatīt un izlīdzināt
#
# Zemāk salīdzinām trīs galveno tabulu izmērus.

# %%
print("products_df izmērs:", products_df.shape)
print("orders_df izmērs:", orders_df.shape)
print("all_sales_enriched_df izmērs:", all_sales_enriched_df.shape)

# %% [markdown]
# ## 27. Rezultātu eksports
#
# Reālos darba procesos notīrītos vai apkopotos datus bieži saglabājam failos.

# %%
output_dir = DATA_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

sales_by_store_df.to_csv(output_dir / "sales_by_store_january.csv")
monthly_store_summary_df.to_csv(output_dir / "sales_by_store_all_months.csv")
orders_df.to_json(output_dir / "orders_flattened.json", orient="records", indent=2)

print("Faili saglabāti mapē:", output_dir.resolve())

# %% [markdown]
# ## 28. Idejas patstāvīgai praksei
#
# Pamēģiniet paši:
# - atlasīt tikai `Office` kategorijas produktus
# - atrast visdārgāko produktu
# - aprēķināt kopējos janvāra ieņēmumus pa produktiem
# - atrast pasūtījumus, kuriem trūkst `loyalty_tier`
# - sakārtot visus pārdošanas ierakstus pēc `units_sold`
# - eksportēt tikai Electronics pārdošanas datus atsevišķā `CSV` failā
#
# Zem šīs vietas varat pievienot savas šūnas.

# %%
# Rakstiet savu prakses kodu šeit.

