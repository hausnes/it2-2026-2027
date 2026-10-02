# Vurdering: Grunnleggende Python

**Tid:** 2 timer · **Maks poeng:** 44

**Hjelpemidler:** Alle ressursene i mappa `grunnleggande-python` og lærebøkene, samt egen kode. Ikke KI.

## Praktisk informasjon

- Lag én `.py`-fil per oppgave, og kall den `oppgave1.py`, `oppgave2.py` og så videre. Oppgave 1–3 kan besvares med kommentarer i én og samme fil.
- Test koden din underveis. Kode som kjører gir flere poeng enn kode som ikke gjør det, men **delvis riktige løsninger gir også poeng**. Leverer du kode som ikke virker, skriv en kommentar om hva du prøvde å få til.
- Bruk gode variabelnavn og kommenter koden der det ikke er åpenbart hva den gjør. På de større oppgavene teller ryddig og lesbar kode med i vurderingen.
- Oppgavene blir gradvis vanskeligere. Del C kombinerer det meste vi har vært gjennom, og gir flest poeng. Det kan lønne seg å gjøre ferdig Del A og B først.

Forslag til tidsbruk: Del A ca. 15 min, Del B ca. 45 min, Del C ca. 60 min.

| Del | Innhold | Poeng |
|---|---|---|
| A | Lese og forstå kode | 9 |
| B | Oppgaver per tema | 17 |
| C | Kombinerte oppgaver | 18 |
| | **Totalt** | **44** |

## Kompetansemål

Prøven vurderer deg i disse kompetansemålene fra [læreplanen i informasjonsteknologi 2](https://www.udir.no/lk20/inf01-03/kompetansemaal-og-vurdering/kv978):

| Kompetansemål | Oppgaver |
|---|---|
| utforske og vurdere alternative løsninger for design og implementering av et program | 9, 10 |
| vurdere og bruke strategier for feilsøking og testing av programkode | 2, 5, 8b, 9c, 10 |
| generalisere løsninger ved å utvikle og bruke gjenbrukbar programkode | 3, 8, 9, 10 |

---

## Del A: Lese og forstå kode (9 poeng)

Oppgavene i denne delen skal løses **uten** å kjøre koden først. Skriv svarene dine som kommentarer. Du kan gjerne kjøre koden etterpå for å sjekke, men forklar i så fall hva du tenkte før du kjørte den.

### Oppgave 1 (4 poeng)

Hva skriver hver av kodesnuttene ut?

a)

```python
minutter = 135
print(f"{minutter // 60} t og {minutter % 60} min")
```

b)

```python
fag = "Programmering"
print(fag[0:4].upper() + fag[-3:])
```

c)

```python
tall = [3, 8, 1, 6]
tall.sort(reverse=True)
print(tall[1], len(tall))
```

d)

```python
total = 0
for i in range(1, 10, 3):
    total += i
print(total)
```

### Oppgave 2 (3 poeng)

Programmet under skal spørre brukeren om alder og fortelle om personen er myndig. Det inneholder **tre feil**. Finn feilene, forklar kort hva som er galt, og skriv en rettet versjon.

```python
alder = input("Hvor gammel er du? ")

if alder >= 18
    print("Du er myndig.")
elif alder = 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")
```

### Oppgave 3 (2 poeng)

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

a) Hva skriver programmet ut?

b) Forklar med egne ord hvorfor `tallene` ser ut som den gjør etter at funksjonen er kalt.

---

## Del B: Oppgaver per tema (17 poeng)

### Oppgave 4: Valgsetninger (3 poeng)

En kino har disse billettprisene:

| Hvem | Pris |
|---|---|
| Barn under 12 år | 80 kr |
| Honnør (67 år eller eldre) | 100 kr |
| Student (mellom 12 og 30 år, og har studentbevis) | 110 kr |
| Alle andre | 150 kr |

Lag et program som spør brukeren om alder og om de har studentbevis (`ja`/`nei`), og som skriver ut hva billetten koster. Er alderen under 0 eller over 120, skal programmet skrive ut en feilmelding i stedet for en pris.

Svaret på `ja`/`nei` skal fungere uansett om brukeren skriver med store eller små bokstaver.

### Oppgave 5: Løkker og feilhåndtering (3 poeng)

Lag et program som spør brukeren hvor mange billetter de vil kjøpe. Man kan kjøpe mellom 1 og 10 billetter.

- Skriver brukeren noe som ikke er et heltall (for eksempel `"to"`), skal programmet gi en feilmelding og spørre på nytt, uten å krasje.
- Skriver brukeren et tall utenfor 1–10, skal programmet også gi en (annen) feilmelding og spørre på nytt.
- Når brukeren har skrevet et gyldig antall, skal programmet skrive ut totalprisen, med 150 kr per billett.

Eksempel på kjøring:

```
Antall billetter: to
Du må skrive inn et heltall.
Antall billetter: 14
Du kan kjøpe mellom 1 og 10 billetter.
Antall billetter: 3
Totalpris: 450 kr
```

### Oppgave 6: Lister (4 poeng)

En værstasjon har målt temperaturen klokka 07 i ti dager:

```python
temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]
```

a) Skriv ut hvor mange målinger det er, og hva den første og den siste målingen var. Bruk indeksering. (1 poeng)

b) Regn ut og skriv ut gjennomsnittstemperaturen, avrundet til én desimal. (1 poeng)

c) Bruk en løkke til å telle hvor mange dager temperaturen var **under** 0 grader, og skriv ut svaret. (1 poeng)

d) Lag en **ny** liste som bare inneholder temperaturene som var **over** 0 grader, sortert fra varmest til kaldest. Skriv ut den nye lista. Den opprinnelige lista skal ikke endres. (1 poeng)

### Oppgave 7: Dictionary (3 poeng)

Her er poengsummene fra en quiz:

```python
poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
```

a) Bruk en `for`-løkke til å skrive ut hver deltaker på formen `Ada har 42 poeng.` (1 poeng)

b) Regn ut og skriv ut hvor mange poeng deltakerne har til sammen, og hvem som vant. (1 poeng)

c) Spør brukeren om et navn. Finnes navnet, skal programmet skrive ut poengsummen. Finnes det ikke, skal programmet skrive ut `Fant ingen deltaker med navnet ...` i stedet for å krasje. (1 poeng)

### Oppgave 8: Funksjoner (4 poeng)

a) Lag en funksjon `konverter_tid(sekunder)` som tar inn et antall sekunder og **returnerer** hvor mange timer, minutter og sekunder det tilsvarer (tre returverdier). Kall funksjonen med `4000`, og skriv ut resultatet på formen `1 t, 6 min, 40 s`. (2 poeng)

b) Lag en funksjon `er_sterkt_passord(passord)` som returnerer `True` hvis passordet oppfyller **alle** kravene under, og `False` ellers: (2 poeng)

- minst 8 tegn langt
- inneholder minst ett siffer
- inneholder minst én stor bokstav

Test funksjonen med disse tre passordene som viser at den fungerer: `"hemmelig"`, `"Hemmelig"` og `"Hemmelig1"`.

*Tips:* `tegn.isdigit()` gir `True` hvis `tegn` er et siffer, og `tegn.isupper()` gir `True` hvis `tegn` er en stor bokstav.

Bruk gjerne type hints på funksjonene dine.

---

## Del C: Kombinerte oppgaver (18 poeng)

I denne delen må du kombinere det du kan om lister, dictionaries, løkker, valgsetninger og funksjoner. Det er ikke nødvendigvis ett riktig svar, så tenk gjennom valgene du tar, og forklar dem med kommentarer.

### Oppgave 9: Varebeholdning i en nettbutikk (9 poeng)

Du skal lage et enkelt lagersystem for en liten nettbutikk som selger datautstyr. For hver vare må butikken holde styr på:

- et **varenummer** (unikt for hver vare, for eksempel `"A100"`)
- **navn**
- **pris**
- **antall på lager**
- **kategori** (for eksempel `"tastatur"`, `"mus"` eller `"skjerm"`)

a) Lag en passende datastruktur for lageret, og fyll den med minst fem varer. Noen av varene skal ha få (under 5) eller ingen på lager. Skriv en kommentar som forklarer **hvorfor** du valgte akkurat denne strukturen. (2 poeng)

b) Lag en funksjon `vis_lager(lager)` som skriver ut alle varene som en ryddig tabell, med prisen med to desimaler. Kolonnene skal stå pent under hverandre. (2 poeng)

c) Lag en funksjon `selg_vare(lager, varenummer, antall)` som: (3 poeng)

- skriver ut en feilmelding og returnerer `False` hvis varenummeret ikke finnes
- skriver ut en feilmelding og returnerer `False` hvis det ikke er nok varer på lager
- ellers trekker antallet fra lagerbeholdningen, skriver ut hva kunden må betale, og returnerer `True`

Vis at funksjonen fungerer ved å kalle den minst tre ganger: ett salg som går bra, ett med ukjent varenummer og ett der det er for få på lager.

d) Lag en funksjon `lav_beholdning(lager, grense=5)` som **returnerer** en liste med navnene på alle varer som har færre enn `grense` på lager, sortert slik at varen med minst på lager kommer først. Skriv ut resultatet. (2 poeng)

### Oppgave 10: Treningslogg (9 poeng)

Lag et program der brukeren kan føre en enkel treningslogg. Hver treningsøkt består av en **aktivitet** (for eksempel `"løping"`) og **antall minutter**.

Programmet skal vise en meny og fortsette å kjøre helt til brukeren velger å avslutte:

```
--- Treningslogg ---
1: Registrer økt
2: Vis alle økter
3: Statistikk
4: Avslutt
Velg: 
```

Krav:

- **Registrer økt:** Brukeren skriver inn aktivitet og antall minutter. Aktiviteten lagres med små bokstaver, og kan ikke være tom. Antall minutter må være et heltall større enn 0. Ugyldig input skal gi en feilmelding og et nytt forsøk, og programmet skal aldri krasje.
- **Vis alle økter:** Skriver ut øktene nummerert fra 1, for eksempel `1. løping: 30 min`. Er det ikke registrert noen økter ennå, skal programmet si fra om det.
- **Statistikk:** Skriver ut antall økter, totalt antall minutter, antall minutter **per aktivitet**, og hvilken aktivitet brukeren har trent mest (flest minutter).
- Et ugyldig menyvalg skal gi en feilmelding.
- Hvert menyvalg (1–3) skal løses i **sin egen funksjon**.

Du bestemmer selv hvordan øktene lagres, men velg en struktur som gjør statistikken enkel å regne ut.

Poengfordeling: menyløkke med avslutning (2), registrering med validering (3), visning (1), statistikk (2), fornuftig bruk av funksjoner (1).
