# Musikkspiller i Python – fra skript til klasser

I denne mappen finner du tre versjoner av det samme programmet: en enkel musikkspiller. Hver versjon bygger videre på den forrige. Poenget er ikke bare sluttresultatet, men **hvordan man kan tenke** når man går fra «kode som virker» til «kode som er organisert med objekter».

| Fil | Hva den viser |
|---|---|
| [v0-geekforgeeks.py](v0-geekforgeeks.py) | Få lyd til å spille i det hele tatt |
| [v1.py](v1.py) | Første versjon med klassene `Song` og `Player` |
| [v2.py](v2.py) | Flere låter, en meny og en spiller som husker om den er på pause |

**Før du starter:** Programmet bruker biblioteket `pygame-ce`. Installer det med

```bash
pip install pygame-ce
```

Kjør programmene fra *denne* mappen, ellers finner ikke Python lydfilene i `lyd/`.

---

## Steg 0: Få det til å virke først

> *Tankegang: Ikke tenk på klasser ennå. Finn ut om ideen i det hele tatt er mulig.*

Når man skal lage noe nytt, er det lurt å starte med å finne et lite eksempel som virker. [v0-geekforgeeks.py](v0-geekforgeeks.py) er hentet fra [GeeksforGeeks](https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/) og gjør bare fire ting:

```python
from pygame import mixer

mixer.init()                                     # 1. Start lydsystemet
mixer.music.load("lyd/horror-hit-logo-142395.mp3")  # 2. Last inn en fil
mixer.music.set_volume(0.7)                      # 3. Sett volumet
mixer.music.play()                               # 4. Spill av

while mixer.music.get_busy():                    # Vent til låten er ferdig
    pass
```

To ting er verdt å legge merke til:

- **`while ... pass`-løkka** er nødvendig fordi `play()` ikke venter. Den starter lyden og går videre med en gang. Uten løkka ville programmet avsluttet, og lyden ville stoppet før du rakk å høre den.
- **Koden som er kommentert ut** nederst viser at man kan pause og fortsette avspillingen. Den tar vi med oss videre.

Nå vet vi at pygame kan spille lyd, og vi vet hvilke funksjoner som finnes: `load`, `play`, `pause`, `unpause`, `stop` og `get_busy`.

---

## Steg 1: Finn «tingene» i programmet → klasser

> *Tankegang: Hvilke ting finnes i programmet mitt? Hva vet hver ting, og hva kan den gjøre?*

Et godt triks for å finne klasser er å beskrive programmet med vanlige ord og se etter **substantiver**:

> «En **spiller** skal kunne laste inn en **låt** og spille den av, pause den og stoppe den.»

Det gir oss to klasser:

| Klasse | Hva den *vet* (attributter) | Hva den *kan gjøre* (metoder) |
|---|---|---|
| `Song` | tittel, filnavn | gi fra seg tittelen og filnavnet |
| `Player` | hvilken låt som er lastet inn | laste inn, spille, pause, stoppe, si om den spiller |

Klassen `Song` i [v1.py](v1.py) er nesten bare en «beholder» for data:

```python
class Song:
    def __init__(self, title, filename):
        self.title = title
        self.filename = filename
```

`Player` er den som *gjør* noe. Legg merke til at den bare pakker inn pygame-kallene fra steg 0 i metoder med gode navn:

```python
class Player:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = None

    def load_song(self, song):
        self.current_song = song
        pygame.mixer.music.load(song.get_filename())

    def play(self):
        pygame.mixer.music.play()
```

### Hvorfor er dette bedre?

Programmet gjør akkurat det samme som før, men nederst i fila leser koden nesten som vanlig tekst:

```python
player.load_song(song1)
player.play()
```

Den som bruker `Player`, trenger ikke å vite noe om `pygame.mixer.music`. Det er **innkapsling**: detaljene er gjemt inne i klassen. Hvis vi en dag bytter fra pygame til et annet lydbibliotek, er det bare innsiden av `Player` som må endres.

Legg også merke til at `load_song` tar imot et helt `Song`-*objekt*, ikke bare et filnavn. Spilleren spør selv låten om filnavnet med `song.get_filename()`. Objekter kan altså samarbeide ved å sende hverandre rundt.

---

## Steg 2: Mange låter, en meny, og en spiller som husker

> *Tankegang: Hva mangler for at dette skal bli et ordentlig program? Hvor hører hver ny ting hjemme?*

I [v2.py](v2.py) gjør vi tre forbedringer.

### 2a) En liste med objekter

I stedet for `song1`, `song2`, `song3` … legger vi alle låtene i en liste:

```python
tracks = []
tracks.append(Track("Horror hit", "lyd/horror-hit-logo-142395.mp3"))
tracks.append(Track("Sunflower Street Drumloop", "lyd/sunflower-street-drumloop-85bpm-163900.mp3"))
```

Nå kan vi bruke en `for`-løkke for å vise alle låtene, og brukeren kan velge en låt med et nummer. (Klassen har også fått nytt navn, fra `Song` til `Track`, fordi ikke alle lydfilene er sanger.)

### 2b) Objektet husker sin egen tilstand

I v1 kunne vi pause, men ikke fortsette. I v2 vil vi at **samme knapp** skal både pause og fortsette. Da må spilleren *huske* om den er på pause. Det gjør vi med et nytt attributt:

```python
def __init__(self):
    pygame.mixer.init()
    self.current_track = None
    self.paused = False          # Ny: spilleren husker om den er på pause

def pause(self):
    if self.paused:
        self.paused = False
        pygame.mixer.music.unpause()
    else:
        self.paused = True
        pygame.mixer.music.pause()
```

Dette er en av de viktigste ideene i OOP: **et objekt har tilstand**, altså verdier som huskes mellom metodekall. Resten av programmet trenger ikke å holde styr på om musikken er på pause. Det er spillerens jobb.

Pass på å holde tilstanden riktig. Når vi trykker *spill* eller *stopp*, er vi ikke lenger på pause, så `play()` og `stop()` setter `self.paused = False`. Ellers kunne spilleren tro at den fortsatt var på pause neste gang.

### 2c) Objektet beskytter seg selv

Hva skjer hvis brukeren trykker *spill* før en låt er valgt? Da krasjer pygame. I stedet sjekker `Player` dette selv:

```python
def play(self):
    if self.current_track is None:
        print("Du må velje ei lydfil først.")
        return
    self.paused = False
    pygame.mixer.music.play()
```

Det er bedre at klassen passer på at den brukes riktig enn at alle som bruker den må huske det.

### 2d) Hva hører hjemme i klassen, og hva gjør ikke det?

Menyen (`show_menu`) er en vanlig funksjon *utenfor* klassen. Hvorfor? Spør deg selv: *Er det å vise en meny noe en musikkspiller gjør?* Egentlig ikke. Spilleren spiller musikk. Menyen hører til **brukergrensesnittet**, altså den delen av programmet som snakker med brukeren (`print` og `input`).

En god tommelfingerregel:

- **Klassen** (`Player`) vet *hvordan* musikk spilles.
- **Hovedprogrammet** (menyen og `while`-løkka) bestemmer *når* og *hva* som skal spilles, basert på hva brukeren vil.

Da kan du gjenbruke `Player` i et helt annet program, for eksempel et spill med grafikk, uten å ta med en tekstmeny du ikke trenger.

---

## Oppsummering: hvordan tenke

1. **Få det til å virke** i et lite skript først (steg 0).
2. **Finn substantivene**, altså tingene i programmet, og gjør dem til klasser (steg 1).
3. **Bestem hva hver klasse vet og kan gjøre**: attributter og metoder.
4. **Gjem detaljene** inne i klassene, slik at resten av koden blir lett å lese.
5. **La objektene huske sin egen tilstand** i stedet for at hovedprogrammet holder styr på alt (steg 2).
6. **Spør hvor ny kode hører hjemme**: i klassen, eller i brukergrensesnittet?

---

## Oppgaver: bygg videre

Prøv å lage din egen `v3.py`. Forslag, omtrent fra lettest til vanskeligst:

1. Legg til et menyvalg for å endre **volumet** (`pygame.mixer.music.set_volume(...)` tar et tall mellom 0.0 og 1.0). Hvilken klasse skal få den nye metoden?
2. La `Track` få et nytt attributt, for eksempel `artist` eller `sjanger`, og vis det i menyen.
3. Programmet krasjer hvis brukeren skriver bokstaver i stedet for et tall, eller et nummer som ikke finnes i lista. Bruk `try`/`except` eller en `if`-test for å hindre dette.
4. Legg til **«neste låt»** og **«forrige låt»**. Tips: spilleren må huske *nummeret* på låten som spilles nå.
5. Lag en klasse `Playlist` som har en liste med `Track`-objekter og metoder som `add_track()` og `get_track(nr)`. Hva blir lettere i hovedprogrammet da?

**Løsningsforslag:** Når du har prøvd selv og diskutert med noen, kan du sammenligne med [losningsforslag.md](losningsforslag.md).
