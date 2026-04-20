# 5. dienas nodarbības plāns - no kopsavilkuma tabulām uz ievadu mašīnmācīšanās pamatos

## Dienas fokuss
5. diena sākas ar 4. dienā nepabeigtā darba pabeigšanu: attīrītu datu kopsavilkšanu un skaidru vizualizāciju izveidi. Tas nav novirzījums no mašīnmācīšanās, bet gan nepieciešamais tilts uz to. Dalībnieki vispirms pabeidz analīzei gatavas tabulas, grupētus kopsavilkumus un diagrammas no sagatavotas datu kopas, un tikai pēc tam pāriet uz uzraudzītās mācīšanās pamatiem. Uzsvars ir praktisks: saprast, kā no attīrītas tabulas nonāk līdz modeļa ievadei, kā izvēlēties mērķa mainīgo, kā atdalīt treniņam un testēšanai paredzētos datus un kā novērtēt vienkāršas prognozes.

## Mērķi
- Pabeigt grupētos kopsavilkumus un vizuālos rezultātus, kas palika nepabeigti 4. dienā
- Savienot aprakstošo analīzi ar pirmajiem prognozēšanas soļiem
- Izprast uzraudzītās mašīnmācīšanās pamata darba plūsmu
- Sagatavot pazīmes un mērķa kolonnu no jau attīrītas datu kopas
- Izveidot vienu vienkāršu regresijas piemēru un vienu vienkāršu klasifikācijas piemēru
- Novērtēt modeļa rezultātus ar pamata rādītājiem un izrunāt ierobežojumus

## Priekšzināšanas
- Python pamati no 1. dienas
- Tīrīšanas un transformēšanas idejas no 2. dienas
- `Pandas` filtrēšana, grupēšana, savienošana un datu formas maiņa no 3. un 4. dienas
- Attīrīta 4. dienas datu kopa, ko var vispirms apkopot un pēc tam izmantot modelēšanai
- Pamata drošība darbā ar tabulām, diagrammām un analītisku jautājumu formulēšanu

## Tēmu secība

### 1. Pabeidzam 4. dienas neizdarīto
- Īss atgādinājums par 4. dienas darba plūsmu: `load -> inspect -> clean -> filter -> combine -> summarize -> reshape -> visualize -> export`
- Atveram 4. dienā sagatavoto datu kopu un nosakām, kas palicis nepabeigts
- Pabeidzam vienu vai divus grupētos kopsavilkumus ar `groupby()`, `agg()` vai `pivot_table()`
- Pārvēršam kopsavilkumu lietojamā diagrammā ar `Pandas` vai `matplotlib`
- Nostiprinām ideju, ka modelēšana sākas tikai tad, kad datu darba plūsma jau ir stabila

### 2. Pāreja no analīzes uz mašīnmācīšanos
- Aprakstošs jautājums pret prognozēšanas jautājumu
- Kāpēc kopsavilkumi un diagrammas joprojām ir svarīgi pirms modeļa veidošanas
- Piemēri:
  - analīze: "Kuram reģionam bija lielākie pārdošanas apjomi iepriekšējā mēnesī?"
  - prognoze: "Kādu pārdošanas vērtību varētu sagaidīt nākamajā mēnesī?"
- Pazīmju, mērķa un vēsturisko novērojumu loma

### 3. Mašīnmācīšanās darba plūsmas pārskats
- Problēmas formulēšana
- Mērķa kolonnas izvēle
- Ievades pazīmju izvēle
- Treniņa un novērtējuma datu atdalīšana
- Modeļa apmācīšana
- Prognožu izveide
- Pārbaude, vai modelis vispār ir noderīgs
- Brīdinājums, ka mašīnmācīšanās modelis neaizstāj datu tīrīšanu, validāciju un nozares izpratni

### 4. Modelim gatavu datu sagatavošana
- Atkārtoti izmantojam 4. dienā attīrīto un papildināto tabulu, nevis atgriežamies pie neapstrādātiem failiem
- Izvēlamies kandidātu kolonnas modelēšanai
- Apstrādājam trūkstošās vērtības vai izņemam nederīgās rindas
- Pārvēršam kategoriskās kolonnas modelim lietojamā formā
- Atdalām:
  - `X` pazīmēm
  - `y` mērķim
- Izvairāmies no datu noplūdes, neizmantojot kolonnas, kuras jau satur atbildi

### 5. Vienkārša regresija
- Kad regresija ir pareizā izvēle
- Skaitliska mērķa piemērs, piemēram, pārdošanas summa, ieņēmumi vai vienību skaits
- `train_test_split`
- Vienkārša regresijas modeļa apmācīšana
- Prognozēto un faktisko vērtību salīdzinājums
- Pamata rādītāji:
  - `MAE`
  - `RMSE`
  - `R^2`
- Piesardzīga rezultātu interpretācija, neuztverot prognozi kā drošu patiesību

### 6. Vienkārša klasifikācija
- Kad klasifikācija ir pareizā izvēle
- Praktiska jautājuma pārvēršana klasēs, piemēram:
  - augsti pret zemi pārdošanas apjomi
  - mērķis sasniegts pret mērķis nav sasniegts
- Vienkārša klasifikācijas modeļa apmācīšana
- Klašu prognožu iegūšana
- Pamata rādītāji:
  - accuracy
  - precision
  - recall
- Sapratne, ka dažādu kļūdu cena var atšķirties

### 7. Novērtēšana, interpretācija un ierobežojumi
- Kāpēc ar labu rezultātu treniņa datos vien nepietiek
- Pārpielāgošanās (`overfitting`) vienkāršā valodā
- Atšķirība starp noderīgu bāzes modeli un reālai izmantošanai gatavu modeli
- Rādītāju lasīšana kopā ar diagrammām un grupētiem kopsavilkumiem
- Situācijas, kad vienkāršs grupēts pārskats ir noderīgāks par modeli

### 8. Kopsavilkums un pāreja uz noslēguma darbu
- Atkārtojam pilno plūsmu:
  - attīrīti dati
  - kopsavilkuma tabula
  - diagramma
  - modeļa ievade
  - prognoze
  - novērtēšana
- Nosakām, kuras daļas jau ir pietiekami stabilas izmantošanai noslēguma mini-projektā vai nākamo paplašinājumu vajadzībām

## Praktiskā daļa

### Uzdevums 1 - pabeigt trūkstošo kopsavilkumu un diagrammu
- Izmantot 4. dienā sagatavoto datu kopu
- Izveidot vismaz vienu grupētu kopsavilkuma tabulu
- Izveidot vienu diagrammu, kas atbild uz skaidru jautājumu no šī kopsavilkuma
- Saglabāt rezultātu esošajā darba plūsmā

### Uzdevums 2 - sagatavot datus modelēšanai
- Izvēlēties vienu mērķa kolonnu
- Izvēlēties nelielu skaitu noderīgu pazīmju kolonnu
- Noņemt vai izlabot trūkstošās vērtības, kas traucē modelim
- Atdalīt datus `X` un `y`
- Izveidot treniņa un testa kopas

### Uzdevums 3 - izveidot vienkāršu regresijas modeli
- Lietot skaitlisku mērķa kolonnu
- Apmācīt modeli ar treniņa datiem
- Iegūt prognozes testa datiem
- Apskatīt dažas prognozētās un faktiskās vērtības
- Parādīt vienu vai divus novērtējuma rādītājus

### Uzdevums 4 - izveidot vienkāršu klasifikācijas modeli
- Izveidot vai izvēlēties kategorisku mērķa kolonnu
- Apmācīt klasifikatoru
- Iegūt prognozes testa datiem
- Pārbaudīt pamata klasifikācijas rādītājus
- Izrunāt, kuras kļūdas būtu sāpīgākas

### Uzdevums 5 - vai mašīnmācīšanās šeit patiešām dod vērtību
- Salīdzināt modeļa rezultātus ar grupētajiem kopsavilkumiem un diagrammām
- Noteikt vienu situāciju, kur aprakstoša analīze ir pietiekama
- Noteikt vienu situāciju, kur prognoze būtu noderīga
- Nosaukt vienu pašreizējās datu kopas vai darba plūsmas ierobežojumu

## Ieteicamais laika sadalījums
- 20 min - 4. dienas statusa atkārtojums un nepabeigto kopsavilkumu pabeigšana
- 25 min - vizualizāciju pabeigšana un diagrammu izvēles apspriešana
- 20 min - pāreja no aprakstošās analīzes uz mašīnmācīšanās domāšanu
- 20 min - mašīnmācīšanās darba plūsmas pārskats un termini
- 25 min - pazīmju, mērķa un train/test sadalījuma sagatavošana
- 30 min - vienkāršas regresijas piemērs
- 30 min - vienkāršas klasifikācijas piemērs
- 20 min - novērtēšana, interpretācija un tipiskās kļūdas
- 35 min - vadīts praktiskais darbs, apskats un noslēgums

## Dienas rezultāts
Pēc 5. dienas dalībnieki var pabeigt nelielu atskaites darba plūsmu no attīrītas datu kopas, izveidot kopsavilkuma tabulu un diagrammu un pēc tam izmantot to pašu sagatavoto datu kopu vienkāršam uzraudzītās mašīnmācīšanās piemēram. Viņi saprot, ka mašīnmācīšanās modelis balstās uz kvalitatīvu datu sagatavošanu, nevis to aizstāj, un prot atšķirt aprakstošās atskaites no vienkāršiem prognozēšanas uzdevumiem.

## Saikne ar noslēguma projektu
Noslēguma projekts var palikt galvenokārt datu darba plūsmas un atskaites uzdevums, mašīnmācīšanos pievienojot tikai tad, ja tā palīdz atbildēt uz realistisku prognozēšanas jautājumu. Pēc 5. dienas dalībniekiem būtu jāsaprot, ka labi dokumentēta, tīrīta un uzticama kopsavilkumu darba plūsma jau pati par sevi ir vērtīgs rezultāts, bet vienkāršs modelis ir papildu iespēja, ja jautājums patiešām prasa prognozi.
