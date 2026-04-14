# Mācību ceļvedis: 2. diena Teksta apstrāde un tīrīšana

Šis ceļvedis atbilst 2. dienas plānam failā `lesson_plan/README_LV.md`, 2. dienas piezīmju blokam failā `notebooks/python_intermediate_text_processing.ipynb` un paraugfailiem mapē `data/day2/`.

Saites šajā ceļvedī tika pārbaudītas 2026. gada 14. aprīlī.

## 2. dienas mērķi

Līdz 2. dienas beigām dalībniekiem vajadzētu spēt:

- nolasīt teksta un CSV tipa datus no failiem
- atpazīt un apstrādāt biežākās kodējuma problēmas
- notīrīt virknes tā, lai tās kļūtu lietojamākas
- izmantot regulārās izteiksmes vienkāršai paraugu meklēšanai
- izveidot nelielu, atkārtojamu tīrīšanas plūsmu

## 1. Teksta apstrādes darba plūsma

Praktiska teksta tīrīšanas darba plūsma parasti izskatās šādi:

1. Nolasīt neapstrādāto ievadi.
2. Normalizēt rindu beigas un atstarpes.
3. Izņemt vai salabot nederīgās vērtības.
4. Standartizēt teksta formātu.
5. Izdalīt noderīgās daļas.
6. Saglabāt notīrīto izvadi.

Šis modelis ir svarīgāks par jebkuru vienu funkciju. Kursā tas atkārtojas vairākkārt.

Ja terminu nav jēgpilni vai ērti pārtulkot, lietojam angļu terminu ar piezīmi. Piemēram, `pipeline` šeit nozīmē datu apstrādes plūsmu vai konveijeru.

## 2. Droša failu nolasīšana

Visbiežāk lietotais raksts ir `with open(...)`, jo tas automātiski aizver failu.

```python
with open("data/day2/responses_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

Lai nolasītu rindas:

```python
with open("data/day2/responses_raw.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
```

Kāpēc `encoding="utf-8"` ir svarīgs:

- tas skaidri nosaka sagaidāmo kodējumu
- tas novērš paļaušanos uz platformas noklusējuma iestatījumiem
- tas samazina neskaidrības, ja faili tiek pārvietoti starp sistēmām

## 3. Kodējuma problēmas

Tipiskas nepareizas dekodēšanas pazīmes:

- vārdos parādās negaidīti lieki simboli
- viena burta vietā redzami divi vai vairāki simboli
- teksts vienā programmā izskatās pareizi, bet citā ir bojāts

Šādas pazīmes parasti nozīmē, ka baitiem ticis piemērots nepareizs kodējums.

Praktisks noteikums šim kursam:

- ja teksta fails saglabāts UTF-8, to vajag atvērt ar `encoding="utf-8"`

Ja teksts jau izskatās bojāts, pārbaudiet:

- kādā kodējumā fails tika saglabāts
- kādu kodējumu Python izmantoja atvēršanai
- vai iepriekšējā sistēma datus neeksportēja nekorekti

## 4. Pamatmetodes virkņu tīrīšanai

Ar vienkāršām virkņu metodēm jāsāk pirms tiek izmantots `regex`.

Termins `regex` šeit atstāts angliski ar piezīmi, jo tas ir plaši lietots tehniskais saīsinājums un nozīmē regulārās izteiksmes.

```python
line = "  Python, Excel, and CSV files!  "

cleaned = line.strip()
lowered = cleaned.lower()
replaced = lowered.replace("csv", "comma-separated values")
parts = replaced.split(",")
```

Noderīgas virkņu metodes 2. dienai:

- `strip()`
- `lower()`
- `upper()`
- `replace()`
- `split()`
- `splitlines()`
- `startswith()`
- `endswith()`

Ar tām bieži pietiek, lai:

- nogrieztu liekās atstarpes
- normalizētu burtu reģistru
- standartizētu atkārtojošās vērtības
- sadalītu rindu daļās

## 5. Saraksti, vārdnīcas, kopas un tuples teksta darbā

2. dienas piezīmju bloks iet tālāk par parastām virknēm, jo teksta tīrīšanā bieži vajag vairākas pamatdatu struktūras.

### Saraksti

Sarakstus izmanto sakārtotām rindu vai tokenu kolekcijām. Termins `token` te nozīmē atsevišķu teksta vienību, parasti vārdu.

```python
cleaned_lines = []

for line in lines:
    line = line.strip()
    if line:
        cleaned_lines.append(line)
```

### Vārdnīcas

Vārdnīcas izmanto skaitīšanai un grupētiem rezultātiem.

```python
counts = {}

for word in ["python", "data", "python"]:
    counts[word] = counts.get(word, 0) + 1
```

### Kopas

Kopas izmanto unikālām vērtībām un ātrai piederības pārbaudei.

```python
stopwords = {"un", "ar", "bet"}
unique_words = set(["python", "data", "python"])
```

Termins `stopwords` šeit lietots angliski ar piezīmi, jo datu apstrādē tas ir standarta apzīmējums. Tas nozīmē stopvārdus.

### Tuples

Tuples izmanto mazām, fiksētām datu vienībām, piemēram, `(word, count)`.

```python
pair = ("python", 3)
```

## 6. Pamata regulārās izteiksmes

Regulārās izteiksmes palīdz gadījumos, kad ar parastām virkņu metodēm nepietiek.

Piemērs: noņemt ciparus.

```python
import re

text = "report_2026_version_2"
result = re.sub(r"\d+", "", text)
print(result)
```

Piemērs: atstāt tikai burtus un atstarpes.

```python
import re

line = "Python 3.14 is useful!"
clean = re.sub(r"[^A-Za-z ]+", "", line)
print(clean)
```

Svarīgas 2. dienas `regex` idejas:

- `\d` atbilst ciparam
- `\s` atbilst tukšumzīmei
- `+` nozīmē viena vai vairākas reizes
- `[]` definē simbolu klasi
- `^` iekš `[]` nozīmē "ne šie simboli"
- regulārajām izteiksmēm parasti izmanto neapstrādātās virknes, piemēram, `r"\d+"`

`Regex` jālieto tad, kad vajag paraugus. To nevajag izmantot katrai virkņu problēmai.

## 7. Tīrīšanas funkcijas veidošana

Tīrīšanas plūsmu ir vieglāk testēt un atkārtoti izmantot, ja tā ir ievietota funkcijā.

```python
import re

def clean_line(line):
    line = line.strip().lower()
    line = re.sub(r"\d+", "", line)
    line = re.sub(r"\s+", " ", line)
    return line
```

Ieguvumi:

- viena vieta, kur uzturēt loģiku
- vieglāka testēšana
- vieglāka atkārtota izmantošana vairākos failos

## 8. Comprehensions un ģeneratori

2. dienas piezīmju blokā tiek ieviesti īsāki datu pārveidošanas paņēmieni.

### Saraksta comprehension

Termins `comprehension` šeit atstāts angliski ar piezīmi, jo latviski nav vienas īsas un vispārpieņemtas tehniskas formas. Tas nozīmē īsu konstrukciju kolekcijas izveidei vai pārveidei.

```python
cleaned_lines = [line.strip() for line in lines if line.strip()]
```

### Ģeneratora izteiksme

```python
words = (word for line in cleaned_lines for word in line.split())
```

Kāpēc tas ir svarīgi:

- `comprehensions` ir īsas un labi lasāmas vienkāršām pārveidēm
- ģeneratori palīdz apstrādāt elementus pa vienam, neveidojot lielus starprezultātu sarakstus

## 9. Vārdu biežumi

Vārdu skaitīšana ir viens no biežākajiem pirmajiem teksta analīzes uzdevumiem.

```python
counts = {}

for line in cleaned_lines:
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1

top_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
print(top_items[:5])
```

Šeit vienlaikus tiek apvienoti vairāki 2. dienas jēdzieni:

- failu nolasīšana
- virkņu sadalīšana
- cikli
- vārdnīcas
- kārtošana

## 10. Notīrīto rezultātu saglabāšana

Notīrīto izvadi vajag skaidri ierakstīt atpakaļ failā.

```python
with open("data/day2/cleaned_responses.txt", "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")
```

Tas palīdz uzturēt reproducējamu darba plūsmu:

- neapstrādātie dati paliek atsevišķi
- notīrītos datus var ģenerēt no jauna
- izvades failus ir viegli pārskatīt

## 11. CSV izpratne

2. dienā tiek apskatīta darbība ar `.txt` un `.csv` failiem.

Ja dati tiešām ir CSV formātā, labāk izmantot Python `csv` moduli, nevis manuāli dalīt virknes, kad:

- vērtībās var būt komati
- svarīgi ir pēdiņu jeb quoting noteikumi
- rindas vajag nolasīt vai ierakstīt strukturēti

Piemērs:

```python
import csv

with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## 12. Biežākie tīrīšanas lēmumi

Pirms tīrīšanas jāizlemj:

- kuras rindas jāizmet pilnībā
- kuras trūkstošās vērtības ir pieļaujamas
- vai teksts jāpārvērš mazajos burtos
- vai pieturzīmes jāsaglabā
- vai skaitļi ir nozīmīgi vai ir tikai troksnis
- kā rīkoties ar dublikātiem

Tie ir datu lēmumi, ne tikai koda lēmumi.

## 13. Tipiskās 2. dienas kļūdas

Biežākās kļūdas:

- aizmirsts `encoding="utf-8"`
- `regex` izmantots tur, kur pietiktu ar `strip()` vai `replace()`
- CSV dati sadalīti ar parastu `split(",")`, lai gan var būt pēdiņas un komati vērtībās
- tīrīšanas laikā nejauši izdzēstas noderīgas rakstzīmes
- neapstrādātie un notīrītie dati sajaukti vienā failā

## 14. Saikne ar pārējo kursu

2. diena veido priekšapstrādes domāšanu, kas vēlāk vajadzīga:

- tabulveida datu tīrīšanai Pandas vidē
- kolonnu standartizēšanai pirms analīzes
- modeļiem sagatavotas ievades datu izveidei vēlākajos mašīnmācīšanās piemēros

## Ieteicamā prakse

- notīrīt `data/day2/responses_raw.txt` līdz ne-tukšu, normalizētu rindu sarakstam
- saskaitīt piecus biežākos vārdus pēc tīrīšanas
- salīdzināt sākotnējo un notīrīto izvadi
- izmēģināt divus `regex` paraugus un precīzi paskaidrot, ko katrs atrod

## Kursa faili

- 2. dienas plāns: `lesson_plan/README_LV.md`
- 2. dienas piezīmju bloks: `notebooks/python_intermediate_text_processing.ipynb`
- neapstrādāto datu piemērs: `data/day2/responses_raw.txt`
- notīrīto datu piemērs: `data/day2/cleaned_responses.txt`
- stopvārdi: `data/day2/stopwords_lv.txt`
- vārdu biežumi: `data/day2/word_frequencies.txt`

## Autoritatīvas atsauces

- Python ievades un izvades apmācība: <https://docs.python.org/3/tutorial/inputoutput.html>
- Iebūvētās `open()` funkcijas dokumentācija: <https://docs.python.org/3/library/functions.html#open>
- Virkņu metodes (`str`): <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>
- `re` regulāro izteiksmju modulis: <https://docs.python.org/3/library/re.html>
- Regular Expression HOWTO: <https://docs.python.org/3/howto/regex.html>
- Unicode HOWTO: <https://docs.python.org/3/howto/unicode.html>
- `csv` modulis: <https://docs.python.org/3/library/csv.html>
