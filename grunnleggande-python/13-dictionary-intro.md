# Dictionary i Python

## Introduksjon

En **dictionary** (ofte kalt *dict*, eller "ordbok" på norsk) er en samling verdier akkurat som en liste, men med en viktig forskjell: mens en liste bruker et *tall* (indeksen) for å finne et element, bruker en dictionary en **nøkkel** (*key*) du velger selv. Hver nøkkel peker på en tilhørende **verdi** (*value*) — derfor snakker vi om **nøkkel-verdi-par**.

```python
frukter_liste = ["eple", "banan", "pære"]
print(frukter_liste[0])  # eple  -  du må huske at eple ligger på indeks 0

priser = {"eple": 3, "banan": 2, "pære": 4}
print(priser["eple"])  # 3  -  du slår rett og slett opp "eple"
```

Tenk på en dictionary som en ordbok i ordets egentlige forstand: du slår opp et *ord* (nøkkelen) for å finne *forklaringen* (verdien) — du blar ikke etter sidetall. Dette gjør dictionaries perfekte når data naturlig hører sammen i par, som et navn og en alder, et fag og en karakter, eller en by og innbyggertallet.

## Steg 1: Opprette en dictionary

En dictionary lages med krøllparenteser `{}`, der hvert par skrives som `nøkkel: verdi`, atskilt med komma:

```python
person = {
    "fornavn": "Per",
    "etternavn": "Christensen"
}
print(person)
```

Noen regler for nøkler og verdier:

- En **nøkkel** må være av en *immutable* (uforanderlig) type — vanligvis en streng eller et tall. Du kan ikke bruke en liste som nøkkel.
- Hver nøkkel kan bare finnes **én gang** i en dictionary. Bruker du samme nøkkel to ganger, overskriver den siste verdien den første.
- En **verdi** kan derimot være hva som helst: et tall, en streng, en liste, eller til og med en annen dictionary (mer om det i steg 6).

```python
ugyldig = {"navn": "Per", "navn": "Kari"}
print(ugyldig)  # {'navn': 'Kari'}  <- "Per" ble overskrevet
```

## Steg 2: Hente ut verdier

Du henter ut en verdi ved å sette nøkkelen i hakeparenteser bak dictionary-navnet:

```python
person = {"fornavn": "Per", "etternavn": "Christensen"}
print(person["etternavn"])  # Christensen
```

Prøver du å hente en nøkkel som ikke finnes, får du en feilmelding (`KeyError`):

```python
print(person["alder"])  # KeyError: 'alder'
```

Er du usikker på om nøkkelen finnes, er `get()` et tryggere alternativ — den returnerer `None` (eller en verdi du selv bestemmer) i stedet for å krasje:

```python
print(person.get("alder"))         # None  -  finnes ikke, men ingen feil
print(person.get("alder", 0))      # 0     -  bruker standardverdien du gir
print(person.get("fornavn", 0))    # Per   -  finnes den, brukes den vanlige verdien
```

## Steg 3: Sjekke om en nøkkel finnes

Med `in`-operatoren kan du sjekke om en **nøkkel** finnes i dictionaryen:

```python
person = {"fornavn": "Per", "etternavn": "Christensen"}

if "fornavn" in person:
    print("Nøkkelen 'fornavn' finnes.")

if "alder" not in person:
    print("Nøkkelen 'alder' finnes IKKE.")
```

**Obs!** I en liste sjekker `in` om en *verdi* finnes (`3 in [1, 2, 3]`). I en dictionary sjekker `in` om en *nøkkel* finnes — ikke en verdi:

```python
print("Per" in person)          # False  -  "Per" er en VERDI, ikke en nøkkel
print("fornavn" in person)      # True   -  "fornavn" ER en nøkkel
print("Per" in person.values()) # True   -  her sjekker vi eksplisitt blant verdiene
```

Du så allerede i forrige steg at `get()` returnerer `None` når nøkkelen ikke finnes. Det betyr at du også kan bruke `get()` sammen med `if`/`else` for å sjekke om en nøkkel finnes:

```python
if person.get("alder") is not None:
    print("Nøkkelen 'alder' finnes.")
else:
    print("Nøkkelen 'alder' finnes IKKE.")
```

Forskjellen på de to måtene: `in` svarer rent på *om* nøkkelen finnes, mens `get()` i tillegg henter verdien — praktisk hvis du uansett skal bruke den videre. Én fallgruve med `get()`-varianten: den gir feil svar dersom nøkkelen finnes, men verdien faktisk *er* `None`. Da er `in` det trygge valget.

## Steg 4: Endre, legge til og fjerne

Dictionaries er, i likhet med lister, **mutable** — du kan endre innholdet direkte.

**Endre et element** ved å tilordne en ny verdi til en eksisterende nøkkel:

```python
person["fornavn"] = "Kari"
print(person)  # {'fornavn': 'Kari', 'etternavn': 'Christensen'}
```

**Legge til** et nytt nøkkel-verdi-par — det finnes ingen `append()` for dictionaries, du tilordner bare en verdi til en nøkkel som ikke finnes fra før, så opprettes den automatisk:

```python
person["alder"] = 42
print(person)  # {'fornavn': 'Kari', 'etternavn': 'Christensen', 'alder': 42}
```

**Fjerne** et element finnes det flere måter å gjøre på:

```python
del person["alder"]              # Fjerner nøkkelen "alder" (og verdien)
etternavn = person.pop("etternavn")  # Fjerner OG returnerer verdien
print(person)
print("Fjernet:", etternavn)
```

`pop()` kan også ta en standardverdi som andre argument, i tilfelle nøkkelen ikke finnes — akkurat som `get()`:

```python
alder = person.pop("alder", "ukjent")
print(alder)  # ukjent  -  "alder" fantes ikke, men det krasjer ikke
```

## Steg 5: Gå gjennom en dictionary (løkker)

En vanlig `for`-løkke over en dictionary gir deg **nøklene**, én etter én:

```python
person = {"fornavn": "Per", "etternavn": "Christensen", "alder": 42}

for nokkel in person:
    print(nokkel)
```

Vil du hente verdien samtidig, bruker du nøkkelen til å slå den opp, akkurat som i steg 2:

```python
for nokkel in person:
    print(nokkel, "->", person[nokkel])
```

Python gir deg tre nyttige metoder for å være tydelig på hva du vil gå gjennom:

```python
print(person.keys())    # dict_keys(['fornavn', 'etternavn', 'alder'])
print(person.values())  # dict_values(['Per', 'Christensen', 42])
print(person.items())   # dict_items([('fornavn', 'Per'), ('etternavn', 'Christensen'), ('alder', 42)])
```

`.items()` er spesielt nyttig i en løkke, siden den gir deg nøkkel og verdi samtidig (akkurat som `enumerate()` gjør for lister):

```python
for nokkel, verdi in person.items():
    print(f"{nokkel}: {verdi}")
```

## Steg 6: Nøstede dictionaries (dict i dict, liste i dict)

En verdi i en dictionary kan selv være en dictionary eller en liste — dette brukes mye for å representere mer sammensatte data, som et register over flere personer:

```python
personer = {
    "999999-99999": {
        "fornavn": "Jo Bjørnar",
        "etternavn": "Hausnes"
    },
    "000000-00000": {
        "fornavn": "Jo Bjarne",
        "etternavn": "Hausnesia"
    }
}

print(personer["000000-00000"]["fornavn"])  # Jo Bjarne
```

Her er den ytre nøkkelen et fødselsnummer, og verdien er en *ny* dictionary med fornavn og etternavn. Du "kjeder" oppslagene: først finner du personen med det ytre fødselsnummeret, deretter feltet du vil ha i den indre dictionaryen.

Verdiene kan også være lister, for eksempel byer med en liste over landemerker:

```python
norske_byer = {
    "Oslo": {
        "innbyggere": 697899,
        "fylke": "Oslo",
        "landemerker": ["Holmenkollen", "Vigelandsparken", "Operaen"]
    },
    "Bergen": {
        "innbyggere": 298969,
        "fylke": "Vestland",
        "landemerker": ["Bryggen", "Fløyen", "Fisketorget"]
    },
    "Trondheim": {
        "innbyggere": 209462,
        "fylke": "Trøndelag",
        "landemerker": ["Nidarosdomen", "Tyholttårnet", "Gamle Bybro"]
    },
    "Stavanger": {
        "innbyggere": 148289,
        "fylke": "Rogaland",
        "landemerker": ["Preikestolen", "Oljemuseet", "Domkirken"]
    }
}

print(norske_byer["Bergen"]["landemerker"][1])  # Fløyen
```

Siden `landemerker` er en vanlig liste, kan du gå gjennom den med en helt vanlig `for`-løkke:

```python
for landemerke in norske_byer["Bergen"]["landemerker"]:
    print(f"{landemerke}.")
```

Og siden `norske_byer` selv er en dictionary, kan du kombinere `.items()` med indre oppslag for å skrive ut alt om alle byene:

```python
for by, info in norske_byer.items():
    print(f"{by} ({info['fylke']}) har {info['innbyggere']} innbyggere.")
    for landemerke in info["landemerker"]:
        print(f"  - {landemerke}")
```

## Steg 7 (bonus): dict comprehension

Akkurat som list comprehension lager en ny liste på én linje, kan **dict comprehension** lage en ny dictionary på én linje:

```python
tall = [1, 2, 3, 4, 5]
kvadrater = {t: t ** 2 for t in tall}
print(kvadrater)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Legg merke til forskjellen fra list comprehension: her skriver vi `nøkkel: verdi` i stedet for bare `verdi`, og bruker krøllparenteser i stedet for hakeparenteser. Du kan også filtrere, akkurat som med lister:

```python
partallskvadrater = {t: t ** 2 for t in tall if t % 2 == 0}
print(partallskvadrater)  # {2: 4, 4: 16}
```

## Steg 8 (bonus): Sortering av en dictionary

Siden Python 3.7 husker en dictionary rekkefølgen elementene ble lagt inn i, men den er ikke *sortert* av seg selv. Bruker du `sorted()` på en dictionary, sorterer den som standard **nøklene**:

```python
karakterer = {"Kari": 5, "Ola": 3, "Nora": 6, "Jonas": 4}

for navn in sorted(karakterer):
    print(navn, "->", karakterer[navn])
```

Vil du sortere etter **verdi** i stedet, må du sortere `.items()` og fortelle `sorted()` hva den skal sammenligne på med `key`:

```python
for navn, karakter in sorted(karakterer.items(), key=lambda par: par[1]):
    print(navn, "->", karakter)

# Høyest karakter først:
for navn, karakter in sorted(karakterer.items(), key=lambda par: par[1], reverse=True):
    print(navn, "->", karakter)
```

`lambda par: par[1]` betyr "for hvert (navn, karakter)-par, sorter etter det andre elementet (indeks 1), altså karakteren".

## Steg 9 (bonus): Telle med en dictionary

Et svært vanlig bruksområde for dictionaries er å **telle** hvor mange ganger noe forekommer, for eksempel ord i en tekst eller karakterer i en klasse. Mønsteret bruker `.get()` med en standardverdi:

```python
ord = ["katt", "hund", "katt", "fisk", "hund", "katt"]
antall = {}

for o in ord:
    antall[o] = antall.get(o, 0) + 1

print(antall)  # {'katt': 3, 'hund': 2, 'fisk': 1}
```

Forklaring: `antall.get(o, 0)` henter gjeldende telling for ordet `o`, eller `0` hvis vi ikke har sett ordet før. Deretter legger vi til `1` og lagrer resultatet tilbake.

Python har også en spesialisert verktøy for nettopp dette, `Counter` fra biblioteket `collections`, som gjør det samme uten at du trenger å skrive løkka selv:

```python
from collections import Counter

ord = ["katt", "hund", "katt", "fisk", "hund", "katt"]
antall = Counter(ord)
print(antall)                 # Counter({'katt': 3, 'hund': 2, 'fisk': 1})
print(antall.most_common(1))  # [('katt', 3)]  -  det mest vanlige ordet
```

## Steg 10 (bonus): Slå sammen dictionaries

Vil du kombinere to dictionaries til én, kan du bruke `update()`, som skriver innholdet fra én dictionary inn i en annen (og overskriver ved like nøkler):

```python
grunndata = {"navn": "Per", "alder": 42}
tilleggsdata = {"by": "Bergen", "alder": 43}

grunndata.update(tilleggsdata)
print(grunndata)  # {'navn': 'Per', 'alder': 43, 'by': 'Bergen'}
```

Siden Python 3.9 finnes det også en kortere skrivemåte med `|`, som lager en *ny* dictionary uten å endre de originale:

```python
a = {"navn": "Per", "alder": 42}
b = {"by": "Bergen", "alder": 43}

kombinert = a | b
print(kombinert)  # {'navn': 'Per', 'alder': 43, 'by': 'Bergen'}
print(a)          # {'navn': 'Per', 'alder': 42}  <- uendret
```

## Oppsummering

| | Liste (`list`) | Dictionary (`dict`) |
|---|---|---|
| Skrivemåte | `[verdi1, verdi2]` | `{nøkkel1: verdi1, nøkkel2: verdi2}` |
| Slår opp med | Tallindeks (`liste[0]`) | Egendefinert nøkkel (`dict["navn"]`) |
| Rekkefølge | Ja, alltid etter indeks | Ja (siden Python 3.7), etter innsettingsrekkefølge |
| Duplikater | Ja, samme verdi kan forekomme flere ganger | Nøkler må være unike, verdier kan gjenta seg |
| Typisk bruk | En samling likeartede ting i rekkefølge | Data som hører sammen i par (navn -> verdi) |

| Situasjon | Løsning |
|---|---|
| Hente en verdi | `dict[nøkkel]` |
| Hente en verdi trygt, uten fare for `KeyError` | `dict.get(nøkkel, standardverdi)` |
| Endre en verdi / legge til et nytt par | `dict[nøkkel] = verdi` |
| Fjerne et par du vet nøkkelen til | `del dict[nøkkel]` eller `dict.pop(nøkkel)` |
| Sjekke om en nøkkel finnes | `nøkkel in dict` |
| Sjekke om en verdi finnes | `verdi in dict.values()` |
| Gå gjennom nøklene | `for nøkkel in dict:` eller `dict.keys()` |
| Gå gjennom verdiene | `dict.values()` |
| Gå gjennom nøkkel og verdi samtidig | `for nøkkel, verdi in dict.items():` |
| Sortere etter nøkkel | `sorted(dict)` |
| Sortere etter verdi | `sorted(dict.items(), key=lambda par: par[1])` |
| Telle forekomster i en liste | `dict[verdi] = dict.get(verdi, 0) + 1`, eller `collections.Counter(liste)` |
| Slå sammen to dictionaries | `dict1.update(dict2)` eller `dict1 \| dict2` |

## Øvingsoppgaver

1. Lag en dictionary `elev` med nøklene `"navn"`, `"klasse"` og `"alder"`, og fyll inn selvvalgte verdier. Skriv ut navnet og klassen med hver sin `print()`.
2. Ta utgangspunkt i `elev` fra oppgave 1. Legg til en ny nøkkel `"skole"` med en selvvalgt verdi, endre verdien på `"alder"` til noe annet, og fjern deretter `"klasse"` med `del`.
3. Lag en dictionary `fag_karakter` med minst fire fag som nøkler og karakterer (tall) som verdier, for eksempel `{"Matematikk": 5, "Norsk": 4}`. Bruk en `for`-løkke med `.items()` til å skrive ut hvert fag og karakteren på formen `Du fikk 5 i Matematikk.`
4. Ta utgangspunkt i `fag_karakter` fra oppgave 3. Bruk `in` til å sjekke om faget `"Engelsk"` finnes som nøkkel, og skriv ut en passende melding uansett om svaret er ja eller nei. Bruk deretter `.get()` til å hente karakteren i `"Engelsk"` med `0` som standardverdi dersom faget ikke finnes.
5. Lag en dictionary som teller bokstaver i et ord, for eksempel `"bergen"`. Bruk en `for`-løkke og mønsteret `dict[bokstav] = dict.get(bokstav, 0) + 1` til å telle hvor mange ganger hver bokstav forekommer, og skriv ut resultatet.
6. (Litt videre­kommen) Lag en dictionary `elever` som registrerer flere elever, der nøkkelen er elevens navn og verdien er en ny dictionary med feltene `"klasse"` og `"karakter"` (se `personer`-eksempelet i teksten for inspirasjon). Skriv ut klassen og karakteren til én valgfri elev ved å kjede oppslagene.
7. (Bonus) Bruk dict comprehension til å lage en dictionary der nøklene er tallene fra 1 til 10, og verdiene er kubikktallene deres (`tall ** 3`).
8. (Bonus) Ta utgangspunkt i `fag_karakter` fra oppgave 3. Bruk `sorted()` med `key=lambda par: par[1]` til å skrive ut fagene sortert fra laveste til høyeste karakter.
9. Under ser du en dictionary med resultater fra en klasse på en prøve, der nøkkelen er elevens navn og verdien er en liste med poengsum på tre ulike delprøver:

    ```python
    resultater = {
        "Kari": [18, 22, 20],
        "Ola": [25, 19, 24],
        "Nora": [15, 17, 16],
        "Jonas": [20, 20, 21],
    }
    ```

    a) Bruk en `for`-løkke med `.items()` til å skrive ut hver elevs navn og summen av poengene deres (bruk `sum()`), på formen `Kari: 60 poeng`.
    b) Lag en ny, tom dictionary `snitt`, og fyll den med hver elevs *gjennomsnittlige* poengsum per delprøve, avrundet til én desimal med `round()`.
    c) Finn og skriv ut navnet på eleven med høyest total poengsum. Du kan enten holde styr på dette selv i løkka, eller bruke `max()` med `key` på `resultater.items()`.

## Løsningsforslag

**Oppgave 1**

```python
elev = {"navn": "Kari", "klasse": "3IM1", "alder": 17}
print(elev["navn"])
print(elev["klasse"])
```

**Oppgave 2**

```python
elev = {"navn": "Kari", "klasse": "3IM1", "alder": 17}
elev["skole"] = "Byåsen videregående"
elev["alder"] = 18
del elev["klasse"]
print(elev)
```

**Oppgave 3**

```python
fag_karakter = {"Matematikk": 5, "Norsk": 4, "Naturfag": 6, "Kroppsøving": 5}

for fag, karakter in fag_karakter.items():
    print(f"Du fikk {karakter} i {fag}.")
```

**Oppgave 4**

```python
fag_karakter = {"Matematikk": 5, "Norsk": 4, "Naturfag": 6, "Kroppsøving": 5}

if "Engelsk" in fag_karakter:
    print("Engelsk finnes i lista over fag.")
else:
    print("Engelsk finnes IKKE i lista over fag.")

engelsk_karakter = fag_karakter.get("Engelsk", 0)
print("Karakter i Engelsk:", engelsk_karakter)
```

**Oppgave 5**

```python
ord = "bergen"
bokstav_telling = {}

for bokstav in ord:
    bokstav_telling[bokstav] = bokstav_telling.get(bokstav, 0) + 1

print(bokstav_telling)  # {'b': 1, 'e': 2, 'r': 1, 'g': 1, 'n': 1}
```

**Oppgave 6**

```python
elever = {
    "Kari Nilsen": {
        "klasse": "3IM1",
        "karakter": 5
    },
    "Ola Berg": {
        "klasse": "3IM2",
        "karakter": 4
    }
}

print(elever["Kari Nilsen"]["klasse"])
print(elever["Kari Nilsen"]["karakter"])
```

**Oppgave 7**

```python
kubikktall = {t: t ** 3 for t in range(1, 11)}
print(kubikktall)
```

**Oppgave 8**

```python
fag_karakter = {"Matematikk": 5, "Norsk": 4, "Naturfag": 6, "Kroppsøving": 5}

for fag, karakter in sorted(fag_karakter.items(), key=lambda par: par[1]):
    print(fag, "->", karakter)
```

**Oppgave 9**

```python
resultater = {
    "Kari": [18, 22, 20],
    "Ola": [25, 19, 24],
    "Nora": [15, 17, 16],
    "Jonas": [20, 20, 21],
}

# a)
for navn, poeng in resultater.items():
    print(f"{navn}: {sum(poeng)} poeng")

# b)
snitt = {}
for navn, poeng in resultater.items():
    snitt[navn] = round(sum(poeng) / len(poeng), 1)
print(snitt)

# c) - løsning med egen løkke
beste_navn = ""
beste_sum = 0
for navn, poeng in resultater.items():
    if sum(poeng) > beste_sum:
        beste_sum = sum(poeng)
        beste_navn = navn
print(f"Høyest poengsum: {beste_navn} med {beste_sum} poeng")

# c) - alternativ løsning med max() og key
beste_navn = max(resultater, key=lambda navn: sum(resultater[navn]))
print(f"Høyest poengsum: {beste_navn} med {sum(resultater[beste_navn])} poeng")
```
