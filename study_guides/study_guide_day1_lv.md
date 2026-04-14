# Mācību ceļvedis: 1. diena Pamati un uzstādīšana

Šis ceļvedis atbilst 1. dienas plānam failā `lesson_plan/README_LV.md`, 1. dienas piezīmju blokam failā `notebooks/python_basics.ipynb` un uzstādīšanas norādēm failā `python_vscode_setup/README.md`.

Saites šajā ceļvedī tika pārbaudītas 2026. gada 14. aprīlī.

## 1. dienas mērķi

Līdz 1. dienas beigām dalībniekiem vajadzētu spēt:

- izskaidrot, kur Python iederas mūsdienu datu darba plūsmās
- uzstādīt lokālu Python vidi VS Code
- saprast atšķirību starp `.py` skriptiem un Jupyter piezīmju blokiem
- uzrakstīt nelielas Python programmas ar mainīgajiem, tipiem, nosacījumiem, cikliem, sarakstiem un virknēm

## 1. Python datu darba plūsmās

Šajā kursā Python galvenokārt tiek izmantots kā praktisks rīks:

- datu nolasīšanai un pārveidošanai
- atkārtotu uzdevumu automatizācijai
- analīzes soļu reproducējamībai
- pārejai no manuāla darba izklājlapās uz atkārtoti lietojamu kodu

Tipiska darba plūsma:

1. Nolasīt ievades datus.
2. Tos notīrīt vai pārveidot.
3. Pārbaudīt rezultātu.
4. Saglabāt izvadi turpmākai analīzei vai atskaitēm.

Ja angļu termins ir noderīgāks nekā tiešs tulkojums, to saglabājam ar piezīmi. Piemēram, `workflow` nozīmē darba plūsmu.

## 2. Lokālās vides uzstādīšana

Kurss izmanto lokālu darba vidi, lai dalībnieki varētu atkārtoti palaist to pašu kodu savā datorā.

Galvenie rīki:

- Python
- VS Code
- Python paplašinājums VS Code vidē
- Jupyter paplašinājums VS Code vidē
- projekta virtuālā vide (`.venv`)

### Kāpēc izmantot virtuālo vidi

Virtuālā vide izolē konkrētā projekta bibliotēkas no pārējās sistēmas. Tas padara vidi reproducējamāku un samazina versiju konfliktus.

### Biežāk izmantotās uzstādīšanas komandas

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS vai Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

VS Code vidē izvēlētajam Python `interpreter` lietojam angļu nosaukumu ar piezīmi, jo tas ir konkrēts VS Code un Python rīka apzīmējums. Tam jānorāda uz projektā izveidoto `.venv`.

## 3. Skripti pret piezīmju blokiem

### `.py` skripti

Vispiemērotākie:

- atkārtojamiem uzdevumiem
- produkcijai tuvām darba plūsmām
- automatizācijai
- kodam, kam jāizpildās no sākuma līdz beigām vienā piegājienā

Piemērs:

```python
name = "Anna"
print(f"Hello, {name}")
```

### Jupyter piezīmju bloki

Vispiemērotākie:

- soli pa solim izpētei
- mācīšanai un demonstrācijām
- situācijām, kur vienkopus vajag kodu, izvadi un piezīmes
- interaktīvai ideju pārbaudei

Svarīgs ieradums piezīmju blokos:

- izpildīt šūnas no augšas uz leju, lai mainīgie un rezultāti būtu konsekventi

Termins `notebook` šeit nozīmē Jupyter piezīmju bloku.

## 4. Mainīgie un pamatdatu tipi

Mainīgais glabā vērtību zem konkrēta nosaukuma.

```python
name = "Anna"
age = 32
height = 1.68
is_active = True
```

Biežāk izmantotie iebūvētie tipi 1. dienā:

- `str`: teksts
- `int`: vesels skaitlis
- `float`: decimālskaitlis
- `bool`: `True` vai `False`

Vērtības tipu var pārbaudīt ar:

```python
print(type(name))
```

## 5. Pamatoperācijas un tipu pārveidošana

Python ļauj veikt aprēķinus ar skaitļiem un salīdzināt vērtības.

```python
a = 10
b = 3

print(a + b)
print(a / b)
print(a > b)
print(a == b)
```

Tipu pārveidošana ir bieži vajadzīga, ja dati sākotnēji ir teksts.

```python
text_number = "45"
number = int(text_number)
price = float("12.50")
label = str(99)
```

Tipu pārveidošana jālieto uzmanīgi. `int("abc")` izraisīs kļūdu, jo šis teksts nav derīgs vesels skaitlis.

## 6. Ievade, izvade un virknes

### Izvade ar `print()`

```python
print("Python works")
```

### Ievade ar `input()`

`input()` vienmēr atgriež tekstu.

```python
name = input("Ievadiet savu vārdu: ")
age = int(input("Ievadiet savu vecumu: "))
print(name, age)
```

### Biežākās virkņu darbības

```python
text = "  Data Processing with Python  "

print(text.strip())
print(text.lower())
print(text.upper())
print(len(text))
print(text.replace("Python", "VS Code"))
```

Šīs metodes tiek nepārtraukti lietotas tīrīšanas un validācijas uzdevumos.

## 7. Nosacījumi

Nosacījumi ļauj kodam zaroties.

```python
score = 78

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Review needed")
```

Svarīga sintakses prasība:

- Python izmanto atkāpes kā valodas daļu

## 8. Cikli

### `for` cikls

`for` izmanto tad, ja jāapstrādā elementi no kolekcijas.

```python
cities = ["Riga", "Liepaja", "Cesis"]

for city in cities:
    print(city)
```

### `while` cikls

`while` izmanto tad, ja atkārtošanās ir atkarīga no nosacījuma.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

## 9. Saraksti

Saraksti glabā sakārtotas vērtību kolekcijas.

```python
numbers = [10, 20, 30]

print(numbers[0])
numbers.append(40)
print(numbers)
```

Sarakstu prasmes, kas ir svarīgas jau sākumā:

- elementu iegūšana pēc indeksa
- iterēšana cauri vērtībām
- jaunu vērtību pievienošana
- pārveidotu sarakstu veidošana

Piemērs:

```python
values = [1, 2, 3, 4]
squared = []

for value in values:
    squared.append(value * value)

print(squared)
```

## 10. Funkcijas

Funkcijas padara kodu atkārtoti lietojamu un vieglāk lasāmu.

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Anna"))
```

1. dienā svarīga ir pamatideja:

- definēt funkciju ar `def`
- padot ievades vērtības kā parametrus
- atgriezt rezultātu ar `return`

## 11. Tipiskās iesācēju kļūdas

Biežākās 1. dienas kļūdas:

- aizmirstas pēdiņas ap tekstu
- sajaukti teksti un skaitļi bez tipu pārveidošanas
- aizmirsts kols aiz `if`, `for`, `while` vai `def`
- nepareizas atkāpes
- mainīgais izmantots pirms tam piešķirta vērtība

Tas viss ir normāli. Svarīgākais ieradums ir izlasīt kļūdas ziņojumu un pārbaudīt tieši to rindu, uz kuru tas norāda.

## 12. Saikne ar pārējo kursu

1. diena izveido pamata ieradumus, kas vajadzīgi tālāk:

- 2. dienā virknes, cikli, saraksti un funkcijas tiek lietotas teksta tīrīšanai
- 3. un 4. dienā tā pati loģika tiek piemērota tabulveida datiem Pandas vidē
- reproducējama lokālā vide kļūst īpaši svarīga, kad projektā ir vairāk failu un bibliotēku

## Ieteicamā prakse

- izveidot skriptu, kas prasa lietotāja vārdu un nodaļu, pēc tam izdrukā noformatētu sveicienu
- uzrakstīt ciklu, kas atlasītu skaitļus, kuri ir lielāki par `10`
- notīrīt teksta vērtību ar `strip()`, `lower()` un `replace()`
- izveidot pārveidotu vērtību sarakstu no cita saraksta

## Kursa faili

- 1. dienas plāns: `lesson_plan/README_LV.md`
- 1. dienas piezīmju bloks: `notebooks/python_basics.ipynb`
- lokālās vides uzstādīšanas norādes: `python_vscode_setup/README.md`
- ievada skriptu piemēri: `scripts/python_basics.py`

## Autoritatīvas atsauces

- Python apmācības pārskats: <https://docs.python.org/3/tutorial/>
- Neformāls ievads Python: <https://docs.python.org/3/tutorial/introduction.html>
- Vadības plūsmas rīki: <https://docs.python.org/3/tutorial/controlflow.html>
- Datu struktūras: <https://docs.python.org/3/tutorial/datastructures.html>
- Iebūvētie tipi: <https://docs.python.org/3/library/stdtypes.html>
- Iebūvētās funkcijas: <https://docs.python.org/3/library/functions.html>
- `venv` virtuālās vides: <https://docs.python.org/3/library/venv.html>
- Python VS Code vidē: <https://code.visualstudio.com/docs/languages/python>
- Jupyter darba sākšana: <https://docs.jupyter.org/en/stable/start/index.html>
