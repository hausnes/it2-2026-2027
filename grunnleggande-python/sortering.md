# Sortering i Python

## Introduksjon

Å **sortere** noe betyr å legge elementene i en bestemt rekkefølge — for eksempel tall fra lavest til høyest, eller navn i alfabetisk rekkefølge. Python har innebygd støtte for sortering som fungerer på lister, tupler, sett og dictionaries, og som du allerede har sett litt av i filene om lister og dictionaries. Denne filen samler alt dette på ett sted og går litt dypere.

### Hvorfor Python oppfører seg annerledes enn JavaScript

Har du programmert litt i JavaScript fra før, har du kanskje opplevd at `[10, 2, 1].sort()` gir det underlige resultatet `[1, 10, 2]` — ikke `[1, 2, 10]`. Det skjer fordi JavaScripts `sort()` **som standard gjør om alt til tekst** før den sammenligner, og teksten `"10"` kommer alfabetisk før `"2"` (fordi `"1"` kommer før `"2"`).

Python gjør **ikke** dette. Python sammenligner elementene med sine *egentlige* verdier — tall sammenlignes som tall, tekst sammenlignes som tekst:

```python
tall = [10, 2, 1]
print(sorted(tall))  # [1, 2, 10]  -  riktig, uten omveier via tekst
```

Konsekvensen er at du i Python **aldri trenger noen "sorter tall riktig"-triks** (som `.sort((a, b) => a - b)` i JavaScript) — `sorted()` og `.sort()` gjør automatisk det riktige, uansett om innholdet er tall eller tekst. Det du derimot må passe på, er at Python **ikke lar deg blande typer** som ikke kan sammenlignes med hverandre:

```python
blanding = [1, "to", 3]
print(sorted(blanding))  # TypeError: '<' not supported between instances of 'str' and 'int'
```

Der JavaScript stille ville gjort alt om til tekst og fortsatt (uten feilmelding, men med et resultat som sannsynligvis ikke er det du ville hatt), stopper Python opp og sier ifra med en gang noe ikke lar seg sammenligne fornuftig.

## Steg 1: `sort()` og `sorted()` — to måter å sortere en liste på

Det finnes to måter å sortere en liste på, og forskjellen mellom dem er viktig.

**`liste.sort()`** sorterer lista **i stedet** (in place) — den endrer selve lista, og returnerer `None`. Bruk denne når du ikke lenger trenger den usorterte rekkefølgen:

```python
tall = [5, 3, 1, 4, 2]
tall.sort()
print(tall)  # [1, 2, 3, 4, 5]
```

**`sorted(liste)`** lar den originale lista være **uendret**, og gir deg i stedet en helt ny, sortert liste tilbake. Bruk denne når du fortsatt trenger den opprinnelige rekkefølgen et annet sted i koden:

```python
tall = [5, 3, 1, 4, 2]
sortert_tall = sorted(tall)

print("Original:", tall)           # [5, 3, 1, 4, 2]  -  uendret
print("Sortert kopi:", sortert_tall)  # [1, 2, 3, 4, 5]
```

**Obs!** En svært vanlig feil er å skrive `tall = tall.sort()`. Siden `.sort()` returnerer `None`, ender du opp med at `tall` blir `None` i stedet for den sorterte lista:

```python
tall = [5, 3, 1, 4, 2]
tall = tall.sort()
print(tall)  # None  <- Feil! .sort() returnerer ingenting
```

Riktig er enten `tall.sort()` alene (uten tilordning), eller `tall = sorted(tall)`.

`sorted()` er dessuten mer fleksibel enn `.sort()`: den fungerer på *alt* du kan gå gjennom med en løkke (en liste, en tupel, et sett, en streng, eller nøklene i en dictionary), og gir deg alltid en vanlig, sortert liste tilbake — mens `.sort()` bare finnes på lister:

```python
print(sorted("banan"))          # ['a', 'a', 'b', 'n', 'n']  -  streng -> liste
print(sorted({3, 1, 2}))        # [1, 2, 3]                   -  sett -> liste
print(sorted((30, 10, 20)))     # [10, 20, 30]                 -  tupel -> liste
```

## Steg 2: Synkende rekkefølge med `reverse=True`

Begge funksjonene tar et valgfritt argument `reverse`, som sorterer synkende (høyest til lavest / å til a) i stedet for stigende:

```python
tall = [5, 3, 1, 4, 2]

tall.sort(reverse=True)
print(tall)  # [5, 4, 3, 2, 1]

navn = ["Kari", "Ola", "Bernt-Åge"]
print(sorted(navn, reverse=True))  # ['Ola', 'Kari', 'Bernt-Åge']
```

## Steg 3: Sortering av tekst — store og små bokstaver

Når Python sorterer strenger, sammenligner den bokstav for bokstav etter tegnenes **Unicode-verdi**. Det viktigste å vite her er at **store bokstaver kommer før små bokstaver**:

```python
ord = ["banan", "Eple", "drue", "Aprikos"]
print(sorted(ord))  # ['Aprikos', 'Eple', 'banan', 'drue']
```

Legg merke til at `"Aprikos"` og `"Eple"` (store forbokstaver) havner *før* `"banan"` og `"drue"` (små forbokstaver), selv om det ikke er alfabetisk rekkefølge slik vi tenker på det i dagligtale. Vil du sortere uavhengig av store/små bokstaver, kan du gjøre alt om til f.eks. små bokstaver *før* sammenligningen — det gjør du med `key`, som er temaet i neste steg.

## Steg 4: Egendefinert sortering med `key` og `lambda`

Noen ganger vil du ikke sortere elementene direkte, men etter en *egenskap* ved dem — for eksempel sortere ord etter lengde, ikke alfabetisk. Da bruker du argumentet `key`, som forteller Python *hva* den skal sammenligne på for hvert element.

```python
ord = ["banan", "kiwi", "fiken", "pære"]
print(sorted(ord, key=len))  # ['kiwi', 'pære', 'banan', 'fiken']
```

Her regner Python ut `len(element)` for hvert element i lista, og sorterer etter *det* — men resultatet inneholder fortsatt de originale ordene, ikke lengdene deres.

`key` kan ta hvilken som helst funksjon, ikke bare `len`. For eksempel gjør `str.lower` sortering av tekst uavhengig av store og små bokstaver:

```python
ord = ["banan", "Eple", "drue", "Aprikos"]
print(sorted(ord, key=str.lower))  # ['Aprikos', 'banan', 'drue', 'Eple']
```

### Lambda — en rask, anonym funksjon

Ofte har du ikke en ferdig funksjon som `len` eller `str.lower` som passer, men vil regne ut noe helt spesifikt selv. Da kan du skrive en liten funksjon *på stedet* med **lambda**, i stedet for å definere en egen `def`-funksjon et annet sted i koden:

```python
def siste_bokstav(ord):
    return ord[-1]

# ...er det samme som:
siste_bokstav = lambda ord: ord[-1]
```

En lambda skrives som `lambda parameter: uttrykk` — den tar inn én eller flere parametere, og returnerer automatisk verdien av uttrykket (du skriver ikke `return`). Poenget med lambda i sammenheng med sortering er at du kan skrive den *direkte* som `key`-argumentet, uten å måtte definere en egen funksjon først:

```python
ord = ["banan", "kiwi", "fiken", "pære"]
print(sorted(ord, key=lambda o: o[-1]))  # Sortert etter siste bokstav i ordet
```

Tommelfingerregel: bruk `key=len` eller `key=str.lower` når en ferdig funksjon finnes og passer, og lambda når du trenger å regne ut noe Python ikke allerede har en funksjon for.

## Steg 5: Sortere lister av tupler eller lister

En svært vanlig situasjon er at du har en liste der hvert element selv er en tupel eller liste med flere verdier — for eksempel (navn, poengsum)-par. Da bruker `key` en lambda som plukker ut riktig del av hvert element med indeksering:

```python
resultater = [("Kari", 88), ("Ola", 95), ("Nora", 72)]

# Sortert etter poengsum, stigende:
print(sorted(resultater, key=lambda par: par[1]))
# [('Nora', 72), ('Kari', 88), ('Ola', 95)]

# Sortert etter poengsum, synkende (høyest først):
print(sorted(resultater, key=lambda par: par[1], reverse=True))
# [('Ola', 95), ('Kari', 88), ('Nora', 72)]
```

`lambda par: par[1]` betyr «for hvert element (som her er en tupel), bruk verdien på indeks 1 — altså poengsummen — som sorteringsgrunnlag».

## Steg 6: Sortere etter flere kriterier

Vil du sortere etter én egenskap først, og bruke en annen egenskap til å avgjøre rekkefølgen når den første er lik, lar du `key` returnere en **tupel**. Python sorterer da etter første element i tupelen, og bruker de neste elementene som "tiebreaker" — akkurat som når du sorterer en klasseliste etter etternavn, og deretter fornavn ved likt etternavn:

```python
elever = [
    ("Berg", "Ola", 5),
    ("Nilsen", "Kari", 4),
    ("Berg", "Anna", 6),
]

# Sortert etter etternavn, deretter fornavn:
for etternavn, fornavn, karakter in sorted(elever, key=lambda e: (e[0], e[1])):
    print(f"{etternavn}, {fornavn}: {karakter}")

# Berg, Anna: 6
# Berg, Ola: 5
# Nilsen, Kari: 4
```

Vil du ha én egenskap stigende og en annen synkende samtidig (f.eks. etternavn A–Å, men innenfor samme etternavn høyeste karakter først), kan du gjøre om tallverdien med et minustegn i stedet for å bruke `reverse`, siden `reverse=True` alltid snur *hele* sorteringen:

```python
# Etternavn stigende, men karakter synkende ved likt etternavn:
for etternavn, fornavn, karakter in sorted(elever, key=lambda e: (e[0], -e[2])):
    print(f"{etternavn}, {fornavn}: {karakter}")
```

## Steg 7: Sortere en dictionary

En dictionary husker rekkefølgen ting ble lagt inn i (siden Python 3.7), men den er ikke sortert av seg selv. Det finnes tre vanlige varianter, avhengig av hva du vil sortere etter og hva du vil ha ut.

**Sortere etter nøkkel**, og gå gjennom i den rekkefølgen — `sorted()` brukt direkte på en dictionary sorterer nøklene:

```python
karakterer = {"Kari": 5, "Ola": 3, "Nora": 6, "Jonas": 4}

for navn in sorted(karakterer):
    print(navn, "->", karakterer[navn])
```

**Sortere etter verdi** — da må du sortere `.items()` (nøkkel-verdi-parene) i stedet, med `key=lambda par: par[1]`:

```python
for navn, karakter in sorted(karakterer.items(), key=lambda par: par[1]):
    print(navn, "->", karakter)
```

**Lage en ny dictionary som *er* sortert** (i stedet for bare å gå gjennom i sortert rekkefølge) — pakk de sorterte parene inn i `dict()`. Siden en dictionary husker innsettingsrekkefølgen, vil den nye dictionaryen da også iterere i sortert rekkefølge:

```python
sortert_etter_verdi = dict(sorted(karakterer.items(), key=lambda par: par[1], reverse=True))
print(sortert_etter_verdi)  # {'Nora': 6, 'Kari': 5, 'Jonas': 4, 'Ola': 3}
```

## Steg 8: Sortere en liste av dictionaries

Dette er trolig den vanligste — og mest forvirrende — kombinasjonen: en liste der hvert element er en dictionary, for eksempel et register over elever. Prinsippet er nøyaktig det samme som i steg 5, men siden hvert element nå er en dictionary i stedet for en tupel, bruker `key` navnet på feltet (nøkkelen) i stedet for en tallindeks:

```python
elever = [
    {"navn": "Ola", "klasse": "3IM2", "karakter": 4},
    {"navn": "Kari", "klasse": "3IM1", "karakter": 5},
    {"navn": "Nora", "klasse": "3IM1", "karakter": 6},
]

# Sortert etter karakter, høyest først:
for elev in sorted(elever, key=lambda e: e["karakter"], reverse=True):
    print(elev["navn"], elev["karakter"])
```

Akkurat som med tupler kan du sortere etter flere felt ved å returnere en tupel fra lambdaen — her sorterer vi etter klasse, og deretter navn innenfor hver klasse:

```python
for elev in sorted(elever, key=lambda e: (e["klasse"], e["navn"])):
    print(elev["klasse"], elev["navn"])
```

**Obs!** Både `.sort()` og `sorted()` med `key` *flytter hele dictionaryen* som ett element — de endrer ikke innholdet i den, bare rekkefølgen dictionaryene kommer i på ytre nivå.

## Steg 9 (bonus): Stabil sortering

Pythons sortering er **stabil**. Det betyr at elementer som er *like* etter sorteringskriteriet, beholder sin **opprinnelige innbyrdes rekkefølge** i resultatet. Dette høres kanskje ut som en detalj, men det er faktisk nyttig: du kan sortere i flere omganger, fra minst til mest viktig kriterium, og få samme resultat som med én kombinert tupel-nøkkel:

```python
elever = [
    {"navn": "Ola", "klasse": "3IM2"},
    {"navn": "Kari", "klasse": "3IM1"},
    {"navn": "Nora", "klasse": "3IM1"},
]

# Sorter først på navn, deretter (stabilt) på klasse:
elever.sort(key=lambda e: e["navn"])
elever.sort(key=lambda e: e["klasse"])

for elev in elever:
    print(elev["klasse"], elev["navn"])
# 3IM1 Kari
# 3IM1 Nora
# 3IM2 Ola
```

Fordi den siste sorteringen (på klasse) er stabil, forstyrrer den ikke navnesorteringen fra steget før *innenfor* hver klasse. Dette er samme resultat som `sorted(elever, key=lambda e: (e["klasse"], e["navn"]))`, men kan være greit å vite om når du støter på det i andres kode.

## Oppsummering

| Situasjon | Løsning |
|---|---|
| Sortere lista selv, stigende (endrer originalen) | `liste.sort()` |
| Få en ny, sortert liste (originalen uendret) | `sorted(liste)` |
| Sortere synkende | `liste.sort(reverse=True)` / `sorted(liste, reverse=True)` |
| Sortere etter en egenskap (f.eks. lengde) | `sorted(liste, key=len)` |
| Sortere uavhengig av store/små bokstaver | `sorted(liste, key=str.lower)` |
| Sortere etter noe du regner ut selv | `sorted(liste, key=lambda x: ...)` |
| Sortere tupler/lister etter ett element | `sorted(liste, key=lambda t: t[1])` |
| Sortere etter flere kriterier | `sorted(liste, key=lambda t: (t[0], t[1]))` |
| Sortere en dictionary etter nøkkel | `sorted(dict)` |
| Sortere en dictionary etter verdi | `sorted(dict.items(), key=lambda par: par[1])` |
| Lage en ny, sortert dictionary | `dict(sorted(dict.items(), key=lambda par: par[1]))` |
| Sortere en liste av dictionaries etter et felt | `sorted(liste, key=lambda d: d["felt"])` |

## Øvingsoppgaver

1. Lag en liste med tallene `[7, 2, 9, 4, 1]`. Sorter lista stigende med `.sort()`, skriv den ut, sorter den deretter synkende og skriv ut på nytt.
2. Lag en liste med tallene `[23, 4, 100, 9, 56]` og skriv ut en sortert kopi med `sorted()` uten å endre originallista. Skriv ut *begge* listene for å vise forskjellen (dette er samme "triks" som gjør at Python ikke trenger noe eget sorteringstriks for tall, i motsetning til JavaScript).
3. Lag en liste med ordene `["epler", "kiwi", "fiken", "sitron", "fe"]`. Skriv ut lista sortert etter *lengde* på ordene, med `key=len`.
4. Lag en liste med navnene `["olsen", "Berg", "aas", "Nilsen"]`. Skriv ut lista sortert vanlig med `sorted()`, og deretter sortert uavhengig av store/små bokstaver med `key=str.lower`. Forklar med egne ord hvorfor de to resultatene er forskjellige.
5. Lag en liste med tupler `[("Ola", 88), ("Kari", 95), ("Nora", 72), ("Jonas", 95)]` som representerer navn og poengsum. Skriv ut lista sortert etter poengsum, høyest først. Hvem havner øverst av de to med poengsum 95, og hvorfor (tenk på stabil sortering)?
6. (Litt videre­kommen) Ta utgangspunkt i lista fra oppgave 5. Bruk en lambda til å sortere listen etter *siste bokstav* i navnet i stedet for poengsum.
7. (Litt videre­kommen) Lag en dictionary `befolkning` med minst fire norske byer som nøkler og innbyggertall som verdier. Skriv ut byene sortert etter innbyggertall, flest først, på formen `Oslo: 697899`.
8. (Avansert) Lag en liste av dictionaries `elever`, der hver dictionary har feltene `"navn"`, `"klasse"` og `"karakter"` (minst fem elever, gjerne med noen som går i samme klasse). Skriv ut elevene sortert etter klasse, og innad i hver klasse etter karakter (høyest først). Bruk en tupel som `key`, og husk minustrikset fra steg 6 for å få karakteren synkende samtidig som klassen er stigende.
9. (Avansert) Under ser du resultater fra en hopp-konkurranse, der hver utøver har flere forsøk:

    ```python
    hopp = [
        {"navn": "Kari", "forsøk": [5.2, 5.8, 5.4]},
        {"navn": "Ola", "forsøk": [5.9, 5.1, 6.0]},
        {"navn": "Nora", "forsøk": [5.5, 5.6, 5.3]},
    ]
    ```

    a) Skriv ut utøverne sortert etter deres *beste* forsøk (bruk `max()` inne i lambdaen), best først.
    b) Lag en ny, sortert liste av dictionaries der hver dictionary i tillegg har fått et nytt felt `"beste"` med utøverens beste resultat (bruk en løkke, ikke comprehension, hvis du ikke har hatt det ennå).

## Løsningsforslag

**Oppgave 1**

```python
tall = [7, 2, 9, 4, 1]
tall.sort()
print(tall)  # [1, 2, 4, 7, 9]

tall.sort(reverse=True)
print(tall)  # [9, 7, 4, 2, 1]
```

**Oppgave 2**

```python
tall = [23, 4, 100, 9, 56]
sortert_tall = sorted(tall)

print("Original:", tall)             # [23, 4, 100, 9, 56]  -  uendret
print("Sortert kopi:", sortert_tall)  # [4, 9, 23, 56, 100]
```

**Oppgave 3**

```python
ord = ["epler", "kiwi", "fiken", "sitron", "fe"]
print(sorted(ord, key=len))  # ['fe', 'kiwi', 'epler', 'fiken', 'sitron']
```

**Oppgave 4**

```python
navn = ["olsen", "Berg", "aas", "Nilsen"]

print(sorted(navn))                  # ['Berg', 'Nilsen', 'aas', 'olsen']
print(sorted(navn, key=str.lower))   # ['aas', 'Berg', 'Nilsen', 'olsen']
```

Uten `key` sammenligner Python bokstavene direkte, og store bokstaver har lavere Unicode-verdi enn små bokstaver — derfor havner `"Berg"` og `"Nilsen"` (store forbokstaver) først. Med `key=str.lower` gjøres alle ordene midlertidig om til små bokstaver *før* sammenligningen, slik at sorteringen blir alfabetisk slik vi vanligvis tenker på det, uavhengig av store/små bokstaver.

**Oppgave 5**

```python
resultater = [("Ola", 88), ("Kari", 95), ("Nora", 72), ("Jonas", 95)]

for navn, poeng in sorted(resultater, key=lambda par: par[1], reverse=True):
    print(navn, poeng)
# Kari 95
# Jonas 95
# Ola 88
# Nora 72
```

`Kari` havner over `Jonas`, siden de har lik poengsum (95) og sortering i Python er *stabil* — elementer som er like etter sorteringskriteriet beholder sin opprinnelige rekkefølge, og `Kari` lå før `Jonas` i den originale lista.

**Oppgave 6**

```python
resultater = [("Ola", 88), ("Kari", 95), ("Nora", 72), ("Jonas", 95)]

for navn, poeng in sorted(resultater, key=lambda par: par[0][-1]):
    print(navn, poeng)
```

**Oppgave 7**

```python
befolkning = {"Oslo": 697899, "Bergen": 298969, "Trondheim": 209462, "Stavanger": 148289}

for by, innbyggere in sorted(befolkning.items(), key=lambda par: par[1], reverse=True):
    print(f"{by}: {innbyggere}")
```

**Oppgave 8**

```python
elever = [
    {"navn": "Ola", "klasse": "3IM2", "karakter": 4},
    {"navn": "Kari", "klasse": "3IM1", "karakter": 5},
    {"navn": "Nora", "klasse": "3IM1", "karakter": 6},
    {"navn": "Jonas", "klasse": "3IM2", "karakter": 6},
    {"navn": "Emma", "klasse": "3IM1", "karakter": 3},
]

for elev in sorted(elever, key=lambda e: (e["klasse"], -e["karakter"])):
    print(elev["klasse"], elev["navn"], elev["karakter"])
# 3IM1 Nora 6
# 3IM1 Kari 5
# 3IM1 Emma 3
# 3IM2 Jonas 6
# 3IM2 Ola 4
```

**Oppgave 9**

```python
hopp = [
    {"navn": "Kari", "forsøk": [5.2, 5.8, 5.4]},
    {"navn": "Ola", "forsøk": [5.9, 5.1, 6.0]},
    {"navn": "Nora", "forsøk": [5.5, 5.6, 5.3]},
]

# a)
for utøver in sorted(hopp, key=lambda u: max(u["forsøk"]), reverse=True):
    print(utøver["navn"], max(utøver["forsøk"]))
# Ola 6.0
# Kari 5.8
# Nora 5.6

# b)
hopp_med_beste = sorted(hopp, key=lambda u: max(u["forsøk"]), reverse=True)
for utøver in hopp_med_beste:
    utøver["beste"] = max(utøver["forsøk"])

for utøver in hopp_med_beste:
    print(utøver)
```
