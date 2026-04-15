# %% [markdown]
# # 3. diena - JSON, CSV un Pandas: darba burtnīca
#
# Šī ir vadīta darba burtnīca 3. dienai.
# Tā seko pilnā materiāla struktūrai, bet nesatur gatavus risinājumus.
#
# Darba pieeja:
# - izlasi sadaļas mērķi;
# - aizpildi `TODO` vietas;
# - palaid šūnas secīgi;
# - salīdzini savus rezultātus ar paskaidrojumiem un sagaidāmo struktūru.
#
# Šajā darba burtnīcā apgūsim:
# - vienkārša `JSON` nolasīšanu;
# - ligzdota `JSON` apskati un izlīdzināšanu;
# - `CSV` failu ielādi ar `pandas`;
# - `DataFrame` atlasi, filtrēšanu, kārtošanu un grupēšanu;
# - `merge()`, `concat()` un rezultātu eksportu.

# %% [markdown]
# ## 0. Sagatavošana
#
# Mērķis: sagatavot importus un atrast projekta datu mapi.
#
# Šī šūna ir iedota gatava, jo tās mērķis nav pārbaudīt sintaksi, bet nodrošināt
# vienādu starta punktu visiem uzdevumiem.

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
    """Atrod projekta sakni gan skripta, gan Jupyter izpildes gadījumā."""
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

print("Projekta sakne:", REPO_ROOT)
print("Datu mape:", DATA_DIR)

# %% [markdown]
# ## 1. Pārbaudi datu failus
#
# Mērķis: pārliecināties, ka redzi visus 3. dienas failus.
#
# Sagaidāmā ideja:
# - mapē vajadzētu būt 2 `json` failiem;
# - mapē vajadzētu būt 3 `csv` failiem.

# %%
# TODO:
# Izveido sarakstu ar failiem mapē DATA_DIR un izdrukā to nosaukumus.
# Hint: vari izmantot DATA_DIR.glob("*") vai DATA_DIR.iterdir()

data_files = []

for path in data_files:
    print(path.name)

# %% [markdown]
# ## 2. Nolasām vienkāršu JSON failu
#
# Mērķis: nolasīt `products_basic.json` ar Python standarta bibliotēku.
#
# Sagaidāmā struktūra:
# - Python tips: `list`
# - katrs elements sarakstā ir `dict`

# %%
products_json_path = DATA_DIR / "products_basic.json"

# TODO:
# 1. Atver failu ar with ... open(..., encoding="utf-8")
# 2. Nolasi saturu ar json.load(...)
# 3. Saglabā rezultātu mainīgajā products_data

products_data = None

if products_data is not None:
    print("Python tips:", type(products_data))
    print("Ierakstu skaits:", len(products_data))

# %% [markdown]
# ## 3. Apskati vienu JSON ierakstu
#
# Mērķis: saprast viena produkta struktūru.
#
# Ko vajadzētu redzēt:
# - viena produkta vārdnīcu;
# - tās atslēgu sarakstu.

# %%
# TODO:
# Izdrukā pirmo elementu un tā atslēgas.
# Hint: pirmajam elementam vari piekļūt ar indeksu [0]

if products_data is not None:
    first_product = None
    product_keys = None

    print(first_product)
    print(product_keys)

# %% [markdown]
# ## 4. Izdrukā pirmos 3 produktus ar ciklu
#
# Mērķis: iziet cauri dažiem ierakstiem un piekļūt atsevišķiem laukiem.
#
# Izdrukā:
# - `product_id`
# - `name`
# - `price`

# %%
# TODO:
# Uzraksti for ciklu, kas apstrādā pirmos 3 produktus.
# Hint: vari izmantot products_data[:3]

if products_data is not None:
    for product in []:
        # print(...)
        pass

# %% [markdown]
# ## 5. Pārveido JSON par DataFrame
#
# Mērķis: izveidot `DataFrame` no saraksta ar vārdnīcām.
#
# Sagaidāmā ideja:
# - rindiņas atbilst produktiem;
# - kolonnas atbilst laukiem kā `name`, `category`, `price`.

# %%
# TODO:
# Izveido DataFrame un saglabā to mainīgajā products_df.
# Hint: pd.DataFrame(...)

products_df = None

if products_df is not None:
    display(products_df)

# %% [markdown]
# ## 6. Apskati DataFrame pamatinformāciju
#
# Mērķis: iepazīt biežāk lietotās DataFrame apskates komandas.
#
# Pamēģini:
# - `.head()`
# - `.shape`
# - `.columns`
# - `.dtypes`
# - `.info()`

# %%
# TODO:
# Palaid vismaz 3 no iepriekš uzskaitītajām komandām.
# Hint: .info() parasti drukā informāciju konsolē

if products_df is not None:
    pass

# %% [markdown]
# ## 7. Atlasi kolonnas
#
# Mērķis: atlasīt vienu kolonnu un vairākas kolonnas.
#
# Uzdevumi:
# - atlasi tikai `name`;
# - atlasi `product_id`, `name`, `category`, `price`.

# %%
# TODO:
# Izveido divas atlases:
# 1. viena kolonna
# 2. vairākas kolonnas

selected_name_column = None
selected_product_columns = None

if selected_name_column is not None:
    display(selected_name_column)

if selected_product_columns is not None:
    display(selected_product_columns)

# %% [markdown]
# ## 8. Filtrē rindas
#
# Mērķis: atlasīt tikai daļu no produktiem pēc nosacījuma.
#
# Uzdevumi:
# - atlasi tikai `Electronics` kategorijas produktus;
# - atlasi `Electronics` produktus ar cenu virs 10.

# %%
# TODO:
# Izveido divus filtrētus DataFrame objektus.
# Hint: kombinē nosacījumus ar & un apaļajām iekavām

electronics_df = None
expensive_electronics_df = None

if electronics_df is not None:
    display(electronics_df)

if expensive_electronics_df is not None:
    display(expensive_electronics_df)

# %% [markdown]
# ## 9. Sakārto datus
#
# Mērķis: sakārtot produktus pēc cenas augošā un dilstošā secībā.

# %%
# TODO:
# Izveido divus rezultātus:
# - pēc cenas augošā secībā
# - pēc cenas dilstošā secībā

products_sorted_asc = None
products_sorted_desc = None

if products_sorted_asc is not None:
    display(products_sorted_asc)

if products_sorted_desc is not None:
    display(products_sorted_desc)

# %% [markdown]
# ## 10. Izveido jaunas kolonnas
#
# Mērķis: pievienot aprēķinātu kolonnu un teksta kolonnu.
#
# Uzdevumi:
# - izveido `price_with_vat`;
# - izveido `name_upper`.
#
# Hint:
# - PVN šeit var būt `1.21`
# - teksta kolonnām noder `.str.upper()`

# %%
# TODO:
# Pievieno divas jaunas kolonnas products_df objektam.

if products_df is not None:
    pass

# %% [markdown]
# ## 11. Grupē produktus pēc kategorijas
#
# Mērķis: izveidot vienkāršu kopsavilkumu ar `groupby()`.
#
# Uzdevumi:
# - aprēķini vidējo cenu katrai kategorijai;
# - izveido kopsavilkuma tabulu ar produktu skaitu un maksimālo cenu.

# %%
# TODO:
# Izveido:
# 1. series vai DataFrame ar vidējo cenu pa kategorijām
# 2. DataFrame ar count un max

average_price_by_category = None
products_summary = None

if average_price_by_category is not None:
    display(average_price_by_category)

if products_summary is not None:
    display(products_summary)

# %% [markdown]
# ## 12. Nolasām ligzdotu JSON failu
#
# Mērķis: saprast, ka `JSON` ne vienmēr ir plakana tabula.
#
# Sagaidāmā ideja:
# - augšējais līmenis ir `dict`;
# - viens no laukiem satur `orders` sarakstu.

# %%
orders_json_path = DATA_DIR / "orders_nested.json"

# TODO:
# Nolasiet failu un saglabājiet to mainīgajā orders_document.

orders_document = None

if orders_document is not None:
    print("Tips:", type(orders_document))
    print("Atslēgas:", list(orders_document.keys()))

# %% [markdown]
# ## 13. Apskati pasūtījumu metadatus un pašu sarakstu
#
# Mērķis: atrast, kur atrodas reālie ieraksti.
#
# Uzdevumi:
# - izdrukā `report_name`, `generated_at`, `currency`;
# - izveido `orders_list = ...`;
# - izdrukā pasūtījumu skaitu.

# %%
# TODO:
# Šeit piekļūsti metadatiem un pasūtījumu sarakstam.

orders_list = None

if orders_document is not None:
    pass

if orders_list is not None:
    print("Pasūtījumu skaits:", len(orders_list))

# %% [markdown]
# ## 14. Piekļūsti ligzdotām vērtībām vienā pasūtījumā
#
# Mērķis: manuāli nolasīt dažus laukus no ligzdotas struktūras.
#
# Izdrukā:
# - `order_id`
# - klienta vārdu
# - klienta pilsētu
# - maksājuma statusu
# - pirmās preces `product_id`

# %%
# TODO:
# Izveido first_order un piekļūsti ligzdotajiem laukiem.
# Hint: būs vajadzīgas vairākas [] piekļuves pēc kārtas

if orders_list is not None and len(orders_list) > 0:
    first_order = None
    # print(...)

# %% [markdown]
# ## 15. Izlīdzini ligzdotu JSON tabulas formā
#
# Mērķis: izveidot vienu rindu katram pasūtījumam.
#
# Šeit nav jāraksta pilnīgi viss no nulles bez palīdzības. Zemāk ir dots karkass.
#
# Vajadzīgie lauki:
# - `order_id`
# - `customer_id`
# - `customer_name`
# - `city`
# - `loyalty_tier`
# - `item_count`
# - `total_quantity`
# - `items_total`
# - `delivery_type`
# - `delivery_cost`
# - `payment_method`
# - `payment_status`
# - `coupon_code`
# - `total_amount`

# %%
# TODO:
# Aizpildi cikla saturu.
# Hint:
# - items = order.get("items", [])
# - sum(...) palīdz saskaitīt quantity vai summas
# - .get() noder laukiem, kuri var arī neeksistēt

order_rows = []

if orders_list is not None:
    for order in orders_list:
        items = order.get("items", [])

        total_quantity = None
        items_total = None
        delivery_cost = None
        total_amount = None

        row = {
            "order_id": None,
            "customer_id": None,
            "customer_name": None,
            "city": None,
            "loyalty_tier": None,
            "item_count": None,
            "total_quantity": total_quantity,
            "items_total": items_total,
            "delivery_type": None,
            "delivery_cost": delivery_cost,
            "payment_method": None,
            "payment_status": None,
            "coupon_code": None,
            "total_amount": total_amount,
        }

        order_rows.append(row)

orders_df = None

if order_rows:
    # TODO: pārvērt order_rows par DataFrame
    pass

if orders_df is not None:
    display(orders_df)

# %% [markdown]
# ## 16. Apskati trūkstošās vērtības un filtrē pasūtījumus
#
# Mērķis:
# - noskaidrot, kur trūkst dati;
# - atlasīt tikai apmaksātos pasūtījumus ar vismaz vienu preci.

# %%
# TODO:
# 1. izmanto isna().sum()
# 2. izveido paid_orders_df

missing_values_summary = None
paid_orders_df = None

if missing_values_summary is not None:
    display(missing_values_summary)

if paid_orders_df is not None:
    display(paid_orders_df)

# %% [markdown]
# ## 17. Nolasām CSV failus
#
# Mērķis: ar `pd.read_csv()` nolasīt janvāra, februāra un produktu tabulas.

# %%
sales_january_path = DATA_DIR / "sales_january.csv"
sales_february_path = DATA_DIR / "sales_february.csv"
products_csv_path = DATA_DIR / "products.csv"

# TODO:
# Nolasiet 3 CSV failus un saglabājiet tos:
# - sales_january_df
# - sales_february_df
# - products_lookup_df

sales_january_df = None
sales_february_df = None
products_lookup_df = None

if sales_january_df is not None:
    display(sales_january_df.head())

# %% [markdown]
# ## 18. Pārveido datumu un aizpildi trūkstošās atlaides
#
# Mērķis:
# - pārvērst `date` kolonnu datumā;
# - aizpildīt tukšās `discount_pct` vērtības ar `0`.

# %%
# TODO:
# 1. izmanto pd.to_datetime(...)
# 2. izmanto fillna(0)

if sales_january_df is not None and sales_february_df is not None:
    pass

# %% [markdown]
# ## 19. Apvieno janvāra pārdošanu ar produktu tabulu
#
# Mērķis: pievienot produktu nosaukumus, kategorijas un cenas.
#
# Uzdevumi:
# - izmanto `merge()`;
# - saglabā rezultātu `sales_january_enriched_df`.

# %%
# TODO:
# Apvieno janvāra pārdošanas tabulu ar produktu lookup tabulu.
# Hint: kopīgā atslēga ir product_id

sales_january_enriched_df = None

if sales_january_enriched_df is not None:
    display(sales_january_enriched_df.head())

# %% [markdown]
# ## 20. Izveido ieņēmumu kolonnas
#
# Mērķis: aprēķināt:
# - `gross_revenue`
# - `net_revenue`
#
# Hint:
# - bruto ieņēmumi = `units_sold * price`
# - neto ieņēmumi = bruto ieņēmumi pēc atlaides

# %%
# TODO:
# Pievieno abas kolonnas sales_january_enriched_df objektam.

if sales_january_enriched_df is not None:
    pass

# %% [markdown]
# ## 21. Izveido kopsavilkumu pa veikaliem un kategorijām
#
# Mērķis: izmantot `groupby()` un `agg()`.
#
# Uzdevumi:
# - kopsavilkums pa `store`;
# - kopsavilkums pa `category`.

# %%
# TODO:
# Izveido:
# - sales_by_store_df
# - sales_by_category_df

sales_by_store_df = None
sales_by_category_df = None

if sales_by_store_df is not None:
    display(sales_by_store_df)

if sales_by_category_df is not None:
    display(sales_by_category_df)

# %% [markdown]
# ## 22. Apvieno janvāra un februāra tabulas ar concat()
#
# Mērķis: vertikāli apvienot divus mēnešus vienā tabulā.

# %%
# TODO:
# Izmanto pd.concat(..., ignore_index=True)

all_sales_df = None

if all_sales_df is not None:
    display(all_sales_df)

# %% [markdown]
# ## 23. Apvieno visus pārdošanas datus ar produktu tabulu
#
# Mērķis:
# - izmantot `merge()` uz apvienotajiem pārdošanas datiem;
# - pievienot ieņēmumu kolonnas arī šeit.

# %%
# TODO:
# 1. izveido all_sales_enriched_df
# 2. pievieno gross_revenue un net_revenue

all_sales_enriched_df = None

if all_sales_enriched_df is not None:
    display(all_sales_enriched_df.head())

# %% [markdown]
# ## 24. Izveido vienkāršu pivot tabulu
#
# Mērķis: kopsavilkums ar:
# - rindās `store`
# - kolonnās `category`
# - vērtībās `net_revenue`

# %%
# TODO:
# Izmanto pd.pivot_table(...)
# Hint: fill_value=0 bieži ir noderīgs

pivot_table_df = None

if pivot_table_df is not None:
    display(pivot_table_df)

# %% [markdown]
# ## 25. Saglabā rezultātus failos
#
# Mērķis: eksportēt dažus rezultātus uz `CSV` un `JSON`.
#
# Uzdevumi:
# - izveido mapi `outputs`;
# - saglabā vismaz vienu `CSV`;
# - saglabā izlīdzināto pasūtījumu tabulu kā `JSON`.

# %%
output_dir = DATA_DIR / "outputs"

# TODO:
# 1. izveido output_dir, ja tā neeksistē
# 2. izmanto to_csv(...)
# 3. izmanto to_json(...)

print("Rezultātu mape būs:", output_dir)

# %% [markdown]
# ## 26. Pašpārbaudes jautājumi
#
# Atbildi sev īsi:
# - Kad `CSV` ir ērtāks par `JSON`?
# - Kad vienkāršu `JSON` var tieši pārvērst par `DataFrame`?
# - Kāpēc ligzdotam `JSON` bieži vajag papildu ciklu vai izlīdzināšanu?
# - Kad izmantot `concat()`, bet kad `merge()`?

# %% [markdown]
# ## 27. Papildu prakse
#
# Ja pamatuzdevumi jau izpildīti, pamēģini:
# - atlasīt tikai `Office` kategorijas produktus;
# - atrast visdārgāko produktu;
# - saskaitīt kopējo `net_revenue` pa produktiem;
# - atrast pasūtījumus bez `loyalty_tier`;
# - eksportēt tikai Electronics pārdošanas datus atsevišķā failā.

# %%
# Rakstiet savu papildu prakses kodu šeit.

