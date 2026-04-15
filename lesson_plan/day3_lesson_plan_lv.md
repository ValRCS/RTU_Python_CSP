# 3. dienas nodarbības plāns — Pandas pamati un ievads JSON

## Dienas fokuss
3. dienā dalībnieki pāriet no vispārīgas datu tīrīšanas uz strukturētu datu apstrādi ar `Pandas`. Galvenais uzsvars ir uz `DataFrame` izmantošanu ikdienas analīzes uzdevumos, kas bieži tiek veikti Excel vidē. Dienas otrajā daļā tiek ieviests pamata darbs ar `JSON`, lai parādītu, kā no pusstrukturētiem datiem nonākt līdz tabulveida analīzei.

## Mērķi
- Saprast, kas ir ārējās bibliotēkas un kāpēc datu darbā izmanto `Pandas`
- Iepazīt `Series` un `DataFrame` pamatstruktūras
- Nolasīt datus no `CSV` un vienkārša `JSON`
- Veikt `filtering`, `selection`, `sorting`, `grouping` un `aggregation`
- Savienot vairākas datu kopas ar `merge` un `concat`
- Parādīt, kā tipiskas Excel darbības tiek aizstātas ar `Pandas` pieeju

## Priekšzināšanas
- Python pamati no 1. dienas
- Failu nolasīšana, virkņu apstrāde un datu tīrīšana no 2. dienas
- Izpratne par tabulas struktūru: rindas, kolonnas, virsraksti

## Tēmu secība

### 1. Ievads ārējās bibliotēkās
- Kas ir ārējā bibliotēka un ar ko tā atšķiras no standarta bibliotēkas
- `import pandas as pd`
- Īss atgādinājums par `pip install`
- Kāpēc `Pandas` ir noderīgs statistikas un biroja datu darba plūsmās

### 2. Pirmā iepazīšanās ar `DataFrame`
- Kas ir `Series`
- Kas ir `DataFrame`
- Rindas, kolonnas un `index`
- Datu apskate ar:
  - `.head()`
  - `.shape`
  - `.columns`
  - `.dtypes`
  - `.info()`

### 3. Datu ielāde `Pandas`
- `CSV` faila nolasīšana ar `pd.read_csv()`
- `DataFrame` izveide no Python sarakstiem un vārdnīcām
- Atšķirība starp strukturētiem un pusstrukturētiem datiem

### 4. Kolonnu un rindu atlase
- Vienas kolonnas atlase
- Vairāku kolonnu atlase
- Rindu atlase pēc nosacījuma
- Biežākie salīdzinājumi un loģiskie operatori
- Vienkārša darbs ar trūkstošām vērtībām

### 5. Datu pārveidošana
- Kolonnu pārdēvēšana
- Jaunas kolonnas izveide
- Datu tipu maiņa
- Vienkāršas teksta operācijas kolonnās
- Sagatavošana turpmākai analīzei

### 6. Kārtošana, grupēšana un apkopošana
- `sort_values()`
- `groupby()`
- Biežākās `aggregation` darbības:
  - `count`
  - `sum`
  - `mean`
  - `min`
  - `max`
- Rezultātu interpretācija un saistība ar tipiskām Excel PivotTable darbībām

### 7. Datu kopu apvienošana
- Vertikāla apvienošana ar `concat`
- Savienošana pēc atslēgas ar `merge`
- Vienkārši piemēri ar divām tabulām
- Biežākās kļūdas: nesakrītoši kolonnu nosaukumi, trūkstošas atslēgas, dublikāti

### 8. Ievads `JSON`
- Kas ir `JSON` un kur tas parādās reālās darba plūsmās
- `JSON` kā ligzdota datu struktūra
- Vienkārša `JSON` nolasīšana Python vidē
- Pārvēršana no `list of dicts` uz `DataFrame`
- Kad `JSON` ir ērts datu apmaiņai un kad labāk izmantot `CSV`

### 9. Eksportēšana
- Rezultāta saglabāšana `CSV`
- Pamata eksportēšana uz `JSON`
- Īss uzsvars uz reproducējamību: no ievades faila līdz gatavam rezultātam ar skriptu vai notebook

## Praktiskā daļa

### Uzdevums 1 — pirmā analīze ar `Pandas`
- Nolasīt `CSV` failu
- Apskatīt datu struktūru
- Identificēt svarīgākās kolonnas

### Uzdevums 2 — Excel darbību atveidošana
- Atlasīt tikai vajadzīgās rindas un kolonnas
- Sakārtot datus pēc izvēlēta lauka
- Izveidot jaunu aprēķinātu kolonnu

### Uzdevums 3 — grupēšana un kopsavilkums
- Sagrupēt datus pēc kategorijas
- Aprēķināt biežumu vai vidējo vērtību
- Interpretēt iegūto kopsavilkumu

### Uzdevums 4 — datu kopu savienošana
- Apvienot divas tabulas pēc kopīgas atslēgas
- Pārbaudīt, vai visas rindas ir savienojušās korekti

### Uzdevums 5 — pamata darbs ar `JSON`
- Nolasīt vienkāršu `JSON` failu
- Pārveidot to par `DataFrame`
- Salīdzināt, kā atšķiras `CSV` un `JSON` ievade

## Ieteicamais laika sadalījums
- 15 min — atkārtojums no 2. dienas un ievads `Pandas`
- 35 min — `DataFrame` pamati un datu ielāde
- 40 min — `filtering`, `selection` un datu pārveidošana
- 35 min — `sorting`, `grouping` un `aggregation`
- 25 min — `merge`, `concat` un darbs ar vairākām tabulām
- 30 min — ievads `JSON` un pāreja uz `DataFrame`
- 30 min — praktiskie uzdevumi un diskusija

## Dienas rezultāts
Pēc 3. dienas dalībnieki spēj nolasīt tabulveida datus `Pandas` vidē, atlasīt un pārveidot kolonnas un rindas, veidot vienkāršus kopsavilkumus, apvienot datu kopas un ielasīt pamata `JSON` datus turpmākai analīzei.

## Pāreja uz 4. dienu
4. dienā šo pamatu var paplašināt ar vairākiem datu avotiem, `Excel` failiem, sarežģītāku `JSON`, pamata `SQL` integrāciju un vizualizāciju ar `matplotlib`.
