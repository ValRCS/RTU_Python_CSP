# Python + Visual Studio Code uzstādīšana (Windows + macOS, aktuāli 2026-04-09)

## Mērķis

Pēc šīs uzstādīšanas jūs spēsiet:
- palaist Python programmas
- strādāt ar Jupyter notebook failiem (.ipynb)
- apstrādāt Excel failus ar Python (`pandas`, `openpyxl`)
- ērti strādāt VS Code vidē ar pareizi izvēlētu `interpreter` un `kernel`

---

# 1. Python uzstādīšana

## Kas šobrīd ir aktuāli

2026. gada 9. aprīlī jaunākais stabilais Python 3 izlaidums ir `Python 3.14.4`.

Ieteikums:
- instalējiet jaunāko stabilo Python 3 versiju
- neizvēlieties `alpha`, `beta` vai citus `pre-release` izlaidumus

## Windows 10/11

### Ieteicamais variants 2026. gadā

Oficiāli ieteiktais ceļš 2026. gadā ir `Python Install Manager`, taču praksē tas vēl nav līdz galam noslīpēts un mācību vidē dažkārt rada lieku neskaidrību.

Tāpēc kursam joprojām ieteicamais variants ir uzstādīt konkrētu stabilu Python versiju tieši no `python.org`, proti, `Python 3.14.4`.

Ieteicamā praktiskā pieeja:

1. Atveriet:
    https://www.python.org/downloads/release/python-3144/
2. Lejupielādējiet `Windows installer (64-bit)` savai sistēmai
3. Uzstādīšanas laikā atzīmējiet `Add Python to PATH`, ja šī opcija tiek piedāvāta
4. Pabeidziet instalāciju
5. Pēc uzstādīšanas atveriet `PowerShell` un pārbaudiet, vai komandas strādā:

```powershell
python --version
py --version
```

Ja viss ir kārtībā, jums jāredz Python 3.14.4 vai 3.14.x.

### Par `Python Install Manager`

`Python Install Manager` joprojām ir oficiāli ieteiktais virziens no Python dokumentācijas puses, tāpēc to ir vērts zināt. Ja vēlaties to izmēģināt, izmantojiet:

```powershell
py --version
py install 3.14
```

Tomēr kursa vajadzībām drošāks un paredzamāks variants joprojām ir tiešā `Python 3.14.4` instalācija.

### Kāpēc nav ieteicama Microsoft Store versija

Microsoft Store variants tehniski var strādāt, bet to labāk izvairīties izmantot mācību nolūkiem, jo tas mēdz radīt:
- neskaidrības ar `App execution aliases`
- konfliktus starp `python`, `py` un citām jau esošām instalācijām
- grūtāk prognozējamu uzvedību, ja datorā vēlāk tiek pievienotas citas Python versijas

Tāpēc šim kursam ieteikums ir:
- neizmantot Microsoft Store versiju, ja vien nav ļoti konkrēts iemesls
- izvēlēties tiešo `python.org` instalāciju

Ja `Python Install Manager` jau ir uzstādīts, tas nav kritiski, bet kursa darbam svarīgākais ir tas, lai gala rezultātā jums būtu skaidri pieejams konkrēts Python `interpreter`, vēlams `Python 3.14.4`.

Pārbaude pēc uzstādīšanas:

```powershell
python --version
py --version
```

### Alternatīva, ja datorā ir ierobežojumi
Ja datorā ir ierobežojumi un nevarat uzstādīt Python, varat izmantot `Anaconda` vai `Miniconda` platformu, kas nodrošina Python vidi bez nepieciešamības veikt tradicionālu instalāciju. Tomēr šī pieeja var būt sarežģītāka iesācējiem, tāpēc to ieteicams tikai tad, ja tiešām nav citas iespējas.
- izmantojiet `python.org` lejupielādes lapu
- vai lūdziet IT nodaļai uzstādīt Python caur oficiālo instalācijas rīku


## macOS (Apple Silicon un Intel)

1. Atveriet:
    https://www.python.org/downloads/macos/
2. Lejupielādējiet jaunāko `macOS installer (.pkg)`
3. Instalējiet to ar noklusējuma iestatījumiem
4. Pēc instalācijas atveriet mapi:

```text
/Applications/Python 3.14/
```

5. Palaidiet:

```text
Install Certificates.command
```

Tas pabeidz SSL sertifikātu uzstādīšanu Python videi.

6. Atveriet `Terminal` un pārbaudiet:

```bash
python3 --version
```

### Svarīga piezīme par macOS

macOS sistēmā bieži jau ir Apple pārvaldīts `python3`, bet tas var nebūt tas, kuru vēlaties izmantot ikdienas darbam. Tāpēc kursam izmantojiet Python no `python.org` un komandu `python3`.

## Pamatojums

Bez Python uzstādīšanas nevar palaist Python programmas, instalēt bibliotēkas vai izmantot notebook. Windows sadaļa ir precizēta atbilstoši oficiālajai 2026. gada pieejai, kur galvenais ceļš ir `Python Install Manager`, bet pragmatiski joprojām ieteicams izmantot tiešo `python.org` instalāciju, lai izvairītos no neskaidrībām. macOS sadaļa ietver svarīgu sertifikātu uzstādīšanu, kas nepieciešama drošai Python darbībai.

---

# 2. Visual Studio Code uzstādīšana

1. Atveriet:
    https://code.visualstudio.com/
2. Lejupielādējiet un instalējiet `Visual Studio Code`
3. Atveriet programmu

## Pamatojums

VS Code būs jūsu galvenā darba vide Python kodiem, notebook failiem un projekta failu pārvaldībai.

---

# 3. Nepieciešamie Extensions VS Code vidē

Atveriet `Extensions` skatu (`Ctrl+Shift+X` vai `Cmd+Shift+X`) un uzstādiet:

- `Python` (Microsoft)
- `Jupyter` (Microsoft)

Parasti `Python` paplašinājums automātiski uzstāda vai aktivizē saistītos komponentus, piemēram, `Pylance`. Atsevišķi to uzstādīt parasti nav nepieciešams, ja vien VS Code to īpaši neprasa.

## Pamatojums

Šie `Extensions` nodrošina:
- Python sintakses atbalstu
- `interpreter` izvēli
- koda palaišanu
- `Jupyter notebook` atbalstu
- `kernel` izvēli notebook failiem

---

# 4. Git uzstādīšana

## Windows 10/11

1. Atveriet:
    https://git-scm.com/download/win
2. Lejupielāde parasti sāksies automātiski
3. Uzstādīšanas laikā varat atstāt noklusējuma iestatījumus
4. Pārbaudiet:

```powershell
git --version
```

## macOS

Vienkāršākais variants ir Apple Command Line Tools:

```bash
xcode-select --install
```

Ja Git jau nav uzstādīts, dažkārt pietiek arī ar:

```bash
git --version
```

un macOS pati piedāvās uzstādīšanu.

Ja vajag jaunāku versiju, var izmantot arī:

https://git-scm.com/download/mac

Pārbaude:

```bash
git --version
```

## Pamatojums

Git ir nepieciešams, lai strādātu ar GitHub projektiem, kursa materiāliem un versiju kontroli.

---

# 5. GitHub Copilot (neobligāti)

Ja vēlaties AI palīdzību koda rakstīšanā, VS Code var uzstādīt:

- `GitHub Copilot`
- `GitHub Copilot Chat`

## Uzstādīšana

1. Atveriet `Extensions`
2. Atrodiet `GitHub Copilot`
3. Nospiediet `Install`
4. Pierakstieties ar savu GitHub kontu

Piezīme:
- nepieciešams GitHub konts
- dažos gadījumos nepieciešama aktīva Copilot piekļuve vai izmēģinājuma plāns

---

# 6. Projekta mapes izveide

Izveidojiet projekta mapi, piemēram:

```text
python_excel_lesson
```

Pēc tam VS Code izvēlieties:

```text
File -> Open Folder
```

un atveriet tieši šo mapi.

## Pamatojums

Tas ļauj VS Code korekti piesaistīt failus, virtuālo vidi un projekta iestatījumus vienai darba vietai.

---

# 7. Virtuālā vide (.venv)

Virtuālā vide ir ieteicamais darba modelis katram projektam atsevišķi.

## Windows

Projekta mapē atveriet `Terminal` un palaidiet:

```powershell
py -m venv .venv
```

Aktivizācija PowerShell vidē:

```powershell
.\.venv\Scripts\Activate.ps1
```

Ja PowerShell bloķē skripta palaišanu, vienai sesijai atļaujiet izpildi:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

un pēc tam atkārtojiet aktivizāciju:

```powershell
.\.venv\Scripts\Activate.ps1
```

## macOS

Projekta mapē atveriet `Terminal` un palaidiet:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Kā saprast, ka vide ir aktivizēta

Terminālī parasti parādās prefikss, piemēram:

```text
(.venv)
```

## Pamatojums

Virtuālā vide izolē konkrētā projekta bibliotēkas no pārējās sistēmas. Tas samazina versiju konfliktus un padara projektu atkārtojamu.

---

# 8. Interpreter izvēle VS Code

Kad `.venv` ir izveidota, VS Code jānorāda, ka tieši šo vidi vajag izmantot.

## Variants A: caur Command Palette

Atveriet:

```text
Ctrl + Shift + P
```

vai macOS:

```text
Cmd + Shift + P
```

Pēc tam izvēlieties:

```text
Python: Select Interpreter
```

un atlasiet `.venv`.

## Variants B: caur Status Bar

Atveriet jebkuru `.py` failu un apakšējā joslā (`Status Bar`) izvēlieties aktīvo Python versiju. No saraksta atlasiet `.venv`.

## Pēc interpreter izvēles

Atverot jaunu termināli VS Code vidē, `.venv` parasti aktivizējas automātiski.

## Pamatojums

Ja nav pareizi izvēlēts `interpreter`, VS Code var izmantot nepareizu Python vidi, un bibliotēkas šķitīs "pazudušas", lai gan tās patiesībā ir uzstādītas citur.

---

# 9. Bibliotēku uzstādīšana

Pēc `.venv` aktivizācijas uzstādiet nepieciešamās bibliotēkas.

Vispirms ieteicams atjaunināt `pip`:

```bash
python -m pip install --upgrade pip
```

Tad uzstādiet darba bibliotēkas:

```bash
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
```

## Kāpēc tieši šīs bibliotēkas

- `pandas` datu apstrādei
- `openpyxl` Excel `.xlsx` failiem
- `matplotlib` diagrammām
- `jupyter` notebook darbībai
- `ipykernel` lokālam Python `kernel` notebook failiem

## Pamatojums

Ar Python vien nepietiek praktiskam darbam ar datiem. Šīs pakotnes veido pamata darba komplektu kursa uzdevumiem.

---

# 10. Python tests

Izveidojiet failu `test.py` ar saturu:

```python
print("Python darbojas!")

import pandas
import openpyxl

print("Bibliotēkas darbojas!")
```

Palaidiet:

```bash
python test.py
```

Ja `.venv` ir aktivizēta, šī pati komanda būs korekta gan Windows, gan macOS vidē.

## Pamatojums

Šis tests vienlaikus pārbauda Python palaišanu un galveno bibliotēku importu.

---

# 11. Jupyter notebook tests

1. VS Code vidē izveidojiet jaunu `.ipynb` failu
2. Augšējā labajā stūrī izvēlieties `kernel`
3. Atlasiet savu `.venv`
4. Pirmajā šūnā palaidiet:

```python
import pandas as pd
print("Notebook darbojas")
```

## Svarīgi

Notebook failam `kernel` jāatbilst tai pašai `.venv`, kur uzstādījāt bibliotēkas.

Ja VS Code rāda citu vidi, manuāli pārslēdziet `kernel` augšējā labajā stūrī.

## Pamatojums

`Interpreter` un `kernel` nav vienmēr viens un tas pats izvēles punkts. Python failam svarīgs ir `interpreter`, notebook failam svarīgs ir `kernel`.

---

# 12. Excel tests

Notebook vai `.py` failā palaidiet:

```python
import pandas as pd

df = pd.DataFrame({
     "Department": ["IT", "HR", "Finance"],
     "Amount": [1200, 800, 1500]
})

df.to_excel("test.xlsx", index=False)
print("Excel fails izveidots")
```

Ja mapē parādās `test.xlsx`, tad `pandas` un `openpyxl` strādā korekti.

## Pamatojums

Šis ir praktisks tests, kas apstiprina, ka Excel eksports tiešām darbojas, nevis tikai bibliotēku imports.

---

# 13. Biežākās problēmas

## Windows

### `python` vai `py` netiek atrasts

Pārbaudiet:

```powershell
python --version
py --version
```

Ja komandas nestrādā:
- aizveriet un atveriet termināli no jauna
- pārliecinieties, ka `Python Install Manager` ir uzstādīts
- pārbaudiet `App execution aliases` Windows iestatījumos

### PowerShell neļauj aktivizēt `.venv`

Izmantojiet:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

### `pip` komanda nestrādā

Izmantojiet nevis `pip`, bet:

```bash
python -m pip
```

Tas ir drošākais variants visās vidēs.

## macOS

### Tiek izmantots nepareizs Python

Pārbaudiet:

```bash
which python3
python3 --version
```

Ja izmantojat Python no `python.org`, rezultātam jāatbilst jaunajai instalācijai.

### HTTPS vai sertifikātu problēmas

Palaidiet:

```text
Install Certificates.command
```

no mapes `/Applications/Python 3.14/`.

## Gan Windows, gan macOS

### VS Code neredz `.venv`

- palaidiet `Python: Select Interpreter`
- ja nepieciešams, aizveriet un atveriet VS Code
- atveriet jaunu termināli pēc interpreter izvēles

### Notebook neredz bibliotēkas

- pārbaudiet, vai notebook `kernel` ir `.venv`
- ja vajag, pārslēdziet `kernel` augšējā labajā stūrī
- pārliecinieties, ka `ipykernel` ir uzstādīts tieši `.venv`

### Notebook nevar palaist kodu

Pārbaudiet, vai darba mape ir `trusted workspace`. `Restricted Mode` var bloķēt notebook izpildi.

---

# 14. Komandu kopsavilkums

## Windows

```powershell
py --version
py install 3.14
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
python test.py
```

## macOS

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib jupyter ipykernel
python test.py
```

---

# 15. Minimālais darba princips

1. Atver projekta mapi VS Code vidē
2. Izveido `.venv`
3. Aktivizē `.venv`
4. Izvēlas pareizo `interpreter`
5. Uzstāda bibliotēkas
6. Python failiem izmanto pareizo `interpreter`
7. Notebook failiem izvēlas pareizo `kernel`
8. Palaiž kodu un iegūst rezultātus

---

# 16. Galvenā ideja

Python šajā kursā tiek izmantots, lai:
- automatizētu darbu ar datiem un Excel
- samazinātu manuālas kļūdas
- ietaupītu laiku
- padarītu analīzi atkārtojamu



