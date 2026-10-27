# Løsningsforslag: bygg videre på musikkspilleren

Dette er løsningsforslag til oppgavene i [README.md](README.md#oppgaver-bygg-videre). Hver oppgave har sin egen fil, og hver fil bygger på den forrige. Det er derfor lurt å sammenligne en fil med den forrige for å se nøyaktig hva som er endret. I VS Code kan du markere to filer i utforskeren, høyreklikke og velge *Compare Selected*.

| Oppgave | Fil | Bygger på |
|---|---|---|
| 1. Volum | [v3-1-volum.py](v3-1-volum.py) | [v2.py](v2.py) |
| 2. Sjanger | [v3-2-sjanger.py](v3-2-sjanger.py) | v3-1 |
| 3. Sikker input | [v3-3-sikker-input.py](v3-3-sikker-input.py) | v3-2 |
| 4. Neste/forrige | [v3-4-neste-forrige.py](v3-4-neste-forrige.py) | v3-3 |
| 5. Playlist | [v3-5-playlist.py](v3-5-playlist.py) | v3-4 |

Husk å kjøre filene fra denne mappen, slik at Python finner lydfilene i `lyd/`.

Dette er *forslag*. Det finnes mange gode løsninger, og din kan godt se annerledes ut.

---

## Oppgave 1: Endre volumet

**Hvilken klasse skal få den nye metoden?** `Player`. Det er spilleren som styrer avspillingen, og volum er en del av det. `Track` er bare en låt og vet ingenting om hvor høyt den spilles.

```python
def __init__(self):
    ...
    self.volume = 100       # Volum i prosent (0-100)

def set_volume(self, volume):
    """Sets the volume. volume is a number from 0 to 100."""
    if volume < 0 or volume > 100:
        print("Volumet må vere mellom 0 og 100.")
        return
    self.volume = volume
    pygame.mixer.music.set_volume(volume / 100)

def get_volume(self):
    return self.volume
```

Ting å legge merke til:

- **Brukeren skriver prosent (0–100), men pygame vil ha et tall mellom 0.0 og 1.0.** Omregningen skjer *inne i* klassen. Den som bruker `Player`, trenger ikke å vite hva pygame vil ha. Det er innkapsling igjen.
- **Spilleren husker volumet selv** (`self.volume`). Da kan hovedprogrammet vise det i statuslinja med `player.get_volume()`.
- **`set_volume` sjekker selv at tallet er gyldig**, på samme måte som `play()` sjekker at en låt er valgt.
- Fordi menyvalg 5 nå brukes til volum, har *Avslutt* fått nummer **0**. Da kan vi legge til flere valg senere uten å flytte på Avslutt. Derfor starter løkka med `val = -1` og går så lenge `val != 0`.

Volumet beholdes når man bytter låt. Det er derfor nok å sette det én gang.

---

## Oppgave 2: Nytt attributt i `Track`

Vi har valgt **sjanger** (`genre`). Et nytt attributt krever tre endringer:

1. En ny parameter i `__init__`, som lagres i `self`:
   ```python
   def __init__(self, title, filename, genre):
       self.title = title
       self.filename = filename
       self.genre = genre
   ```
2. En get-metode:
   ```python
   def get_genre(self):
       return self.genre
   ```
3. Alle stedene der vi lager en `Track`, må sende med det nye argumentet:
   ```python
   Track("Horror hit", "lyd/horror-hit-logo-142395.mp3", "Skrekk")
   ```

Så kan vi vise sjangeren i menyen:

```python
print(f"{i}: {track.get_title()} ({track.get_genre()})")
```

Legg merke til at `Player` ikke trengte noen endringer i det hele tatt. Spilleren bryr seg bare om filnavnet. Når hver klasse har sin egen tydelige jobb, blir endringer *lokale*: du endrer bare der det trengs.

---

## Oppgave 3: Ikke krasj ved ugyldig input

Det er tre steder brukeren skriver et tall: menyvalget, låtnummeret og volumet. I stedet for å skrive den samme sjekken tre ganger, lager vi **én funksjon** som alle tre stedene bruker:

```python
def ask_number(question, lowest, highest):
    '''Asks for a whole number between lowest and highest. Keeps asking until the answer is valid.'''
    while True:
        try:
            number = int(input(question))
            if number >= lowest and number <= highest:
                return number
            print(f"Talet må vere mellom {lowest} og {highest}.")
        except ValueError:
            print("Du må skrive eit heilt tal.")
```

Slik virker den:

- `int(...)` gir en `ValueError` hvis brukeren skriver noe som ikke er et heltall, for eksempel `abc`. Da hopper vi til `except` og spør på nytt.
- Hvis tallet er gyldig, men utenfor området, skriver vi en melding og spør på nytt.
- `return` avslutter både løkka og funksjonen. Vi kommer altså bare ut av `while True` når svaret er gyldig.

I hovedprogrammet blir det slik:

```python
val = ask_number("\nKva vil du gjere? ", 0, 5)
valgt_nr = ask_number("Vel lydfil: ", 0, len(tracks) - 1)
nytt_volum = ask_number("Nytt volum (0-100): ", 0, 100)
```

Legg merke til `len(tracks) - 1` for låtnummeret. Da fungerer sjekken også hvis vi legger til flere låter senere.

**Hvorfor er dette en funksjon og ikke en metode i `Player`?** Å spørre brukeren om noe er brukergrensesnitt, ikke noe en musikkspiller gjør. Det er samme tankegang som for `show_menu()`.

Fordi `ask_number` garanterer et gyldig menyvalg, er `case _:` («Ugyldig val») fjernet. Den kan aldri skje lenger.

---

## Oppgave 4: Neste og forrige låt

Dette er den største endringen. For å vite hva som er *neste* låt, må spilleren vite to ting:

1. **Hele lista** med låter, og ikke bare den ene som spilles.
2. **Nummeret** på låten som spilles nå.

Derfor gir vi `Player` lista når vi oppretter den, og spilleren husker et nummer i stedet for et `Track`-objekt:

```python
def __init__(self, tracks):
    pygame.mixer.init()
    self.tracks = tracks
    self.current_nr = None      # None = ingen låt valgt
    ...

player = Player(tracks)
```

Da må `load_track` ta imot et *nummer*:

```python
def load_track(self, nr):
    self.current_nr = nr
    self.paused = False
    track = self.tracks[nr]
    pygame.mixer.music.load(track.get_filename())
```

Nå er neste og forrige enkle å lage:

```python
def next_track(self):
    if self.current_nr is None:
        nr = 0
    else:
        nr = self.current_nr + 1
        if nr >= len(self.tracks):  # Forbi siste låt? Start på nytt.
            nr = 0
    self.load_track(nr)
    self.play()

def previous_track(self):
    if self.current_nr is None:
        nr = 0
    else:
        nr = self.current_nr - 1
        if nr < 0:                  # Før første låt? Gå til siste.
            nr = len(self.tracks) - 1
    self.load_track(nr)
    self.play()
```

Ting å legge merke til:

- **Tenk på kanttilfellene.** Hva skjer etter siste låt? Før første låt? Når ingen låt er valgt ennå? Alle tre er håndtert med `if`-tester.
- **Metoder kan kalle andre metoder i samme objekt** med `self.`. `next_track` gjenbruker `self.load_track()` og `self.play()` i stedet for å kalle pygame direkte.
- `get_current_track()` slår nå opp i lista med nummeret: `return self.tracks[self.current_nr]`. Hovedprogrammet merker ingen forskjell, fordi det fortsatt får et `Track`-objekt tilbake. Det er nok en fordel med innkapsling: *innsiden* kan endres uten at *utsiden* trenger å endres.

*Ekstra:* De to `if`-testene for å gå rundt kan erstattes med modulo: `nr = (self.current_nr + 1) % len(self.tracks)`. Det er kortere, men vanskeligere å lese hvis du ikke har sett `%` før.

---

## Oppgave 5: Klassen `Playlist`

```python
class Playlist:
    """A class to represent a list of tracks."""

    def __init__(self, name):
        self.name = name
        self.tracks = []

    def get_name(self):
        return self.name

    def add_track(self, track):
        self.tracks.append(track)

    def get_track(self, nr):
        return self.tracks[nr]

    def get_number_of_tracks(self):
        return len(self.tracks)
```

`Player` får nå en `Playlist` i stedet for en liste, og spør spillelista når den trenger noe:

| Før (v3-4) | Etter (v3-5) |
|---|---|
| `self.tracks[nr]` | `self.playlist.get_track(nr)` |
| `len(self.tracks)` | `self.playlist.get_number_of_tracks()` |

Hovedprogrammet blir slik:

```python
playlist = Playlist("Mine favorittar")
playlist.add_track(Track("Horror hit", "lyd/horror-hit-logo-142395.mp3", "Skrekk"))
...
player = Player(playlist)
```

### Hva blir lettere i hovedprogrammet?

- **Koden sier hva den gjør.** `playlist.add_track(...)` er lettere å forstå enn `tracks.append(...)`. Man ser med en gang at det er snakk om en spilleliste.
- **Spillelista kan få flere egenskaper**, for eksempel et navn. Det kunne ikke en vanlig liste ha.
- **Det blir lett å ha flere spillelister**, for eksempel `trening = Playlist("Trening")` og `rolig = Playlist("Rolig")`. Spilleren kan bytte mellom dem uten at koden i `Player` må endres.
- **`Player` vet ikke lenger at låtene ligger i en liste.** Hvis vi senere vil lese låtene fra en fil eller sortere dem, er det bare `Playlist` som må endres.

Nå har programmet tre klasser med hver sin tydelige jobb:

| Klasse | Jobb |
|---|---|
| `Track` | Vet alt om *én* låt |
| `Playlist` | Holder orden på *mange* låter |
| `Player` | *Spiller av* låter fra en spilleliste |

### Ideer til å gå enda videre

- Legg til `remove_track(nr)` eller `shuffle()` i `Playlist`. Tips: `import random` og `random.shuffle(lista)`.
- La brukeren velge mellom flere spillelister i menyen.
- Les låtene inn fra en CSV-fil i stedet for å skrive dem i koden.
