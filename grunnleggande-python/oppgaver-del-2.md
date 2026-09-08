# Oppgåver: Valsetningar og løkker

Desse oppgåvene byggjer vidare på det du har jobba med i:

- [05-valsetningar.py](05-valsetningar.py)
- [06-valsetningar-tekstbasert-eventyrspel.py](06-valsetningar-tekstbasert-eventyrspel.py)
- [07-valsetningar-stein-saks-papir.py](07-valsetningar-stein-saks-papir.py)
- [08-valsetningar-innlogging.py](08-valsetningar-innlogging.py)
- [09-lokker-for.py](09-lokker-for.py)

Lag ei ny `.py`-fil per oppgåve (eller ei fil per del), og test koden din før du ser på løysingsforslaget. Løysingsforslaga er berre **eitt** av fleire moglege svar — så lenge koden din gjer det same og er lett å lese, er det like bra.

**Vanskelegheitsgrad:** ⭐ enkel · ⭐⭐ middels · ⭐⭐⭐ utfordring

---

## Del A: Valsetningar (if / elif / else)

### Oppgåve 1 ⭐
Ta imot eit heiltal frå brukaren. Skriv ut om talet er positivt, negativt eller null (bruk `if`/`elif`/`else`).

<details>
<summary>💡 Løysingsforslag</summary>

```python
tal = int(input("Skriv inn eit heiltal: "))

if tal > 0:
    print(f"{tal} er positivt.")
elif tal < 0:
    print(f"{tal} er negativt.")
else:
    print("Talet er null.")
```

</details>

### Oppgåve 2 ⭐⭐
Ta imot tre ulike tal frå brukaren, og skriv ut kva for eitt av dei som er **størst**. Du treng ikkje bruke funksjonen `max()` — løys det med samanlikningar (`if`/`elif`/`else`).

<details>
<summary>💡 Løysingsforslag</summary>

```python
tal1 = float(input("Skriv inn første tal: "))
tal2 = float(input("Skriv inn andre tal: "))
tal3 = float(input("Skriv inn tredje tal: "))

if tal1 >= tal2 and tal1 >= tal3:
    storst = tal1
elif tal2 >= tal1 and tal2 >= tal3:
    storst = tal2
else:
    storst = tal3

print(f"Det største talet er {storst}.")
```

</details>

### Oppgåve 3 ⭐⭐
Ta imot ein alder frå brukaren, og skriv ut kva for **livsfase** personen er i, etter denne inndelinga:
- 0–2 år: "baby"
- 3–12 år: "barn"
- 13–19 år: "tenåring"
- 20–66 år: "vaksen"
- 67 år og eldre: "pensjonist"

<details>
<summary>💡 Løysingsforslag</summary>

```python
alder = int(input("Kor gamal er du? "))

if alder <= 2:
    livsfase = "baby"
elif alder <= 12:
    livsfase = "barn"
elif alder <= 19:
    livsfase = "tenåring"
elif alder <= 66:
    livsfase = "vaksen"
else:
    livsfase = "pensjonist"

print(f"Du er ein {livsfase}.")
```

</details>

### Oppgåve 4 ⭐⭐⭐ (utfordring)
Lag eit enkelt karakterprogram: ta imot ei poengsum mellom 0 og 100 frå brukaren, og bruk **nøsta** (nested) `if`-setningar til å først sjekke at talet faktisk er gyldig (mellom 0 og 100), og deretter — berre viss det er gyldig — rekne ut karakteren etter denne skalaen:
- 90–100: A
- 75–89: B
- 60–74: C
- 45–59: D
- 30–44: E
- 0–29: F

Viss talet er ugyldig (under 0 eller over 100), skal programmet skrive ut ei feilmelding i staden for ein karakter.

<details>
<summary>💡 Løysingsforslag</summary>

```python
poeng = int(input("Skriv inn poengsum (0-100): "))

if poeng < 0 or poeng > 100:
    print("Ugyldig poengsum! Må vere mellom 0 og 100.")
else:
    if poeng >= 90:
        karakter = "A"
    elif poeng >= 75:
        karakter = "B"
    elif poeng >= 60:
        karakter = "C"
    elif poeng >= 45:
        karakter = "D"
    elif poeng >= 30:
        karakter = "E"
    else:
        karakter = "F"

    print(f"Karakteren din er {karakter}.")
```

</details>

### Oppgåve 5 ⭐⭐⭐ (bonus, vanskeleg)
Lag eit program som avgjer om eit år er eit **skotår**. Reglane er:
- Året må vere delelig med 4.
- **Men** viss året òg er delelig med 100, er det **ikkje** eit skotår ...
- **Med mindre** året i tillegg er delelig med 400 — då er det likevel eit skotår.

(T.d. er 2000 eit skotår, men 1900 er det ikkje. 2024 er eit skotår, 2023 er det ikkje.)

Ta imot eit årstal frå brukaren, og skriv ut om det er eit skotår. Prøv først å løyse det med nøsta `if`-setningar, og tenk deretter over om du kan skrive **heile** logikken som eitt einaste boolsk uttrykk med `and`/`or`/`not`.

<details>
<summary>💡 Løysingsforslag</summary>

```python
ar = int(input("Skriv inn eit årstal: "))

# Løysing med nøsta if-setningar
if ar % 4 == 0:
    if ar % 100 == 0:
        if ar % 400 == 0:
            erSkotar = True
        else:
            erSkotar = False
    else:
        erSkotar = True
else:
    erSkotar = False

print(f"{ar} er eit skotår: {erSkotar}")

# Alternativ: same logikk som eitt boolsk uttrykk
erSkotarKort = (ar % 4 == 0 and ar % 100 != 0) or (ar % 400 == 0)
print(f"{ar} er eit skotår (kort versjon): {erSkotarKort}")
```

</details>

---

## Del B: Løkker (for og while)

### Oppgåve 6 ⭐
Bruk ei `for`-løkke og `range()` til å skrive ut alle partal frå 2 til og med 20.

<details>
<summary>💡 Løysingsforslag</summary>

```python
for tal in range(2, 21, 2):
    print(tal)
```

</details>

### Oppgåve 7 ⭐⭐
Bruk ei `while`-løkke til å be brukaren om eit passord, heilt til brukaren skriv inn det rette passordet (t.d. `"hemmeleg123"`). Skriv ut "Feil passord, prøv igjen." for kvart feilforsøk, og "Velkomen!" når passordet er rett.

<details>
<summary>💡 Løysingsforslag</summary>

```python
RETT_PASSORD = "hemmeleg123"
passord = input("Skriv inn passord: ")

while passord != RETT_PASSORD:
    print("Feil passord, prøv igjen.")
    passord = input("Skriv inn passord: ")

print("Velkomen!")
```

</details>

### Oppgåve 8 ⭐⭐
Bruk ei `for`-løkke til å rekne ut summen av alle tal frå 1 til og med 100 (`range()` er nyttig her). Skriv ut summen til slutt. Sjekk om svaret ditt stemmer med formelen `n * (n + 1) / 2`.

<details>
<summary>💡 Løysingsforslag</summary>

```python
sum = 0

for tal in range(1, 101):
    sum += tal

print(f"Summen av 1 til 100 er {sum}.")

n = 100
kontroll = n * (n + 1) / 2
print(f"Kontroll med formel: {kontroll}")
```

</details>

### Oppgåve 9 ⭐⭐⭐ (utfordring)
Lag eit program som let brukaren gjette på eit tilfeldig heiltal mellom 1 og 100 (`random.randint(1, 100)`). Bruk ei `while`-løkke som held fram til brukaren gjettar rett, og gi hint undervegs: "For høgt!" eller "For lågt!". Tel kor mange forsøk brukaren brukte, og skriv talet ut til slutt saman med ei gratulasjonsmelding.

<details>
<summary>💡 Løysingsforslag</summary>

```python
import random

tallet = random.randint(1, 100)
gjetning = 0
antallForsok = 0

while gjetning != tallet:
    gjetning = int(input("Gjett eit tal mellom 1 og 100: "))
    antallForsok += 1

    if gjetning < tallet:
        print("For lågt!")
    elif gjetning > tallet:
        print("For høgt!")

print(f"Rett! Du brukte {antallForsok} forsøk.")
```

</details>

### Oppgåve 10 ⭐⭐⭐ (bonus, vanskeleg)
Lag eit program som sjekkar om eit heiltal (større enn 1) er eit **primtal** (eit tal som berre er deleleg med 1 og seg sjølv). Ta imot talet frå brukaren, og bruk ei `for`-løkke saman med `break` til å sjekke om talet er deleleg med noko anna enn 1 og seg sjølv. Tips: du treng berre sjekke deletal opp til og med kvadratrota av talet (`int(math.sqrt(tal))`), det er nok til å avgjere om talet er eit primtal.

Utvid gjerne programmet til å skrive ut **alle** primtal opp til og med talet brukaren skreiv inn (bruk ei ytre løkke i tillegg).

<details>
<summary>💡 Løysingsforslag</summary>

```python
import math

tal = int(input("Skriv inn eit heiltal (større enn 1): "))

erPrimtal = True
for deletall in range(2, int(math.sqrt(tal)) + 1):
    if tal % deletall == 0:
        erPrimtal = False
        break

print(f"{tal} er eit primtal: {erPrimtal}")

# Bonus: skriv ut alle primtal opp til og med "tal"
print("Primtal opp til og med", tal, ":")
for kandidat in range(2, tal + 1):
    erPrimtalKandidat = True
    for deletall in range(2, int(math.sqrt(kandidat)) + 1):
        if kandidat % deletall == 0:
            erPrimtalKandidat = False
            break

    if erPrimtalKandidat:
        print(kandidat, end=" ")

print()
```

</details>