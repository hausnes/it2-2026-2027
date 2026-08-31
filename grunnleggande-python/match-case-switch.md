# Switch i Python: match-case

## Introduksjon

Mange språk (Java, C, JavaScript m.fl.) har ei eiga `switch`-setning. Python hadde lenge berre `if`/`elif`/`else`, men frå og med Python 3.10 fekk me `match`/`case` — Python sin variant av switch. Han fungerer litt annleis (og er faktisk kraftigare) enn switch i andre språk, så her er ein rask gjennomgang med samanlikning mot if-else.

## Det enklaste eksempelet

Samanlikn desse to løysingane på same problem — skriv ut kva dag det er ut frå eit tal (1-7):

```python
# Med if-elif-else
dag = 3

if dag == 1:
    print("Måndag")
elif dag == 2:
    print("Tysdag")
elif dag == 3:
    print("Onsdag")
else:
    print("Ukjend dag")
```

```python
# Med match-case
dag = 3

match dag:
    case 1:
        print("Måndag")
    case 2:
        print("Tysdag")
    case 3:
        print("Onsdag")
    case _:
        print("Ukjend dag")
```

Legg merke til `case _:` heilt til slutt — dette er ein *wildcard* som fangar opp alt som ikkje matcha over, altså det same som `else`.

## Fleire verdiar i same case

I mange andre språk må du skrive fleire `case`-linjer etter kvarandre for å behandle dei likt (og hugse `break` for å ikkje "falle gjennom"). I Python kan du bruke `|` (eller-operatoren) for å slå saman fleire verdiar i éin case:

```python
# Med if-elif-else
maned = 7

if maned == 12 or maned == 1 or maned == 2:
    print("Vinter")
elif maned == 3 or maned == 4 or maned == 5:
    print("Vår")
elif maned == 6 or maned == 7 or maned == 8:
    print("Sommar")
else:
    print("Haust")
```

```python
# Med match-case
maned = 7

match maned:
    case 12 | 1 | 2:
        print("Vinter")
    case 3 | 4 | 5:
        print("Vår")
    case 6 | 7 | 8:
        print("Sommar")
    case _:
        print("Haust")
```

## Match-case fungerer på meir enn tal

Ein av dei store fordelane med `match` samanlikna med switch i andre språk, er at han fungerer fint på strengar òg:

```python
kommando = "start"

match kommando:
    case "start":
        print("Startar programmet...")
    case "stopp":
        print("Stoppar programmet...")
    case "pause":
        print("Set programmet på pause...")
    case _:
        print("Ukjend kommando")
```

## Guard-uttrykk: case med vilkår

Du kan leggje til eit ekstra vilkår på ein case med `if`. Dette kallast ein *guard*:

```python
alder = 17

match alder:
    case n if n < 0:
        print("Ugyldig alder")
    case n if n < 18:
        print("Du er mindreårig")
    case n if n < 67:
        print("Du er vaksen")
    case _:
        print("Du er pensjonist")
```

Her fangar `n` opp verdien til `alder`, slik at du kan bruke han i vilkåret. Merk at dette byrjar likne ganske mykje på ei vanleg if-elif-kjede — og då kan det ofte vere like greitt (eller greiare) å faktisk bruke if-else. `match` skin best når du matchar mot konkrete, kjende verdiar.

## Matching mot strukturar (litt meir avansert)

`match` kan også sjå på *forma* på data, ikkje berre enkeltverdiar. Dette kallast *pattern matching* og finst ikkje i tradisjonelle switch-setningar. Eit lite smakebit med tuples:

```python
punkt = (0, 5)

match punkt:
    case (0, 0):
        print("Origo")
    case (0, y):
        print(f"På y-aksen, y = {y}")
    case (x, 0):
        print(f"På x-aksen, x = {x}")
    case (x, y):
        print(f"Vanleg punkt: ({x}, {y})")
```

Her hentar `match` automatisk ut verdiane frå tuplet og lagrar dei i `x`/`y` dersom dei ikkje er faste tal som `0`. Dette er vanskeleg å skrive like ryddig med if-else.

## Oppsummering: switch vs. match-case

| Switch (Java/C/JS) | match-case (Python) |
|---|---|
| `switch (x) { case 1: ... break; }` | `match x: case 1: ...` |
| Må hugse `break`, elles "fall-through" | Ingen fall-through — berre éin case køyrer |
| Vanlegvis berre tal/strengar/enum | Tal, strengar, tuples, lister, objekt m.m. |
| `default:` | `case _:` |
| Ingen innebygd støtte for vilkår i case | Guard-uttrykk med `case x if ...:` |

## Når bør du bruke kva?

- **if-elif-else**: Når du har få, ulike vilkår, eller vilkår med samanlikningar (`<`, `>`, `and`, `or`) som ikkje handlar om å matche éin konkret verdi.
- **match-case**: Når du samanliknar éin variabel mot fleire konkrete, kjende verdiar (tal, strengar, kommandoar) — då blir koden ofte ryddigare å lese enn ei lang if-elif-kjede.

## Øvingsoppgåver

1. Lag eit program som ber brukaren om eit tal frå 1 til 12, og skriv ut namnet på den tilsvarande månaden med `match`. Bruk `case _:` for ugyldige tal.
2. Skriv om oppgåve 1 slik at fleire månadstal blir handsama i same case, og skriv i staden ut kva årstid månaden høyrer til (bruk `|`).
3. Lag eit enkelt "meny-program" som ber brukaren skrive inn ein kommando (`"hjelp"`, `"start"`, `"avslutt"`) og brukar `match` til å skrive ut ei tilbakemelding for kvar kommando.
4. Bruk ein guard (`case n if ...:`) til å lage eit program som tek imot ein poengsum (0-100) og skriv ut bokstavkarakter (A, B, C, D, E, F) ut frå intervall.
5. Skriv same løysing som i oppgåve 4, men med if-elif-else i staden. Samanlikn dei to løysingane — kva synest du er lettast å lese?

## Løysingsforslag

**Oppgåve 1**

```python
tal = int(input("Skriv inn eit tal frå 1 til 12: "))

match tal:
    case 1:
        print("Januar")
    case 2:
        print("Februar")
    case 3:
        print("Mars")
    case 4:
        print("April")
    case 5:
        print("Mai")
    case 6:
        print("Juni")
    case 7:
        print("Juli")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("Oktober")
    case 11:
        print("November")
    case 12:
        print("Desember")
    case _:
        print("Ugyldig tal")
```

**Oppgåve 2**

```python
tal = int(input("Skriv inn eit tal frå 1 til 12: "))

match tal:
    case 12 | 1 | 2:
        print("Vinter")
    case 3 | 4 | 5:
        print("Vår")
    case 6 | 7 | 8:
        print("Sommar")
    case 9 | 10 | 11:
        print("Haust")
    case _:
        print("Ugyldig tal")
```

**Oppgåve 3**

```python
kommando = input("Skriv inn ein kommando (hjelp/start/avslutt): ")

match kommando:
    case "hjelp":
        print("Tilgjengelege kommandoar: hjelp, start, avslutt")
    case "start":
        print("Programmet startar...")
    case "avslutt":
        print("Avsluttar programmet. Ha det!")
    case _:
        print("Ukjend kommando. Skriv 'hjelp' for oversikt.")
```

**Oppgåve 4**

```python
poeng = int(input("Skriv inn poengsum (0-100): "))

match poeng:
    case n if n >= 90:
        print("A")
    case n if n >= 80:
        print("B")
    case n if n >= 70:
        print("C")
    case n if n >= 60:
        print("D")
    case n if n >= 50:
        print("E")
    case _:
        print("F")
```

**Oppgåve 5**

```python
poeng = int(input("Skriv inn poengsum (0-100): "))

if poeng >= 90:
    print("A")
elif poeng >= 80:
    print("B")
elif poeng >= 70:
    print("C")
elif poeng >= 60:
    print("D")
elif poeng >= 50:
    print("E")
else:
    print("F")
```

Her ser du at når case-ane er bygd opp av `if`-vilkår (guards) i staden for konkrete verdiar, blir `match`-versjonen nesten identisk med if-elif-versjonen — berre med litt anna syntaks. Dette illustrerer poenget frå før: `match` gir størst gevinst når du matchar mot konkrete, kjende verdiar (som i oppgåve 1-3), ikkje når du uansett treng samanlikningar som `>=`.