# Oppgave: Lag din egen bank

I denne oppgaven skal du lage et lite banksystem som kjører i terminalen. Du skal **ikke** bruke noe nytt — bare det du allerede kan: variabler, dictionaries, funksjoner, valgsetninger og løkker.

Målet er å lage en fungerende **prototype** ganske raskt. Ta godt vare på koden din! Senere i timen kommer banken med noen nye ønsker som du skal bygge inn i *din egen* kode — og neste time skal vi diskutere hva som ble tungvint, og hvordan vi kan gjøre det bedre.

---

## Del 1: Krav til programmet

Programmet skal vise en meny og la brukeren velge hva som skal gjøres, helt til brukeren velger å avslutte:

```
--- BANKEN ---
1: Vis saldo
2: Sett inn penger
3: Ta ut penger
4: Opprett ny kunde
0: Avslutt
Velg:
```

**Minstekrav:**

1. Programmet starter med kundene fra startdataene under.
2. Brukeren kan **se saldoen** på en konto ved å skrive inn kontonummeret.
3. Brukeren kan **sette inn** penger på en konto.
4. Brukeren kan **ta ut** penger fra en konto — men ikke mer enn det som står på kontoen.
5. Brukeren kan **opprette en ny kunde** (som starter med 0 kr).
6. Programmet skal ikke godta negative beløp (man kan ikke sette inn -500 kr).

**Utvidelser** (hvis du blir ferdig):

- Vis en oversikt over alle kunder og saldoene deres.
- Overfør penger fra én konto til en annen.
- Programmet skal ikke krasje om brukeren skriver bokstaver når det spørres etter et beløp (hint: `try`/`except`).
- **Lagre dataene i en JSON-fil**, slik at pengene ikke forsvinner når programmet avsluttes (se hint 5).

---

## Startdata

Lim inn dette øverst i programmet ditt:

```python
kunder = {
    "1001": {"navn": "Ola Nordmann", "saldo": 1500},
    "1002": {"navn": "Kari Nordmann", "saldo": 3200},
    "1003": {"navn": "Per Hansen", "saldo": 250},
}
```

---

## Hint

Prøv gjerne selv først, og bruk hintene når du står fast.

### Hint 1: Hvordan er dataene organisert?

`kunder` er **en dictionary der hver verdi også er en dictionary**. Kontonummeret er **nøkkelen**, og verdien er informasjonen om kunden. Slik henter og endrer du ting:

```python
print(kunder["1001"]["navn"])    # Ola Nordmann
print(kunder["1001"]["saldo"])   # 1500

kunder["1001"]["saldo"] += 200   # Ola får 200 kr
```

Legg merke til at kontonummeret er en **tekst** (`"1001"`), ikke et tall (`1001`). Det passer fint, siden `input()` alltid gir oss tekst — da kan vi bruke svaret fra brukeren direkte:

```python
kontonummer = input("Kontonummer: ")   # f.eks. "1001"
if kontonummer in kunder:
    print(kunder[kontonummer]["saldo"])
else:
    print("Fant ikke kontoen.")
```

### Hint 2: Lag én funksjon per operasjon

Lag en funksjon for hver ting banken kan gjøre. Send med `kunder` som parameter, slik at funksjonen får tilgang til dataene:

```python
def vis_saldo(kunder, kontonummer):
    ...

def sett_inn(kunder, kontonummer, belop):
    ...

def ta_ut(kunder, kontonummer, belop):
    ...

def opprett_kunde(kunder, navn):
    ...
```

**Nyttig å vite:** Når du endrer en dictionary *inne i* en funksjon, endres den originale dictionaryen også. Du trenger altså ikke `return` for å få endringen med deg tilbake:

```python
def sett_inn(kunder, kontonummer, belop):
    kunder[kontonummer]["saldo"] += belop   # Endrer den samme dictionaryen som utenfor


sett_inn(kunder, "1001", 500)
print(kunder["1001"]["saldo"])   # 2000
```

### Hint 3: Nytt kontonummer

En enkel måte å lage et nytt kontonummer på er å ta utgangspunkt i hvor mange kunder det er fra før:

```python
kontonummer = str(1001 + len(kunder))   # 3 kunder fra før -> "1004"
kunder[kontonummer] = {"navn": navn, "saldo": 0}
```

### Hint 4: Menyen

Menyen er en `while True`-løkke som spør brukeren hva den vil gjøre, og kaller riktig funksjon:

```python
def meny():
    while True:
        print("\n--- BANKEN ---")
        print("1: Vis saldo")
        # ... resten av valgene
        valg = input("Velg: ")

        if valg == "1":
            kontonummer = input("Kontonummer: ")
            vis_saldo(kunder, kontonummer)
        elif valg == "2":
            ...
        elif valg == "0":
            break


meny()
```

**Tips:** Lag og test én funksjon av gangen! Få `vis_saldo` til å virke før du begynner på `sett_inn`.

### Hint 5 (utvidelse): Lagre i JSON-fil

Lag en fil som heter `kunder.json` i **samme mappe** som Python-fila di, og lim inn startdataene. JSON ser nesten helt ut som en Python-dictionary (men krever `"doble fnutter"`):

```json
{
    "1001": {"navn": "Ola Nordmann", "saldo": 1500},
    "1002": {"navn": "Kari Nordmann", "saldo": 3200},
    "1003": {"navn": "Per Hansen", "saldo": 250}
}
```

Python har et innebygd bibliotek som heter `json`. Med `json.load()` gjøres innholdet i fila om til en vanlig dictionary, og med `json.dump()` går det motsatt vei:

```python
import json
from pathlib import Path

# Finn kunder.json i samme mappe som denne Python-fila
FILSTI = Path(__file__).resolve().parent.joinpath("kunder.json")


def les_data():
    with open(FILSTI, encoding="utf-8") as fil:
        return json.load(fil)


def lagre_data(kunder):
    with open(FILSTI, "w", encoding="utf-8") as fil:
        json.dump(kunder, fil, indent=4, ensure_ascii=False)
```

- `Path(__file__)...` sørger for at Python finner fila uansett hvilken mappe terminalen står i. Se [lese_filer.md](../../../grunnleggande-python/lese_filer.md) (steg 3 og 7).
- `"w"` (*write*) betyr at fila overskrives med det nye innholdet.
- `indent=4` gjør fila pen og lesbar, og `ensure_ascii=False` gjør at `æ`, `ø` og `å` lagres som vanlige bokstaver.

Bytt ut startdataene i koden med `kunder = les_data()`, og kall `lagre_data(kunder)` rett etter hver endring (innskudd, uttak, ny kunde).

> ⚠️ Får du en feilmelding når fila leses, er det ofte en skrivefeil i JSON-fila. Vanlige feil: komma etter siste element, eller `'enkle fnutter'` i stedet for `"doble fnutter"`.

---

## Sjekkliste

- [ ] Jeg kan se saldoen til en kunde.
- [ ] Jeg kan sette inn og ta ut penger, og saldoen blir riktig.
- [ ] Jeg får ikke tatt ut mer enn det som står på kontoen.
- [ ] Jeg får ikke satt inn eller tatt ut negative beløp.
- [ ] Jeg kan opprette en ny kunde.
- [ ] Programmet krasjer ikke om jeg skriver et kontonummer som ikke finnes.

Når du er ferdig med minstekravene, si fra til læreren. Da får du [endringsrunden](endringsrunde.md) — nye ønsker fra banken.

---

**Løsningsforslag:** [bank.py](bank.py) (minstekrav og alle utvidelser) og [bank_endringer.py](bank_endringer.py) (etter endringsrunden).
