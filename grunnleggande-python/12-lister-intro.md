# Lister i Python

## Introduksjon

En **liste** er en samling verdier lagret i én og samme variabel. I stedet for å ha ti separate variabler for ti navn, kan du ha én liste med ti navn i seg. Lister er en av de mest brukte datastrukturene i Python, og de fleste programmer du kommer til å skrive vil bruke lister på et eller annet tidspunkt.

Du har allerede møtt noe lignende: en streng (`str`) er en sekvens av bokstaver.

```python
setning = "Hei, verden!"
for bokstav in setning:
    print(bokstav, end=" ")
```

En liste fungerer på samme måte — du kan gå gjennom den med en løkke, hente ut enkeltelementer og finne lengden med `len()` — men mens en streng bare kan inneholde tegn, kan en liste inneholde *hva som helst*: tall, tekst, andre lister, eller en blanding av alt sammen.

## Steg 1: Opprette en liste

En liste lages med hakeparenteser `[]`, med elementene atskilt med komma:

```python
frukter = ["eple", "banan", "pære"]
print(frukter)
```

Lister kan blande typer, og kan også inneholde andre lister:

```python
blanding = [1, 2, 3, 4, 5, ["seks", "sju"]]
print(blanding)
```

## Steg 2: Hente ut elementer (indeksering)

Hvert element i en liste har en **indeks** — en plassering — som starter på `0`, ikke `1`.

```python
frukter = ["eple", "banan", "pære"]

print(frukter[0])  # eple  (første element)
print(frukter[1])  # banan
print(frukter[2])  # pære  (siste element)
```

Python lar deg også telle **bakfra** med negative indekser. `-1` er alltid siste element, `-2` er nest siste, og så videre:

```python
print(frukter[-1])  # pære  (siste element)
print(frukter[-2])  # banan (nest siste)
```

Dette er svært nyttig når du vil hente det siste elementet uten å måtte vite hvor langt lista er (`frukter[len(frukter) - 1]` blir fort tungvint).

Prøver du å hente en indeks som ikke finnes, får du en feilmelding (`IndexError`):

```python
print(frukter[10])  # IndexError: list index out of range
```

## Steg 3: Endre, legge til og fjerne elementer

Lister er **mutable** — det betyr at du kan endre innholdet direkte, uten å lage en ny liste.

**Endre et element** ved å tilordne en ny verdi til en indeks:

```python
frukter[1] = "appelsin"
print(frukter)  # ['eple', 'appelsin', 'pære']
```

**Legge til** et element bakerst med `append()`:

```python
frukter.append("kiwi")
print(frukter)  # ['eple', 'appelsin', 'pære', 'kiwi']
```

**Sette inn** et element på en bestemt plass med `insert(indeks, verdi)`:

```python
frukter.insert(1, "mango")
print(frukter)  # ['eple', 'mango', 'appelsin', 'pære', 'kiwi']
```

**Fjerne** et element finnes det flere måter å gjøre på, avhengig av hva du vet:

```python
frukter.remove("mango")   # Fjerner det første elementet som er lik "mango"
siste = frukter.pop()     # Fjerner OG returnerer siste element i lista
del frukter[0]            # Fjerner elementet på indeks 0
print(frukter)
print("Fjernet:", siste)
```

`remove()` bruker altså *verdien*, mens `pop()` og `del` bruker *indeksen* (`pop()` uten argument tar siste element).

## Steg 4: Sjekke om et element finnes

Med `in`-operatoren kan du sjekke om en verdi finnes i en liste, uten å lete etter den selv:

```python
tall = [1, 2, 3, 4, 5]

if 3 in tall:
    print("Tallet 3 er i lista.")

if 8 not in tall:
    print("Tallet 8 er IKKE i lista.")
```

## Steg 5: Gå gjennom en liste (løkker)

Det finnes flere måter å iterere over en liste på — de gir samme resultat, men egner seg til litt ulike ting.

**for-in-løkke** — den vanligste og mest lesbare måten, brukes når du bare trenger *verdiene*:

```python
for tall in [1, 2, 3, 4, 5]:
    print(tall)
```

**while-løkke** — mer å skrive, men nyttig hvis du trenger finere kontroll over når løkka skal stoppe eller hoppe videre:

```python
tall = [1, 2, 3, 4, 5]
i = 0
while i < len(tall):
    print(tall[i])
    i += 1
```

**for-in-range-løkke med indeks** — brukes når du trenger selve *indeksen*, for eksempel for å endre elementer mens du går gjennom lista:

```python
tall = [1, 2, 3, 4, 5]
for i in range(len(tall)):
    print(i, tall[i])
```

**enumerate() (bonus, mer pythonisk)** — gjør nøyaktig det samme som varianten over, men på en renere måte. `enumerate()` gir deg både indeksen og verdien samtidig:

```python
tall = [1, 2, 3, 4, 5]
for i, verdi in enumerate(tall):
    print(i, verdi)
```

Bruk `enumerate()` fremfor `range(len(...))` når du kan — det er lettere å lese, og du unngår å skrive `tall[i]` gjentatte ganger.

## Steg 6: Slicing — hente en del av lista

Med **slicing** kan du hente ut et utsnitt av lista med syntaksen `liste[start:stopp]`. Utsnittet inkluderer `start`, men *ikke* `stopp`:

```python
tall = [10, 20, 30, 40, 50]

print(tall[1:3])   # [20, 30]  (indeks 1 og 2)
print(tall[:2])    # [10, 20]  (fra start til og med indeks 1)
print(tall[2:])    # [30, 40, 50]  (fra indeks 2 til slutten)
print(tall[-2:])   # [40, 50]  (de to siste)
print(tall[:])     # [10, 20, 30, 40, 50]  (en kopi av hele lista)
```

## Steg 7: Sortering

`sort()` sorterer lista **i stedet**, altså endrer den originale lista, og returnerer ingenting selv:

```python
bokstaver = ["e", "b", "C", "a", "d"]
bokstaver.sort()
print(bokstaver)  # ['C', 'a', 'b', 'd', 'e']  (store bokstaver sorteres først)

bokstaver.sort(reverse=True)
print(bokstaver)  # Synkende rekkefølge
```

Ønsker du å beholde den originale lista uendret, bruk `sorted()` i stedet — den returnerer en *ny*, sortert liste:

```python
tall = [5, 3, 1, 4, 2]
sortert_tall = sorted(tall)

print("Original:", tall)          # [5, 3, 1, 4, 2]  (uendret)
print("Sortert kopi:", sortert_tall)  # [1, 2, 3, 4, 5]
```

## Steg 8: Kopiere en liste

Det er lett å tro at `liste2 = liste1` lager en kopi, men det gjør det **ikke**. Begge variabelnavnene peker da på den *samme* lista i minnet:

```python
liste1 = [1, 2, 3]
liste2 = liste1  # IKKE en kopi!

liste2.append(4)
print(liste1)  # [1, 2, 3, 4]  <- Endres også, selv om vi bare endret liste2!
```

For å lage en faktisk kopi bruker du `.copy()` (eller `list(liste1)`):

```python
liste1 = [1, 2, 3]
liste2 = liste1.copy()

liste2.append(4)
print(liste1)  # [1, 2, 3]     <- Uendret
print(liste2)  # [1, 2, 3, 4]
```

**Obs! (litt videre­kommen)** `.copy()` er en *grunn* kopi (*shallow copy*). Den kopierer selve lista, men hvis lista inneholder andre lister, deles de indre listene fortsatt mellom original og kopi:

```python
liste1 = [1, 2, [3, 4]]
liste2 = liste1.copy()

liste2[2].append(5)
print(liste1)  # [1, 2, [3, 4, 5]]  <- Den indre lista endres i BEGGE!
print(liste2)  # [1, 2, [3, 4, 5]]
```

Skal du kopiere en liste som inneholder andre lister, og vil ha en helt uavhengig kopi, trenger du `copy.deepcopy()` fra biblioteket `copy`:

```python
import copy

liste1 = [1, 2, [3, 4]]
liste2 = copy.deepcopy(liste1)

liste2[2].append(5)
print(liste1)  # [1, 2, [3, 4]]     <- Nå er den uendret
print(liste2)  # [1, 2, [3, 4, 5]]
```

## Steg 9: Multidimensjonale lister

En liste kan inneholde andre lister som elementer — dette brukes ofte til å representere tabeller, rutenett eller koordinater:

```python
koordinater = [
    [1, 2, 3],
    [4, 5, 6],
]

print(koordinater)

for k in koordinater:
    print("Koordinat:", k[0], k[1], k[2])
```

Du kan også hente ut et enkeltelement direkte med to indekser etter hverandre: `koordinater[0][1]` gir `2` (rad 0, kolonne 1).

## Steg 10 (bonus): List comprehension

Når du lager en ny liste ved å gå gjennom en annen, skriver du ofte noe slikt:

```python
tall = [1, 2, 3, 4, 5]
kvadrater = []
for t in tall:
    kvadrater.append(t ** 2)

print(kvadrater)  # [1, 4, 9, 16, 25]
```

Python har en kortere skrivemåte for akkurat dette mønsteret, kalt **list comprehension**:

```python
tall = [1, 2, 3, 4, 5]
kvadrater = [t ** 2 for t in tall]
print(kvadrater)  # [1, 4, 9, 16, 25]
```

Du kan også legge på en betingelse, som fungerer som et filter:

```python
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
partall = [t for t in tall if t % 2 == 0]
print(partall)  # [2, 4, 6, 8, 10]
```

List comprehension er ikke pensum i seg selv her, men det er lurt å kunne *lese* den — du vil møte den mye i andres Python-kode.

## Steg 11 (bonus): Statistikk og analyse av lister

Python har flere innebygde funksjoner som gjør det unødvendig å skrive egne løkker for å analysere tall i en liste.

**Antall, sum, høyeste og laveste verdi:**

```python
tall = [4, 8, 15, 16, 23, 42]

print(len(tall))  # 6   - antall elementer
print(sum(tall))  # 108 - summen av alle tallene
print(max(tall))  # 42  - høyeste verdi
print(min(tall))  # 4   - laveste verdi
```

**Gjennomsnitt** finnes ikke som egen innebygd funksjon, men er lett å regne ut selv ved å kombinere `sum()` og `len()`. `round()` er nyttig for å avrunde resultatet til et gitt antall desimaler:

```python
tall = [4, 8, 15, 16, 23, 42]
gjennomsnitt = sum(tall) / len(tall)
print(gjennomsnitt)              # 18.0
print(round(gjennomsnitt, 1))    # 18.0 avrundet til én desimal
```

**Telle forekomster** av en bestemt verdi med `count()`, og **finne indeksen** til en verdi med `index()`:

```python
karakterer = [4, 5, 3, 5, 6, 5, 2]

print(karakterer.count(5))  # 3 - femmeren forekommer tre ganger
print(karakterer.index(5))  # 1 - den FØRSTE femmeren ligger på indeks 1
```

**max() og min() med `key`**: du kan også bruke `max()`/`min()` på lister som ikke er tall, ved å fortelle Python hva den skal sammenligne på. Her finner vi det lengste og korteste navnet i en liste med `key=len`:

```python
navn = ["Kristoffer", "Eli", "Bernt-Åge", "Nora"]

print(max(navn, key=len))  # Kristoffer - det lengste navnet
print(min(navn, key=len))  # Eli - det korteste navnet
```

**Bonus (litt videre­kommen):** trenger du median (midterste verdi) eller typetall (mest vanlige verdi), finnes ikke det som innebygde funksjoner — da kan biblioteket `statistics` hjelpe deg:

```python
import statistics

tall = [4, 8, 15, 16, 23, 42]

print(statistics.mean(tall))      # 18    - gjennomsnitt
print(statistics.median(tall))    # 15.5  - medianen (midterste verdi i sortert rekkefølge)
print(statistics.mode([1, 2, 2, 3]))  # 2 - den mest vanlige verdien (typetall)
```

`statistics.median()` sorterer lista selv, så du trenger ikke sortere den på forhånd.

## Tuppel — en liste som ikke kan endres

Et **tuppel** (`tuple`) ligner på en liste, men er **immutable** — når det først er laget, kan innholdet ikke endres. Det skrives med runde parenteser `()` i stedet for hakeparenteser:

```python
koordinat = (1, 2, 3)
print(koordinat[0])  # 1
```

Prøver du å endre et element, får du en feilmelding:

```python
koordinat[0] = 9  # TypeError: 'tuple' object does not support item assignment
```

Du kan derimot lage et *nytt* tuppel ved å slå sammen med `+`:

```python
koordinat = (1, 2, 3)
koordinat = koordinat + (4,)  # Legg merke til kommaet — (4) alene ville bare vært tallet 4
print(koordinat)  # (1, 2, 3, 4)
```

Bruk tuppel når du har data som ikke skal kunne endres ved en feiltagelse — for eksempel faste koordinater, eller når du returnerer flere verdier fra en funksjon.

## Sett — bare unike verdier

Et **sett** (`set`) er en usortert samling der hver verdi bare kan forekomme én gang. Det skrives med krøllparenteser `{}`:

```python
unike_tall = {1, 2, 3, 4, 5}
print(unike_tall)
```

Setter er nyttige for å fjerne duplikater fra en liste, siden dupliserte verdier automatisk forsvinner:

```python
tall_med_duplikater = [1, 2, 2, 3, 3, 3, 4]
unike_tall = set(tall_med_duplikater)
print(unike_tall)  # {1, 2, 3, 4}
```

Samme prinsipp fungerer på en streng, siden en streng også er en sekvens av tegn:

```python
unike_bokstaver = set("Hello, world!")
print(unike_bokstaver)
```

Legg merke til at rekkefølgen i et sett ikke er garantert — hvis du trenger rekkefølge, bruk en liste.

## Oppsummering

| Type | Skrivemåte | Kan endres? | Rekkefølge? | Duplikater tillatt? |
|---|---|---|---|---|
| Liste (`list`) | `[1, 2, 3]` | Ja | Ja | Ja |
| Tuppel (`tuple`) | `(1, 2, 3)` | Nei | Ja | Ja |
| Sett (`set`) | `{1, 2, 3}` | Ja (kan legge til/fjerne, men innholdet er alltid unikt) | Nei | Nei |

| Situasjon | Løsning |
|---|---|
| Legge til ett element bakerst | `liste.append(verdi)` |
| Sette inn et element på en bestemt plass | `liste.insert(indeks, verdi)` |
| Fjerne et element du vet *verdien* av | `liste.remove(verdi)` |
| Fjerne et element du vet *indeksen* til | `del liste[indeks]` eller `liste.pop(indeks)` |
| Sjekke om en verdi finnes | `verdi in liste` |
| Hente en del av lista | `liste[start:stopp]` |
| Sortere lista selv (endrer originalen) | `liste.sort()` |
| Få en ny, sortert liste (originalen uendret) | `sorted(liste)` |
| Sum, høyeste og laveste verdi | `sum(liste)`, `max(liste)`, `min(liste)` |
| Gjennomsnitt | `sum(liste) / len(liste)` |
| Telle forekomster av en verdi | `liste.count(verdi)` |
| Finne indeksen til en verdi | `liste.index(verdi)` |
| Median eller typetall | `statistics.median(liste)`, `statistics.mode(liste)` |
| Kopiere en liste (uten nøstede lister) | `liste.copy()` |
| Kopiere en liste med nøstede lister | `copy.deepcopy(liste)` |
| Data som ikke skal kunne endres | tuppel i stedet for liste |
| Kun unike verdier, rekkefølge er uviktig | sett i stedet for liste |

## Øvingsoppgaver

1. Lag en liste med navnene på fem venner. Skriv ut det første og det siste navnet i lista ved hjelp av indeksering (bruk negativ indeks for det siste).
2. Ta utgangspunkt i lista fra oppgave 1. Legg til ett nytt navn bakerst med `append()`, og fjern deretter det andre navnet med `remove()`.
3. Lag en liste med tallene fra 1 til 10. Bruk en `for`-løkke til å skrive ut bare partallene i lista.
4. Lag en liste med tallene `[4, 1, 3, 9, 2]`. Skriv ut en sortert kopi av lista med `sorted()`, og skriv deretter ut den originale lista for å vise at den er uendret.
5. Lag en liste `original = [1, 2, 3]`. Lag en kopi kalt `feil_kopi` med `feil_kopi = original` (uten `.copy()`), legg til et tall i `feil_kopi`, og skriv ut begge listene. Forklar med egne ord hvorfor `original` også endret seg.
6. (Litt videre­kommen) Lag en 3x3-matrise som en liste av lister (ni tall, valgfritt hvilke). Bruk to `for`-løkker etter hverandre (en ytre og en indre) til å skrive ut hvert enkelt tall.
7. (Bonus) Bruk list comprehension til å lage en liste med kvadrattallene til tallene fra 1 til 10 (altså `[1, 4, 9, ..., 100]`).
8. Lag en liste med seks eksamenskarakterer, for eksempel `[4, 5, 3, 6, 5, 4]`. Skriv ut høyeste karakter, laveste karakter, og gjennomsnittskarakteren avrundet til én desimal med `round()`. Bruk deretter `count()` til å finne ut hvor mange ganger karakteren 4 forekommer.
9. Under ser du flyreisetider (i minutter) mellom fire norske flyplasser, lagret som en liste med navn og en tilhørende multidimensjonal liste, der `reisetider[i][j]` er reisetiden fra flyplass `i` til flyplass `j` (en flyplass har alltid reisetid `0` til seg selv):

    ```python
    flyplasser = ["Flesland", "Gardermoen", "Værnes", "Sola"]
    reisetider = [
        [0, 55, 70, 50],
        [55, 0, 60, 55],
        [70, 60, 0, 80],
        [50, 55, 80, 0],
    ]
    ```

    a) Finn indeksen til `"Flesland"` og `"Værnes"` med `.index()`, og bruk dem til å skrive ut reisetiden mellom de to flyplassene.
    b) Bruk to `for`-løkker etter hverandre (en ytre og en indre, begge med `enumerate()`) til å skrive ut alle reisene på formen `Fra Flesland til Gardermoen: 55 minutter`. Hopp over cellene der reisetiden er `0`.
    c) Finn og skriv ut den lengste reisetiden i hele tabellen, og hvilke to flyplasser den er mellom.

## Løsningsforslag

**Oppgave 1**

```python
venner = ["Ola", "Kari", "Per", "Nora", "Jonas"]
print(venner[0])
print(venner[-1])
```

**Oppgave 2**

```python
venner = ["Ola", "Kari", "Per", "Nora", "Jonas"]
venner.append("Emma")
venner.remove(venner[1])
print(venner)
```

**Oppgave 3**

```python
tall = list(range(1, 11))
for t in tall:
    if t % 2 == 0:
        print(t)
```

**Oppgave 4**

```python
tall = [4, 1, 3, 9, 2]
sortert_tall = sorted(tall)
print("Sortert kopi:", sortert_tall)
print("Original:", tall)
```

**Oppgave 5**

```python
original = [1, 2, 3]
feil_kopi = original
feil_kopi.append(4)
print(original)    # [1, 2, 3, 4]
print(feil_kopi)    # [1, 2, 3, 4]
```

`original` og `feil_kopi` peker på den samme lista i minnet — `feil_kopi = original` kopierer ikke innholdet, bare *navnet* som peker til lista. Derfor slår en endring via det ene navnet ut på begge.

**Oppgave 6**

```python
matrise = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for rad in matrise:
    for tall in rad:
        print(tall)
```

**Oppgave 7**

```python
kvadrater = [t ** 2 for t in range(1, 11)]
print(kvadrater)
```

**Oppgave 8**

```python
karakterer = [4, 5, 3, 6, 5, 4]

print("Høyeste:", max(karakterer))
print("Laveste:", min(karakterer))
print("Gjennomsnitt:", round(sum(karakterer) / len(karakterer), 1))
print("Antall firere:", karakterer.count(4))
```

**Oppgave 9**

```python
flyplasser = ["Flesland", "Gardermoen", "Værnes", "Sola"]
reisetider = [
    [0, 55, 70, 50],
    [55, 0, 60, 55],
    [70, 60, 0, 80],
    [50, 55, 80, 0],
]

# a)
i = flyplasser.index("Flesland")
j = flyplasser.index("Værnes")
print(f"Flesland til Værnes: {reisetider[i][j]} minutter")

# b)
for i, fra in enumerate(flyplasser):
    for j, til in enumerate(flyplasser):
        if reisetider[i][j] != 0:
            print(f"Fra {fra} til {til}: {reisetider[i][j]} minutter")

# c)
lengste = 0
par = ("", "")
for i, fra in enumerate(flyplasser):
    for j, til in enumerate(flyplasser):
        if reisetider[i][j] > lengste:
            lengste = reisetider[i][j]
            par = (fra, til)

print(f"Lengste reisetid: {lengste} minutter, mellom {par[0]} og {par[1]}")
```
