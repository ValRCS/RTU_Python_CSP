# 3. dienas nodarbības plāns — JSON pamati un Pandas ievads

## Dienas fokuss
3. dienā dalībnieki sāk ar pamata darbu ar `JSON`, izmantojot Python standarta bibliotēku, un pēc tam pāriet uz strukturētu datu apstrādi ar `Pandas`. Šāda secība ļauj vispirms saprast pusstrukturētus datus un tikai pēc tam parādīt, kā tos pārvērst `DataFrame` formā turpmākai analīzei un Excel tipa darba plūsmām.

## Mērķi
- Saprast, kā nolasīt un interpretēt vienkāršu `JSON` bez ārējām bibliotēkām
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

### 1. Ievads `JSON`
- Kas ir `JSON` un kur tas parādās reālās darba plūsmās
- `JSON` kā ligzdota datu struktūra
- Darbs ar Python `json` moduli
- Vienkārša `JSON` nolasīšana Python vidē
- Atšķirība starp `JSON`, `CSV` un Python vārdnīcām/sarakstiem

### 2. Pāreja no `JSON` uz tabulveida datiem
- Kad `JSON` var analizēt tieši Python struktūrās
- Kad ērtāk to pārvērst par `DataFrame`
- Pārvēršana no `list of dicts` uz tabulveida datiem
- Ierobežojumi: ligzdotas struktūras, nevienmērīgi lauki, trūkstošas atslēgas

### 3. Ievads ārējās bibliotēkās
- Kas ir ārējā bibliotēka un ar ko tā atšķiras no standarta bibliotēkas
- `import pandas as pd`
- Īss atgādinājums par `pip install`
- Kāpēc `Pandas` ir noderīgs statistikas un biroja datu darba plūsmās

### 4. Pirmā iepazīšanās ar `DataFrame`
- Kas ir `Series`
- Kas ir `DataFrame`
- Rindas, kolonnas un `index`
- Datu apskate ar:
  - `.head()`
  - `.shape`
  - `.columns`
  - `.dtypes`
  - `.info()`

### 5. Datu ielāde `Pandas`
- `CSV` faila nolasīšana ar `pd.read_csv()`
- `DataFrame` izveide no Python sarakstiem un vārdnīcām
- Atšķirība starp strukturētiem un pusstrukturētiem datiem

### 6. Kolonnu un rindu atlase
- Vienas kolonnas atlase
- Vairāku kolonnu atlase
- Rindu atlase pēc nosacījuma
- Biežākie salīdzinājumi un loģiskie operatori
- Vienkārša darbs ar trūkstošām vērtībām

### 7. Datu pārveidošana
- Kolonnu pārdēvēšana
- Jaunas kolonnas izveide
- Datu tipu maiņa
- Vienkāršas teksta operācijas kolonnās
- Sagatavošana turpmākai analīzei

### 8. Kārtošana, grupēšana un apkopošana
- `sort_values()`
- `groupby()`
- Biežākās `aggregation` darbības:
  - `count`
  - `sum`
  - `mean`
  - `min`
  - `max`
- Rezultātu interpretācija un saistība ar tipiskām Excel PivotTable darbībām

### 9. Datu kopu apvienošana
- Vertikāla apvienošana ar `concat`
- Savienošana pēc atslēgas ar `merge`
- Vienkārši piemēri ar divām tabulām
- Biežākās kļūdas: nesakrītoši kolonnu nosaukumi, trūkstošas atslēgas, dublikāti

### 10. Eksportēšana
- Rezultāta saglabāšana `CSV`
- Pamata eksportēšana uz `JSON`
- Īss uzsvars uz reproducējamību: no ievades faila līdz gatavam rezultātam ar skriptu vai notebook

## Praktiskā daļa

### Uzdevums 1 — pamata darbs ar `JSON`
- Nolasīt vienkāršu `JSON` failu
- Apskatīt tā struktūru Python vidē
- Saprast, kuras daļas ir gatavas pārvēršanai tabulā

### Uzdevums 2 — pirmā analīze ar `Pandas`
- Pārvērst vienkāršu `JSON` vai nolasīt `CSV` failu kā `DataFrame`
- Apskatīt datu struktūru
- Identificēt svarīgākās kolonnas

### Uzdevums 3 — Excel darbību atveidošana
- Atlasīt tikai vajadzīgās rindas un kolonnas
- Sakārtot datus pēc izvēlēta lauka
- Izveidot jaunu aprēķinātu kolonnu

### Uzdevums 4 — grupēšana un kopsavilkums
- Sagrupēt datus pēc kategorijas
- Aprēķināt biežumu vai vidējo vērtību
- Interpretēt iegūto kopsavilkumu

### Uzdevums 5 — datu kopu savienošana
- Apvienot divas tabulas pēc kopīgas atslēgas
- Pārbaudīt, vai visas rindas ir savienojušās korekti

### Uzdevums 6 — `JSON` un `CSV` salīdzinājums
- Salīdzināt, kā atšķiras `CSV` un `JSON` ievade
- Izvērtēt, kurš formāts ir ērtāks konkrētam uzdevumam
- Pārvērst `JSON` datus par `DataFrame` turpmākai analīzei

## Ieteicamais laika sadalījums
- 20 min — atkārtojums no 2. dienas un ievads `JSON`
- 25 min — Python `json` modulis un `JSON` struktūras apskate
- 25 min — pāreja no `JSON` uz `DataFrame` un ievads `Pandas`
- 35 min — `DataFrame` pamati un datu ielāde
- 35 min — `filtering`, `selection` un datu pārveidošana
- 30 min — `sorting`, `grouping` un `aggregation`
- 20 min — `merge`, `concat` un darbs ar vairākām tabulām
- 30 min — praktiskie uzdevumi un diskusija

## Dienas rezultāts
Pēc 3. dienas dalībnieki spēj nolasīt pamata `JSON` datus ar Python standarta bibliotēku, saprast, kad tos ir vērts pārvērst tabulveida struktūrā, un pēc tam izmantot `Pandas`, lai atlasītu un pārveidotu kolonnas un rindas, veidotu kopsavilkumus un apvienotu datu kopas.

## Pāreja uz 4. dienu
4. dienā šo pamatu var paplašināt ar vairākiem datu avotiem, `Excel` failiem, sarežģītāku `JSON`, pamata `SQL` integrāciju un vizualizāciju ar `matplotlib`.
