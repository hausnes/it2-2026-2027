# Filhåndtering i Python

*Sammendrag basert på Smidig IT-2 (Ola Lie), bolk 1.6, med utvidede eksempler for CSV, JSON og åpne API-er.*

**Kompetansemål:**
- Gjøre rede for standarder for lagring, utveksling og sikring av ulike typer data.
- Bruke programmering til å innhente, analysere og presentere informasjon fra reelle datasett.

## Steg 1: Litt om filer

Alt som lagres på en datamaskin — dokumenter, bilder, programmer — ligger til slutt som filer på et platelager (HDD/SSD) eller eksternt (minnepinne, minnekort). Helt nederst består alle filer av 0-er og 1-ere (*bit*), gruppert i grupper på 8 (*byte*). Operativsystemet holder rede på hvor hver fil begynner og slutter.

Et filnavn består av `<navn>.<filtype>`. Filtypen forteller operativsystemet hvilket program som normalt skal åpne fila (`.docx` → Word, `.jpg` → bildeviser), men dette er bare en *avtale* — ingenting hindrer deg i å endre filtypen, selv om filen fortsatt inneholder det samme.

Mange filtyper har derfor også en **filsignatur** (et "magisk nummer") som de første bytene i fila, som programmer kan bruke til å *gjenkjenne* det faktiske innholdet uavhengig av filtypen. For eksempel starter `.jpg`-filer typisk med `FF D8`, mens `.mp3`-filer starter med `49 44 33`.

Du kan se hex-koden til en fil i terminalen i VS Code:

```powershell
# PowerShell (standard i VS Code sitt terminalvindu på Windows)
format-hex <filnavn>

# Bare første linje:
format-hex <filnavn> | Select-Object -First 1
```

```bash
# macOS: hexdump -C -n <antall bytes> <filnavn>
hexdump -C -n 16 bilde.jpg
```

## Steg 2: Rene tekstfiler og "flate filer"

Rene tekstfiler som `.txt`, `.csv` og `.json` har som regel **ingen** filsignatur — de er lesbare rett fram som tekst. Når slike filer inneholder strukturerte data, kalles de gjerne **flate filer**. Hver linje tilsvarer da én rad (eller "post"), omtrent som en rad i en database:

- I en `.txt`-fil kan hvert felt ligge på en fast posisjon på linja.
- I en `.csv`-fil (*comma-separated values*) skilles feltene med komma i stedet, så de trenger ikke stå på faste posisjoner.
- `.json` er strukturert annerledes igjen, se steg 7.

**Linjeskift** er verdt å kjenne til: skriver du en tekstfil på Windows, settes `0D 0A` inn mellom hver linje når du trykker Enter — `0D` er CR (*Carriage Return*, fra skrivemaskinenes vogn-retur) og `0A` er LF (*Line Feed*, "rull fram én linje"). macOS/Linux bruker kun `0A`. Dette er sjelden noe du trenger å tenke på i Python selv, men forklarer hvorfor tekstfiler noen ganger ser "annerledes ut" mellom operativsystem.

## Steg 3: Finn riktig filsti med `pathlib`

Når du åpner en fil med `open()`, leter Python etter den relativt til **gjeldende arbeidsmappe** — ikke nødvendigvis mappa der Python-fila ligger. Har du åpnet et helt annet mappenivå i VS Code (`File > Open Folder...`), kan `open("data.txt")` da feile selv om fila faktisk ligger rett ved siden av programmet ditt.

To løsninger:

1. Åpne (`File > Open Folder...`) akkurat den mappa der programmet ligger, **eller**
2. I VS Code: gå til tannhjulet nederst til venstre → *Settings* → søk `python.terminal` → huk av **Execute in File Dir**.

Den mest robuste løsningen er likevel å bruke biblioteket `pathlib`, slik at koden finner riktig fil uansett hvilken mappe terminalen står i:

```python
from pathlib import Path

# Mappa der DENNE Python-fila ligger:
mappe = Path(__file__).resolve().parent
```

`Path` tillater i og for seg å lime sammen stier med `/`, men det er forvirrende siden Windows egentlig bruker `\`. Bruk heller `.joinpath()`, som fungerer likt på alle operativsystem:

```python
from pathlib import Path

# Eksempel: data-mappa ligger ved siden av mappa programmet ditt kjører fra,
# og fila du vil lese er data/txt/filnavn.txt
filsti = Path(__file__).resolve().parent.parent.joinpath("data", "txt", "filnavn.txt")

with open(filsti, encoding="utf-8") as fil:
    print(fil.read())
```

**I Jupyter** finnes ikke `__file__` (koden kjøres interaktivt, ikke fra en fil), så der bruker du i stedet gjeldende arbeidskatalog — forutsatt at du ikke bytter den underveis i notatblokka:

```python
import os
from pathlib import Path

filsti = Path(os.getcwd()).parent.joinpath("data", "txt", "filnavn.txt")
```

## Steg 4: Lese fra en fil

Bruk alltid `with open(...)` fremfor `fil = open(...)` + `fil.close()`. Fordelen er at Python garantert lukker fila for deg igjen, selv om noe skulle feile underveis i blokka:

```python
with open("navn.txt", encoding="utf-8") as fil:
    innhold = fil.read()   # Hele fila som ÉN streng

print(innhold)
```

Det finnes tre vanlige måter å lese på, avhengig av hva du trenger:

```python
with open("navn.txt", encoding="utf-8") as fil:
    print(fil.read())        # Hele innholdet som én streng
```

```python
with open("navn.txt", encoding="utf-8") as fil:
    print(fil.readlines())   # Hele innholdet som en LISTE av linjer (med \n på slutten)
```

```python
with open("navn.txt", encoding="utf-8") as fil:
    forste_linje = fil.readline()   # Én og én linje om gangen
    andre_linje = fil.readline()
    print(forste_linje, end="")     # end="" for å slippe dobbel linjeskift
    print(andre_linje, end="")
```

Den vanligste og mest lesbare måten å gå gjennom hele fila linje for linje, er faktisk å bruke selve fil-objektet direkte i en `for`-løkke:

```python
with open("navn.txt", encoding="utf-8") as fil:
    for linje in fil:
        print(linje.strip())   # .strip() fjerner \n på slutten av hver linje
```

**Filpekeren** er posisjonen Python leser fra i fila akkurat nå — den flytter seg automatisk etter hvert som du leser. `fil.read(2)` leser bare de neste 2 tegnene, og `fil.seek(0)` flytter pekeren tilbake til starten av fila hvis du vil lese den på nytt:

```python
with open("navn.txt", encoding="utf-8") as fil:
    print(fil.read(2))   # Bare de to første tegnene
    fil.seek(0)           # Hopp tilbake til start
    print(fil.read())     # Hele fila, fra start igjen
```

## Steg 5: Skrive til en fil

Skal du skrive til en fil, må du åpne den med `mode="w"` (write). Fila opprettes hvis den ikke finnes fra før, og **overskrives** hvis den finnes:

```python
with open("navn.txt", mode="w", encoding="utf-8") as fil:
    fil.write("Kari\n")
    fil.write("Nilsen\n")
```

Vil du i stedet **legge til** på slutten av en eksisterende fil uten å slette det som allerede står der, bruk `mode="a"` (append):

```python
with open("navn.txt", mode="a", encoding="utf-8") as fil:
    fil.write("Ny linje på slutten\n")
```

`encoding="utf-8"` bør du alltid ta med når teksten kan inneholde norske bokstaver (æ, ø, å) — uten den risikerer du at disse blir lagret eller lest feil. Grunnen er at å/Å i UTF-8 faktisk lagres som to byte (`C3 85` i hex for `Å`), mens en vanlig bokstav som `1` bare trenger én byte (`31`).

## Steg 6: Lese CSV-filer

Tenk deg at du har en fil `elever.csv` med dette innholdet:

```csv
navn,klasse,karakter
Kari,3IM1,5
Ola,3IM2,4
Nora,3IM1,6
```

**Uten noe bibliotek** kan du lese og tolke dette selv med `split(",")`, siden en CSV-fil i bunn og grunn bare er tekst med komma som skilletegn:

```python
with open("elever.csv", encoding="utf-8") as fil:
    overskrifter = fil.readline().strip().split(",")   # ['navn', 'klasse', 'karakter']

    for linje in fil:
        felt = linje.strip().split(",")
        navn, klasse, karakter = felt
        print(f"{navn} går i {klasse} og har karakteren {karakter}.")
```

Dette fungerer for enkle filer, men blir fort skjørt (hva om et felt selv inneholder komma?). Derfor har Python et innebygd bibliotek, `csv`, som håndterer slike detaljer for deg:

```python
import csv

with open("elever.csv", encoding="utf-8") as fil:
    csv_leser = csv.reader(fil)
    overskrifter = next(csv_leser)   # Hopper over/henter ut den første linja (overskriftene)

    for rad in csv_leser:
        navn, klasse, karakter = rad
        print(f"{navn} går i {klasse} og har karakteren {karakter}.")
```

Enda ryddigere er `csv.DictReader`, som automatisk bruker den første linja som nøkler, slik at hver rad blir en **dictionary** du kan slå opp i med feltnavn i stedet for posisjon:

```python
import csv

with open("elever.csv", encoding="utf-8") as fil:
    csv_leser = csv.DictReader(fil)

    for rad in csv_leser:
        print(f"{rad['navn']} går i {rad['klasse']} og har karakteren {rad['karakter']}.")
```

Å **skrive** en CSV-fil gjøres på tilsvarende vis med `csv.writer` (eller `csv.DictWriter`):

```python
import csv

elever = [
    {"navn": "Kari", "klasse": "3IM1", "karakter": 5},
    {"navn": "Ola", "klasse": "3IM2", "karakter": 4},
]

with open("nye_elever.csv", mode="w", encoding="utf-8", newline="") as fil:
    csv_skriver = csv.DictWriter(fil, fieldnames=["navn", "klasse", "karakter"])
    csv_skriver.writeheader()
    csv_skriver.writerows(elever)
```

`newline=""` bør alltid stå med når du skriver CSV-filer på Windows — uten den kan `csv`-biblioteket ende opp med å sette inn tomme, ekstra linjeskift.

## Steg 7: Lese JSON-filer

**JSON** (*JavaScript Object Notation*) er et tekstformat som ligner svært på Python sine dictionaries og lister — det er derfor JSON er et av de aller vanligste formatene å hente data fra, ikke minst fra API-er (se steg 8). En fil `elever.json` kan for eksempel se slik ut:

```json
[
    {"navn": "Kari", "klasse": "3IM1", "karakter": 5},
    {"navn": "Ola", "klasse": "3IM2", "karakter": 4},
    {"navn": "Nora", "klasse": "3IM1", "karakter": 6}
]
```

Legg merke til at dette rett og slett er en liste av dictionaries — akkurat den strukturen du allerede kjenner fra Python. Det innebygde biblioteket `json` gjør om JSON-tekst til ekte Python-lister og -dictionaries automatisk:

```python
import json

with open("elever.json", encoding="utf-8") as fil:
    elever = json.load(fil)   # json.load() -  les rett fra en ÅPEN FIL

for elev in elever:
    print(f"{elev['navn']} går i {elev['klasse']} og har karakteren {elev['karakter']}.")
```

Har du i stedet JSON-tekst som allerede ligger i en vanlig Python-streng (for eksempel hentet fra et API, se steg 8), bruker du `json.loads()` (*load string*) i stedet:

```python
import json

json_tekst = '{"navn": "Kari", "klasse": "3IM1", "karakter": 5}'
elev = json.loads(json_tekst)
print(elev["navn"])   # Kari
```

Å **skrive** Python-data til en JSON-fil gjøres med `json.dump()` (til fil) eller `json.dumps()` (til streng), som er det motsatte av `load`/`loads`:

```python
import json

elever = [
    {"navn": "Kari", "klasse": "3IM1", "karakter": 5},
    {"navn": "Ola", "klasse": "3IM2", "karakter": 4},
]

with open("nye_elever.json", mode="w", encoding="utf-8") as fil:
    json.dump(elever, fil, indent=4, ensure_ascii=False)
```

`indent=4` gjør fila lesbar for mennesker (innrykk i stedet for alt på én linje), og `ensure_ascii=False` sørger for at norske bokstaver skrives som æ, ø, å i stedet for kryptiske escape-koder.

**Nøstede data.** JSON-filer er ofte dypere nøstet enn eksempelet over — akkurat som nøstede dictionaries og lister i Python (se eget notat om dictionaries). Har du for eksempel:

```json
{
    "skole": "Eksempel vgs",
    "elever": [
        {"navn": "Kari", "fag": ["Matematikk", "Naturfag"]},
        {"navn": "Ola", "fag": ["Norsk", "Engelsk"]}
    ]
}
```

...leser du deg ned gjennom strukturen på nøyaktig samme måte som du ville gjort med en vanlig Python-dictionary:

```python
import json

with open("skole.json", encoding="utf-8") as fil:
    data = json.load(fil)

print(data["skole"])                        # Eksempel vgs
for elev in data["elever"]:
    print(elev["navn"], "har fagene", elev["fag"])
```

## Steg 8: Lese data fra et åpent API

Et **API** (*Application Programming Interface*) er en tjeneste på nett du kan sende en forespørsel til og få strukturerte data tilbake — som oftest i JSON-format. I stedet for å laste ned en fil manuelt, henter programmet ditt ferske data direkte over internett.

For å snakke med et API fra Python trenger du biblioteket `requests`, som **ikke** følger med Python fra før av og må installeres én gang:

```powershell
pip install requests
```

Den enkleste bruken er å sende en `GET`-forespørsel til en URL, og deretter tolke svaret som JSON — akkurat som i steg 7, bare at teksten nå kommer fra internett i stedet for en fil:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
svar = requests.get(url)

brukere = svar.json()   # Tolker svaret som JSON, gir deg en liste av dictionaries

for bruker in brukere:
    print(bruker["name"], "-", bruker["email"])
```

Det er alltid lurt å sjekke om forespørselen faktisk lyktes, via `svar.status_code` (`200` betyr OK) før du stoler på innholdet:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"
svar = requests.get(url)

if svar.status_code == 200:
    bruker = svar.json()
    print(f"{bruker['name']} bor i {bruker['address']['city']}.")
else:
    print(f"Noe gikk galt. Statuskode: {svar.status_code}")
```

Mange API-er lar deg også sende med **parametere** i forespørselen, for eksempel for å søke eller filtrere. Da sender du dem som en dictionary via `params`, i stedet for å bygge URL-en selv med `?`- og `&`-tegn:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
parametere = {"userId": 1}   # Tilsvarer ...posts?userId=1 i URL-en

svar = requests.get(url, params=parametere)
innlegg = svar.json()

print(f"Fant {len(innlegg)} innlegg fra bruker 1.")
for post in innlegg:
    print("-", post["title"])
```

Bortsett fra at dataen kommer fra internett i stedet for en lokal fil, er alt du allerede kan om lister og dictionaries direkte overførbart: et API-svar er som regel bare JSON — altså lister og dictionaries — akkurat som i steg 7.

## Oppsummering

| Situasjon | Løsning |
|---|---|
| Åpne en fil trygt (lukkes automatisk) | `with open(filnavn, encoding="utf-8") as fil:` |
| Finne riktig filsti uansett arbeidsmappe | `Path(__file__).resolve().parent` (`pathlib`) |
| Lese hele fila som én streng | `fil.read()` |
| Lese hele fila som en liste av linjer | `fil.readlines()` |
| Lese én og én linje | `fil.readline()`, eller `for linje in fil:` |
| Skrive til fil (overskriver) | `open(filnavn, mode="w", encoding="utf-8")` |
| Skrive til fil (legger til på slutten) | `open(filnavn, mode="a", encoding="utf-8")` |
| Lese en CSV-fil rad for rad | `csv.reader(fil)` |
| Lese en CSV-fil som dictionaries | `csv.DictReader(fil)` |
| Skrive en CSV-fil fra dictionaries | `csv.DictWriter(fil, fieldnames=...)` |
| Lese en JSON-fil | `json.load(fil)` |
| Tolke en JSON-streng (f.eks. fra et API) | `json.loads(tekst)` |
| Skrive Python-data til en JSON-fil | `json.dump(data, fil, indent=4, ensure_ascii=False)` |
| Hente JSON-data fra et åpent API | `requests.get(url).json()` |

## Øvingsoppgaver

1. Lag en tekstfil `navn.txt` med ditt fornavn på første linje og etternavn på andre linje (du kan enten opprette fila manuelt i VS Code, eller skrive den fra Python med `mode="w"`). Skriv deretter et Python-program som åpner fila med `with open(...)` og skriver ut innholdet med `.read()`.
2. Utvid programmet fra oppgave 1 slik at det i stedet leser fila linje for linje med en `for`-løkke over fil-objektet, og skriver ut hver linje med `.strip()` slik at du ikke får doble linjeskift.
3. Lag en CSV-fil `frukt.csv` med kolonnene `navn` og `pris` og minst tre rader. Les fila med `csv.DictReader`, og skriv ut hver frukt på formen `Eple koster 12 kr`.
4. Ta utgangspunkt i oppgave 3. Regn ut og skriv ut *totalprisen* for alle fruktene til sammen ved å summere `pris`-feltet mens du går gjennom radene (husk at verdiene fra `csv.DictReader` er tekst, så du må gjøre dem om med `int()` eller `float()` først).
5. Lag en liste med minst tre dictionaries som representerer favorittfilmene dine (nøkler som `"tittel"` og `"ar"`), og skriv dem til en fil `filmer.json` med `json.dump()`. Skriv deretter et *eget* program som leser samme fil med `json.load()` og skriver ut filmene igjen.
6. (Litt videre­kommen) Bruk `requests` til å hente `https://jsonplaceholder.typicode.com/users`, og skriv ut navn og by (`address["city"]`) for alle brukerne. Finn deretter, med vanlig Python-logikk (ingen nye biblioteker), navnet på brukeren med **lengst** navn.

## Løsningsforslag

**Oppgave 1**

```python
with open("navn.txt", mode="w", encoding="utf-8") as fil:
    fil.write("Kari\n")
    fil.write("Nilsen\n")

with open("navn.txt", encoding="utf-8") as fil:
    print(fil.read())
```

**Oppgave 2**

```python
with open("navn.txt", encoding="utf-8") as fil:
    for linje in fil:
        print(linje.strip())
```

**Oppgave 3**

```python
import csv

with open("frukt.csv", mode="w", encoding="utf-8", newline="") as fil:
    fil.write("navn,pris\nEple,12\nBanan,8\nPære,15\n")

with open("frukt.csv", encoding="utf-8") as fil:
    csv_leser = csv.DictReader(fil)
    for rad in csv_leser:
        print(f"{rad['navn']} koster {rad['pris']} kr")
```

**Oppgave 4**

```python
import csv

with open("frukt.csv", encoding="utf-8") as fil:
    csv_leser = csv.DictReader(fil)
    totalpris = 0
    for rad in csv_leser:
        totalpris += int(rad["pris"])

print(f"Totalpris: {totalpris} kr")
```

**Oppgave 5**

```python
# skriv_filmer.py
import json

filmer = [
    {"tittel": "Inception", "ar": 2010},
    {"tittel": "Interstellar", "ar": 2014},
    {"tittel": "The Matrix", "ar": 1999},
]

with open("filmer.json", mode="w", encoding="utf-8") as fil:
    json.dump(filmer, fil, indent=4, ensure_ascii=False)
```

```python
# les_filmer.py
import json

with open("filmer.json", encoding="utf-8") as fil:
    filmer = json.load(fil)

for film in filmer:
    print(f"{film['tittel']} ({film['ar']})")
```

**Oppgave 6**

```python
import requests

svar = requests.get("https://jsonplaceholder.typicode.com/users")
brukere = svar.json()

for bruker in brukere:
    print(bruker["name"], "-", bruker["address"]["city"])

lengste_navn = max(brukere, key=lambda b: len(b["name"]))
print(f"\nLengst navn: {lengste_navn['name']}")
```
