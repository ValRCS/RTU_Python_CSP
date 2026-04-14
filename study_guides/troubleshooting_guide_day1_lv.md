# Problēmu novēršanas ceļvedis: 1. diena Pamati un uzstādīšana

Šis ceļvedis paredzēts 1. dienas materiāliem:

- `lesson_plan/README.md`
- `study_guides/study_guide_day1.md`
- `notebooks/python_basics.ipynb`
- `python_vscode_setup/README.md`

Saites šajā ceļvedī tika pārbaudītas 2026. gada 14. aprīlī.

## Ko aptver šis ceļvedis

1. dienas problēmas parasti iedalās četrās grupās:

1. Kods nav derīgs Python.
2. Kods ir derīgs, bet izpildes laikā rodas kļūda.
3. VS Code vai Jupyter izmanto nepareizo vidi.
4. Piezīmju bloks ir nonācis neparedzētā stāvoklī agrāk palaistu šūnu, `input()` vai pārtrauktas izpildes dēļ.

Ātrākais veids, kā atgūties, ir vispirms noteikt, kurā grupā problēma ietilpst, nevis haotiski mainīt visu pēc kārtas.

## Ātrā sākotnējā pārbaude

Kad kaut kas nestrādā, pārbaudiet šo secībā:

1. Izlasiet kļūdas ziņojuma pēdējo rindu. Tajā parasti ir nosaukta pati problēma, piemēram, `SyntaxError`, `NameError` vai `TypeError`.
2. Pārbaudiet faila vai šūnas numuru un rindas numuru.
3. Ja strādājat piezīmju blokā, pārbaudiet, vai vajadzīgās iepriekšējās šūnas tiešām tika palaistas.
4. Ja neizdodas importi vai pakotnes, pārbaudiet pareizo VS Code `interpreter` vai piezīmju bloka `kernel`.
5. Ja šūna izskatās iestrēgusi, pārbaudiet, vai tā negaida `input()` vai arī `kernel` joprojām nav aizņemts.
6. Mainiet vienu lietu vienlaikus un palaidiet vēlreiz.

## Kā lasīt Python kļūdu

Python kļūdā parasti ir trīs noderīgas daļas:

- atrašanās vieta
- `traceback` jeb izsaukumu ķēde ar kontekstu
- izņēmuma tips un ziņojums

Piemērs:

```python
age = int("abc")
```

Tipisks rezultāts:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

Kā to interpretēt:

- `ValueError` nozīmē, ka darbība ir pareiza, bet konkrētā vērtība nav pieņemama.
- `int("abc")` neizdevās, jo `"abc"` nav derīgs vesels skaitlis.

Sintakses kļūdās Python bieži norāda vietu, kur problēmu pamanīja, ne vienmēr vietu, kur tā sākās. Piemēram, trūkstošs kols var tikt atklāts tikai pie nākamā elementa.

## Biežākās 1. dienas kļūdas

### `SyntaxError`

Ko tas nozīmē:

- Python vispār nevarēja izparsēt kodu.

Biežākie cēloņi:

- trūkst kola aiz `if`, `for`, `while` vai `def`
- trūkst pēdiņu vai tās nesakrīt
- trūkst aizverošās iekavas
- izmantots `=` tur, kur bija domāts `==`
- `Code` šūnā ierakstīts parasts teksts, nevis Python kods

Piemērs:

```python
if age > 18
    print("Adult")
```

Kā labot:

- pārbaudiet rindu, ko norāda Python
- pārbaudiet arī rindu tieši virs tās
- pārbaudiet kolus, iekavas, komatus un pēdiņas

Noderīgs ieradums:

- ja redzat `SyntaxError`, vispirms salabojiet koda struktūru un tikai pēc tam domājiet par loģiku

### `IndentationError`

Ko tas nozīmē:

- Python gaidīja pareizi atkāpinātu bloku, bet to nesaņēma.

Biežākie cēloņi:

- aizmirsts atkāpināt kodu `if`, `for`, `while` vai `def` blokā
- viena rinda atkāpināta par maz vai par daudz

Piemērs:

```python
if age > 18:
print("Adult")
```

Labojums:

- konsekventi atkāpiniet bloka saturu, parasti ar 4 atstarpēm

Pareiza versija:

```python
if age > 18:
    print("Adult")
```

### `TabError`

Ko tas nozīmē:

- atkāpēs ir sajaukti tabulatori un atstarpes.

Labojums:

- izmantojiet tikai atstarpes
- ja vajag, VS Code apakšējā statusa joslā pārslēdziet atkāpju veidu

Ar šo kļūdu saskaras arī pieredzējuši lietotāji, īpaši pēc koda ielīmēšanas no dažādiem avotiem.

### `NameError`

Ko tas nozīmē:

- jūs izmantojāt mainīgo vai funkcijas nosaukumu, kas pašreizējā stāvoklī neeksistē.

Biežākie cēloņi:

- drukas kļūda nosaukumā
- mēģinājums izmantot mainīgo pirms tas definēts
- piezīmju bloka šūna ar definīciju nav palaista
- `kernel` tika pārstartēts un mainīgie tika notīrīti

Piemērs:

```python
print(total_amount)
```

Labojums:

- pārbaudiet rakstību simbolu pa simbolam
- definējiet mainīgo pirms izmantošanas
- piezīmju blokos vēlreiz palaidiet agrākās sagatavošanas šūnas

### `TypeError`

Ko tas nozīmē:

- darbība nav derīga dotajiem datu tipiem.

Biežākie cēloņi:

- teksts tiek tieši saskaitīts ar skaitli
- tiek izsaukts objekts, kas nav funkcija
- tiek indeksēta vērtība, kas nav secība

Piemērs:

```python
"Age: " + 25
```

Labojums:

- pārveidojiet tipus apzināti

Pareiza versija:

```python
"Age: " + str(25)
```

### `ValueError`

Ko tas nozīmē:

- tips ir pieņemams, bet konkrētā vērtība nav derīga.

Biežākie cēloņi:

- `int()` vai `float()` tiek lietots nederīgam tekstam
- tiek izpakots nepareizs vērtību skaits

Piemērs:

```python
age = int("twenty")
```

Labojums:

- pirms pārveidošanas izdrukājiet vērtību
- ja vajag, noņemiet liekās atstarpes ar `strip()`
- validējiet lietotāja ievadi pirms pārveidošanas

Drošāks variants:

```python
raw = input("Enter age: ").strip()
age = int(raw)
```

### `ZeroDivisionError`

Ko tas nozīmē:

- kods mēģināja dalīt ar nulli.

Piemērs:

```python
10 / 0
```

Labojums:

- pirms dalīšanas pārbaudiet dalītāju

Piemērs:

```python
if count != 0:
    average = total / count
```

### `ModuleNotFoundError`

Ko tas nozīmē:

- Python nevar atrast pakotni, kuru mēģināt importēt.

Biežākie cēloņi 1. dienā:

- pakotne nav uzstādīta
- tā ir uzstādīta citā Python vidē
- VS Code izmanto nepareizo `interpreter`
- piezīmju bloks izmanto nepareizo `kernel`

Piemērs:

```python
import pandas
```

Labojums:

1. Pārbaudiet izvēlēto `interpreter` VS Code vidē `.py` failiem.
2. Pārbaudiet izvēlēto `kernel` piezīmju blokiem.
3. Uzstādiet pakotnes tieši tajā vidē:

```powershell
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

### `AttributeError`

Ko tas nozīmē:

- jūs mēģināt objektam izsaukt darbību, ko šis tips neatbalsta.

Biežākie cēloņi:

- virkņu metodes tiek sauktas skaitļiem
- sarakstu metodes tiek sauktas virknēm
- nepareizi uzrakstīts metodes nosaukums

Piemērs:

```python
age = 25
age.strip()
```

Labojums:

- pārbaudiet faktisko tipu ar `type(age)`
- pārliecinieties, ka attiecīgā metode šim tipam tiešām eksistē

### `EOFError`

Ko tas nozīmē:

- `input()` gaidīja ievadi, bet tā netika saņemta.

Kur tas parādās:

- dažreiz piezīmju blokos vai interaktīvās vidēs, ja ievade tiek pārtraukta vai nav pieejama

Labojums:

- palaidiet šūnu vēlreiz
- ievadiet prasīto vērtību
- ja vide nav piemērota ievadei, uz laiku aizstājiet `input()` ar fiksētu testvērtību

Piemērs:

```python
name = "Test User"
```

### `KeyboardInterrupt`

Ko tas nozīmē:

- izpilde tika manuāli pārtraukta.

Biežākie cēloņi:

- nospiesta pārtraukšanas komanda
- `kernel` tika apturēts, jo šūna iestrēga
- kods gaidīja `input()` un izpilde tika atcelta

Labojums:

- tas ne vienmēr nozīmē kļūdu kodā
- noskaidrojiet, vai kods bija lēns, iestrēdzis ciklā vai gaidīja ievadi

## Problēmas, kas raksturīgas piezīmju blokiem

### Problēma: `input()` bloķē piezīmju bloku

Pazīmes:

- šūna rāda, ka joprojām darbojas
- nākamās šūnas nevar palaist
- piezīmju bloks izskatās iesalis
- tiek gaidīta ievade

Kas notiek:

- `input()` aptur izpildi līdz brīdim, kamēr lietotājs kaut ko ievada

Kā atgūties:

1. Atrodiet aktīvo ievades lauku vai prompt un ievadiet vērtību.
2. Nospiediet Enter, lai izpilde turpinātos.
3. Ja nevēlaties turpināt, pārtrauciet `kernel`.
4. Palaidiet šūnu vēlreiz pēc tam, kad esat izlēmis, kādu testvērtību lietot.

Labs atkļūdošanas paņēmiens:

- mācīšanas vai testēšanas laikā uz laiku aizstājiet `input()` ar fiksētu vērtību

Piemērs:

```python
name = "Anna"
```

Šī koda vietā:

```python
name = input("Enter your name: ")
```

Tas noņem interaktivitāti un padara atkļūdošanu vienkāršāku.

### Problēma: piezīmju bloks atceras vecas vērtības

Pazīmes:

- jūs izmainījāt kodu, bet rezultāts šķiet nekonsekvents
- mainīgais eksistē, kaut gan definējošā šūna vairs nav redzama
- vienam studentam ir cits rezultāts nekā citam

Kas notiek:

- piezīmju bloka `kernel` glabā mainīgos atmiņā līdz pārstartēšanai

Labojums:

1. Pārstartējiet `kernel`.
2. Palaidiet šūnas no augšas uz leju.
3. Agrīnajos uzdevumos neleciet haotiski pa piezīmju bloku.

### Problēma: piezīmju bloks nezina mainīgo, kas noteikti eksistē

Pazīmes:

- vēlākā šūnā parādās `NameError`

Kas notiek:

- agrākā šūna, kas definē mainīgo, nav palaista pašreizējā `kernel` sesijā

Labojums:

- palaidiet piezīmju bloku secīgi no sākuma

### Problēma: šūna nekad nebeidz darbu

Iespējamie cēloņi:

- tiek gaidīts `input()`
- ir bezgalīgs vai ļoti ilgs `while` cikls
- `kernel` ir iestrēdzis

Kā atkļūdot:

1. Pārbaudiet, vai kodā ir `input()`.
2. Pārbaudiet, vai cikla mainīgie tiešām mainās.
3. Pārtrauciet `kernel`.
4. Vienkāršojiet šūnu un palaidiet mazākas koda daļas.

Slikta cikla piemērs:

```python
count = 1
while count <= 3:
    print(count)
```

Kāpēc tas iestrēgst:

- `count` nekad nemainās

Labojums:

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

### Problēma: Markdown paskaidrojums tika palaists kā Python kods

Pazīmes:

- parādās `SyntaxError` pie teksta, kas izskatās kā parasts teikums

Labojums:

- pārliecinieties, ka šūnas tips ir `Markdown`, nevis `Code`

Piezīmju blokos tā ir bieža kļūda, un sākumā tā var šķist mulsinoša, jo kļūdas ziņojums neizskatās saistīts ar pašu problēmu.

## VS Code un vides problēmas

### Problēma: netiek atrasts `python` vai `py`

Pārbaudiet:

```powershell
python --version
py --version
```

Ja tas neizdodas:

- aizveriet un atveriet termināli no jauna
- pārliecinieties, ka Python ir uzstādīts
- Windows vidē pārbaudiet, vai pieejams Python launcher

### Problēma: PowerShell neļauj aktivizēt `.venv`

Tipisks labojums:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Pēc tam aktivizējiet vēlreiz:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Problēma: `pip` uzvedas nekonsekventi

Labojums:

- lietojiet `python -m pip`, nevis vienkārši `pip`

Piemērs:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

Tas samazina risku instalēt pakotnes nepareizajā Python vidē.

### Problēma: VS Code izmanto nepareizu Python vidi

Pazīmes:

- kods strādā terminālī, bet nestrādā VS Code
- importi strādā vienā failā, bet citā ne
- pakotnes izskatās uzstādītas, bet joprojām nevar importēt

Labojums:

1. Atveriet `Command Palette`.
2. Palaidiet `Python: Select Interpreter`.
3. Izvēlieties projekta `.venv`.
4. Pēc pārslēgšanas atveriet jaunu termināli.

### Problēma: piezīmju blokam ir nepareizs `kernel`

Pazīmes:

- importi piezīmju blokā nestrādā
- piezīmju bloka uzvedība atšķiras no `.py` failiem

Labojums:

1. Atveriet piezīmju bloku.
2. Augšējā labajā stūrī atveriet `kernel` izvēli.
3. Izvēlieties vidi, kas atbilst `.venv`.
4. Ja vajag, uzstādiet `ipykernel` tieši šajā vidē.

### Problēma: piezīmju bloka izpilde ir bloķēta

Iespējamais cēlonis:

- darba mape atrodas `Restricted Mode` vai nav uzticama

Labojums:

- ja tā ir jūsu kursa mape, piešķiriet darba videi uzticību

## Loģikas kļūdas, kas ne vienmēr rada izņēmumu

Dažas kļūdas dod nepareizu rezultātu, bet neizmet izņēmumu.

### Vecs mainīgais tiek izmantots nejauši

Piemērs:

```python
count = 5
count = 2
```

Tas ir derīgs Python, taču loģiski tas var būt nepareizi, ja otrā piešķire bija nejauša.

Kā to atkļūdot:

- izdrukājiet vērtības pēc svarīgiem soļiem
- lietojiet saprotamus mainīgo nosaukumus

### Salīdzināšana sajaukta ar piešķiršanu vai otrādi

Piemēri:

```python
x = 5
```

pret:

```python
x == 5
```

Pirmais piešķir vērtību. Otrais salīdzina.

Ja kods "neko jēdzīgu nedara", pārbaudiet, vai izmantots pareizais operators.

### Šūnas palaistas nepareizā secībā

Tā ir viena no lielākajām piezīmju blokiem raksturīgajām loģikas problēmām.

Labojums:

- pārstartējiet `kernel`
- palaidiet visas šūnas no augšas

### Pārrakstīti iebūvētie nosaukumi

Piemērs:

```python
list = [1, 2, 3]
```

Tas strādā, bet vēlāk var salauzt šādu kodu:

```python
list("abc")
```

jo `list` tagad norāda uz jūsu mainīgo, nevis uz iebūvēto funkciju.

Izvairieties no šādiem nosaukumiem:

- `list`
- `str`
- `int`
- `input`
- `type`

## Praktiska atkļūdošanas pieeja

Lietojiet šo procesu minēšanas vietā:

1. Atkārtojiet problēmu ar iespējami mazāko koda piemēru.
2. Izlasiet precīzu kļūdas tipu un ziņojumu.
3. Pārbaudiet mainīgo vērtības ar `print(...)`.
4. Pārbaudiet tipus ar `type(...)`.
5. Piezīmju blokos vēlreiz palaidiet agrākās šūnas vai pārstartējiet `kernel`.
6. Ja neizdodas importi, pārbaudiet `interpreter` vai `kernel`.
7. Pēc katra labojuma palaidiet kodu vēlreiz un pārliecinieties, ka simptoms tiešām mainījies.

## Noderīgi debug izdrukas piemēri 1. dienai

Ja problēma nav skaidra, izdrukājiet starpvērtības.

```python
raw_age = input("Enter age: ")
print("raw_age =", raw_age)
print("type(raw_age) =", type(raw_age))
age = int(raw_age)
print("age =", age)
```

Cikliem:

```python
for value in [1, 2, 3]:
    print("value =", value)
```

Nosacījumiem:

```python
score = 78
print("score >= 60:", score >= 60)
```

Šie paņēmieni ir vienkārši, bet tie noņem minēšanu.

## Kad pārstartēt, palaist vēlreiz vai veidot vidi no jauna

Pārstartējiet piezīmju bloka `kernel`, ja:

- mainīgo stāvoklis šķiet nekonsekvents
- šūnas tika palaistas nepareizā secībā
- piezīmju bloks ir iestrēdzis

Palaidiet pašreizējo šūnu vēlreiz, ja:

- salabojāt lokālu sintakses vai loģikas problēmu
- izmainījāt tikai vienu rindu šajā šūnā

Palaidiet visu piezīmju bloku no augšas, ja:

- viena šūna ir atkarīga no agrākā stāvokļa
- izmainījāt mainīgo definīcijas, ko izmanto vēlāk
- neesat pārliecināts, ka pašreizējais `kernel` stāvoklis ir tīrs

Veidojiet vidi no jauna tikai tad, ja:

- importi neizdodas, jo pakotnes tiešām trūkst
- atkal un atkal tiek izvēlēts nepareizais `interpreter` vai `kernel`

## Minimālās atkopšanas komandas

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

Pamata pārbaudes:

```powershell
python --version
python -m pip --version
```

## Autoritatīvas atsauces

- Python apmācība par kļūdām un izņēmumiem: <https://docs.python.org/3/tutorial/errors.html>
- Iebūvētie izņēmumi: <https://docs.python.org/3/library/exceptions.html>
- Iebūvētās `input()` funkcijas dokumentācija: <https://docs.python.org/3/library/functions.html#input>
- Iebūvētās `int()` funkcijas dokumentācija: <https://docs.python.org/3/library/functions.html#int>
- Python VS Code vidē: <https://code.visualstudio.com/docs/languages/python>
- Jupyter piezīmju bloki VS Code vidē: <https://code.visualstudio.com/docs/datascience/jupyter-notebooks>
- Jupyter `kernel` pārvaldība VS Code vidē: <https://code.visualstudio.com/docs/datascience/jupyter-kernel-management>
- VS Code Workspace Trust: <https://code.visualstudio.com/docs/editing/workspaces/workspace-trust>
