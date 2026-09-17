# JSON, lister og dictionaries: games.json

## Introduksjon

Du har nå lært om **lister** og **dictionaries** hver for seg. I virkeligheten møter du sjelden bare den ene eller den andre — ekte data er som regel en **kombinasjon**: lister av dictionaries, dictionaries med lister inni seg, og gjerne flere nivåer med nøster inni hverandre.

Et svært vanlig format for å lagre og utveksle slike data er **JSON** (*JavaScript Object Notation*). Den gode nyheten er at du allerede kan lese JSON — for JSON *er* rett og slett lister og dictionaries skrevet som tekst:

| JSON | Python |
|---|---|
| `{ }` (objekt) | `dict` |
| `[ ]` (array) | `list` |
| `"tekst"` | `str` |
| `42` / `3.14` | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

I denne mappen ligger fila [games.json](games.json) — hele Steam-biblioteket til læreren din, hentet direkte fra Steams API. Det er et ekte datasett med over 2000 spill, og vi skal bruke det til å øve på akkurat det du nettopp har lært: å slå opp i dictionaries og gå gjennom lister.

## Steg 1: Åpne og laste inn fila

Python har et innebygd bibliotek som heter `json`, som gjør jobben med å tolke JSON-tekst til lister og dictionaries for deg:

```python
import json

with open("games.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))  # <class 'dict'>
```

`json.load(f)` leser hele fila og bygger opp de tilhørende Python-objektene automatisk. Etter dette kallet er `data` en helt vanlig Python-verdi — du trenger ikke tenke på at den «egentlig» kom fra en JSON-fil lenger.

## Steg 2: Utforske strukturen

Før du begynner å hente ut data, bør du finne ut hvordan strukturen faktisk ser ut. `data` er en dictionary med noen få nøkler på toppnivå:

```python
print(data.keys())
# dict_keys(['antall_spill', 'hentet_dato', 'spill'])
```

- `data["antall_spill"]` og `data["hentet_dato"]` er enkle verdier (henholdsvis en tekst og en dato).
- `data["spill"]` er der alt interessant skjer: en **liste** med ett element per spill.

Hvert element i denne lista er igjen en **dictionary**, med informasjon om ett enkelt spill:

```python
forste_spill = data["spill"][0]
print(type(forste_spill))  # <class 'dict'>
print(forste_spill)
```

Legg merke til mønsteret: `data` er en dict, `data["spill"]` er en list, og hvert element i den lista er igjen en dict. **Dict → list → dict.** Så snart du har sett dette mønsteret, er resten bare å kombinere det du allerede kan om oppslag i dict og løkker over list.

## Steg 3: Hente ut enkeltverdier

Siden `data["spill"]` er en liste, bruker du vanlig indeksering for å komme til ett bestemt spill, og deretter vanlig dict-oppslag for å hente et felt fra det spillet:

```python
print(data["spill"][0]["name"])   # Half-Life
print(data["spill"][3]["name"])   # Half-Life Deathmatch: Source
```

Du kan lese `data["spill"][0]["name"]` fra venstre mot høyre: «i `data`, hent `spill`-lista, ta element `0`, og hent `name`-feltet fra den dictionaryen».

Vil du vite hvor mange spill som finnes, er det fristende å bruke `data["antall_spill"]` — men se hva som faktisk står der:

```python
print(data["antall_spill"])  # "hemmelig"
```

Læreren din har rett og slett skjult dette feltet. **Stol aldri blindt på et felt som påstår å telle noe** — bruk `len()` på selve lista i stedet, det gir deg det ekte tallet:

```python
print(len(data["spill"]))  # 2384
```

## Steg 4: Løkke gjennom alle spillene

Skal du gjøre noe med *alle* spillene, går du gjennom `data["spill"]` med en vanlig `for`-løkke, akkurat som med enhver annen liste. Hvert element `spill` du får ut i løkka er én dictionary:

```python
for spill in data["spill"]:
    print(spill["name"])
```

Siden hvert `spill` er en dictionary, kan du bruke alt du kan om dictionaries inni løkka — for eksempel å bare skrive ut spill som oppfyller en betingelse:

```python
for spill in data["spill"]:
    if spill["playtime_forever_hours"] > 50:
        print(f"{spill['name']} – {spill['playtime_forever_hours']} timer")
```

## Steg 5: Finne informasjon i datasettet

Et vanlig mønster er å lete gjennom hele lista etter én bestemt ting, for eksempel spillet med lengst spilletid. Du løser det på samme måte som å finne det største tallet i en liste med tall — du holder styr på det beste svaret du har funnet så langt, mens du går gjennom løkka:

```python
maks_spilletid = 0
mest_spilte_spill = ""

for spill in data["spill"]:
    if spill["playtime_forever_hours"] > maks_spilletid:
        maks_spilletid = spill["playtime_forever_hours"]
        mest_spilte_spill = spill["name"]

print(f"Mest spilte spill: {mest_spilte_spill} ({maks_spilletid} timer)")
```

Dette er nøyaktig samme mønster som i [tolk.py](tolk.py) — det eneste nye her er at «listen med tall» er byttet ut med «en liste med dictionaries», der vi ser på ett bestemt felt (`playtime_forever_hours`) i hver av dem.

## Steg 6: Bygge en lenke til spillets bilde

Steam lagrer et forsidebilde for hvert spill, og du kan bygge lenken til det selv ut fra `appid`-en til spillet:

```python
spill = data["spill"][3]
biletsti = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{spill['appid']}/header.jpg"
print(biletsti)
```

Dette er bare vanlig f-streng-formatering — du henter en verdi ut av en dictionary (`spill["appid"]`), og setter den inn i en tekst.

## Oppsummering

| Du vil... | Kode |
|---|---|
| Laste inn en JSON-fil | `json.load(f)` |
| Hente ut ett spill fra lista | `data["spill"][i]` |
| Hente ett felt fra ett spill | `data["spill"][i]["name"]` |
| Telle antall spill (trygt) | `len(data["spill"])` |
| Gå gjennom alle spillene | `for spill in data["spill"]:` |
| Hente et felt inni løkka | `spill["playtime_forever_hours"]` |
| Finne "den beste" ut fra ett felt | Løkke som holder styr på beste verdi så langt |

Kort sagt: `games.json` er ikke noe nytt du må lære — det er en **liste av dictionaries**, akkurat som du allerede kjenner fra tidligere. Alt du trenger er `json.load()` for å komme dit.

## Øvingsoppgaver

Ta utgangspunkt i koden fra Steg 1 for å laste inn `games.json` i alle oppgavene under.

**Enkle**

1. Skriv ut navnet og `appid` til det tiende spillet i lista (husk at lister er 0-indekserte).
2. Bruk `len()` til å skrive ut hvor mange spill som finnes i datasettet.
3. Bruk en `for`-løkke til å skrive ut navnene på de 5 første spillene i lista.

**Middels**

4. Tell hvor mange spill du har spilt *null* timer (`playtime_forever_hours == 0`), og hvor mange du har spilt *mer enn* null timer. Skriv ut begge tallene.
5. Regn ut det totale antallet timer du har spilt til sammen, ved å summere `playtime_forever_hours` for alle spillene i lista. Avrund svaret til én desimal med `round()`.
6. Lag en ny liste `spilte_spill`, som bare inneholder *navnene* på spillene du har spilt minst 5 timer. Skriv ut hvor mange spill som havner i denne lista.

**Avanserte**

7. Finn spillet med lengst spilletid uten å skrive løkka selv — bruk `max()` med `key=lambda spill: spill["playtime_forever_hours"]` direkte på `data["spill"]`.
8. Bruk `sorted()` til å skrive ut navn og spilletid for de 5 spillene med lengst spilletid, sortert fra høyest til lavest.
9. Lag en dictionary `spilletid_pr_spill`, der nøkkelen er navnet på spillet og verdien er spilletiden i timer — men bare for spill du faktisk har spilt (`playtime_forever_hours > 0`). Skriv ut hvor mange nøkler dictionaryen får.
10. **Bonus:** La brukeren skrive inn navnet på et spill i biblioteket. Gå gjennom `data["spill"]` og finn spillet med akkurat det navnet, og skriv deretter ut lenken til forsidebildet dets (se Steg 6). Skriv ut en fin feilmelding dersom navnet ikke finnes i lista.

## Løsningsforslag

**Oppgave 1**

```python
spill = data["spill"][9]
print(spill["name"], spill["appid"])
# Uplink 1510
```

**Oppgave 2**

```python
print(len(data["spill"]))
# 2384
```

**Oppgave 3**

```python
for spill in data["spill"][:5]:
    print(spill["name"])
```

**Oppgave 4**

```python
uspilte = 0
spilte = 0

for spill in data["spill"]:
    if spill["playtime_forever_hours"] == 0:
        uspilte += 1
    else:
        spilte += 1

print(f"Uspilte: {uspilte}, spilte: {spilte}")
# Uspilte: 2044, spilte: 340
```

**Oppgave 5**

```python
total_timer = 0

for spill in data["spill"]:
    total_timer += spill["playtime_forever_hours"]

print(round(total_timer, 1))
# 1425.5
```

**Oppgave 6**

```python
spilte_spill = []

for spill in data["spill"]:
    if spill["playtime_forever_hours"] >= 5:
        spilte_spill.append(spill["name"])

print(len(spilte_spill))
# 62
```

**Oppgave 7**

```python
mest_spilte = max(data["spill"], key=lambda spill: spill["playtime_forever_hours"])
print(f"{mest_spilte['name']} – {mest_spilte['playtime_forever_hours']} timer")
# Stormworks: Build and Rescue – 178 timer
```

**Oppgave 8**

```python
topp5 = sorted(data["spill"], key=lambda spill: spill["playtime_forever_hours"], reverse=True)[:5]

for spill in topp5:
    print(f"{spill['name']}: {spill['playtime_forever_hours']} timer")

# Stormworks: Build and Rescue: 178 timer
# Hero Academy: 82 timer
# The Elder Scrolls V: Skyrim: 71.9 timer
# Divinity: Original Sin (Classic): 51.5 timer
# Tales of ARISE: 46.6 timer
```

**Oppgave 9**

```python
spilletid_pr_spill = {}

for spill in data["spill"]:
    if spill["playtime_forever_hours"] > 0:
        spilletid_pr_spill[spill["name"]] = spill["playtime_forever_hours"]

print(len(spilletid_pr_spill))
# 340

# Samme løsning som dict comprehension (bonusstoffet fra 13-dictionary-intro.md):
spilletid_pr_spill = {
    spill["name"]: spill["playtime_forever_hours"]
    for spill in data["spill"]
    if spill["playtime_forever_hours"] > 0
}
```

**Oppgave 10**

```python
navn = input("Hvilket spill vil du se bilde av? ")
funnet = None

for spill in data["spill"]:
    if spill["name"] == navn:
        funnet = spill
        break

if funnet is not None:
    biletsti = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{funnet['appid']}/header.jpg"
    print(biletsti)
else:
    print(f"Fant ikke noe spill som heter «{navn}».")
```

---

## Bonus: Hent ditt eget Steam-bibliotek

Alt du har gjort over har brukt læreren sitt datasett. Har du en egen Steam-konto, kan du hente ut *ditt eget* bibliotek og kjøre akkurat den samme koden på dine egne data.

Dette gjøres med scriptet [hent_steam.py](hent_steam.py), som snakker med Steams offisielle API og lagrer resultatet som en ny `games.json`-fil.

**Slik gjør du det:**

1. Sørg for at profilen din (og spilldetaljene dine) er satt til **offentlig** i Steam-innstillingene — ellers får du ingen data tilbake.
2. Skaff deg en API-nøkkel fra [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).
3. Finn din egen **SteamID64** på [steamid.io](https://steamid.io/).
4. Åpne [hent_steam.py](hent_steam.py), og fyll inn nøkkelen og ID-en din i de to variablene øverst:

   ```python
   STEAM_API_KEY = "DIN_API_NØKKEL_HER"
   STEAM_ID64 = "DIN_STEAMID64_HER"
   ```

5. Installer biblioteket `requests` hvis du ikke har det fra før: `pip install requests`.
6. Kjør scriptet: `python hent_steam.py`.

Resultatet havner i en `games.json`-fil i samme mappe, med nøyaktig samme struktur som fila du har jobbet med i denne guiden — så all koden og alle oppgavene over kan du kjøre rett på dine egne data, bare med andre tall og spillnavn i svarene.

**Obs!** En API-nøkkel er personlig — ikke del den med andre, og ikke last den opp til GitHub eller lignende.
