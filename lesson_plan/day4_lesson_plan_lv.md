# 4. dienas nodarbības plāns — Pandas darba plūsma: no datu avotiem līdz vizuālam rezultātam

## Dienas fokuss
4. diena ir veidota ap pilnu `Pandas` darba plūsmu, nevis atsevišķu funkciju sarakstu. Dalībnieki strādā cauri reālistiskai secībai: ielādē datus, apskata tos, attīra, filtrē, apvieno tabulas, veido kopsavilkumus, pārveido rezultātu formu, vizualizē secinājumus un eksportē gala rezultātus. Mērķis nav aptvert pilnīgi visu `Pandas`, bet iemācīt praktisku analīzes darba plūsmu, ko var atkārtoti lietot reālās statistikas un biroja datu situācijās.

## Mērķi
- Nolasīt tabulveida datus no `CSV`, `Excel`, `JSON`, `SQLite` un HTML tabulu avotiem ar `Pandas`
- Apskatīt ielādētos datus un pamanīt struktūru, tipus un kvalitātes problēmas
- Attīrīt un standartizēt datus pirms analīzes
- Lietot elastīgus filtrēšanas un atlases paņēmienus, tai skaitā SQL līdzīgu sintaksi ar `query()`
- Apvienot tabulas ar `merge` un `concat`
- Veidot kopsavilkumus ar `groupby()`, `agg()` un `pivot_table()`
- Pārveidot datus atskaitēm ar `pivot()` un `melt()`
- Izveidot vienkāršus vizuālus rezultātus ar `Pandas` diagrammām un `matplotlib`
- Eksportēt attīrītus datus, kopsavilkumus un atskaitei gatavus rezultātus

## Priekšzināšanas
- Python pamati no 1. dienas
- Failu nolasīšanas un datu tīrīšanas idejas no 2. dienas
- `JSON`, `Series`, `DataFrame`, filtrēšana, grupēšana un pamata savienojumi no 3. dienas
- Pamata izpratne par Excel tabulām un vienkāršiem SQL jēdzieniem, piemēram, `SELECT`, `WHERE` un `GROUP BY`

## Tēmu secība

### 1. Darba plūsmas pārskats un domāšanas modelis
- 4. dienas darba plūsma: `load -> inspect -> clean -> filter -> combine -> summarize -> reshape -> visualize -> export`
- Kāpēc šāda secība ir noderīgāka nekā atsevišķu komandu mācīšanās izolēti
- Īss atgādinājums par `Series`, `DataFrame`, `index`, kolonnām un `dtypes`
- Kāpēc tabulveida darbā parasti priekšroka tiek dota vektorizētām `Pandas` operācijām, nevis manuāliem cikliem

### 2. Datu ielāde no vairākiem avotiem
- `CSV` failu nolasīšana ar `pd.read_csv()`
- `Excel` failu nolasīšana ar `pd.read_excel()`
- Vienas lapas vai vairāku lapu ielāde no viena `Excel` faila ar `sheet_name`
- Īss `JSON` ielādes atkārtojums ar `pd.read_json()` un saikne ar 3. dienu
- Datu nolasīšana no `SQLite` datubāzes ar `pd.read_sql_query()`
- SQL vaicājuma rezultāta izmantošana kā vēl viena `DataFrame` ievade `Pandas` darba plūsmā
- HTML tabulu nolasīšana ar `pd.read_html()`
- Noderīgi parametri:
  - `usecols`
  - `sheet_name`
  - `dtype`
  - `parse_dates`
  - `index_col`
- Īss uzsvars uz to, ka jāielādē tikai vajadzīgās kolonnas, lapas, rindas un tabulas
- Pamatideja:
  - ne visi avoti obligāti jāizmanto tālāk
  - daļa no šiem `DataFrame` objektiem vēlāk tiks apskatīti, attīrīti, filtrēti un apvienoti

### 3. Ielādēto datu apskate
- Ātra apskate ar:
  - `.head()`
  - `.tail()`
  - `.sample()`
  - `.shape`
  - `.columns`
  - `.dtypes`
  - `.info()`
  - `.describe()`
- `.value_counts()` izmantošana ātrai biežumu pārbaudei
- Potenciālo savienojuma atslēgu, datumu lauku, kategorisko un skaitlisko kolonnu atpazīšana
- Agrīno problēmu pamanīšana:
  - trūkstošas vērtības
  - nekonsekventi kolonnu nosaukumi
  - negaidīti datu tipi
  - dublikātu rindas

### 4. Datu tīrīšana un sagatavošana
- Kolonnu nosaukumu standartizēšana
- Kolonnu pārsaukšana
- Trūkstošo vērtību apstrāde ar:
  - `.isna()`
  - `.fillna()`
  - `.dropna()`
- Datu tipu maiņa ar `astype()` un datumu pārvēršana
- Teksta kolonnu tīrīšana ar:
  - `.str.strip()`
  - `.str.lower()`
  - `.str.replace()`
  - `.str.contains()`
- Dublikātu atrašana un noņemšana ar:
  - `.duplicated()`
  - `.drop_duplicates()`
- Aprēķinātu kolonnu veidošana turpmākai analīzei

### 5. Filtrēšana un datu atlase
- Vienas vai vairāku kolonnu atlase
- Rindu atlase ar loģiskām maskām
- `.loc[]` un `.iloc[]` lietošana
- Vairāku nosacījumu veidošana ar `&`, `|` un `~`
- Bieži noderīgas metodes:
  - `.isin()`
  - `.between()`
  - `.str.contains()`
- Rezultātu kārtošana ar `sort_values()`
- SQL līdzīga sintakse ar `query()`
- Pazīstamu SQL ideju pārnešana uz `Pandas`:
  - `SELECT`
  - `WHERE`
  - `ORDER BY`
  - `LIMIT` ar `.head()`

### 6. Vairāku tabulu apvienošana
- Vertikāla salikšana ar `pd.concat()`
- Saistītu tabulu savienošana ar `pd.merge()`
- Savienojumu tipi:
  - `left`
  - `inner`
  - `right`
  - `outer`
- Piemērotu savienojuma atslēgu izvēle
- `merge` rezultātu validēšana, pārbaudot rindu skaitu un nesavienotās vērtības
- Biežākās kļūdas:
  - dublētas atslēgas
  - nesakrītoši kolonnu nosaukumi
  - negaidīta rindu savairošanās
  - pēc savienojuma pazuduši ieraksti

### 7. Grupēšana un kopsavilkumi
- Grupēšana ar `groupby()`
- Biežāk lietotās agregācijas:
  - `count`
  - `sum`
  - `mean`
  - `min`
  - `max`
  - `nunique`
- `.agg()` izmantošana ar vairākām kopsavilkuma funkcijām
- Agregēto rezultātu kārtošana
- Saikne starp grupētiem kopsavilkumiem un Excel PivotTable domāšanu

### 8. Datu formas pārveidošana atskaitēm
- Kad tabulu ir ērtāk analizēt garajā formā un kad platākā formā
- `pivot_table()` kopsavilkuma tabulām
- `pivot()` datu pārkārtošanai, ja vērtības jau ir unikālas
- `melt()` pārejai no wide uz long formu
- Atskaitei gatava rezultāta sagatavošana Excel tipa pārskatiem un diagrammām

### 9. Vizualizācija ar `Pandas` un `matplotlib`
- Ātras diagrammas tieši no `Series` un `DataFrame`
- Biežākie diagrammu tipi:
  - stabiņu diagramma
  - līniju diagramma
  - histogramma
  - izkliedes diagramma
  - box plot
- Diagrammas izvēle atkarībā no analītiskā jautājuma
- Pamata uzlabojumi diagrammām:
  - virsraksti
  - asu nosaukumi
  - attēla izmērs
  - pagriezti kategoriju nosaukumi
- Saprast, kad pietiek ar `Pandas` diagrammu iespējām un kad vairāk kontroles dod `matplotlib`

### 10. Eksports un reproducējamība
- Attīrītu datu eksportēšana ar:
  - `to_csv()`
  - `to_excel()`
  - `to_json()`
- Kopsavilkuma tabulu saglabāšana atskaitēm
- Darba plūsmas reproducējamības uzturēšana piezīmju blokā vai skriptā
- Darba strukturēšana tā, lai ievades, pārveides, kopsavilkuma un izvades soļi būtu skaidri un atkārtojami

## Praktiskā daļa

### Uzdevums 1 — vairāku avotu ielāde un apskate
- Nolasīt vienu `CSV` failu
- Nolasīt `Excel` darbgrāmatu un ielādēt vismaz divas dažādas lapas
- Atkārtoti izmantot vienu `JSON` avotu no 3. dienas un ielādēt to `DataFrame`
- Ielādēt vienu tabulu no `SQLite` datubāzes vaicājuma
- Ielādēt vienu HTML tabulu
- Salīdzināt to struktūru un atrast kolonnas, ko vēlāk varētu izmantot savienošanai
- Apskatīt datu tipus un trūkstošās vērtības

### Uzdevums 2 — tīrīšana un standartizēšana
- Standartizēt kolonnu nosaukumus
- Pārvērst vienu vai vairākas kolonnas skaitliskā vai datetime formātā
- Apstrādāt trūkstošās vērtības un noņemt dublikātus
- Izveidot vienu aprēķinātu kolonnu

### Uzdevums 3 — filtrēšana ar SQL līdzīgu domāšanu
- Atlasīt tikai vajadzīgās kolonnas
- Filtrēt rindas pēc vairākiem nosacījumiem
- Atveidot vienkāršu SQL tipa `WHERE` nosacījumu gan ar loģiskām maskām, gan ar `query()`
- Sakārtot un apskatīt iegūto apakškopu

### Uzdevums 4 — datu kopu apvienošana pēc sagatavošanas
- Izvēlēties daļu no iepriekš ielādētajiem avotiem pēc apskates, tīrīšanas un filtrēšanas
- Apvienot divas saistītas tabulas ar `merge()`
- Salikt kopā divus līdzīgus izgriezumus ar `concat()`
- Pārbaudīt, vai gala rezultātam ir gaidītais rindu skaits

### Uzdevums 5 — grupēti kopsavilkumi un Pivot tipa atskaite
- Izveidot grupētu kopsavilkumu ar `groupby()`
- Izveidot `pivot_table()` kopsavilkumu vadības atskaitei
- Salīdzināt rezultātu ar to, ko parasti veidotu Excel vidē

### Uzdevums 6 — vizualizācija un eksports
- Izveidot vienu diagrammu no kopsavilkuma tabulas
- Eksportēt attīrīto datu kopu un gala kopsavilkumu
- Saglabāt rezultātus tādā formātā, ko vēlāk var izmantot cits kolēģis vai cits skripts

## Ieteicamais laika sadalījums
- 15 min — 3. dienas atkārtojums un 4. dienas darba plūsmas pārskats
- 40 min — `CSV`, vairāku lapu `Excel`, `JSON`, `SQLite` un HTML tabulu nolasīšana ar `Pandas`
- 20 min — struktūras, datu tipu un kvalitātes problēmu apskate
- 30 min — tīrīšana, tipu maiņa, trūkstošās vērtības un aprēķinātās kolonnas
- 25 min — filtrēšana, atlase, kārtošana un SQL līdzīgā `query()` sintakse
- 20 min — tabulu apvienošana ar `merge` un `concat`
- 30 min — `groupby()`, `agg()` un `pivot_table()`
- 15 min — datu formas pārveidošana ar `pivot()` un `melt()`
- 20 min — vizualizācija ar `Pandas` un `matplotlib`
- 10 min — eksports, mini pilnā darba plūsma un kopsavilkums

## Dienas rezultāts
Pēc 4. dienas dalībnieki spēj paņemt vairākus neapstrādātus ievades failus, apskatīt to struktūru, attīrīt un standartizēt tos, filtrēt un apvienot datus, izveidot kopsavilkumus un Pivot tipa rezultātus, vizualizēt galvenos secinājumus un eksportēt rezultātus reproducējamā formā. Šajā brīdī `Pandas` kļūst nevis tikai par tabulu bibliotēku, bet par praktisku pilna cikla analīzes darba plūsmu.

## Pāreja uz 5. dienu
5. dienā šīs sagatavotās un kopsavilktās datu kopas var izmantot kā ievadi pamata mašīnmācīšanās darba plūsmām. 4. dienā apgūtā disciplīna par datu tīrīšanu, kolonnu atlasi un uzticamu analīzei gatavu tabulu veidošanu ir būtiska pirms jebkura modelēšanas soļa.
