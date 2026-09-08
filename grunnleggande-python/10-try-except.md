# Try/except i Python: feilhåndtering

## Introduksjon

Når Python møter noe den ikke klarer å utføre — som å gjøre om teksten `"hei"` til et heltall — stopper programmet og skriver ut en feilmelding (en *traceback*). Med `try`/`except` kan du fange opp slike feil (*unntak*, eller *exceptions*) selv, og la programmet fortsette i stedet for å krasje.

## Steg 1: Uten feilhåndtering

```python
tall = input("Skriv et tall: ")
tall = int(tall)
print(f"Du skrev inn {tall}.")
```

Skriver brukeren `"hei"` i stedet for et tall, kaster `int()` et `ValueError`, og programmet krasjer med en traceback. Det vil vi unngå.

## Steg 2: Den enkleste try/except

```python
tall = input("Skriv et tall: ")

try:
    tall = int(tall)
except ValueError:
    print("Du må skrive inn et heltall.")

print(f"Du skrev inn {tall}.")
```

Nå krasjer ikke programmet lenger. Men prøv å kjøre det med `"hei"` som input: det skriver ut `Du skrev inn hei.` — altså som om det gikk bra! Feilen ble fanget opp, men programmet gjorde aldri noe med at input faktisk var ugyldig. Vi trenger en måte å be brukeren prøve igjen.

## Steg 3: Gjenta til gyldig input

*(Eksempelet under er fra boka, kap. 1C, "validering av input")*

```python
gyldig = False

while not gyldig:
    tall = input("Skriv et tall: ")

    try:
        tall = int(tall)
        gyldig = True
    except ValueError:
        print("Du må skrive inn et heltall.")

print(f"Du skrev inn {tall}.")
```

Løkka fortsetter å spørre helt til `int(tall)` lykkes uten å kaste noe unntak, og først da settes `gyldig = True`.

## Steg 4: Skill feilhåndtering fra vanlig validering

Det er lett å tro at all validering hører hjemme i en `try`-blokk, men det stemmer ikke: `try`/`except` er for feil Python selv kaster (som `ValueError`), mens en betingelse som "tallet må være positivt" er noe *du* sjekker med en vanlig `if`. Bland du dem sammen i samme `try`, blir det fort vanskeligere å se hva som faktisk er feilhåndtering.

```python
gyldig = False

while not gyldig:
    tall = input("Skriv et positivt tall: ")

    try:
        tall = int(tall)
    except ValueError:
        print("Du må skrive inn et heltall.")
        continue

    if tall > 0:
        gyldig = True
    else:
        print("Tallet må være større enn 0.")

print(f"Du skrev inn {tall}.")
```

Her ligger `int(tall)` alene i `try`-blokka. `continue` sender løkka rett til neste runde hvis input ikke var et tall, slik at vi slipper å neste en `if` inni `try`-blokka.

## Steg 5 (litt videre­kommen): Fange en avbrytelse med Ctrl+C

`KeyboardInterrupt` er unntaket Python kaster når brukeren trykker Ctrl+C. Det kan du fange akkurat som `ValueError` — men da bør det ligge i en egen, ytre `try` rundt hele løkka, ikke blandes inn i valideringen:

```python
gyldig = False

try:
    while not gyldig:
        tall = input("Skriv et positivt tall: ")

        try:
            tall = int(tall)
        except ValueError:
            print("Du må skrive inn et heltall.")
            continue

        if tall > 0:
            gyldig = True
        else:
            print("Tallet må være større enn 0.")
except KeyboardInterrupt:
    print("\nProgrammet ble avbrutt av brukeren.")
else:
    print(f"Du skrev inn {tall}.")
```

Legg merke til `else` på den ytre `try`: den kjører bare hvis *ingen* unntak oppstod i `try`-blokka, altså bare hvis brukeren faktisk fullførte løkka uten å avbryte med Ctrl+C.

## Steg 6 (bonus): Flere feiltyper i samme program

Et program kan fint ha flere `except`-blokker for helt ulike feiltyper, så lenge de faktisk kan oppstå naturlig i samme kodeblokk. Her ber vi brukeren om en indeks i en liste — da kan to forskjellige ting gå galt: teksten er ikke et tall (`ValueError`), eller tallet er gyldig men ligger utenfor listas område (`IndexError`). Kombinert med den ytre Ctrl+C-fangsten fra steg 5 får vi tre ulike unntakstyper i ett og samme program:

```python
frukter = ["eple", "banan", "pære", "kiwi"]
gyldig = False

try:
    while not gyldig:
        indeks = input(f"Velg en frukt (0-{len(frukter) - 1}): ")

        try:
            indeks = int(indeks)
            valgt_frukt = frukter[indeks]
            gyldig = True
        except ValueError:
            print("Du må skrive inn et heltall.")
        except IndexError:
            print("Det finnes ingen frukt på den plassen.")
except KeyboardInterrupt:
    print("\nProgrammet ble avbrutt av brukeren.")
else:
    print(f"Du valgte {valgt_frukt}.")
```

Legg merke til at de to indre `except`-blokkene fanger feil som begge kommer fra samme linje (`frukter[int(indeks)]`), men av helt forskjellige grunner — det er derfor de fortjener hver sin feilmelding i stedet for én felles.

## Oppsummering

| Situasjon | Løsning |
|---|---|
| En operasjon kan kaste et unntak du vil håndtere (f.eks. `int()` på ugyldig tekst) | `try`/`except` |
| En verdi må bare oppfylle en betingelse (f.eks. være positiv) | vanlig `if` |
| Kode som kun skal kjøre hvis ingen feil oppstod | `try`/`except`/`else` |
| Kode som alltid skal kjøre, uansett resultat (opprydding) | `try`/`except`/`finally` |
| Flere ulike feiltyper som skal håndteres ulikt | flere `except`-blokker |

## Øvingsoppgåver

1. Lag et program som ber brukeren om et heltall, og bruk `try`/`except` til å håndtere ugyldig input helt til brukeren skriver noe gyldig.
2. Utvid programmet slik at tallet også må være mellom 1 og 100. Pass på at denne sjekken ikke ligger inni `try`-blokka.
3. Lag et program som ber brukeren om to tall og deler det første på det andre. Bruk to `except`-blokker: én som fanger `ValueError` (hvis brukeren ikke skriver tall) og én som fanger `ZeroDivisionError` (hvis brukeren deler på 0), med hver sin feilmelding.
4. Legg til en `finally`-blokk i oppgave 3 som alltid skriver ut `"Forsøk på divisjon avsluttet."`, uansett om det gikk bra eller ikke.
5. (Avansert) Bruk programmet fra oppgave 1 eller 2, og la det kunne avbrytes med Ctrl+C uten at det krasjer med en stygg feilmelding.

## Løysingsforslag

**Oppgåve 1**

```python
gyldig = False

while not gyldig:
    tall = input("Skriv et heltall: ")

    try:
        tall = int(tall)
        gyldig = True
    except ValueError:
        print("Du må skrive inn et heltall.")

print(f"Du skrev inn {tall}.")
```

**Oppgåve 2**

```python
gyldig = False

while not gyldig:
    tall = input("Skriv et heltall mellom 1 og 100: ")

    try:
        tall = int(tall)
    except ValueError:
        print("Du må skrive inn et heltall.")
        continue

    if 1 <= tall <= 100:
        gyldig = True
    else:
        print("Tallet må være mellom 1 og 100.")

print(f"Du skrev inn {tall}.")
```

**Oppgåve 3**

```python
try:
    tall1 = int(input("Skriv det første tallet: "))
    tall2 = int(input("Skriv det andre tallet: "))
    resultat = tall1 / tall2
except ValueError:
    print("Du må skrive inn tall.")
except ZeroDivisionError:
    print("Du kan ikke dele på 0.")
else:
    print(f"Resultat: {resultat}")
```

**Oppgåve 4**

```python
try:
    tall1 = int(input("Skriv det første tallet: "))
    tall2 = int(input("Skriv det andre tallet: "))
    resultat = tall1 / tall2
except ValueError:
    print("Du må skrive inn tall.")
except ZeroDivisionError:
    print("Du kan ikke dele på 0.")
else:
    print(f"Resultat: {resultat}")
finally:
    print("Forsøk på divisjon avsluttet.")
```

**Oppgåve 5**

```python
gyldig = False

try:
    while not gyldig:
        tall = input("Skriv et heltall mellom 1 og 100: ")

        try:
            tall = int(tall)
        except ValueError:
            print("Du må skrive inn et heltall.")
            continue

        if 1 <= tall <= 100:
            gyldig = True
        else:
            print("Tallet må være mellom 1 og 100.")
except KeyboardInterrupt:
    print("\nProgrammet ble avbrutt av brukeren.")
else:
    print(f"Du skrev inn {tall}.")
```
