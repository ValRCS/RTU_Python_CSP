"""Python pamati secigai izpildei.

Saja faila apvienoti notebook piemeru kodi un isas piezimes.
Ej cauri failam no augstas uz leju, palaid sadalas un papildini
komentetos uzdevumus ar saviem piemeriem.
"""

# 1. Pirmais Python kods
print("Hello Python Pasaule")

# Pamegini pats:
# print("Mani sauc ...")
# print("Es stradaju ...")


# 2. Mainigie un vienkarsi aprekini
x = 10
print("x vertiba ir:", x)
print("x + 5 =", x + 5)

# Pamegini pats:
# y = 7
# print("y =", y)
# print("y + 2 =", y + 2)
# print("y * 3 =", y * 3)


# 3. Mainigie un vertibu parrakstisana
vards = "Anna"
vecums = 32
pilseta = "Riga"

print(vards)
print(vecums)
print(pilseta)

skaits = 5
print("Sakuma:", skaits)

skaits = 8
print("Pec parrakstisanas:", skaits)

# Pamegini pats:
# amats = "Analitikis"
# darba_vieta = "RTU"
# print(vards, amats, darba_vieta)


# 4. Pamata datu tipi
teksts = "Python"
skaits = 10
temperatura = 21.5
ir_aktivs = True

print(type(teksts))
print(type(skaits))
print(type(temperatura))
print(type(ir_aktivs))

# type() parada, kada tipa ir vertiba.
# Pamegini pats:
# mans_teksts = "Sveiki"
# mans_skaitlis = 25
# mans_decimals = 3.14
# mans_statuss = False
# print(type(mans_teksts))
# print(type(mans_skaitlis))
# print(type(mans_decimals))
# print(type(mans_statuss))


# 5. Parveidosana starp tipiem
skaitlis_teksta = "123"
skaitlis = int(skaitlis_teksta)
print(skaitlis)
print(type(skaitlis))

vecums = 35
teksts = str(vecums)
print(teksts)
print(type(teksts))

# Pamegini pats:
# teksts_ar_skaitli = "45"
# print(int(teksts_ar_skaitli))
# skaitlis_ar_komatu = 12.7
# print(type(skaitlis_ar_komatu))
# print(str(skaitlis_ar_komatu))


# 6. Operatori
a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(b <= 2)

ir_pilngadigs = True
ir_registrets = False

print(ir_pilngadigs and ir_registrets)
print(ir_pilngadigs or ir_registrets)
print(not ir_registrets)

# Pamegini pats:
# c = 8
# d = 5
# print(c + d)
# print(c > d)
# print(c > 0 and d > 0)


# 7. Ievade ar input()
# input() ir noderigs, bet to parasti grib palaist apzinati.
# Atkomente zemak esoso funkcijas izsaukumu, kad gribi patestet ievadi.
def ievades_piemeri():
    vards = input("Ievadiet savu vardu: ")
    print("Sveiki,", vards)

    gads = int(input("Ievadiet savu dzimsanas gadu: "))
    print("Jusu ievaditais gads:", gads)


# ievades_piemeri()

# Pamegini pats:
# lietotaja_vards = input("Ievadi savu vardu: ")
# lietotaja_vecums = input("Ievadi savu vecumu: ")
# print("Sveiki,", lietotaja_vards)
# print("Tev ir", lietotaja_vecums, "gadi.")


# 8. Teksta apstrades pamati
teksts = "Python"
print(teksts[0])
print(teksts[1])
print(len(teksts))

teksts = "  Riga  "
print(teksts)
print(teksts.strip())
print(teksts.lower())
print(teksts.upper())

vards = "Anna"
uzvards = "Berzina"
pilns_vards = vards + " " + uzvards
print(pilns_vards)

# Noderigas darbibas ar tekstu:
# len(teksts), teksts.lower(), teksts.upper(), teksts.strip()
#
# Pamegini pats:
# mans_teksts = "  Programmesana  "
# print(mans_teksts)
# print(mans_teksts.strip())
# print(mans_teksts.lower())
# print(mans_teksts.upper())


# 9. Nosacijumi ar if, elif, else
vecums = 20

if vecums >= 18:
    print("Pilngadigs")
else:
    print("Nepilngadigs")

punkti = 85

if punkti >= 90:
    print("Izcili")
elif punkti >= 70:
    print("Labi")
else:
    print("Jauzlabo")

# Svarigi:
# aiz nosacijuma jaliek :
# koda bloki jaatkapina ar atstarpem
#
# Pamegini pats:
# skaitlis = 4
# if skaitlis > 0:
#     print("Pozitivs")
# elif skaitlis < 0:
#     print("Negativs")
# else:
#     print("Nulle")


# 10. Cikls for
for i in range(5):
    print(i)

for skaitlis in range(1, 6):
    print("Skaitlis:", skaitlis)

for burts in "Python":
    print(burts)

# range(5) dod 0, 1, 2, 3, 4
# range(1, 6) dod 1, 2, 3, 4, 5
#
# Pamegini pats:
# for skaitlis in range(1, 11):
#     print(skaitlis)
#
# for skaitlis in range(2, 11, 2):
#     print("Para skaitlis:", skaitlis)


# 11. Cikls while
x = 1

while x <= 5:
    print(x)
    x += 1

# Uzmanies no bezgaliga cikla:
# ja aizmirsti mainit nosacijuma mainigo, cikls var nebeigties.
#
# Pamegini pats:
# y = 1
# while y <= 7:
#     print(y)
#     y += 1


# 12. Sarakstu pamati
pilsetas = ["Riga", "Liepaja", "Daugavpils"]
print(pilsetas)
print(pilsetas[0])
print(pilsetas[1])
print(len(pilsetas))

pilsetas = ["Riga", "Liepaja"]
pilsetas.append("Jelgava")
print(pilsetas)

nodalas = ["IT", "HR", "Finanses"]
for nodala in nodalas:
    print("Nodala:", nodala)

# Pamegini pats:
# mani_elementi = ["sarkans", "zils", "zals"]
# print(mani_elementi)
# print(mani_elementi[0])
# mani_elementi.append("dzeltens")
# print(mani_elementi)


# 13. Funkciju pamati
def sasveicinaties():
    print("Sveiki!")


sasveicinaties()


def sasveicinaties_ar_vardu(vards):
    print("Sveiki,", vards)


sasveicinaties_ar_vardu("Anna")
sasveicinaties_ar_vardu("Janis")


def saskaitit(a, b):
    return a + b


rezultats = saskaitit(5, 7)
print(rezultats)


def kvadrats(x):
    return x * x


print(kvadrats(4))
print(kvadrats(9))

# print() izvada rezultatu ekrana.
# return atdod rezultatu talakai izmantosanai.
#
# Pamegini pats:
# def dubultot(skaitlis):
#     return skaitlis * 2
#
# print(dubultot(6))


# 14. Tipiskas kludas
# Sie piemeri ir atstati komentaros, lai fails paliktu izpildams.

# Kluda 1: pietrukst pedinu
# print(Hello)

# Kluda 2: pietrukst kola
# if 5 > 2
#     print("pareizi")

# Kluda 3: nezinams mainigais
# print(nezinams_mainigais)


# 15. Mini praktiskais darbs
# Izveido savu mazo programmu:
# 1. prasi lietotajam ievadit vardu
# 2. prasi ievadit vecumu
# 3. izdruka isu zinjojumu
#
# Piemera karkass:
# vards = input("Ievadi vardu: ")
# vecums = int(input("Ievadi vecumu: "))
# if vecums >= 18:
#     print(vards, "ir pilngadigs")
# else:
#     print(vards, "nav pilngadigs")


# 16. Papildu uzdevumi atrakajiem studentiem
# Pamegini izveidot:
# - funkciju, kas aprekina taisnstura laukumu
# - ciklu, kas izdrukaa tikai nepara skaitlus
# - sarakstu ar 5 vertibam un parbaudi, vai taja ir konkrets elements
