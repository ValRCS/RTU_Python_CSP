# Mācību ceļvedis: Python funkcijas

Šis ceļvedis papildina 1. dienas piezīmju bloku failā `notebooks/python_basics.ipynb` un sasaucas ar 2. dienas materiāliem failā `study_guides/study_guide_day2_lv.md`, kur funkcijas jau tiek lietotas teksta tīrīšanas darbplūsmās.

Saites šajā ceļvedī tika pārbaudītas 2026. gada 15. aprīlī.

## Ceļveža mērķi

Pēc šī ceļveža izlasīšanas dalībniekam vajadzētu spēt:

- izskaidrot, kas ir funkcija un kāpēc tā ir noderīga
- definēt vienkāršas funkcijas ar `def`
- lietot parametrus un argumentus
- saprast atšķirību starp `print()` un `return`
- izmantot funkcijas atkārtoti lietojamam kodam
- pamanīt biežākās iesācēju kļūdas darbā ar funkcijām

## 1. Kāpēc vispār vajag funkcijas

Sākumā ir viegli uzrakstīt visu kodu vienā garā blokā. Tas strādā maziem piemēriem, bet kļūst neērti, ja:

- viens un tas pats kods jāatkārto vairākās vietās
- grūti saprast, ko konkrēta koda daļa dara
- kļūdu labojumi jāveic vairākās vietās
- uzdevums kļūst pārāk garš vienai šūnai vai vienam skriptam

Funkcija ļauj iedot koda blokam skaidru nosaukumu un izmantot to atkārtoti.

Praktiska ideja:

- ja jūs varat pateikt “šī koda daļa dara vienu noteiktu darbu”, tā bieži ir laba kandidāte funkcijai

## 2. Kas ir funkcija

Funkcija ir nosaukts koda bloks, kuru var izsaukt, kad tas vajadzīgs.

Vienkāršs piemērs:

```python
def sasveicinaties():
    print("Sveiki!")
```

Lai funkcija tiešām izpildītos, to vajag izsaukt:

```python
sasveicinaties()
```

Svarīgi:

- `def` sāk funkcijas definīciju
- pēc funkcijas nosaukuma ir iekavas
- rindas beigās ir kols `:`
- funkcijas saturs ir atkāpināts

## 3. Definēšana un izsaukšana

Funkciju vispirms definē, tikai pēc tam izsauc.

```python
def pateikt_vardu():
    print("Mani sauc Anna")

pateikt_vardu()
```

Ja mēģināsiet izsaukt funkciju pirms definīcijas, Python dos kļūdu, jo šajā brīdī nosaukums vēl nav zināms.

## 4. Parametri un argumenti

Funkcija bieži ir noderīgāka, ja tai var padot ievades vērtības.

```python
def sasveicinaties_ar_vardu(vards):
    print("Sveiki,", vards)
```

Izsaukumi:

```python
sasveicinaties_ar_vardu("Anna")
sasveicinaties_ar_vardu("Jānis")
```

Termini:

- parametrs ir mainīgais funkcijas definīcijā, piemēram, `vards`
- arguments ir konkrētā vērtība funkcijas izsaukumā, piemēram, `"Anna"`

Funkcijai var būt arī vairāki parametri:

```python
def pilns_vards(vards, uzvards):
    return f"{vards} {uzvards}"

print(pilns_vards("Anna", "Ozola"))
```

## 5. `print()` un `return` nav viens un tas pats

Šī ir viena no svarīgākajām iesācēju tēmām.

### `print()`

`print()` tikai parāda vērtību ekrānā.

```python
def paradit_summa(a, b):
    print(a + b)
```

### `return`

`return` atdod rezultātu tālākai izmantošanai kodā.

```python
def saskaitit(a, b):
    return a + b

rezultats = saskaitit(5, 7)
print(rezultats)
```

Kāpēc `return` parasti ir svarīgāks:

- atgriezto vērtību var saglabāt mainīgajā
- to var padot citai funkcijai
- to var izmantot nosacījumos un aprēķinos

Piemērs:

```python
def kvadrats(x):
    return x * x

skaitlis = kvadrats(4)
print(skaitlis + 10)
```

Ja funkcija tikai izdrukā rezultātu, bet neko neatgriež, to ir grūtāk izmantot tālākos aprēķinos.

## 6. Funkcijas, kas atgriež loģisku vērtību

Daudzas funkcijas neatgriež tekstu vai skaitli, bet gan `True` vai `False`.

```python
def ir_pozitivs(skaitlis):
    return skaitlis > 0

print(ir_pozitivs(8))
print(ir_pozitivs(-3))
```

Šādas funkcijas ir noderīgas pārbaudēm:

```python
def ir_garaks_par_pieciem(text):
    return len(text) > 5

if ir_garaks_par_pieciem("Python"):
    print("Teksts ir pietiekami garš")
```

## 7. Noklusētās parametru vērtības

Dažreiz gribas, lai funkcija strādā arī tad, ja nepadod visas vērtības.

```python
def sasveicinaties(vards="student"):
    return f"Sveiki, {vards}!"

print(sasveicinaties())
print(sasveicinaties("Anna"))
```

Tas nozīmē:

- ja arguments netiek padots, tiks izmantota noklusētā vērtība
- ja arguments tiek padots, tas aizstāj noklusēto vērtību

## 8. Vairāku vērtību atgriešana

Python funkcija var atgriezt vairāk nekā vienu vērtību. Praktiski tas nozīmē, ka Python atgriež `tuple`.

```python
def summa_un_starpiba(a, b):
    return a + b, a - b

summa, starpiba = summa_un_starpiba(10, 4)
print(summa)
print(starpiba)
```

Šis ir ērts veids, kā no vienas funkcijas iegūt vairākus saistītus rezultātus.

## 9. Vietējie un globālie mainīgie

Mainīgais, kas izveidots funkcijas iekšpusē, parasti ir pieejams tikai šajā funkcijā.

```python
def paraugs():
    x = 10
    print(x)

paraugs()
```

Bet šis nestrādās:

```python
def paraugs():
    x = 10

paraugs()
print(x)
```

Te radīsies `NameError`, jo `x` bija lokāls jeb vietējs mainīgais.

Praktisks noteikums iesācējiem:

- nepaļaujieties uz “slepeniem” globāliem mainīgajiem
- labāk padodiet vajadzīgās vērtības funkcijai kā parametrus
- labāk atgrieziet rezultātus ar `return`

## 10. Funkcijas un saraksti

Funkcijas kļūst īpaši noderīgas, kad viens un tas pats darbs jāveic ar daudziem elementiem.

```python
def dubultot(x):
    return x * 2

skaitli = [1, 2, 3, 4]
rezultati = []

for skaitlis in skaitli:
    rezultati.append(dubultot(skaitlis))

print(rezultati)
```

Šeit funkcija glabā vienu skaidru darbību, bet cikls to piemēro vairākiem elementiem.

## 11. Funkcijas datu apstrādes kontekstā

Šajā kursā funkcijas ir īpaši svarīgas datu apstrādē un tīrīšanā.

Piemērs ar teksta tīrīšanu:

```python
def notirit_rindu(rinda):
    rinda = rinda.strip()
    rinda = rinda.lower()
    rinda = rinda.replace("  ", " ")
    return rinda

teksti = ["  Python  ", " Data Science ", "PYTHON"]

for teksts in teksti:
    print(notirit_rindu(teksts))
```

Ieguvumi:

- viena vieta, kur uzturēt tīrīšanas loģiku
- vieglāk pārbaudīt rezultātu
- vieglāk izmantot to pašu darbību daudzām rindām

## 12. Kā rakstīt labākas funkcijas

Labs sākuma līmeņa ieradums ir rakstīt mazas un skaidras funkcijas.

Vēlams:

- funkcijai ir viena galvenā atbildība
- funkcijas nosaukums apraksta darbību
- parametru nosaukumi ir saprotami
- funkcija atgriež rezultātu, nevis tikai izdrukā visu

Mazāk vēlams:

- viena funkcija dara pārāk daudz dažādu lietu
- funkcija paļaujas uz ārējiem mainīgajiem bez vajadzības
- funkcija vienlaikus lasa ievadi, tīra datus, drukā rezultātus un saglabā failu, lai gan to var sadalīt mazākos soļos

Labs piemērs:

```python
def pilns_vards(vards, uzvards):
    return f"{vards.strip()} {uzvards.strip()}"
```

Sliktāks piemērs:

```python
def darit_visu(x):
    print(x)
    x = x.strip()
    x = x.lower()
    print(x)
    return len(x)
```

Otrā versija nav “nepareiza” sintaktiski, bet tā dara vairākas dažādas lietas vienlaikus un ir grūtāk atkārtoti lietojama.

## 13. Biežākās iesācēju kļūdas

### Aizmirsts kols vai atkāpes

```python
def sasveicinaties()
    print("Sveiki!")
```

Te būs `SyntaxError`, jo trūkst kola.

### Funkcija nav izsaukta

```python
def sasveicinaties():
    print("Sveiki!")
```

Šī funkcija ir definēta, bet nekas netiks izdrukāts, kamēr neuzrakstīsiet:

```python
sasveicinaties()
```

### Sajaukts `print` ar `return`

```python
def saskaitit(a, b):
    print(a + b)

rezultats = saskaitit(2, 3)
print(rezultats)
```

Šeit vispirms tiks izdrukāts `5`, bet pēc tam `None`, jo funkcija neko neatgrieza.

### Nepareizs argumentu skaits

```python
def saskaitit(a, b):
    return a + b

saskaitit(5)
```

Te būs `TypeError`, jo trūkst otrā argumenta.

### Mainīgais no funkcijas iekšpuses nav pieejams ārpus tās

```python
def izveidot():
    teksts = "Python"

izveidot()
print(teksts)
```

Te būs `NameError`, jo `teksts` eksistēja tikai funkcijas iekšienē.

## 14. Kā domāt par funkcijas veidošanu

Ja ir lielāks uzdevums, uzdodiet sev trīs jautājumus:

1. Kādu vienu darbu šī funkcija darīs?
2. Kāda ievade tai vajadzīga?
3. Ko tai vajadzētu atgriezt?

Piemērs:

- uzdevums: pārbaudīt, vai ievadītais teksts nav tukšs
- ievade: viena virkne
- izvade: `True` vai `False`

```python
def nav_tuks(text):
    return text.strip() != ""
```

Tā ir laba sākuma pieeja, jo funkcijas robežas ir skaidras.

## 15. Nelieli praktiski uzdevumi

Izmēģiniet uzrakstīt:

1. funkciju `dubultot(x)`, kas atgriež skaitļa dubultvērtību
2. funkciju `ir_para(skaitlis)`, kas atgriež `True`, ja skaitlis ir pāra skaitlis
3. funkciju `pilns_vards(vards, uzvards)`, kas atgriež pilno vārdu vienā virknē
4. funkciju `notirit_tekstu(text)`, kas lieto `strip()` un `lower()`
5. funkciju `cena_ar_pvn(cena, likme=0.21)`, kas atgriež cenu ar PVN

## 16. Saikne ar pārējo kursu

Funkcijas nav atsevišķa tēma, kas pazūd pēc viena piemēra. Tās turpinās parādīties visā kursā:

- 1. dienā tās palīdz strukturēt mazas programmas
- 2. dienā tās veido teksta tīrīšanas soļus
- vēlāk tās palīdz sadalīt datu apstrādes plūsmas saprotamos posmos
- strādājot ar lielākiem projektiem, funkcijas palīdz uzturēt kodu pārskatāmu

## Autoritatīvas atsauces

- Python pamācības sadaļa par funkciju definēšanu: <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
- Vadības plūsmas rīki Python pamācībā: <https://docs.python.org/3/tutorial/controlflow.html>
- Iebūvētās funkcijas: <https://docs.python.org/3/library/functions.html>
- Datu tipi un darbības ar virknēm: <https://docs.python.org/3/library/stdtypes.html>
