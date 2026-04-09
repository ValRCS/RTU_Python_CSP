"""Python pamati secīgai izpildei.

Šajā failā apvienoti piezīmju grāmatas piemēru kodi un īsas piezīmes.
Ej cauri failam no augšas uz leju, palaid sadaļas un papildini
komentētos uzdevumus ar saviem piemēriem.
"""

# 1. Pirmais Python kods
print("Sveika, Python pasaule!")

# Pamēģini pats:
# print("Mani sauc ...")
# print("Es strādāju ...")


# 2. Mainīgie un vienkārši aprēķini
x = 10
print("x vērtība ir:", x)
print("x + 5 =", x + 5)

# Pamēģini pats:
# y = 7
# print("y =", y)
# print("y + 2 =", y + 2)
# print("y * 3 =", y * 3)


# 3. Mainīgie un vērtību pārrakstīšana
vards = "Anna"
vecums = 32
pilseta = "Rīga"

print(vards)
print(vecums)
print(pilseta)

skaits = 5
print("Sākumā:", skaits)

skaits = 8
print("Pēc pārrakstīšanas:", skaits)

# Pamēģini pats:
# amats = "Analītiķis"
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

# type() parāda, kāda tipa ir vērtība.
# Pamēģini pats:
# mans_teksts = "Sveiki"
# mans_skaitlis = 25
# mans_decimals = 3.14
# mans_statuss = False
# print(type(mans_teksts))
# print(type(mans_skaitlis))
# print(type(mans_decimals))
# print(type(mans_statuss))


# 5. Pārveidošana starp tipiem
skaitlis_teksta = "123"
skaitlis = int(skaitlis_teksta)
print(skaitlis)
print(type(skaitlis))

vecums = 35
teksts = str(vecums)
print(teksts)
print(type(teksts))

# Pamēģini pats:
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

# Pamēģini pats:
# c = 8
# d = 5
# print(c + d)
# print(c > d)
# print(c > 0 and d > 0)


# 7. Ievade ar input()
# input() ir noderīgs, bet to parasti grib palaist apzināti.
# Atkomentē zemāk esošo funkcijas izsaukumu, kad gribi patestēt ievadi.
def ievades_piemeri():
    vards = input("Ievadiet savu vārdu: ")
    print("Sveiki,", vards)

    gads = int(input("Ievadiet savu dzimšanas gadu: "))
    print("Jūsu ievadītais gads:", gads)


# ievades_piemeri()

# Pamēģini pats:
# lietotaja_vards = input("Ievadi savu vārdu: ")
# lietotaja_vecums = input("Ievadi savu vecumu: ")
# print("Sveiki,", lietotaja_vards)
# print("Tev ir", lietotaja_vecums, "gadi.")


# 8. Teksta apstrādes pamati
teksts = "Python"
print(teksts[0])
print(teksts[1])
print(len(teksts))

teksts = "  Rīga  "
print(teksts)
print(teksts.strip())
print(teksts.lower())
print(teksts.upper())

vards = "Anna"
uzvards = "Bērziņa"
pilns_vards = vards + " " + uzvards
print(pilns_vards)

# Noderīgas darbības ar tekstu:
# len(teksts), teksts.lower(), teksts.upper(), teksts.strip()
#
# Pamēģini pats:
# mans_teksts = "  Programmēšana  "
# print(mans_teksts)
# print(mans_teksts.strip())
# print(mans_teksts.lower())
# print(mans_teksts.upper())


# 9. Nosacījumi ar if, elif, else
vecums = 20

if vecums >= 18:
    print("Pilngadīgs")
else:
    print("Nepilngadīgs")

punkti = 85

if punkti >= 90:
    print("Izcili")
elif punkti >= 70:
    print("Labi")
else:
    print("Jāuzlabo")

# Svarīgi:
# aiz nosacījuma jāliek :
# koda bloki jāatkāpina ar atstarpēm
#
# Pamēģini pats:
# skaitlis = 4
# if skaitlis > 0:
#     print("Pozitīvs")
# elif skaitlis < 0:
#     print("Negatīvs")
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
# Pamēģini pats:
# for skaitlis in range(1, 11):
#     print(skaitlis)
#
# for skaitlis in range(2, 11, 2):
#     print("Pāra skaitlis:", skaitlis)


# 11. Cikls while
x = 1

while x <= 5:
    print(x)
    x += 1

# Uzmanies no bezgalīga cikla:
# ja aizmirsti mainīt nosacījuma mainīgo, cikls var nebeigties.
#
# Pamēģini pats:
# y = 1
# while y <= 7:
#     print(y)
#     y += 1


# 12. Sarakstu pamati
pilsetas = ["Rīga", "Liepāja", "Daugavpils"]
print(pilsetas)
print(pilsetas[0])
print(pilsetas[1])
print(len(pilsetas))

pilsetas = ["Rīga", "Liepāja"]
pilsetas.append("Jelgava")
print(pilsetas)

nodalas = ["IT", "HR", "Finanses"]
for nodala in nodalas:
    print("Nodaļa:", nodala)

# Pamēģini pats:
# mani_elementi = ["sarkans", "zils", "zaļš"]
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
sasveicinaties_ar_vardu("Jānis")


def saskaitit(a, b):
    return a + b


rezultats = saskaitit(5, 7)
print(rezultats)


def kvadrats(x):
    return x * x


print(kvadrats(4))
print(kvadrats(9))

# print() izvada rezultātu ekrānā.
# return atdod rezultātu tālākai izmantošanai.
#
# Pamēģini pats:
# def dubultot(skaitlis):
#     return skaitlis * 2
#
# print(dubultot(6))


# 14. Tipiskās kļūdas
# Šie piemēri ir atstāti komentāros, lai fails paliktu izpildāms.

# Kļūda 1: pietrūkst pēdiņu
# print(Hello)

# Kļūda 2: pietrūkst kola
# if 5 > 2
#     print("pareizi")

# Kļūda 3: nezināms mainīgais
# print(nezinams_mainigais)


# 15. Mini praktiskais darbs
# Izveido savu mazo programmu:
# 1. prasi lietotājam ievadīt vārdu
# 2. prasi ievadīt vecumu
# 3. izdrukā īsu ziņojumu
#
# Piemēra karkass:
# vards = input("Ievadi vārdu: ")
# vecums = int(input("Ievadi vecumu: "))
# if vecums >= 18:
#     print(vards, "ir pilngadīgs")
# else:
#     print(vards, "nav pilngadīgs")


# 16. Papildu uzdevumi ātrākajiem studentiem
# Pamēģini izveidot:
# - funkciju, kas aprēķina taisnstūra laukumu
# - ciklu, kas izdrukā tikai nepāra skaitļus
# - sarakstu ar 5 vērtībām un pārbaudi, vai tajā ir konkrēts elements
