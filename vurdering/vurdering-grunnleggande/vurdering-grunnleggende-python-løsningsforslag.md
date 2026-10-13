# Løsningsforslag: Vurdering i grunnleggende Python

Dette er et løsningsforslag til [prøven i grunnleggende Python](vurdering-grunnleggende-python.md). Det er laget for at du skal kunne gå gjennom oppgavene på nytt i ditt eget tempo.

Det finnes nesten alltid flere riktige måter å løse en programmeringsoppgave på. Der flere av dere løste en oppgave på ulike måter, viser jeg derfor flere alternativer, og forklarer fordeler og ulemper ved hvert av dem. Under mange av oppgavene står det også en liste over **vanlige feil** fra besvarelsene, slik at du kan sjekke om du har gjort noen av dem.

**Tips:** Prøv å løse oppgaven selv først, før du leser løsningen. Kjør så koden din, og sammenlign med løsningsforslaget.

## Innhold

- [Del A: Lese og forstå kode](#del-a-lese-og-forstå-kode)
  - [Oppgave 1](#oppgave-1) · [Oppgave 2](#oppgave-2) · [Oppgave 3](#oppgave-3)
- [Del B: Oppgaver per tema](#del-b-oppgaver-per-tema)
  - [Oppgave 4: Valgsetninger](#oppgave-4-valgsetninger) · [Oppgave 5: Løkker og feilhåndtering](#oppgave-5-løkker-og-feilhåndtering) · [Oppgave 6: Lister](#oppgave-6-lister) · [Oppgave 7: Dictionary](#oppgave-7-dictionary) · [Oppgave 8: Funksjoner](#oppgave-8-funksjoner)
- [Del C: Kombinerte oppgaver](#del-c-kombinerte-oppgaver)
  - [Oppgave 9: Varebeholdning](#oppgave-9-varebeholdning-i-en-nettbutikk) · [Oppgave 10: Treningslogg](#oppgave-10-treningslogg)
- [Generelle råd](#generelle-råd)

---

## Del A: Lese og forstå kode

I denne delen skulle du forutsi hva koden gjør **uten** å kjøre den. Et godt svar har to deler:

1. **Nøyaktig hva som skrives ut**, tegn for tegn.
2. **En forklaring** på hvorfor.

Flere av dere forklarte godt hva koden gjør, men glemte å skrive opp selve utskriften. Husk at spørsmålet var *«Hva skriver kodesnuttene ut?»*.

### Oppgave 1

#### a)

```python
minutter = 135
print(f"{minutter // 60} t og {minutter % 60} min")
```

**Utskrift:** `2 t og 15 min`

- `//` er **heltallsdivisjon**. Den deler og kaster bort desimalene: `135 // 60` er `2`, fordi 60 går opp i 135 to hele ganger.
- `%` er **modulo** og gir **resten** etter heltallsdivisjonen: `2 * 60 = 120`, og `135 - 120 = 15`.

`//` og `%` hører ofte sammen. Med dem kan du gjøre om minutter til timer og minutter, sekunder til minutter og sekunder, og så videre. Du får bruk for dette igjen i oppgave 8a.

#### b)

```python
fag = "Programmering"
print(fag[0:4].upper() + fag[-3:])
```

**Utskrift:** `PROGing`

Det hjelper å skrive opp indeksene:

```
 P  r  o  g  r  a  m  m  e  r  i  n  g
 0  1  2  3  4  5  6  7  8  9 10 11 12
-13                      ...  -3 -2 -1
```

- `fag[0:4]` gir tegnene fra og med indeks 0 **til, men ikke med**, indeks 4: `"Prog"`.
- `.upper()` gjør alle bokstavene store: `"PROG"`.
- `fag[-3:]` starter tre tegn fra slutten og går helt til enden: `"ing"`. Negative indekser teller bakfra, så `-1` er siste tegn.
- `+` skjøter sammen to strenger: `"PROG" + "ing"` blir `"PROGing"`.

**Vanlige feil:** Å tro at slutt-indeksen er med (`[0:4]` gir fire tegn, ikke fem), og å tro at `[-3:]` bare gir ett tegn.

#### c)

```python
tall = [3, 8, 1, 6]
tall.sort(reverse=True)
print(tall[1], len(tall))
```

**Utskrift:** `6 4`

- `tall.sort(reverse=True)` sorterer lista **synkende**, altså fra størst til minst. Lista blir `[8, 6, 3, 1]`.
- `tall[1]` er det **andre** elementet, fordi indekseringen starter på 0. Det er `6`.
- `len(tall)` er antall elementer: `4`.
- Når `print` får flere verdier med komma mellom, skrives de ut med ett mellomrom mellom: `6 4`.

**Vanlige feil:** Flere svarte `1` eller `14`. Det skjer hvis du tror `reverse=True` bare snur lista (som ville gitt `[6, 1, 8, 3]`), eller glemmer at den blir sortert. `sort(reverse=True)` **sorterer**, og sorteringen blir synkende.

#### d)

```python
total = 0
for i in range(1, 10, 3):
    total += i
print(total)
```

**Utskrift:** `12`

`range(start, stopp, steg)` gir tallene fra `start`, med `steg` mellom, så lenge de er **mindre enn** `stopp`:

| Runde | `i` | `total` etterpå |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 4 | 5 |
| 3 | 7 | 12 |
| (neste ville vært 10, men 10 er ikke mindre enn 10) | | |

**Tips:** Lag en slik tabell for hånd når du skal forstå en løkke. Det kalles å «trace» koden, og er en av de beste måtene å finne feil på.

### Oppgave 2

```python
alder = input("Hvor gammel er du? ")

if alder >= 18
    print("Du er myndig.")
elif alder = 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")
```

De tre feilene:

1. **`input()` gir alltid en streng.** Selv om brukeren skriver `16`, er `alder` teksten `"16"`, ikke tallet 16. Python kan ikke sammenligne tekst med tall (`"16" >= 18` gir `TypeError`), og kan heller ikke regne ut `18 - "16"`. Løsningen er å gjøre om svaret med `int()`.
2. **Det mangler kolon etter `if alder >= 18`.** Alle `if`, `elif`, `else`, `for`, `while` og `def` må slutte med `:`. Uten kolon gir Python `SyntaxError` før programmet i det hele tatt starter.
3. **`=` er tilordning, `==` er sammenligning.** `alder = 17` betyr «la `alder` bli 17». For å *sjekke* om `alder` er 17, må du skrive `alder == 17`.

Rettet versjon:

```python
alder = int(input("Hvor gammel er du? "))

if alder >= 18:
    print("Du er myndig.")
elif alder == 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")
```

**Legg merke til:** Feil 2 og 3 er *syntaksfeil*, som Python oppdager før koden kjører. Feil 1 er en *kjøretidsfeil*, som først viser seg når programmet kommer til linja. Hvis du har den gamle, feilaktige koden stående i samme fil som den rettede, vil hele fila gi `SyntaxError` og ingenting kjører. `try`/`except` hjelper heller ikke mot syntaksfeil. Sett den gamle koden i en kommentar eller en `"""`-blokk.

### Oppgave 3

```python
def dobbel_partall(liste):
    resultat = []
    for tall in liste:
        if tall % 2 == 0:
            resultat.append(tall * 2)
        else:
            resultat.append(tall)
    return resultat

tallene = [1, 2, 3, 4]
nye = dobbel_partall(tallene)
print(nye)
print(tallene)
print(sum(nye) > 10)
```

#### a)

**Utskrift:**

```
[1, 4, 3, 8]
[1, 2, 3, 4]
True
```

- Funksjonen går gjennom tallene. Partall (der `tall % 2 == 0`) blir doblet, og oddetall legges til som de er. Derfor blir `nye` lik `[1, 4, 3, 8]`.
- `tallene` er uendret: `[1, 2, 3, 4]` (se b).
- `sum(nye)` er `1 + 4 + 3 + 8 = 16`, og `16 > 10` er `True`. Legg merke til at det er summen av den **nye** lista som sammenlignes med tallet 10. Den gamle lista er ikke med i sammenligningen.

#### b)

Denne deloppgaven var det få som fikk helt til. Spørsmålet er **hvorfor** `tallene` fortsatt er `[1, 2, 3, 4]`. Det holder ikke å forklare hva funksjonen gjør med tallene.

**Svar:** Funksjonen lager en **helt ny liste**, `resultat = []`, og legger verdiene inn i *den* med `append`. Den opprinnelige lista (`liste`, som er den samme lista som `tallene`) blir bare *lest*, aldri endret. Funksjonen returnerer den nye lista, og den lagres i `nye`. Derfor finnes det etterpå to forskjellige lister.

Til sammenligning kunne en funksjon endre den opprinnelige lista, for eksempel slik:

```python
def dobbel_partall_på_stedet(liste):
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            liste[i] = liste[i] * 2

tallene = [1, 2, 3, 4]
dobbel_partall_på_stedet(tallene)
print(tallene)  # [1, 4, 3, 8], nå er den opprinnelige lista endret!
```

Her skrives det til `liste[i]`, og da endres lista som ble sendt inn. Dette er viktig å forstå: Når du sender en liste til en funksjon, får funksjonen tilgang til **den samme lista**, ikke en kopi. Det er altså koden *inne i* funksjonen som avgjør om lista endres eller ikke.

---

## Del B: Oppgaver per tema

### Oppgave 4: Valgsetninger

#### Løsning 1: én `if`/`elif`-kjede

```python
alder = int(input("Hvor gammel er du? "))
studentbevis = input("Har du studentbevis? (ja/nei) ").lower()

if alder < 0 or alder > 120:
    print("Ugyldig alder.")
elif alder < 12:
    print("Billetten koster 80 kr.")
elif alder >= 67:
    print("Billetten koster 100 kr.")
elif alder <= 30 and studentbevis == "ja":
    print("Billetten koster 110 kr.")
else:
    print("Billetten koster 150 kr.")
```

**Hvorfor fungerer dette?**

- **Rekkefølgen betyr alt.** Python sjekker betingelsene ovenfra og ned, og stopper ved den *første* som er sann. Derfor sjekker vi ugyldig alder **først**. Ellers ville `-3` blitt fanget av `alder < 12` og fått barnebillett.
- Når vi kommer til studentlinja, vet vi allerede at alderen er minst 12 (ellers hadde `alder < 12` slått til). Derfor trenger vi bare å sjekke `alder <= 30`. Det er likevel helt riktig, og kanskje tydeligere, å skrive `12 <= alder <= 30`.
- `.lower()` gjør svaret om til små bokstaver, så `JA`, `Ja` og `ja` blir like. Det er mye kortere enn å sjekke alle variantene hver for seg.
- `and` krever at **begge** deler er sanne: riktig alder **og** studentbevis.

#### Løsning 2: spør bare om studentbevis når det er relevant

Flere av dere gjorde dette, og det er en fin idé. Hvorfor spørre en 8-åring om studentbevis?

```python
alder = int(input("Hvor gammel er du? "))

if alder < 0 or alder > 120:
    print("Ugyldig alder.")
elif alder < 12:
    print("Billetten koster 80 kr.")
elif alder >= 67:
    print("Billetten koster 100 kr.")
elif alder <= 30:
    studentbevis = input("Har du studentbevis? (ja/nei) ").lower()
    if studentbevis == "ja":
        print("Billetten koster 110 kr.")
    else:
        print("Billetten koster 150 kr.")
else:
    print("Billetten koster 150 kr.")
```

Her er `if` inne i en `elif` (en *nøstet* valgsetning). Husk å gi en pris også når svaret er `nei`.

#### Løsning 3: sjekk gyldig alder rundt alt

```python
alder = int(input("Hvor gammel er du? "))
studentbevis = input("Har du studentbevis? (ja/nei) ").lower()

if 0 <= alder <= 120:
    if alder < 12:
        pris = 80
    elif alder >= 67:
        pris = 100
    elif alder <= 30 and studentbevis == "ja":
        pris = 110
    else:
        pris = 150
    print(f"Billetten koster {pris} kr.")
else:
    print("Ugyldig alder.")
```

Her lagres prisen i en variabel, og skrives ut **ett** sted. Det gjør det lettere å endre teksten senere. `0 <= alder <= 120` er en *kjedet sammenligning*, som betyr det samme som `0 <= alder and alder <= 120`.

#### Test med disse verdiene

| Alder | Studentbevis | Forventet |
|---|---|---|
| 10 | ja | 80 kr |
| 25 | JA | 110 kr |
| 25 | nei | 150 kr |
| 30 | ja | 110 kr |
| 31 | ja | 150 kr |
| 67 | nei | 100 kr |
| −3 | | feilmelding |

Legg merke til **grenseverdiene** 30 og 67. Det er der feilene oftest skjuler seg.

**Vanlige feil:**

- **Ingen sjekk av ugyldig alder.**
- **`alder > 67` i stedet for `alder >= 67`.** Da betaler en 67-åring full pris, selv om «67 år eller eldre» skal ha honnør.
- **`.lower()` og så sammenligning med `"Ja"`.** Etter `.lower()` finnes det ingen store bokstaver lenger, så `"Ja"` blir aldri likt. Sammenlign med `"ja"`.
- **Ingen pris når svaret er «nei».** Med en nøstet `if` uten `else` får en 20-åring uten studentbevis ingen pris.

### Oppgave 5: Løkker og feilhåndtering

#### Løsning 1: `while True` med `break`

```python
BILLETTPRIS = 150

while True:
    try:
        antall = int(input("Antall billetter: "))
    except ValueError:
        print("Du må skrive inn et heltall.")
        continue

    if 1 <= antall <= 10:
        break

    print("Du kan kjøpe mellom 1 og 10 billetter.")

print(f"Totalpris: {antall * BILLETTPRIS} kr")
```

**Slik fungerer den:**

- `while True` er en løkke som går «for alltid», helt til vi selv stopper den med `break`.
- `int(...)` gir `ValueError` hvis teksten ikke er et heltall, for eksempel `"to"` eller `""`. Da hopper Python til `except`-blokka, i stedet for å krasje.
- `continue` hopper rett til neste runde i løkka, så vi spør på nytt.
- Hvis tallet er gyldig, går vi ut av løkka med `break`. Ellers skriver vi en feilmelding, og løkka spør på nytt.
- `BILLETTPRIS` er skrevet med store bokstaver. Det er en vanlig måte å vise at en verdi er en **konstant**, som ikke skal endres underveis.

#### Løsning 2: med en `gyldig`-variabel

```python
BILLETTPRIS = 150
gyldig = False

while not gyldig:
    tekst = input("Antall billetter: ")

    try:
        antall = int(tekst)
    except ValueError:
        print("Du må skrive inn et heltall.")
        continue

    if 1 <= antall <= 10:
        gyldig = True
    else:
        print("Du kan kjøpe mellom 1 og 10 billetter.")

print(f"Totalpris: {antall * BILLETTPRIS} kr")
```

Dette gjør det samme. Noen synes det er lettere å lese `while not gyldig` enn `while True` med `break`. Velg det du synes er tydeligst.

#### Hvor skal intervallsjekken stå?

Mange av dere la `if 1 <= antall <= 10` **inne i** `try`-blokka:

```python
try:
    antall = int(input("Antall billetter: "))
    if 1 <= antall <= 10:
        ...
except ValueError:
    ...
```

Det fungerer her, men det er en god vane å ha **så lite kode som mulig** i `try`-blokka. Bare linja som faktisk kan gi feilen du fanger (`int(...)`), bør stå der. Da er det tydelig hvilken feil `except` er ment for, og du risikerer ikke å skjule andre feil ved et uhell.

#### Hvorfor ikke lage en egen funksjon som sjekker om teksten er et tall?

Det går an, og det kan være god trening. Men det er lett å gjøre feil. Et eksempel fra besvarelsene sjekket om alle tegnene var med i `"123567890"`, der sifferet `4` hadde falt ut. Da ble `4` og `14` avvist. En tom tekst `""` slapp også gjennom sjekken og fikk `int("")` til å krasje. `try`/`except ValueError` lar Python selv avgjøre hva som er et gyldig heltall, og det er både kortere og tryggere. (Python har også `tekst.isdigit()`, men den godtar for eksempel ikke `-3`.)

**Vanlige feil:**

- **`antall < 10` i stedet for `antall <= 10`.** Da avvises 10 billetter. Test alltid grenseverdiene 0, 1, 10 og 11.
- **`antall >= 1 or antall <= 10`.** Med `or` er betingelsen alltid sann, fordi alle tall er enten minst 1 *eller* høyst 10. Du trenger `and`, eller enda bedre `1 <= antall <= 10`.
- **Bare `except:` uten `ValueError`.** Da fanges *alle* feil, også feil du ikke har tenkt på, og det blir vanskeligere å feilsøke.

### Oppgave 6: Lister

```python
temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]
```

#### a)

```python
print(f"Antall målinger: {len(temperaturer)}")
print(f"Første måling: {temperaturer[0]}")
print(f"Siste måling: {temperaturer[-1]}")
```

Utskrift: `10` målinger, første `4.5` og siste `-3.5`.

- Den første målingen har indeks **0**, ikke 1.
- `temperaturer[-1]` er alltid det siste elementet, uansett hvor lang lista er. `temperaturer[9]` gir riktig svar her, men slutter å virke hvis lista får flere eller færre målinger. Det samme gjør `temperaturer[len(temperaturer) - 1]`, men `[-1]` er kortere.

#### b)

```python
gjennomsnitt = sum(temperaturer) / len(temperaturer)
print(f"Gjennomsnitt: {gjennomsnitt:.1f} grader")
```

Utskrift: `Gjennomsnitt: 0.8 grader`.

Det er to gode måter å avrunde til én desimal:

| Måte | Eksempel | Hva skjer |
|---|---|---|
| Formatering i f-strengen | `f"{gjennomsnitt:.1f}"` | Tallet *vises* med én desimal. Verdien i variabelen er uendret. |
| `round()` | `round(gjennomsnitt, 1)` | Gir et nytt tall som *er* avrundet. |

**Vanlige feil:**

- **`round(gjennomsnitt, 1)` på en linje for seg selv.** `round()` endrer ikke variabelen. Den *returnerer* et nytt tall, og det må du ta vare på: `gjennomsnitt = round(gjennomsnitt, 1)`.
- **`round(..., 2)`** gir to desimaler, ikke én.
- **`(x // 0.1) / 10`** runder alltid *ned* (0.79 blir 0.7), og det er ikke det samme som å avrunde.

#### c)

```python
dager_under_null = 0
for temperatur in temperaturer:
    if temperatur < 0:
        dager_under_null += 1

print(f"Dager under 0 grader: {dager_under_null}")
```

Utskrift: `4`. Dette er det klassiske mønsteret for å **telle**: start på 0, gå gjennom alt, og legg til 1 hver gang betingelsen stemmer. Legg merke til at `0.0` ikke telles, fordi `0.0 < 0` er `False`.

Noen brukte `for i in range(len(temperaturer))` og `temperaturer[i]`. Det er også riktig, men når du ikke trenger indeksen, er `for temperatur in temperaturer` enklere å lese.

#### d)

Her skal vi lage en **ny** liste med plussgrader, sortert fra varmest til kaldest, **uten** å endre den opprinnelige lista.

**Løsning 1: løkke, `append` og `sort`**

```python
plussgrader = []
for temperatur in temperaturer:
    if temperatur > 0:
        plussgrader.append(temperatur)

plussgrader.sort(reverse=True)
print(plussgrader)
```

**Løsning 2: `sorted()` direkte**

```python
plussgrader = []
for temperatur in sorted(temperaturer, reverse=True):
    if temperatur > 0:
        plussgrader.append(temperatur)

print(plussgrader)
```

Her sorterer vi *først* og filtrerer *etterpå*. Det går like bra, fordi rekkefølgen beholdes når vi plukker ut elementer. `sorted()` lager en ny, sortert liste og lar `temperaturer` være i fred.

**Løsning 3: list comprehension**

```python
plussgrader = sorted([temperatur for temperatur in temperaturer if temperatur > 0], reverse=True)
print(plussgrader)
```

Dette er en kompakt skrivemåte for det samme som løsning 1. Les det som «lag en liste med `temperatur` for hver `temperatur` i `temperaturer`, hvis `temperatur > 0`».

Alle tre gir `[7.0, 5.5, 4.5, 3.0, 1.5]`. Legg merke til at `0.0` ikke er med, fordi 0 ikke er *over* 0.

**`.sort()` eller `sorted()`?** Dette er verdt å lære seg godt:

| | `liste.sort()` | `sorted(liste)` |
|---|---|---|
| Endrer den opprinnelige lista? | **Ja** | Nei |
| Returnerer | `None` | En ny, sortert liste |

Derfor skriver `print(plussgrader.sort(reverse=True))` ut `None`. `.sort()` sorterer lista, men returnerer ingenting. Sorter først, og skriv ut lista etterpå, eller bruk `sorted()`.

Og husk: `temperaturer.sort()` vil endre den *opprinnelige* lista, og det sa oppgaven at du ikke skulle gjøre.

**Vanlige feil:** Å sortere hele lista og ta de fem første (`sorted(temperaturer, reverse=True)[:5]`). Det gir riktig svar her, men bare fordi det tilfeldigvis er nøyaktig fem plussgrader. Med andre målinger blir svaret feil. Koden skal løse *problemet*, ikke bare gi riktig svar for akkurat disse tallene.

### Oppgave 7: Dictionary

```python
poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
```

#### a)

**Løsning 1: med `.items()`**

```python
for navn, antall in poeng.items():
    print(f"{navn} har {antall} poeng.")
```

**Løsning 2: løkke over nøklene**

```python
for navn in poeng:
    print(f"{navn} har {poeng[navn]} poeng.")
```

Begge er riktige. En `for`-løkke direkte over en dictionary gir nøklene. `.items()` gir både nøkkel og verdi samtidig, så du slipper å slå opp `poeng[navn]`.

Ikke lag en egen liste med navnene (`["Ada", "Linus", ...]`) og iterer over den. Da må du endre koden hver gang en deltaker kommer til, og dictionaryen inneholder jo allerede navnene.

#### b)

Totalsummen er enkel med `sum(poeng.values())` og gir `167`. Det er flere måter å finne vinneren på.

**Løsning 1: løkke som husker den beste så langt**

```python
totalt = 0
vinner = ""
høyest = 0

for navn, antall in poeng.items():
    totalt += antall
    if antall > høyest:
        høyest = antall
        vinner = navn

print(f"Til sammen: {totalt} poeng.")
print(f"Vinneren er {vinner} med {høyest} poeng.")
```

Dette er et viktig mønster: Vi går gjennom alle, og hver gang vi finner noen som er bedre enn den beste vi har sett, oppdaterer vi. Fordelen er at vi gjør både totalsummen og vinneren i samme løkke.

(Tips: Hvis poengene kunne vært negative, burde `høyest` startet på det første elementet eller på `float("-inf")` i stedet for 0.)

**Løsning 2: `max()` med `key`**

```python
totalt = sum(poeng.values())
vinner = max(poeng, key=poeng.get)

print(f"Til sammen: {totalt} poeng. Vinneren er {vinner}.")
```

`max(poeng)` alene sammenligner **nøklene**, altså navnene, alfabetisk. Den gir `"Linus"`, fordi L kommer sist i alfabetet av navnene. Med `key=poeng.get` sier vi: «sammenlign hvert navn etter verdien det har i `poeng`». Da får vi `"Grace"`.

**Vanlige feil:**

- **`max(poeng.keys())`** gir navnet som kommer sist i alfabetet, ikke den med flest poeng.
- **Å skrive `"Grace vant"` rett inn i koden.** Programmet skal *finne* vinneren selv, slik at det fungerer også med andre poengsummer.

#### c)

**Løsning 1: sjekk med `in`**

```python
navn = input("Hvem vil du slå opp? ")

if navn in poeng:
    print(f"{navn} har {poeng[navn]} poeng.")
else:
    print(f"Fant ingen deltaker med navnet {navn}.")
```

**Løsning 2: `.get()`**

```python
navn = input("Hvem vil du slå opp? ")
resultat = poeng.get(navn)

if resultat is None:
    print(f"Fant ingen deltaker med navnet {navn}.")
else:
    print(f"{navn} har {resultat} poeng.")
```

`.get(nøkkel)` gir `None` i stedet for å krasje når nøkkelen ikke finnes. Bruk `is None` og ikke bare `if resultat:`. Ellers ville en deltaker med **0 poeng** blitt behandlet som om hun ikke fantes, fordi 0 regnes som «usann».

**Løsning 3: `try`/`except KeyError`**

```python
navn = input("Hvem vil du slå opp? ")

try:
    print(f"{navn} har {poeng[navn]} poeng.")
except KeyError:
    print(f"Fant ingen deltaker med navnet {navn}.")
```

`poeng[navn]` gir `KeyError` når navnet ikke finnes, og den fanger vi. Skriv `except KeyError` og ikke bare `except`, så du ikke skjuler andre feil.

**Ekstra: ikke skille mellom store og små bokstaver**

En av dere laget et søk som fungerer både med `ada` og `Ada`. Det er en god idé, men det må gjøres riktig. Hvis du bare gjør brukerens input om til små bokstaver, blir `"ada"` aldri funnet, fordi nøkkelen er `"Ada"`. Du må sammenligne små bokstaver med små bokstaver:

```python
søk = input("Hvem vil du slå opp? ").strip().lower()

funnet = False
for navn, antall in poeng.items():
    if navn.lower() == søk:
        print(f"{navn} har {antall} poeng.")
        funnet = True

if not funnet:
    print(f"Fant ingen deltaker med navnet {søk}.")
```

### Oppgave 8: Funksjoner

#### a)

```python
def konverter_tid(sekunder: int) -> tuple[int, int, int]:
    timer = sekunder // 3600
    minutter = sekunder % 3600 // 60
    rest = sekunder % 60
    return timer, minutter, rest


t, m, s = konverter_tid(4000)
print(f"{t} t, {m} min, {s} s")  # 1 t, 6 min, 40 s
```

**Utregningen:**

- Én time er `60 * 60 = 3600` sekunder. `4000 // 3600` er `1` time.
- `4000 % 3600` er `400` sekunder som er igjen etter de hele timene. `400 // 60` er `6` minutter.
- `4000 % 60` er `40` sekunder.

**Hvorfor `return` og ikke `print`?** Oppgaven ba om at funksjonen skulle **returnere** tre verdier. En funksjon som returnerer verdier, kan brukes til mye mer. Du kan skrive verdiene ut i et hvilket som helst format, regne videre med dem, eller sammenligne dem. En funksjon som bare skriver ut, kan bare skrive ut. Det samme gjelder å returnere en ferdig tekst (`return f"{timer} t, ..."`). Da kan du ikke regne med tallene etterpå.

En funksjon som bare skriver ut og ikke har `return`, returnerer `None`. Derfor gir `print(konverter_tid(4000))` en ekstra linje med `None` hvis funksjonen selv skriver ut.

**Pakke ut verdiene:** `return timer, minutter, rest` returnerer egentlig en *tuple* `(1, 6, 40)`. Med `t, m, s = konverter_tid(4000)` pakker vi den ut i tre variabler. Det går også an å skrive `tid = konverter_tid(4000)` og bruke `tid[0]`, `tid[1]` og `tid[2]`, men utpakking gir mer lesbare navn enn tall-indekser.

**Alternativ med `divmod`:** Python har en innebygd funksjon som gir både `//` og `%` på én gang:

```python
def konverter_tid(sekunder: int) -> tuple[int, int, int]:
    timer, rest = divmod(sekunder, 3600)
    minutter, sekunder = divmod(rest, 60)
    return timer, minutter, sekunder
```

#### b)

**Løsning 1: løkke med to «flagg»**

```python
def er_sterkt_passord(passord: str) -> bool:
    har_siffer = False
    har_stor_bokstav = False

    for tegn in passord:
        if tegn.isdigit():
            har_siffer = True
        if tegn.isupper():
            har_stor_bokstav = True

    return len(passord) >= 8 and har_siffer and har_stor_bokstav


print(er_sterkt_passord("hemmelig"))   # False: ingen siffer, ingen stor bokstav
print(er_sterkt_passord("Hemmelig"))   # False: ingen siffer
print(er_sterkt_passord("Hemmelig1"))  # True
```

**Slik fungerer den:**

- Vi starter med å anta at passordet *ikke* har siffer eller stor bokstav (`False`).
- Vi går gjennom passordet **tegn for tegn**. Finner vi et siffer eller en stor bokstav, setter vi det tilhørende flagget til `True`. Et flagg som har blitt `True`, blir aldri satt tilbake til `False`.
- Til slutt returnerer vi resultatet av hele uttrykket. `len(passord) >= 8 and har_siffer and har_stor_bokstav` er allerede `True` eller `False`, så vi trenger ingen `if` for å returnere det.

Det er også helt greit å skrive slutten slik, hvis du synes det er tydeligere:

```python
    if len(passord) >= 8 and har_siffer and har_stor_bokstav:
        return True
    else:
        return False
```

**Løsning 2: `any()`**

```python
def er_sterkt_passord(passord: str) -> bool:
    har_siffer = any(tegn.isdigit() for tegn in passord)
    har_stor_bokstav = any(tegn.isupper() for tegn in passord)
    return len(passord) >= 8 and har_siffer and har_stor_bokstav
```

`any(...)` er `True` hvis *minst ett* av elementene er sant. Det er en kortere måte å skrive løkka i løsning 1 på.

**Test grensene!** Oppgaven sa *minst* 8 tegn, altså `>= 8`. Test derfor med et passord på nøyaktig 8 tegn, for eksempel `"Hemmel1g"`, som skal gi `True`. En av dere testet akkurat dette og fikk `False`, fordi koden sjekket `> 8`. Det er et godt eksempel på at det ikke holder å teste. Du må også se på resultatet og spørre deg om det er det du forventet.

**Vanlige feil:**

- **`passord.isdigit()` på hele strengen** sjekker om *hele* passordet består av siffer, ikke om det *inneholder* et siffer. Du må sjekke hvert tegn for seg.
- **`len.passord`** er ikke gyldig Python. Det skal være `len(passord)`.
- **Funksjonen skriver ut «sterkt» eller «svakt» i stedet for å returnere `True`/`False`.**

---

## Del C: Kombinerte oppgaver

I Del C er det ikke ett riktig svar. Det viktigste er at du tar et bevisst valg og kan forklare det.

### Oppgave 9: Varebeholdning i en nettbutikk

#### a) Datastruktur

Dere valgte mange ulike strukturer. Her er de vanligste, med fordeler og ulemper.

**Alternativ 1: dictionary med varenummer som nøkkel, og en dictionary per vare**

```python
# Lageret er en dictionary der varenummeret er nøkkelen. Varenummeret er unikt,
# og det er det vi slår opp på når vi selger en vare. Da kan vi finne en vare
# direkte med lager["A100"], uten å lete gjennom alle varene.
# Hver vare er en ny dictionary, slik at feltene har navn ("pris", "antall")
# i stedet for tall-indekser. Det gjør koden lettere å lese.
lager = {
    "A100": {"navn": "Mekanisk tastatur", "pris": 899.0, "antall": 12, "kategori": "tastatur"},
    "A101": {"navn": "Trådløst tastatur", "pris": 499.0, "antall": 3, "kategori": "tastatur"},
    "B200": {"navn": "Gamingmus", "pris": 649.5, "antall": 0, "kategori": "mus"},
    "B201": {"navn": "Kontormus", "pris": 199.0, "antall": 25, "kategori": "mus"},
    "C300": {"navn": "27\" skjerm", "pris": 2999.0, "antall": 4, "kategori": "skjerm"},
}
```

Dette er trolig den mest praktiske løsningen for denne oppgaven, fordi `selg_vare` skal slå opp på varenummer. Legg merke til at varenummeret ikke trenger å stå inne i hver vare også, fordi det allerede er nøkkelen.

Bruk **samme nøkler** i alle varene. Skriver du `"Varenummer"` i én vare og `"varenummer"` i en annen, er det to forskjellige nøkler for Python.

**Alternativ 2: liste av dictionaries**

```python
# En liste av dictionaries, én per vare. En liste tar vare på rekkefølgen, og er
# lett å gå gjennom og sortere. Ulempen er at vi må lete gjennom hele lista for å
# finne en vare med et bestemt varenummer.
lager = [
    {"varenummer": "A100", "navn": "Mekanisk tastatur", "pris": 899.0, "antall": 12, "kategori": "tastatur"},
    {"varenummer": "A101", "navn": "Trådløst tastatur", "pris": 499.0, "antall": 3, "kategori": "tastatur"},
    {"varenummer": "B200", "navn": "Gamingmus", "pris": 649.5, "antall": 0, "kategori": "mus"},
    {"varenummer": "B201", "navn": "Kontormus", "pris": 199.0, "antall": 25, "kategori": "mus"},
    {"varenummer": "C300", "navn": "27\" skjerm", "pris": 2999.0, "antall": 4, "kategori": "skjerm"},
]
```

Også et godt valg. Her må varenummeret stå inne i hver vare. Husk **komma** mellom elementene i lista og mellom feltene i hver dictionary. Mangler ett komma, kjører ingenting.

**Andre varianter fra besvarelsene:**

- **Dictionary med kategori som nøkkel**, og en liste med varer i hver kategori (`{"tastatur": [...], "mus": [...]}`). Det gjør det enkelt å vise varer per kategori, men vanskeligere å finne en vare ut fra varenummer, fordi du må lete i alle kategoriene.
- **Klasser.** Fungerer fint, men er ikke noe vi har gått gjennom ennå. Strukturen ble da en dictionary med lister av objekter.
- **Liste av lister** (`["A100", "Tastatur", 899, 12, "tastatur"]`). Fungerer, men `vare[3]` sier mye mindre enn `vare["antall"]`.

**Om begrunnelsen:** En god begrunnelse forklarer hvorfor strukturen passer til *det programmet skal gjøre*. Hva skal du slå opp på? Må du sortere? Er det viktig med rekkefølge? «Jeg har brukt det før» eller en liste over hvilke felter som er med, er ikke en begrunnelse for valget.

Resten av løsningene bruker **alternativ 1**. Under hver deloppgave står det hvordan koden ville sett ut med alternativ 2.

#### b) `vis_lager`

```python
def vis_lager(lager: dict) -> None:
    print(f"{'Varenr':<8}{'Navn':<20}{'Kategori':<10}{'Pris':>10}{'Antall':>8}")
    print("-" * 56)
    for varenummer, vare in lager.items():
        print(f"{varenummer:<8}{vare['navn']:<20}{vare['kategori']:<10}"
              f"{vare['pris']:>10.2f}{vare['antall']:>8}")
```

Utskrift:

```
Varenr  Navn                Kategori        Pris  Antall
--------------------------------------------------------
A100    Mekanisk tastatur   tastatur      899.00      12
A101    Trådløst tastatur   tastatur      499.00       3
B200    Gamingmus           mus           649.50       0
B201    Kontormus           mus           199.00      25
C300    27" skjerm          skjerm       2999.00       4
```

**Formateringskoder i f-strenger:**

| Kode | Betyr |
|---|---|
| `:<20` | Venstrejuster i et felt som er 20 tegn bredt |
| `:>10` | Høyrejuster i et felt som er 10 tegn bredt (fint for tall) |
| `:.2f` | To desimaler |
| `:>10.2f` | Begge deler: høyrejustert, 10 tegn bredt, to desimaler |

Overskriftene bruker de **samme breddene** som radene, og derfor står kolonnene pent under hverandre.

**Vanlige feil:**

- **`round(pris, 2)`** gir ikke to desimaler: `round(100, 2)` er fortsatt `100`. For å *vise* to desimaler må du bruke formatering (`:.2f`).
- **Å hoppe over varer med 0 på lager.** Oppgaven sa *alle* varene, og det er nyttig å se hvilke som er utsolgt.
- **Å bruke en global variabel inne i funksjonen i stedet for parameteren `lager`.** Bruk alltid parameterne funksjonen får inn.

Med en liste av dictionaries (alternativ 2) blir løkka `for vare in lager:`, og varenummeret hentes med `vare['varenummer']`.

#### c) `selg_vare`

```python
def selg_vare(lager: dict, varenummer: str, antall: int) -> bool:
    if varenummer not in lager:
        print(f"Fant ingen vare med varenummer {varenummer}.")
        return False

    vare = lager[varenummer]

    if vare["antall"] < antall:
        print(f"Bare {vare['antall']} igjen av {vare['navn']}, kan ikke selge {antall}.")
        return False

    vare["antall"] -= antall
    å_betale = antall * vare["pris"]
    print(f"Solgt {antall} stk. {vare['navn']}. Å betale: {å_betale:.2f} kr")
    return True


selg_vare(lager, "A100", 2)    # går bra
selg_vare(lager, "X999", 1)    # ukjent varenummer
selg_vare(lager, "C300", 10)   # for få på lager
```

**Slik er den bygd opp:** Vi sjekker feilene **først**, og går ut av funksjonen med `return False` med en gang vi finner en. Hvis vi kommer forbi begge sjekkene, vet vi at alt er i orden, og kan gjennomføre salget. Dette kalles ofte *tidlig retur*, og gjør at vi slipper mange nivåer med `if`/`else` inni hverandre.

`vare = lager[varenummer]` gir oss en snarvei til varen. Når vi endrer `vare["antall"]`, endrer vi den samme dictionaryen som ligger i `lager`.

**Alternativ med `try`/`except KeyError`:**

```python
def selg_vare(lager: dict, varenummer: str, antall: int) -> bool:
    try:
        vare = lager[varenummer]
    except KeyError:
        print(f"Fant ingen vare med varenummer {varenummer}.")
        return False

    if vare["antall"] < antall:
        print(f"Bare {vare['antall']} igjen av {vare['navn']}.")
        return False

    vare["antall"] -= antall
    print(f"Å betale: {antall * vare['pris']:.2f} kr")
    return True
```

**Med en liste av dictionaries** må vi lete etter varen med en løkke:

```python
def selg_vare(lager: list, varenummer: str, antall: int) -> bool:
    for vare in lager:
        if vare["varenummer"] == varenummer:
            if vare["antall"] < antall:
                print(f"Bare {vare['antall']} igjen av {vare['navn']}.")
                return False
            vare["antall"] -= antall
            print(f"Å betale: {antall * vare['pris']:.2f} kr")
            return True

    # Hvis vi kommer hit, gikk løkka gjennom hele lista uten å finne varen.
    print(f"Fant ingen vare med varenummer {varenummer}.")
    return False
```

Legg merke til at «fant ikke varen» står **etter** løkka. Vi kan ikke vite at varen mangler før vi har sjekket alle.

**Vanlige feil:**

- **`vare["antall"] > antall`** i stedet for `>=`, eller `< antall` som i løsningen over. Med `>` kan du aldri selge de siste varene på lager: 4 på lager og 4 bestilt blir avvist. Test med akkurat så mange som er på lager.
- **Ingen `return False` på slutten av en av feilgrenene.** Da returnerer funksjonen `None`. Det ligner på `False`, men er ikke det samme.
- **Glemme å skrive ut hva kunden må betale.**
- **Bare ett testkall.** Oppgaven ba om tre kall, ett for hver situasjon. Det er nettopp slik du viser at alle grenene i funksjonen virker.

#### d) `lav_beholdning`

```python
def lav_beholdning(lager: dict, grense: int = 5) -> list[str]:
    lave = []
    for vare in lager.values():
        if vare["antall"] < grense:
            lave.append(vare)

    lave.sort(key=lambda vare: vare["antall"])

    navn = []
    for vare in lave:
        navn.append(vare["navn"])
    return navn


print(lav_beholdning(lager))
```

Etter salgene over gir dette `['Gamingmus', 'Trådløst tastatur', '27" skjerm']`.

**Slik fungerer den:**

1. **Filtrer:** Vi plukker ut varene som har færre enn `grense` på lager. `grense: int = 5` er en *standardparameter*. Kaller du funksjonen uten `grense`, blir den 5, men du kan også skrive `lav_beholdning(lager, 10)`.
2. **Sorter:** Vi må sortere etter **antall**, ikke etter navn. `key=lambda vare: vare["antall"]` betyr «sorter hver vare etter verdien i `vare["antall"]`». Vi sorterer *hele varene* og ikke bare navnene, fordi vi trenger antallet for å sortere.
3. **Hent navnene:** Til slutt lager vi en liste med bare navnene, og **returnerer** den.

Om `lambda`: `lambda vare: vare["antall"]` er en liten funksjon uten navn. Den betyr det samme som:

```python
def hent_antall(vare):
    return vare["antall"]

lave.sort(key=hent_antall)
```

**Alternativ uten `lambda`, med tupler:**

```python
def lav_beholdning(lager: dict, grense: int = 5) -> list[str]:
    lave = []
    for vare in lager.values():
        if vare["antall"] < grense:
            lave.append((vare["antall"], vare["navn"]))

    lave.sort()   # tupler sorteres etter første element først
    return [navn for antall, navn in lave]
```

Når Python sorterer tupler, sammenligner den det første elementet først. Ved å legge antallet først blir lista sortert etter antall. Er to antall like, sorteres de etter navnet.

**Vanlige feil:**

- **`sorted(navneliste)`** sorterer navnene alfabetisk, ikke etter antall på lager.
- **Ingen sortering**, eller sortering feil vei. Oppgaven sa at varen med *minst* på lager skal komme først, altså stigende.
- **`print` i stedet for `return`** inne i funksjonen.
- **Å skrive en egen sorteringsalgoritme.** Det er god trening, men det er lett å gjøre feil, og `sort`/`sorted` med `key` gjør jobben for deg.

#### Hele programmet

Her er hele løsningen samlet, så du kan kjøre den:

```python
lager = {
    "A100": {"navn": "Mekanisk tastatur", "pris": 899.0, "antall": 12, "kategori": "tastatur"},
    "A101": {"navn": "Trådløst tastatur", "pris": 499.0, "antall": 3, "kategori": "tastatur"},
    "B200": {"navn": "Gamingmus", "pris": 649.5, "antall": 0, "kategori": "mus"},
    "B201": {"navn": "Kontormus", "pris": 199.0, "antall": 25, "kategori": "mus"},
    "C300": {"navn": "27\" skjerm", "pris": 2999.0, "antall": 4, "kategori": "skjerm"},
}


def vis_lager(lager: dict) -> None:
    print(f"{'Varenr':<8}{'Navn':<20}{'Kategori':<10}{'Pris':>10}{'Antall':>8}")
    print("-" * 56)
    for varenummer, vare in lager.items():
        print(f"{varenummer:<8}{vare['navn']:<20}{vare['kategori']:<10}"
              f"{vare['pris']:>10.2f}{vare['antall']:>8}")


def selg_vare(lager: dict, varenummer: str, antall: int) -> bool:
    if varenummer not in lager:
        print(f"Fant ingen vare med varenummer {varenummer}.")
        return False

    vare = lager[varenummer]

    if vare["antall"] < antall:
        print(f"Bare {vare['antall']} igjen av {vare['navn']}, kan ikke selge {antall}.")
        return False

    vare["antall"] -= antall
    å_betale = antall * vare["pris"]
    print(f"Solgt {antall} stk. {vare['navn']}. Å betale: {å_betale:.2f} kr")
    return True


def lav_beholdning(lager: dict, grense: int = 5) -> list[str]:
    lave = []
    for vare in lager.values():
        if vare["antall"] < grense:
            lave.append(vare)

    lave.sort(key=lambda vare: vare["antall"])

    navn = []
    for vare in lave:
        navn.append(vare["navn"])
    return navn


vis_lager(lager)
print()
print(selg_vare(lager, "A100", 2))    # True
print(selg_vare(lager, "X999", 1))    # False, ukjent varenummer
print(selg_vare(lager, "C300", 10))   # False, for få på lager
print(selg_vare(lager, "C300", 4))    # True, akkurat så mange som er på lager
print()
print(lav_beholdning(lager))
```

### Oppgave 10: Treningslogg

Dette er den største oppgaven, og det lønner seg å dele den opp. Bygg og test én del om gangen: først menyen, så registrering, så visning, og så statistikk.

#### Valg av datastruktur

**Alternativ 1: liste av dictionaries**, én per økt:

```python
okter = [
    {"aktivitet": "løping", "minutter": 30},
    {"aktivitet": "sykling", "minutter": 45},
    {"aktivitet": "løping", "minutter": 20},
]
```

Rekkefølgen på øktene beholdes, og det passer godt til «Vis alle økter». Statistikk per aktivitet må regnes ut med en løkke.

**Alternativ 2: dictionary med aktivitet som nøkkel og en liste med minutter:**

```python
okter = {
    "løping": [30, 20],
    "sykling": [45],
}
```

Statistikken blir veldig enkel (`sum(okter["løping"])`), men vi mister rekkefølgen øktene ble registrert i. Visningen blir da gruppert per aktivitet.

**Alternativ 3: to parallelle lister**, én med aktiviteter og én med minutter. Det fungerer, men det er lett at listene kommer ut av takt. Én liste med dictionaries holder sammen det som hører sammen.

Løsningen under bruker **alternativ 1**.

#### Løsning

```python
# Øktene lagres som en liste av dictionaries. Da tas rekkefølgen vare på,
# og hver økt har navngitte felter ("aktivitet" og "minutter").


def les_aktivitet() -> str:
    """Spør til brukeren skriver en aktivitet som ikke er tom."""
    while True:
        aktivitet = input("Aktivitet: ").strip().lower()
        if aktivitet != "":
            return aktivitet
        print("Aktiviteten kan ikke være tom.")


def les_minutter() -> int:
    """Spør til brukeren skriver et heltall større enn 0."""
    while True:
        try:
            minutter = int(input("Antall minutter: "))
        except ValueError:
            print("Du må skrive inn et heltall.")
            continue

        if minutter > 0:
            return minutter
        print("Antall minutter må være større enn 0.")


def registrer_okt(okter: list[dict]) -> None:
    aktivitet = les_aktivitet()
    minutter = les_minutter()
    okter.append({"aktivitet": aktivitet, "minutter": minutter})
    print("Økta er registrert.")


def vis_okter(okter: list[dict]) -> None:
    if len(okter) == 0:
        print("Ingen økter registrert ennå.")
        return

    for nummer, okt in enumerate(okter, start=1):
        print(f"{nummer}. {okt['aktivitet']}: {okt['minutter']} min")


def vis_statistikk(okter: list[dict]) -> None:
    if len(okter) == 0:
        print("Ingen økter registrert ennå.")
        return

    # Summer minutter per aktivitet i en dictionary: {"løping": 50, "sykling": 45}
    per_aktivitet = {}
    for okt in okter:
        aktivitet = okt["aktivitet"]
        if aktivitet in per_aktivitet:
            per_aktivitet[aktivitet] += okt["minutter"]
        else:
            per_aktivitet[aktivitet] = okt["minutter"]

    print(f"Antall økter: {len(okter)}")
    print(f"Totalt: {sum(per_aktivitet.values())} min")
    print("Per aktivitet:")
    for aktivitet, minutter in per_aktivitet.items():
        print(f"  {aktivitet}: {minutter} min")

    mest_trent = max(per_aktivitet, key=per_aktivitet.get)
    print(f"Du har trent mest {mest_trent} ({per_aktivitet[mest_trent]} min).")


def main() -> None:
    okter = []

    while True:
        print("\n--- Treningslogg ---")
        print("1: Registrer økt")
        print("2: Vis alle økter")
        print("3: Statistikk")
        print("4: Avslutt")
        valg = input("Velg: ")

        if valg == "1":
            registrer_okt(okter)
        elif valg == "2":
            vis_okter(okter)
        elif valg == "3":
            vis_statistikk(okter)
        elif valg == "4":
            print("Ha det!")
            break
        else:
            print("Ugyldig valg. Skriv 1, 2, 3 eller 4.")


main()
```

#### Forklaring, del for del

**Menyløkka (`main`)**

- `while True` gjentar menyen til brukeren velger 4. Da går vi ut av løkka med `break`.
- Vi sammenligner med **tekst** (`"1"`, `"2"` …) i stedet for å bruke `int(input(...))`. Da kan programmet aldri krasje på menyvalget, selv om brukeren skriver `hei`. Det havner bare i `else`, som gir en feilmelding.
- Etter hvert valg **returnerer** funksjonen tilbake hit, og løkka viser menyen på nytt.

**Ikke kall menyen fra funksjonene!** Flere av dere lot funksjonene kalle `main()` eller `startmeny()` på slutten for å komme tilbake til menyen:

```python
def registrer():
    ...
    main()   # ikke gjør dette
```

Det ser ut til å virke, men hvert kall starter en **ny** meny *oppå* den gamle, i stedet for å gå tilbake. Etter en stund ligger det mange menyer stablet oppå hverandre. Da må du kanskje trykke 4 flere ganger for å avslutte, og etter svært mange valg krasjer programmet med `RecursionError`. Når en funksjon er ferdig, går Python automatisk tilbake dit funksjonen ble kalt fra, altså til løkka. Det er nettopp det vi vil.

**`match`/`case` i stedet for `if`/`elif`.** Det er like bra:

```python
        match valg:
            case "1":
                registrer_okt(okter)
            case "2":
                vis_okter(okter)
            case "3":
                vis_statistikk(okter)
            case "4":
                print("Ha det!")
                break
            case _:
                print("Ugyldig valg.")
```

**En dictionary med funksjoner.** En av dere laget en dictionary der hvert menyvalg peker på en funksjon. Det er en elegant løsning:

```python
handlinger = {
    "1": registrer_okt,
    "2": vis_okter,
    "3": vis_statistikk,
}

valg = input("Velg: ")
if valg == "4":
    ...
elif valg in handlinger:
    handlinger[valg](okter)   # henter funksjonen og kaller den
else:
    print("Ugyldig valg.")
```

Legg merke til at det står `registrer_okt` *uten* parenteser i dictionaryen. Da lagrer vi selve funksjonen, ikke resultatet av å kalle den.

**Registrering**

- Vi har laget to små hjelpefunksjoner, `les_aktivitet` og `les_minutter`. Hver av dem har én jobb: å spørre helt til svaret er gyldig, og så **returnere** det. Det gjør `registrer_okt` kort og lett å lese.
- `.strip()` fjerner mellomrom før og etter, så `"   "` regnes som tom. `.lower()` gjør `Løping` og `løping` like, og det er viktig for statistikken. Ellers blir de telt som to forskjellige aktiviteter.
- `les_minutter` følger nøyaktig samme mønster som oppgave 5: `try`/`except ValueError` for tekst, og en egen sjekk for at tallet er større enn 0.
- «Ugyldig input skal gi en feilmelding og et nytt forsøk.» Det betyr at vi spør på nytt **inne i registreringen**, ikke sender brukeren tilbake til menyen.

**Visning**

- Vi sjekker først om lista er tom. `return` i en funksjon uten returverdi betyr bare «gå ut av funksjonen nå».
- `enumerate(okter, start=1)` gir både et nummer og selve økta i hver runde, og nummereringen starter på 1. Uten `enumerate` kan du bruke en teller:

  ```python
  nummer = 1
  for okt in okter:
      print(f"{nummer}. {okt['aktivitet']}: {okt['minutter']} min")
      nummer += 1
  ```

**Statistikk**

- `per_aktivitet` er en dictionary som summerer minutter for hver aktivitet. Dette er et veldig nyttig mønster. Finnes nøkkelen fra før, legger vi til. Hvis ikke, lager vi den. Det kan skrives kortere med `.get()`:

  ```python
  per_aktivitet[aktivitet] = per_aktivitet.get(aktivitet, 0) + okt["minutter"]
  ```

  `.get(aktivitet, 0)` gir den nåværende summen, eller 0 hvis aktiviteten ikke finnes ennå.
- Totalt antall minutter er summen av alle verdiene.
- `max(per_aktivitet, key=per_aktivitet.get)` finner aktiviteten med flest minutter, på samme måte som vinneren i oppgave 7b.
- Skriv ut statistikken pent, linje for linje. Ikke skriv ut hele dictionaryen med `print(per_aktivitet)`.

**Hvorfor sender vi `okter` som parameter?**

Alle funksjonene får lista inn som parameter, i stedet for å bruke en global variabel. Da er det tydelig hvilke data hver funksjon jobber med, og funksjonene kan testes hver for seg:

```python
test = [{"aktivitet": "løping", "minutter": 30}, {"aktivitet": "yoga", "minutter": 60}]
vis_statistikk(test)
```

En løsning med en global liste og `global` i funksjonene fungerer også, men det blir fort uoversiktlig i større programmer.

**Vanlige feil:**

- **Valg 4 avslutter ikke**, fordi `while True` ikke har noen `break`.
- **`int(input("Velg: "))` uten `try`.** Da krasjer menyen hvis brukeren skriver en bokstav.
- **Ingen melding ved ugyldige menyvalg som `5`.**
- **Minutter lagres som tekst**, fordi `int()` mangler. Da kan du ikke summere dem.
- **Aktiviteten lagres ikke med små bokstaver.**
- **`>= 0` i stedet for `> 0`**, så en økt på 0 minutter godtas.
- **Ingen melding når det ikke er registrert noen økter.**

---

## Generelle råd

Disse rådene gjelder hele prøven, og er det som oftest kostet poeng:

1. **Les oppgaven nøye, og lag en sjekkliste.** Mange mistet poeng på detaljer som stod i oppgaveteksten: «minst 8 tegn», «67 år eller eldre», «to desimaler», «sortert slik at varen med minst på lager kommer først», «returnerer». Gå gjennom oppgaveteksten punkt for punkt til slutt, og kryss av.

2. **Test grenseverdiene.** Feilene skjuler seg nesten alltid ved grensene: 0, 1, 10 og 11 billetter, 30 og 67 år, et passord på nøyaktig 8 tegn, å selge akkurat så mange som er på lager. Test også med ugyldig input, som tekst, tomt svar og negative tall.

3. **Sjekk resultatet, ikke bare at koden kjører.** Når du tester, må du vite hva svaret *skal* være, og sammenligne. Kode som kjører uten feilmelding, kan fortsatt gi feil svar.

4. **Kjør koden ofte.** Skriv litt, kjør, skriv litt til, og kjør igjen. Da finner du syntaksfeil (som et manglende komma eller kolon) med en gang, mens du ennå husker hva du nettopp skrev. Venter du til slutt, kan én liten feil gjøre at ingenting kjører.

5. **`return` i stedet for `print` i funksjoner.** En funksjon som returnerer, kan brukes videre. En funksjon som bare skriver ut, kan bare skrive ut.

6. **La programmet regne ut svaret.** Ikke skriv inn svar som `"Grace vant"` eller `[:5]` fordi du vet hva svaret er. Koden skal virke også når dataene endres.

7. **Fordel tiden.** Del C gir flest poeng. Det kan lønne seg å skrive en enkel versjon av alle deloppgavene først, og så forbedre dem etterpå, i stedet for å gjøre én deloppgave perfekt og ikke rekke resten. Rekker du ikke å bli ferdig, skriv i en kommentar hva du hadde tenkt å gjøre. Det viser at du forstår oppgaven.
