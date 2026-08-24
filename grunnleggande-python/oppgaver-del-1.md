# Oppgåver: Variablar, navngjeving, operatorar og tekstar

Desse oppgåvene byggjer vidare på det du har jobba med i:

- [01-variabler-input-print.py](01-variabler-input-print.py)
- [02-navngjeving.py](02-navngjeving.py)
- [03-operatorar-utskrift-import-bibliotek.py](03-operatorar-utskrift-import-bibliotek.py)
- [04-tekstar.py](04-tekstar.py)

Lag ei ny `.py`-fil per oppgåve (eller ei fil per del), og test koden din før du ser på løysingsforslaget. Løysingsforslaga er berre **eitt** av fleire moglege svar — så lenge koden din gjer det same og er lett å lese, er det like bra.

**Vanskegrad:** ⭐ enkel · ⭐⭐ middels · ⭐⭐⭐ utfordring

---

## Del A: Variablar, input og print

### Oppgåve 1 ⭐
Lag to variablar, `namn` og `alder`, basert på input frå brukaren (`alder` skal vere eit heiltal). Skriv ut ei helsing med f-string som òg fortel kor gammal brukaren blir *neste* år.

<details>
<summary>💡 Løysingsforslag</summary>

```python
namn = input("Kva heiter du? ")
alder = int(input("Kor gammal er du? "))
print(f"Hei, {namn}! Neste år fyller du {alder + 1} år.")
```

</details>

### Oppgåve 2 ⭐
Ta imot to tal frå brukaren (bruk `float`). Rekn ut summen, differansen og produktet av dei, og skriv ut alle tre resultata med f-strings.

<details>
<summary>💡 Løysingsforslag</summary>

```python
tal1 = float(input("Skriv inn første tal: "))
tal2 = float(input("Skriv inn andre tal: "))

summen = tal1 + tal2
differansen = tal1 - tal2
produktet = tal1 * tal2

print(f"Sum: {summen}")
print(f"Differanse: {differansen}")
print(f"Produkt: {produktet}")
```

</details>

### Oppgåve 3 ⭐⭐
Ta imot lengde og breidde på eit rom (i meter, som `float`). Rekn ut arealet og omkrinsen, og skriv begge ut med **to desimalar**.

<details>
<summary>💡 Løysingsforslag</summary>

```python
lengde = float(input("Lengde på rommet (meter): "))
breidde = float(input("Breidde på rommet (meter): "))

areal = lengde * breidde
omkrins = 2 * (lengde + breidde)

print(f"Arealet er {areal:.2f} m² og omkrinsen er {omkrins:.2f} m.")
```

</details>

### Oppgåve 4 ⭐⭐
`print()` kan ta imot fleire parametre enn det du kanskje har brukt til no. Skriv eit program som:
1. Skriv ut ein dato (dag, månad, år som tre separate variablar) med `sep="-"` slik at det blir sjåande ut som `24-8-2026`.
2. Bruker `end=" "` på eitt `print()`-kall slik at neste `print()` fortset på **same linje**.

<details>
<summary>💡 Løysingsforslag</summary>

```python
dag = 24
manad = 8
ar = 2026
print(dag, manad, ar, sep="-")

print("Dette er starten,", end=" ")
print("og dette kjem rett etter - på same linje.")
```

</details>

### Oppgåve 5 ⭐⭐⭐ (utfordring)
Lag to variablar `a` og `b` med kvar sin verdi. Bytt om verdiane deira **utan** å lage ein tredje hjelpevariabel. (Tips: Python kan tilordne fleire variablar på éi linje, t.d. `x, y = 1, 2`.) Skriv ut verdiane både før og etter byttet.

<details>
<summary>💡 Løysingsforslag</summary>

```python
a = 5
b = 10
print(f"Før bytte: a = {a}, b = {b}")

a, b = b, a

print(f"Etter bytte: a = {a}, b = {b}")
```

</details>

---

## Del B: Navngjeving og konstantar

### Oppgåve 6 ⭐
Koden under reknar ut KMI (kroppsmasseindeks), men er dårleg navngjeven:

```python
x = 180
y = 75
z = x / (y / 100) ** 2
```

Skriv om koden med tydelege, beskrivande variabelnamn, i éin konsekvent navngjevingsstandard (t.d. camelCase eller snake_case).

<details>
<summary>💡 Løysingsforslag</summary>

```python
hoydeCm = 180
vektKg = 75

hoydeM = hoydeCm / 100
kmi = vektKg / hoydeM ** 2

print(f"KMI: {kmi:.1f}")
```

</details>

### Oppgåve 7 ⭐⭐
Lag ein **konstant** `MVA_SATS` sett til `0.25` (25 % meirverdiavgift). Ta imot ein pris utan mva frå brukaren, og rekn ut og skriv ut prisen inkludert mva.

<details>
<summary>💡 Løysingsforslag</summary>

```python
MVA_SATS = 0.25  # 25 % meirverdiavgift

prisUtenMva = float(input("Pris utan meirverdiavgift: "))
prisMedMva = prisUtenMva * (1 + MVA_SATS)

print(f"Pris med mva: {prisMedMva:.2f} kr")
```

</details>

### Oppgåve 8 ⭐⭐
Lag ein funksjon `reknUtOmkrinsSirkel(radius)` som returnerer omkrinsen av ein sirkel (bruk `math.pi`). Hugs: funksjonsnamn bør vere verb som beskriv kva funksjonen gjer. Kall funksjonen og skriv ut resultatet med to desimalar.

<details>
<summary>💡 Løysingsforslag</summary>

```python
import math

def reknUtOmkrinsSirkel(radius):
    omkrins = 2 * math.pi * radius
    return omkrins

print(f"{reknUtOmkrinsSirkel(5):.2f}")
```

</details>

---

## Del C: Operatorar og rekkefølgje

### Oppgåve 9 ⭐
Gjett først kva desse to linjene skriv ut **før** du køyrer koden, skriv gjetninga di som ein kommentar, og sjekk om du hadde rett:

```python
resultat = 3 + 4 * 2 - 6 / 3 ** 2
print(resultat)
```

<details>
<summary>💡 Løysingsforslag</summary>

```python
# Rekkefølgje: eksponent -> gange/deling -> pluss/minus
# 3 ** 2 = 9, altså 6 / 9 = 0.6666...
# 4 * 2 = 8
# 3 + 8 - 0.6666... = 10.3333...
resultat = 3 + 4 * 2 - 6 / 3 ** 2
print(resultat)  # 10.333333333333334
```

</details>

### Oppgåve 10 ⭐⭐
Du skal rekne ut gjennomsnittsprisen på tre varer med prisane 100, 150 og 200 kr. Skriv koden med parentesar slik at du får **rett** svar (tips: utan parentesar rundt summen vil `/` berre gjelde det siste tallet).

<details>
<summary>💡 Løysingsforslag</summary>

```python
pris1 = 100
pris2 = 150
pris3 = 200

gjennomsnitt = (pris1 + pris2 + pris3) / 3
print(f"Gjennomsnittleg pris: {gjennomsnitt:.2f} kr")
```

</details>

### Oppgåve 11 ⭐⭐
Ta imot eit heiltal frå brukaren som representerer talet på sekund som har gått sidan midnatt. Bruk heiltalsdivisjon (`//`) og modulus (`%`) til å rekne ut kor mange timar, minutt og sekund det tilsvarar, og skriv det ut i formatet `TT:MM:SS` (bruk `:02` i f-stringen for å alltid få to sifre).

<details>
<summary>💡 Løysingsforslag</summary>

```python
totalSekund = int(input("Kor mange sekund har gått sidan midnatt? "))

timar = totalSekund // 3600
restSekund = totalSekund % 3600
minutt = restSekund // 60
sekund = restSekund % 60

print(f"{timar:02}:{minutt:02}:{sekund:02}")
```

</details>

### Oppgåve 12 ⭐⭐⭐ (utfordring)
Same idé som oppgåve 11, men no skal du ta imot eit **stort** tal sekund og rekne ut kor mange heile **dagar**, timar, minutt og sekund det utgjer. Du skal berre bruke `//` og `%` — ingen løkker eller if-setningar er nødvendig.

<details>
<summary>💡 Løysingsforslag</summary>

```python
totalSekund = int(input("Skriv inn eit stort tal sekund: "))

dagar = totalSekund // 86400
restEtterDagar = totalSekund % 86400

timar = restEtterDagar // 3600
restEtterTimar = restEtterDagar % 3600

minutt = restEtterTimar // 60
sekund = restEtterTimar % 60

print(f"{dagar} dagar, {timar} timar, {minutt} minutt og {sekund} sekund.")
```

</details>

### Oppgåve 13 ⭐⭐⭐ (utfordring)
Rentesrenteformelen er `sluttbeløp = beløp * (1 + rente) ** antallÅr`, der `rente` er eit desimaltal (t.d. 5 % = 0.05). Ta imot startbeløp, årleg rente i prosent og talet på år frå brukaren, og skriv ut sluttbeløpet med to desimalar. Du treng verken løkke eller if-setning — berre eksponent-operatoren.

<details>
<summary>💡 Løysingsforslag</summary>

```python
belop = float(input("Startbeløp (kr): "))
renteProsent = float(input("Årleg rente i prosent: "))
antallAr = int(input("Kor mange år skal pengane stå? "))

rente = renteProsent / 100
sluttbelop = belop * (1 + rente) ** antallAr

print(f"Etter {antallAr} år har du {sluttbelop:.2f} kr.")
```

</details>

### Oppgåve 14 ⭐⭐⭐ (utfordring)
Modulus (`%`) kan brukast til å sjekke om eit tal er oddetal eller partal (resten etter deling på 2 er anten 0 eller 1). Ta imot eit heiltal frå brukaren, og skriv ut om det er eit oddetal eller eit partal. (Same `if`/`else`-mønster som i eksempelet i [04-tekstar.py](04-tekstar.py).)

<details>
<summary>💡 Løysingsforslag</summary>

```python
tal = int(input("Skriv inn eit heiltal: "))

if tal % 2 == 0:
    print(f"{tal} er eit partal.")
else:
    print(f"{tal} er eit oddetal.")
```

</details>

---

## Del D: Import og bibliotek

### Oppgåve 15 ⭐
Importer `math`-biblioteket. Ta imot eit tal frå brukaren, og skriv ut kvadratrota av det, avrunda til to desimalar.

<details>
<summary>💡 Løysingsforslag</summary>

```python
import math

tal = float(input("Skriv inn eit tal: "))
print(f"Kvadratrota av {tal} er {math.sqrt(tal):.2f}.")
```

</details>

### Oppgåve 16 ⭐⭐
Volumet av ei kule reknar du ut med formelen `(4/3) * π * r³`. Ta imot radiusen frå brukaren, og bruk `math.pi` til å rekne ut og skrive ut volumet, med to desimalar.

<details>
<summary>💡 Løysingsforslag</summary>

```python
import math

radius = float(input("Radius på kula (cm): "))
volum = (4 / 3) * math.pi * radius ** 3

print(f"Volumet av kula er {volum:.2f} cm³.")
```

</details>

### Oppgåve 17 ⭐⭐
`math` er ikkje det einaste innebygde biblioteket i Python. Prøv å importere `random`-biblioteket, og bruk funksjonen `random.randint(1, 100)` til å skrive ut eit tilfeldig heiltal mellom 1 og 100. (Google/dokumentasjonen er lov å bruke her!) Finn ut kva verdiar dette kan returnere, og test programmet fleire gonger. Altså, er det til og med 1 og 100, eller til dømes berre mellom 1 og 99?

Finn ut om random-biblioteket har andre funksjonar som kan vere nyttige, og prøv dei ut.

<details>
<summary>💡 Løysingsforslag</summary>

```python
import random

tilfeldigTal = random.randint(1, 100)
print(f"Det tilfeldige talet er {tilfeldigTal}.")
```

</details>

---

## Del E: Tekstar og strengmanipulering

### Oppgåve 18 ⭐
Ta imot eit filnamn frå brukaren (t.d. `bilde.png`). Bruk slicing (som i [04-tekstar.py](04-tekstar.py)) til å hente ut og skrive ut dei tre siste teikna (filtypen).

<details>
<summary>💡 Løysingsforslag</summary>

```python
filnamn = input("Skriv inn eit filnamn (t.d. bilde.png): ")
filtype = filnamn[-3:]
print(f"Filtypen er .{filtype}")
```

</details>

### Oppgåve 19 ⭐⭐
Lag ein streng `handleliste` med nokre varer, med tilfeldig store og små bokstavar blanda (t.d. `"Melk, BrØd, Ost, Egg, JordbÆr"`). Ta imot ei vare frå brukaren, og sjekk — uavhengig av store/små bokstavar — om ho finst på lista, med `in`-operatoren og `.lower()`.

<details>
<summary>💡 Løysingsforslag</summary>

```python
handleliste = "Melk, BrØd, Ost, Egg, JordbÆr"
vare = input("Kva vil du sjekke om er på handlelista? ")

if vare.lower() in handleliste.lower():
    print(f"Ja, {vare} står på lista!")
else:
    print(f"Nei, {vare} står ikkje på lista.")
```

</details>

### Oppgåve 20 ⭐⭐
Ta imot eit fullt namn (fornamn og etternamn, adskilt med mellomrom) frå brukaren. Lag eit brukarnamn på forma `f.etternamn` (første bokstav i fornamnet + punktum + etternamn), alt med små bokstavar. Bruk `.replace()` til å erstatte `æ`, `ø` og `å` med høvesvis `ae`, `o` og `a`.

<details>
<summary>💡 Løysingsforslag</summary>

```python
navn = input("Skriv inn fullt namn: ")
delar = navn.split(" ")
fornamn = delar[0]
etternamn = delar[-1]

brukarnamn = (fornamn[0] + "." + etternamn).lower()
brukarnamn = brukarnamn.replace("æ", "ae").replace("ø", "o").replace("å", "a")

print(f"Brukarnamnet ditt er: {brukarnamn}")
```

</details>

### Oppgåve 21 ⭐⭐⭐ (utfordring)
Ta imot eit ord eller ein setning frå brukaren. Fjern mellomrom og gjer om til små bokstavar, reverser strengen med slicing (`[::-1]`), og skriv ut om strengen er eit palindrom (er lik seg sjølv baklengs), t.d. "Anna" eller "Ole er en leo".

<details>
<summary>💡 Løysingsforslag</summary>

```python
tekst = input("Skriv inn eit ord eller ein setning: ")
tekstLower = tekst.lower().replace(" ", "")
reversert = tekstLower[::-1]

print(f"Reversert: {reversert}")
print(f"Er det eit palindrom? {tekstLower == reversert}")
```

</details>

### Oppgåve 22 ⭐⭐⭐ (utfordring)
Lag variablane `vareNamn`, `antall` og `prisPerStk` for éi vare, og rekn ut totalprisen. Skriv ut ei "kvittering" med to linjer (overskrift + verdiar) der kolonnene er høgrejusterte og har fast breidde, og prisane har to desimalar. Bruk formateringsspesifikasjonar i f-stringen, t.d. `{verdi:>10.2f}` (høgrejustert, breidde 10, to desimalar).

<details>
<summary>💡 Løysingsforslag</summary>

```python
vareNamn = "Kaffikopp"
antall = 3
prisPerStk = 89.5
totalpris = antall * prisPerStk

print(f"{'Vare':10}{'Antall':>8}{'Pris/stk':>10}{'Totalt':>10}")
print(f"{vareNamn:10}{antall:>8}{prisPerStk:>10.2f}{totalpris:>10.2f}")
```

</details>

### Oppgåve 23 ⭐⭐⭐ (utfordring)
Slicing med `[-3:]` (som i oppgåve 18) fungerer dårleg dersom filtypen ikkje er nøyaktig tre teikn (t.d. `.py`, `.jpeg` eller filer utan filtype i det heile). Løys oppgåve 18 på nytt, men bruk i staden `.split(".")` til å dele opp filnamnet, og hent ut det siste elementet i lista som blir returnert.

<details>
<summary>💡 Løysingsforslag</summary>

```python
filnamn = input("Skriv inn eit filnamn: ")
delar = filnamn.split(".")
filtype = delar[-1]

print(f"Filtypen er .{filtype}")
```

</details>
