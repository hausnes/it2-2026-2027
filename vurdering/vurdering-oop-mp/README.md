# Vurdering: Eget OOP-prosjekt med fagsamtale

**Fagsamtale:** fredag 20. november, ca. 30 minutter · **Arbeidstid:** 12 skoletimer + hjemmearbeid

Prosjektet (koden) skal leveres inn i forkant av samtalen, i løpet av timene vi har dagen før.

I dette prosjektet skal du lage ditt eget program i Python ved hjelp av **objektorientert programmering (OOP)**. Du velger selv hva programmet skal handle om. Prosjektet avsluttes med en **fagsamtale** med læreren. Der viser du frem programmet, forklarer hvordan det fungerer og gjør endringer i koden mens læreren ser på.

Det viktigste er ikke at programmet er veldig stort eller avansert, men at du **forstår all koden** og kan bruke den til å vise hva du kan om programmering.

## Kompetansemål

Prosjektet vurderer deg i disse kompetansemålene fra [læreplanen i informasjonsteknologi 2](https://www.udir.no/lk20/inf01-03/kompetansemaal-og-vurdering/kv978):

| Kompetansemål | Hva det betyr i dette prosjektet |
|---|---|
| utvikle objektorienterte programmer med klasser, objekter, metoder og arv | Programmet ditt er bygget opp av egne klasser, der objektene har attributter og metoder, og minst én klasse arver fra en annen. |
| anvende objektorientert modellering til å beskrive et programs struktur | Du lager et klassediagram som viser klassene i programmet og hvordan de henger sammen. |
| utforske og vurdere alternative løsninger for design og implementering av et program | Du kan forklare hvorfor du har delt programmet inn i akkurat disse klassene, og hva du kunne ha gjort annerledes. |
| vurdere og bruke strategier for feilsøking og testing av programkode | Du tester programmet underveis, håndterer feil fra brukeren og kan finne og rette feil i koden. |
| generalisere løsninger ved å utvikle og bruke gjenbrukbar programkode | Du bruker klasser, metoder og arv slik at du slipper å skrive den samme koden flere ganger. |

---

## Oppgaven

Lag et program i Python som bruker OOP. Programmet skal kjøres i terminalen, men du kan gjerne bruke biblioteker som `rich.pixels`, `pygame-ce` eller lignende hvis du vil. NB: PyGame er et eget tema etter jul, så vent gjerne med det.

### Krav til programmet

Programmet ditt skal ha:

1. **Minst tre egne klasser**, der hver klasse har attributter og metoder som hører naturlig til den.
2. **Arv:** Minst én klasse skal arve fra en annen klasse og bruke `super()`. Subklassen skal enten legge til noe nytt eller overstyre minst én metode.
3. **Objekter som samarbeider:** Objektene skal bruke eller endre hverandre. For eksempel kan en spiller angripe en fiende, eller en bank kan ha mange kontoer.
4. **Mange objekter samlet** i en liste eller en dictionary, som programmet går gjennom med en løkke.
5. **Brukerinput**, for eksempel en meny der brukeren velger hva som skal skje.
6. **Feilhåndtering:** Programmet skal ikke krasje hvis brukeren skriver noe ugyldig.
7. **Lesbar kode:** gode navn på klasser, metoder og variabler, og kommentarer der det ikke er åpenbart hva koden gjør.

I tillegg skal du lage:

8. **Et klassediagram** som viser klassene dine med attributter og metoder, og hvilke klasser som arver fra hverandre. Du kan tegne det på papir, i et tegneprogram eller i en `README.md`. Se [eksempelet under](#eksempel-på-klassediagram).
9. **En README.md** i prosjektmappa di som 
   - forklarer hva programmet gjør og hvordan det kjøres 
   - hvilke kilder du har brukt (nettsider, eksempelkode og lignende)
   - hvordan du har brukt KI (se [Bruk av KI](#bruk-av-ki))
   - en kort oppsummering av hva du har gjort, når (logg)

### Bruk av KI

Du kan bruke KI-verktøy som ChatGPT, Copilot eller Claude i prosjektet, men du må være åpen om hvordan du har brukt dem. Skriv i README.md:

- hvilke KI-verktøy du har brukt
- hva du har brukt dem til, for eksempel til å få idéer, til å få forklart en feilmelding eller til å skrive kode
- hvilke deler av koden som er skrevet eller endret med hjelp fra KI.

Det er lov å få hjelp, men du må fortsatt forstå, forklare og endre **all** koden selv under fagsamtalen. Bruk KI som en lærer du kan spørre, ikke som noen som gjør jobben for deg. Spør gjerne KI om å *forklare* koden, ikke bare om å skrive den.

### Ideer til prosjekter

Det er helt fint å lage noe som ligner på det vi har jobbet med i timene, men da må du bygge det videre med dine egne ideer. Har du ikke noe annet du har lyst til å lage, kan du for eksempel velge et av disse:

- **Rollespill / dungeon crawler:** en spiller som går gjennom rom og kjemper mot ulike fiender. Se [dungeon_crawler_rpg](../../oop/dungeon_crawler_rpg/).
- **Kjæledyrspill:** flere typer dyr med ulike behov, som du må ta vare på. Se [kjaeledyr](../../oop/kjaeledyr/).
- **Bank:** kunder med ulike typer kontoer, renter og transaksjoner. Se [bank](../../oop/bank/oop/).
- **Musikkspiller:** låter, spillelister og en spiller med meny. Se [terminal-musikkspelar](../../oop/terminal-musikkspelar/).
- **Quizspill:** ulike typer spørsmål (flervalg, sant/usant, tall) og spillere med poeng.
- **Nettbutikk eller lager:** varer i ulike kategorier, handlekurv og kvittering.
- **Bibliotek:** bøker, filmer og spill som kan lånes ut og leveres tilbake av ulike lånere.

Hvis du har en egen idé, snakk med læreren i løpet av den første perioden. Da kan læreren hjelpe deg å finne ut om idéen er passe stor.

### Forslag til plan for de 12 timene

| Timer | Hva du bør gjøre |
|---|---|
| 1–2 | Velg idé. Lag en første versjon av klassediagrammet: hvilke klasser trenger du, og hva skal de inneholde? Opprett også README.md og begynn å dokumentere arbeidet der. |
| 3–6 | Lag klassene én om gangen. Test hver klasse før du går videre til neste. |
| 7–9 | Få objektene til å samarbeide, og lag menyen og resten av programmet. |
| 10–11 | Legg til feilhåndtering, test med feil input og rydd i koden. Oppdater klassediagrammet. |
| 12 | Ferdigstill README.md, og øv på å forklare koden din. |

**Tips:** Lag en liten versjon som virker først, og bygg videre derfra. Et lite program som virker og som du forstår, er bedre enn et stort program som ikke virker.

### Eksempel på klassediagram

Et klassediagram er en tegning av klassene i programmet ditt. Det viser hva hver klasse inneholder, og hvordan klassene henger sammen. Hver klasse tegnes som en boks med tre deler:

1. **Øverst:** navnet på klassen
2. **I midten:** attributtene (det objektet *har*)
3. **Nederst:** metodene (det objektet *kan gjøre*)

En pil fra én klasse til en annen betyr **arv**. Pila peker *mot* klassen det arves fra (superklassen).

Slik kan et enkelt klassediagram for et rollespill se ut. Her arver `Player` og `Skeleton` fra `Character`, og de får derfor også `name`, `hp` og metodene til `Character`. I boksene til subklassene skriver du bare det som er **nytt** eller **overstyrt**.

```
        ┌──────────────────────┐
        │      Character       │
        ├──────────────────────┤
        │ name                 │
        │ hp                   │
        ├──────────────────────┤
        │ is_alive()           │
        │ attack()             │
        │ take_damage(damage)  │
        └──────────────────────┘
               ▲          ▲
               │          │
┌──────────────┴───┐  ┌───┴──────────────┐
│      Player      │  │     Skeleton     │
├──────────────────┤  ├──────────────────┤
│ strength         │  │ bones            │
│ inventory        │  │                  │
├──────────────────┤  ├──────────────────┤
│ attack()         │  │ attack()         │
│ use_item(item)   │  │                  │
└──────────────────┘  └──────────────────┘
```

Det viktigste er at diagrammet **stemmer med koden din**, og at du kan bruke det til å forklare hvordan programmet er bygget opp. Lag gjerne diagrammet *før* du begynner å kode, og oppdater det underveis.

---

## Fagsamtalen

Fagsamtalen varer i ca. 30 minutter. Ta med prosjektet på din egen PC, og sjekk at programmet kjører før samtalen starter. Fagsamtalen har tre deler:

1. **Vis frem programmet.** Kjør programmet og vis hva det kan gjøre.
2. **Forklar koden.** Gå gjennom klassediagrammet og koden. Forklar hvordan programmet er bygget opp, og hvorfor du har valgt å gjøre det slik.
3. **Gjør endringer.** Læreren ber deg om å endre noe eller legge til ny funksjonalitet mens læreren ser på. Det kan for eksempel være å
   - legge til et nytt attributt eller en ny metode i en klasse
   - lage en ny subklasse som arver fra en av klassene dine
   - endre hvordan en metode virker
   - finne og rette en feil
   - få programmet til å tåle en ny type ugyldig input.

Du må kunne forklare **all** koden i prosjektet ditt, også kode du har fått hjelp til av KI eller hentet fra nettet eller fra eksemplene i timene. Under samtalen kan læreren også spørre hvordan du har brukt KI.

### Begreper du skal kunne

Du skal kunne forklare disse begrepene og vise hvor de brukes i ditt eget program:

| OOP | Generell programmering |
|---|---|
| klasse og objekt (instans) | variabel og datatype |
| attributt | liste og dictionary |
| metode | løkke (`for` og `while`) |
| `__init__` (konstruktør) | valgsetning (`if`, `elif`, `else`) |
| `self` | funksjon, parameter, argument og returverdi |
| `__str__` | feilhåndtering (`try` og `except`) |
| arv, subklasse og superklasse | feilsøking og testing |
| `super()` | gjenbrukbar kode |
| å overstyre en metode | |
| innkapsling | |
| klassediagram | |

---

## Vurderingskriterier for høy måloppnåelse

For høy måloppnåelse viser du at du

**Utvikler objektorienterte programmer**
- har laget et program som virker og som oppfyller alle kravene til programmet
- har klasser der attributtene og metodene hører naturlig sammen, og der hver klasse har sin egen tydelige oppgave
- bruker arv på en måte som gir mening, med `super()` og minst én metode som er overstyrt
- har objekter som samarbeider, for eksempel ved at metoder tar imot andre objekter som argumenter
- kan forklare presist og med riktige begreper hvordan klasser, objekter, metoder og arv virker i ditt eget program

**Modellerer programmets struktur**
- har laget et klassediagram som stemmer med koden, og som viser attributter, metoder og arv
- kan bruke klassediagrammet til å forklare hvordan programmet henger sammen

**Vurderer alternative løsninger**
- kan begrunne hvorfor programmet er delt inn i akkurat disse klassene og metodene
- kan beskrive minst én annen måte programmet kunne vært laget på, og si noe om fordeler og ulemper ved den

**Feilsøker og tester**
- har et program som tåler ugyldig input uten å krasje
- kan forklare hvordan du har testet programmet underveis
- finner og retter feil i koden din på en strukturert måte, for eksempel ved å lese feilmeldingen, bruke `print()` eller debuggeren

**Lager gjenbrukbar kode**
- har kode uten unødvendig gjentakelse, fordi du bruker klasser, metoder, løkker og arv
- kan selvstendig gjøre endringer og legge til ny funksjonalitet under fagsamtalen, fordi koden er bygget slik at den er lett å utvide
- skriver lesbar kode med gode navn og nyttige kommentarer
