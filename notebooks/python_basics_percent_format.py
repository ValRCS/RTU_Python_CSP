# %% [markdown]
# # Python pamati — 1. diena
# 
# ## Notebook mērķis
# 
# Šajā notebook mēs soli pa solim iepazīsimies ar:
# - pirmo Python programmu
# - Jupyter Notebook šūnām
# - Markdown pamatiem notebook vidē
# - Python pamatsintaksi
# - mainīgajiem un datu tipiem
# - operatoriem
# - ievadi ar `input()`
# - tekstu apstrādes pamatiem
# - nosacījumiem
# - cikliem
# - sarakstu pamatiem
# - funkciju pamatiem
# 
# ## Svarīgi
# - Strādājam lēni un secīgi.
# - Izpildām šūnas no augšas uz leju.
# - Droši mainām piemērus un skatāmies, kas notiek.
# - Kļūdas ir normāla mācību procesa daļa.

# %% [markdown]
# ## Kā lietot šo notebook
# 
# - **Code** šūnās rakstām un palaižam Python kodu.
# - **Markdown** šūnās rakstām piezīmes, virsrakstus un paskaidrojumus.
# - Šūnu var palaist ar **Shift + Enter**.
# - Ja rezultāti šķiet dīvaini, dažreiz palīdz:
#   - palaist šūnu vēlreiz
#   - pārstartēt kernel
#   - izpildīt notebook no sākuma

# %% [markdown]
# # 1. Pirmais Python kods
# 
# Sāksim ar pašu vienkāršāko piemēru.
# Funkcija `print()` izvada tekstu ekrānā.

# %%
print("Hello Python Pasaule tik tiešām!")

# %% [markdown]
# ### Uzdevums
# Izmainiet tekstu funkcijā `print()` un palaidiet šūnu vēlreiz.
# 
# Pamēģiniet:
# - savu vārdu
# - savas nodaļas nosaukumu
# - divas atsevišķas `print()` rindas

# %%
# Ierakstiet savu kodu zemāk.
# Piemērs:
# print("Mani sauc ...")
# print("Es strādāju ...")
print("Mani sauc Valdis.")
print("Es strādāju kā datu zinātnieks.")
# Jūs varat izmantot arī emocijzīmes, lai padarītu savu kodu jautrāku! 😊
print("Es mīlu Python! 🐍")

# %% [markdown]
# # 2. Jupyter Notebook šūnas
# 
# Notebook sastāv no šūnām. Galvenie šūnu tipi ir:
# 
# - **Code** — izpildāms Python kods
# - **Markdown** — teksts, paskaidrojumi, virsraksti, saraksti
# 
# Šeit parādīsim, ka notebook "atceras" iepriekš izveidotos mainīgos.

# %%
# koda šūna, kurā tiek definēta mainīgā x vērtība un izvadīta uz ekrāna
x = 20 # izpildes brīdi atmiņā sāk dzīvot mainīgais x ar vērtību 20
print("x vērtība ir:", x)
# kas svarīgi pēc šūnas izpildes, mainīgais x joprojām ir pieejams un var tikt izmantots citās šūnās

# %%
print("x + 5 =", x + 5) # tāda x ir atmiņā, tāpēc varam to izmantot un veikt ar to dažādas darbības, piemēram, saskaitīt ar 5. Rezultāts būs 15. 😊

# %% [markdown]
# ### Piezīme
# Ja mēģināsiet palaist otro šūnu pirms pirmās, var rasties kļūda, jo `x` vēl nebūs definēts.
# Tāpēc notebook jāizpilda secīgi.

# %% [markdown]
# ### Uzdevums
# Izveidojiet mainīgo `y` un piešķiriet tam skaitli.
# Pēc tam izdrukājiet:
# - pašu `y`
# - `y + 2`
# - `y * 3`

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 3. Markdown pamati notebook vidē
# 
# Markdown šūnas ļauj veidot:
# - virsrakstus
# - sarakstus
# - treknrakstu
# - slīprakstu
# - īsus paskaidrojumus
# 
# ## Piemēri Markdown sintaksei
# 
# ### Virsraksts
# `# Virsraksts`
# 
# ### Apakšvirsraksts
# `## Apakšvirsraksts`
# 
# ### Saraksts
# `- punkts 1`
# `- punkts 2`
# `* punkts 3`
# 
# ### Treknraksts
# `**svarīgs teksts**`
# 
# ### Slīpraksts
# `*piezīme*`

# %% [markdown]
# ### Uzdevums
# Izveidojiet jaunu Markdown šūnu zem šīs vietas un uzrakstiet:
# - savu virsrakstu
# - vienu teikumu par Python
# - īsu 3 punktu sarakstu
# 
# Šo uzdevumu veiciet, pievienojot jaunu Markdown šūnu manuāli.

# %% [markdown]
# ### Piemērs ar bildēm un saitēm
# 
# #### Vairāk par Markdown sintaksi 
# 
# * [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).
# * [Github Markdown Guide](https://guides.github.com/features/mastering-markdown/).
# 
# #### Bilžu iekļaušana
# `![alternatīvais teksts](attēla_url)`
# 
# ![RTU logo](https://www.rtu.lv/images/logo_lv.svg?v=1.1)
# 
# 
# #### HTML izmantošana Markdown šūnās
# 
# ```html
# <div style="background-color: lightblue; padding: 10px; border-radius: 5px;">
#     <h2 style="color: darkblue;">Šis ir HTML bloks</h2>
#     <p>Šeit var izmantot arī HTML, lai izveidotu stilizētus elementus.</p>
# </div>
# ```
# Praksē ar HTML nav tik ērti strādāt, tāpēc to izmantojam tikai īpašos gadījumos, kad Markdown nepietiek.
# 
# #### Krāsas Markdown
# 
# Krāsas bez HTML, nav standartizētas Markdown sintaksē, bet dažas platformas atbalsta paplašinājumus, piemēram:
# 
# `rgb(9, 105, 218)`
# 
# #### AR HTML krāsu
# ```html<span style="color: rgb(9, 105, 218);">Šis teksts ir krāsains!</span>```
# 
# Piemēram, varam izveidot šis būs 
# <span style="color: rgb(9, 105, 218);">zils teksts, </span>
# izmantojot HTML krāsu kodu.

# %% [markdown]
# # 4. Mainīgie un vērtības
# 
# Mainīgais ir nosaukums, pie kura glabājas kāda vērtība.
# 
# Piemēri:
# - teksts
# - skaitlis
# - patiesuma vērtība (`True` vai `False`)

# %%
vards = "Anna"
vecums = 32
pilseta = "Rīga"

print(vards)
print(vecums)
print(pilseta)

# %% [markdown]
# ### Svarīgi principi
# - Mainīgajiem dodam saprotamus nosaukumus.
# - Vienādības zīme `=` Python valodā šeit nozīmē **piešķiršanu**, nevis salīdzināšanu.
# - Mainīgo var pārrakstīt ar jaunu vērtību.
# - Latviskās garumzīmes un mīkstinājuma zīmes mainīgajos stingri neiesaku :)
# - Mainīgie ir pieejami visā notebook vidē pēc to definēšanas, līdz notebook tiek restartēts.
# 
# #### Precizējums par piešķiršanu
# 
# Tehniski mēs Python ar mainīgo veidojam norādi/refenci/alias uz kādiem datiem, kas atrodas atmiņā. Tāpēc, kad mēs mainīgajam piešķiram jaunu vērtību, mēs vienkārši mainām šo norādi uz citu datu objektu. Tas ir iemesls, kāpēc dažreiz var rasties negaidīti rezultāti, īpaši ar sarežģītākiem datu tipiem, piemēram, sarakstiem vai vārdnīcām.

# %%
skaits = 5
print("Sākumā:", skaits)

skaits = 8
print("Pēc pārrakstīšanas:", skaits)

# %%
# Par lielajiem burtiem
PI = 3.14159 # tas ir vienkāršs mainīgais, bet ar lielajiem burtiem, lai norādītu, ka tas ir constants (nemainīgs). Tas ir tikai konvencija, un Python pats to neuzlūko kā īpašu.
print("PI vērtība ir:", PI)
# teorētiski es vārētu vēlāk pārrakstīt PI ar citu vērtību, bet tas būtu slikta prakse, jo tas var radīt neskaidrības un kļūdas kodā. Constants parasti tiek atstāti nemainīgi, lai nodrošinātu koda stabilitāti un lasāmību.

# %% [markdown]
# ### Uzdevums
# Izveidojiet 3 mainīgos:
# - savs vārds
# - amats
# - darba vieta vai nodaļa
# 
# Tad izdrukājiet tos atsevišķās rindās.

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 5. Pamata datu tipi
# 
# Šajā nodarbībā izmantosim četrus ļoti svarīgus datu tipus:
# 
# - `str` — teksts
# - `int` — vesels skaitlis
# - `float` — daļskaitlis
# - `bool` — loģiska vērtība (`True` vai `False`)

# %%
teksts = "Python"
skaits = 10
temperatura = 21.5
ir_aktivs = True
nekas = None

print(type(teksts))
print(type(skaits))
print(type(temperatura))
print(type(ir_aktivs))
print(type(nekas))

# %%
my_value = 0.1+0.2
print("my_value:", my_value)
rounded_value = round(my_value, 2) # iespējams ka vajag 4 vai 6 ciparus, lai redzētu precīzu rezultātu, bet šeit es izvēlos 2 ciparus aiz komata, lai tas būtu vieglāk lasāms.
print("my_value noapaļots līdz 2 cipariem aiz komata:", rounded_value)

# %% [markdown]
# ### Piezīme
# Funkcija `type()` parāda, kāda tipa ir vērtība.

# %% [markdown]
# ### Uzdevums
# Izveidojiet pa vienam piemēram katram no šiem tipiem un izdrukājiet to tipus ar `type()`.

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 6. Pārvēršana starp tipiem
# 
# Dažreiz nepieciešams tekstu pārvērst par skaitli vai skaitli par tekstu.

# %%
skaitlis_teksta = "123"
skaitlis = int(skaitlis_teksta)

print(skaitlis)
print(type(skaitlis))

# %%
vecums = 35
teksts = str(vecums)

print(teksts)
print(type(teksts))

# %% [markdown]
# ### Uzdevums
# Izveidojiet:
# - tekstu `"45"` un pārvērtiet to par `int`
# - skaitli `12.7` un apskatiet tā tipu
# - skaitli `99` un pārvērtiet to par tekstu

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 7. Operatori
# 
# ## Aritmētiskie operatori
# - `+` saskaitīšana
# - `-` atņemšana
# - `*` reizināšana
# - `/` dalīšana
# - `//` veselā dalīšana
# - `%` atlikums
# - `**` pakāpe
# 
# ## Salīdzināšanas operatori
# - `==`
# - `!=`
# - `>`
# - `<`
# - `>=`
# - `<=`
# 
# ## Loģiskie operatori
# - `and`
# - `or`
# - `not`

# %%
a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b) # šis operators atgriež atlikumu pēc dalīšanas
print("a ** b =", a ** b)

# %%
# integer Python atbalsta ļoti lielus skaitļus, tāpēc nav jāuztraucas par integer overflow, 
# kā tas varētu būt citās programmēšanas valodās. 
# Python automātiski pārslēdzas uz garāku integer tipu, ja skaitlis pārsniedz parasto integer robežas. Tas ļauj mums strādāt ar ļoti lieliem skaitļiem bez problēmām.

# %%
# agrāk populārs bija int32
2**32 # no šī veidojās 4GB atmiņas ierobežojums, jo katrs int aizņem 4 baitus (32 bitus)

# %%
# kā ar 64bit adresēm?
2**64 # tas ir ļoti liels skaitlis, un tas ļauj adresēt daudz lielāku atmiņu, nekā 32 bitu sistēmas. Tas ir iemesls, kāpēc mūsdienu datoros un operētājsistēmās tiek izmantoti 64 bitu procesori, jo tie var efektīvāk pārvaldīt lielas atmiņas apjomu.

# %%
10**100 # tas ir 1 ar 100 nullēm, un tas ir ļoti liels skaitlis, bet Python to var apstrādāt bez problēmām.
# nāk no https://en.wikipedia.org/wiki/Googol

# %%
a = 10
b = 3

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(b <= 2)

# %%
ir_pilngadigs = True
ir_registrets = False

print(ir_pilngadigs and ir_registrets)
print(ir_pilngadigs or ir_registrets)
print(not ir_registrets)

# %% [markdown]
# ## Boolean algebra
# 
# Tātad patiesuma vertības nāk no https://en.wikipedia.org/wiki/Boolean_algebra

# %% [markdown]
# ### Uzdevums
# Izveidojiet divus skaitļus un:
# - saskaitiet tos
# - salīdziniet tos
# - izveidojiet vienu loģisku izteiksmi ar `and` vai `or`

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 8. Ievade ar `input()`
# 
# Funkcija `input()` ļauj saņemt ievadi no lietotāja.
# 
# Svarīgi:
# - `input()` rezultāts pēc noklusējuma ir teksts (`str`)
# - ja vajag skaitli, parasti jālieto `int()` vai `float()`

# %%
vards = input("Ievadiet savu vārdu: ")
print("Sveiki,", vards)

# %%
gads = int(input("Ievadiet savu dzimšanas gadu: "))
print("Jūsu ievadītais gads:", gads)

# %% [markdown]
# ### Uzdevums
# Uzrakstiet programmu, kas:
# - prasa lietotājam ievadīt savu vārdu
# - prasa ievadīt vecumu
# - izvada īsu sveicienu

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 9. Teksta apstrādes pamati
# 
# Python valodā teksts ir ļoti bieži lietots datu tips.
# Apskatīsim dažas noderīgas darbības ar tekstu.

# %%
teksts = "Python"
print(teksts[0]) # Python indeksēšana sākas no 0, tāpēc teksts[0] atgriež pirmo burtu "P".
print(teksts[1])
print("Garums", len(teksts))

# %%
# Python piedāva dubulto indeksāciju arī no beigām ar negativiem indeksiem
print("Pēdējais burts:", teksts[-1]) # tas atgriež pēdējo burtu "n"
print("Otrais no beigām:", teksts[-2]) # tas atgriež otro burtu no beigām "o"

# %% [markdown]
# ![Python string operations](https://developers.google.com/static/edu/python/images/hello.png)

# %%
teksts = "  Riga  "

print(teksts)
print(teksts.strip())
print(teksts.lower())
print(teksts.upper())
# jāņem vēra, ka šis operācijas nemodificē oriģinālo tekstu, bet atgriež jaunu tekstu ar veiktajām izmaiņām. 
# Ja mēs gribētu saglabāt izmaiņas, mums būtu jāpiešķir rezultāts atpakaļ mainīgajam teksts, piemēram:
tira_riga = teksts.strip()
print(tira_riga)

# %%
vards = "Anna"
uzvards = "Bērziņa"

# conkatenation (salikšana) ar + operatoru
pilns_vards = vards + " " + uzvards
print(pilns_vards)

# %% [markdown]
# ### Piezīme
# Noderīgas darbības:
# - `len(teksts)` — garums
# - `teksts.lower()` — mazie burti
# - `teksts.upper()` — lielie burti
# - `teksts.strip()` — noņem tukšumus sākumā un beigās

# %% [markdown]
# ### Uzdevums
# Izveidojiet mainīgo ar tekstu, kuram sākumā un beigās ir atstarpes.
# Pēc tam:
# - izdrukājiet oriģinālo tekstu
# - izdrukājiet tekstu bez liekām atstarpēm
# - izdrukājiet to tikai ar lielajiem burtiem
# - izdrukājiet teksta garumu

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 10. Nosacījumi ar `if`, `elif`, `else`
# 
# Nosacījumi ļauj programmā pieņemt lēmumus.

# %%
vecums = 12

# ieverojam nav obligatas iekavas ap nosacījumu, ja tas ir tikai viens nosacījums, bet es izvēlos tās izmantot, lai padarītu kodu skaidrāku un vieglāk lasāmu.
if vecums >= 18: # otrs ievērojam ka pēc : nāk atkāpe, un viss kas ir zemāk un ievelkts tiek uzskatīts par daļu no if nosacījuma bloka. Ja nosacījums ir patiess, tad tiek izpildīts viss, kas ir ievelkts zem if. Ja nosacījums ir nepaties, tad tiek izpildīts viss, kas ir ievelkts zem else.
    # izveidojas zarojums, un mēs varam izpildīt dažādas darbības atkarībā no nosacījuma patiesuma vai nepatiesuma.
    print("Pilngadīgs")
else:
    print("Nepilngadīgs")
    # esam otrā zarā, un varam izpildīt citas darbības, 
    # piemēram, izvadīt citu tekstu vai veikt citas pārbaudes.
# te esam āra no zarojumiem un esam uz pamatceļa, un varam turpināt izpildīt citas darbības, kas nav saistītas ar if-else nosacījumu.
print("Vienmēr izpildīsies, jo tas nav saistīts ar if-else nosacījumu.")

# %% [markdown]
# ## Daudz zarojumi
# 
# Python var zaroties daudzos līmeņos, bet praksē ieteicams vairāk par 3-4 nezarojumiem neveidot, lai kods būtu viegli saprotams.

# %%
# elif mums ļauj pārbaudīt vairākus nosacījumus pēc kārtas, un izpildīt atbilstošo bloku, ja kāds no nosacījumiem ir patiess. Ja neviens nosacījums nav patiess, tad tiek izpildīts else bloks (ja tas ir definēts).
punkti = 85 # iedomāsimies ka šeit dati nāk no kādas datubāzes vai tiek aprēķināti, un mēs vēlamies izvadīt atbilstošu tekstu atkarībā no punktu skaita.

if punkti >= 90:
    print("Izcili")
elif punkti >= 70:
    print("Labi")
else:
    print("Jāuzlabo")

# %%
# ja vajag pārbaudīt vai kāds skaitlis ir diapazona ir divi varianti
skaitlis = 15
if 10 <= skaitlis <= 20:
    print("Skaitlis ir diapazonā no 10 līdz 20")    
# else nav obligāts, un ja mums nav nepieciešams veikt kādas darbības, kad skaitlis nav diapazonā, tad mēs varam vienkārši izlaist else daļu.

# %%
# var arī lietot garo formu, bet tas ir mazāk ērti un mazāk lasāms:
if skaitlis >= 10 and skaitlis <= 20:
    print("Skaitlis ir diapazonā no 10 līdz 20")

# %% [markdown]
# ### Svarīgi
# - Aiz nosacījuma jāliek kols `:`
# - Koda bloki jāatkāpina ar atstarpēm (parasti 4 atstarpes)
# - Python izmanto atkāpes kā daļu no sintakses

# %% [markdown]
# ### Uzdevums
# Uzrakstiet programmu, kas:
# - pārbauda skaitli
# - ja tas ir pozitīvs, izvada `Pozitīvs`
# - ja tas ir negatīvs, izvada `Negatīvs`
# - citādi izvada `Nulle`

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 11. Cikls `for`
# 
# Cikls `for` ļauj atkārtot darbības vairākas reizes.

# %%
for i in range(5): #ieverojam atkal atkāpe pēc :
    print(i)

# %%
# varam uzstādīt sākumu un beigu vērtību, piemēram, range(1, 6) izvadīs skaitļus no 1 līdz 5 (beigu vērtība nav iekļauta)
for skaitlis in range(1, 6):
    print("Skaitlis:", skaitlis)

# %%
# var uzstādīt soli arī
for skaitlis in range(0, 11, 2): # tas izvadīs pāra skaitļus no 0 līdz 10
    print("Pāra skaitlis:", skaitlis)

# solis var būt negatīvs bet jābūt veselam skaitlim, piemēram, range(5, 0, -1) izvadīs skaitļus no 5 līdz 1
for skaitlis in range(5, 0, -1):
    print("Skaitlis:", skaitlis)

# %%
# tipisks paņēmies ar for ciklu ir iziet cauri katram elementam kādā kolekcijā, piemēram, tekstā, sarakstā vai vārdnīcā. Šeit mēs iziesim cauri katram burtam tekstā "Python" un izvadīsim to uz ekrāna.
# string - teksts tādad ir virkne/kolekcija ar simboliem/burtiem, un mēs varam iziet cauri katram simbolam ar for ciklu.
# tehniski Python nav simboli/char, ir tikai stringi, arī 1 garuma
for burts in "Python":
    print(burts)

# %% [markdown]
# ### Piezīme
# `range(5)` dod skaitļus:
# `0, 1, 2, 3, 4`
# 
# `range(1, 6)` dod skaitļus:
# `1, 2, 3, 4, 5`

# %% [markdown]
# ### Uzdevums
# 1. Izdrukājiet skaitļus no 1 līdz 10  
# 2. Izdrukājiet tikai pāra skaitļus no 2 līdz 10  
# 3. Izdrukājiet katru burtu no sava vārda atsevišķā rindā

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 12. Cikls `while`
# 
# Cikls `while` atkārtojas, kamēr nosacījums ir patiess.

# %%
# pamatdoma while cikls ir nenoteiktu reižu atkārtošana, kamēr ir spēkā kāds nosacījums. Šeit mēs izvadīsim skaitļus no 1 līdz 5, izmantojot while ciklu.
x = 1

while x <= 5:
    print(x)
    x += 1 # tas ir tas pats kas x = x + 1, un tas palielina x vērtību par 1 katrā iterācijā, līdz x kļūst lielāks par 5, un cikls beidzas.

# %% [markdown]
# ### Svarīgi
# Ja ciklā aizmirst mainīt mainīgā vērtību, cikls var kļūt bezgalīgs.

# %% [markdown]
# ### Uzdevums
# Uzrakstiet `while` ciklu, kas izdrukā skaitļus no 1 līdz 7.

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 13. Sarakstu pamati
# 
# Saraksts (`list`) ļauj glabāt vairākas vērtības vienā mainīgajā.

# %%
pilsetas = ["Rīga", "Liepāja", "Daugavpils", "Ogre", "Jelgava"]

# tā pati indeksācija kas ir string strādas arī list
print(pilsetas)
print(pilsetas[0])
print(pilsetas[1])
print(len(pilsetas))

# %%
pilsetas = ["Rīga", "Liepāja"]
pilsetas.append("Jelgava") # šī darbība modificē oriģinālo sarakstu, un pievieno jaunu elementu "Jelgava" saraksta beigās.

print(pilsetas)

# %%
nodaļas = ["IT", "HR", "Finanses"]

for nodala in nodaļas:
    print("Nodaļa:", nodala)

# %% [markdown]
# ### Uzdevums
# Izveidojiet sarakstu ar vismaz 3 elementiem.
# Pēc tam:
# - izdrukājiet visu sarakstu
# - izdrukājiet pirmo elementu
# - pievienojiet vēl vienu elementu ar `append()`
# - izdrukājiet sarakstu vēlreiz

# %%
# Rakstiet savu kodu šeit

# %% [markdown]
# # 14. Funkciju pamati
# 
# Funkcija ļauj:
# - atkārtoti izmantot kodu
# - padarīt programmu saprotamāku
# - sadalīt lielāku uzdevumu mazākās daļās - skaldi un valdi princips

# %%
# python sintakse funkcijām ir šāda
# def atslēgas vārds un tad funkcijas nosaukums, un iekavas, kur var ievietot parametrus, un pēc tam : un atkāpe, un viss kas ir ievelkts zem funkcijas definīcijas tiek uzskatīts par daļu no funkcijas.
def sasveicinaties(): # atceramies ka pēc : nāk atkāpe, un viss kas ir ievelkts zem funkcijas definīcijas tiek uzskatīts par daļu no funkcijas.
    print("Sveiki!")
    print("Patiešām prieks!")
    # Te vel funkcijas definīcijas turpinās
# šeit jau ir beigusies funkcijas definīcija, un mēs esam atpakaļ uz pamatlīmeņa, un varam turpināt rakstīt citu kodu, kas nav saistīts ar funkciju sasveicinaties.

# pēc šūnas palaišanas mums ir piekļuve funkcijai sasveicinaties, un mēs varam to izsaukt jebkurā vietā kodā, un tā izpildīs visu, kas ir ievelkts zem tās definīcijas.

# %%
# tātad ja mums ir jau palaista iepriekšējā šūna, kurā ir definēta funkcija sasveicinaties, tad mēs varam izsaukt šo funkciju, un tā izpildīs visu, kas ir ievelkts zem tās definīcijas, šajā gadījumā izvadīs "Sveiki!" uz ekrāna.
sasveicinaties()

# %% [markdown]
# ### Piezīme
# Funkcija vispirms ir jādefinē, un tikai pēc tam to var izsaukt.

# %%
# vards ir funkcijas parametrs, 
# un tas ir kā mainīgais, 
# kas tiek definēts funkcijas iekšpusē, 
# un tam tiek piešķirta vērtība, kad mēs izsaucam funkciju. Šajā gadījumā, kad mēs izsaucam funkciju sasveicinaties_ar_vardu("Anna"), vards būs "Anna" funkcijas iekšpusē, un tāpēc funkcija izvadīs "Sveiki, Anna".
def sasveicinaties_ar_vardu(vards):
    print("Sveiki,", vards)
    # vards šeit vēl ir pieejams
    print(f"Vārds funkcijas iekšpusē ir: {vards}")
# šeit jau vards nebūs pieejams, jo mēs esam ārā no funkcijas definīcijas, un vards ir tikai funkcijas iekšpusē.

# %%
# šī funkcija jau ir eleastīga, jo ņems pretīs jebkuru vārdu, ko mēs ievadīsim kā argumentu, un izvadīs to sveicienā. Mēs varam izsaukt šo funkciju ar dažādiem vārdiem, un tā izvadīs atbilstošu sveicienu katram no tiem.
sasveicinaties_ar_vardu("Anna")
sasveicinaties_ar_vardu("Jānis")

# %%
# nākošais solis ir funkcijas kas atgriež vērtību, nevis tikai izvada to uz ekrāna. Šeit mēs definēsim funkciju saskaitit, kas ņem divus parametrus a un b, un atgriež to summu.
def saskaitit(a, b):
    # es varētu veikt arī kādas darbības šeit ar a un b, piemēram, pārbaudīt vai tie ir skaitļi, vai veikt kādas citas operācijas, bet šeit es vienkārši atgriežu to summu.
    return a + b

# %%
rezultats = saskaitit(5, 7) # ja funkcija atgriež vērtību, mēs varam to saglabāt mainīgajā rezultats, un pēc tam izvadīt šo rezultātu uz ekrāna.
print(rezultats)

# %% [markdown]
# ### Atšķirība starp `print` un `return`
# 
# - `print(...)` parāda rezultātu ekrānā
# - `return ...` atdod rezultātu tālākai izmantošanai

# %%
def kvadrats(x):
    return x * x

print(kvadrats(4))
print(kvadrats(9))

# %%
# drukāt kvadrātu funkcija
def print_kvadrats(x):
    print(f"{x} kvadrāts ir {x * x}") # print ir tā saucamais blakusefekts, jo tas izvada tekstu uz ekrāna, bet neatgriež vērtību, un tāpēc mēs nevaram izmantot šo funkciju kā daļu no citas darbības, piemēram, saskaitīt ar citu skaitli.
    # tehniski ši funkcija ir Return None, pēc noklusējuma

print_kvadrats(4) # rezultāts nekur netiek saglabāts, bet tiek izvadīts uz ekrāna, un funkcija neatgriež vērtību, tāpēc mēs nevaram to izmantot kā daļu no citas darbības, piemēram, saskaitīt ar citu skaitli.
print_kvadrats(9)

# %%
# mēs varejām izmanto funkciju kvadrāts pie drukas
# definesim vēl vienu drukas funkciju
def atkal_drukat_kvadrats(x):
    mans_kvadrats = kvadrats(x) # šeit mēs varam izmantot funkciju kvadrats, jo tā atgriež vērtību, un mēs varam šo vērtību saglabāt mainīgajā mans_kvadrats, un pēc tam izvadīt to uz ekrāna.
    print(f"{x} kvadrāts ir {mans_kvadrats}")
    # šeit vēl ir pieejams iekšējais mainīgasi mans_kvadrats
# šeit vair šāda mainīgā nav

# izdrukāsim
atkal_drukat_kvadrats(4)
atkal_drukat_kvadrats(9)


# %%
# es protams varēju saglabāt kvadratus globāli
kvadrats_4 = kvadrats(4)
kvadrats_9 = kvadrats(9)
# te ir arī vērts padomāt vai nav ērtāk glabāt kvadrātus kāda kopējā datu struktūrā
# piemēram sarakstā

# %%
# mēs varam gan drukāt gan atgriezt vērtības vienā funkcijā
def drukat_un_atgriezt_kvadrats(x):
    kvadrats_x = kvadrats(x) # šeit mēs varam izmantot funkciju kvadrats, jo tā atgriež vērtību, un mēs varam šo vērtību saglabāt mainīgajā kvadrats_x, un pēc tam izvadīt to uz ekrāna.
    print(f"{x} kvadrāts ir {kvadrats_x}")
    return kvadrats_x # un šeit mēs atgriežam šo vērtību, lai to varētu izmantot kā daļu no citas darbības, piemēram, saskaitīt ar citu skaitli.

kvadrats_5 = drukat_un_atgriezt_kvadrats(5) # šeit mēs izsaucam funkciju, un tā gan izvada tekstu uz ekrāna, gan atgriež kvadrātu, ko mēs saglabājam mainīgajā kvadrats_5, un pēc tam varam izmantot šo mainīgo kā daļu no citas darbības, piemēram, saskaitīt ar citu skaitli.
print("Kvadrāts no 5 ir:", kvadrats_5)

# %% [markdown]
# ### Uzdevums
# Izveidojiet:
# 1. funkciju, kas izdrukā sveicienu  
# 2. funkciju, kas pieņem vienu skaitli un atgriež tā dubultvērtību  
# 3. funkciju, kas pārbauda, vai skaitlis ir pāra skaitlis

# %%
# Rakstiet savu kodu šeit 
# tātad rakstam def tad savu funkciju tad parametrus un tad darāmo pēc atkāpes un : un viss kas ir ievelkts zem funkcijas definīcijas tiek uzskatīts par daļu no funkcijas.

# %% [markdown]
# # 15. Tipiskās kļūdas
# 
# Mācoties Python, bieži sastopamas šādas kļūdas:
# - aizmirstas pēdiņas tekstam
# - aizmirsts kols `:`
# - nepareizas atkāpes
# - izmantots nedefinēts mainīgais
# - sajaukti datu tipi

# %% [markdown]
# ### Uzdevums: izlabo kļūdas
# 
# Palaidiet šīs šūnas pa vienai un mēģiniet saprast kļūdu.
# Pēc tam izlabojiet tās.

# %%
# Kļūda 1
# print(Hello)

# %%
# Kļūda 2
# if 5 > 2
#     print("pareizi")

# %%
# Kļūda 3
# print(nezinams_mainigais)

# %% [markdown]
# # 16. Mini praktiskais darbs
# 
# ## Uzdevums
# Izveidojiet vienkāršu programmu, kas:
# 1. prasa lietotājam ievadīt vārdu
# 2. prasa ievadīt vecumu
# 3. izvada atbilstošu ziņu:
#    - ja vecums ir mazāks par 18
#    - ja vecums ir 18 vai vairāk
# 4. izmanto vismaz vienu funkciju

# %%
# Rakstiet savu risinājumu šeit

# %% [markdown]
# # 17. Papildu uzdevumi ātrākajiem studentiem
# 
# Ja pamatuzdevumi jau izpildīti, pamēģiniet:
# 
# 1. Uzrakstīt funkciju, kas pieņem vārdu un pilsētu un izvada pilnu teikumu  
# 2. Uzrakstīt ciklu, kas saskaita skaitļus no 1 līdz 10  
# 3. Izveidot sarakstu ar 5 skaitļiem un izdrukāt tikai tos, kas ir lielāki par 10  
# 4. Uzrakstīt funkciju, kas atgriež `True`, ja teksts nav tukšs

# %%
# Papildu darbs

# %% [markdown]
# # 18. Kopsavilkums
# 
# Šajā notebook mēs apguvām:
# - `print()`
# - notebook šūnu tipus
# - Markdown pamatus
# - mainīgos
# - datu tipus
# - operatorus
# - `input()`
# - tekstu apstrādi
# - `if`, `elif`, `else`
# - `for` un `while`
# - sarakstu pamatus
# - funkciju pamatus
# 
# ## Ko vēl neapskatījām
# Apzināti šodien neapskatījām:
# - klases un objektorientētu programmēšanu
# - dekoratorus
# - ģeneratorus
# - ārējās bibliotēkas
# - failu apstrādi
# - moduļus
# 
# To darīsim vēlāk, kad būs droši apgūti pamati.


