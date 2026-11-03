# Kart: gå rundt i et rutenett

Et lite eksempel på hvordan en spillkarakter kan gå rundt på et kart. Kartet er en **todimensjonal liste** (en liste med lister), og hver celle inneholder et tall som forteller hva som ligger der.

| Fil | Hva den inneholder |
| --- | --- |
| [main.py](main.py) | Klassene `Map` og `Player`, og en løkke der du styrer med w/a/s/d |
| [main-v2.py](main-v2.py) | Samme kart, men nå kan du gå i kamp mot fiendene (se [del 5](#5-versjon-2-kamp-mot-fiender)) |
| [main-v3.py](main-v3.py) | Som v2, men med pikselgrafikk for kartet og kampene (se [del 6](#6-versjon-3-pikselgrafikk-med-rich-pixels)) |
| [main-v4.py](main-v4.py) | Som v3, men skjermen tømmes før hver tegning, så det ser ut som et spill (se [del 7](#7-versjon-4-tømme-skjermen-mellom-hver-tegning)) |
| [graphics.py](graphics.py) | Klassen `Graphics`, som tegner med rich-pixels. Brukes av `main-v3.py` og `main-v4.py` |

Kjør med:

```
python main.py
python main-v2.py
python main-v3.py
python main-v4.py
```

`main-v3.py` og `main-v4.py` trenger biblioteket rich-pixels. Installer det først med `pip install rich-pixels`.

---

## 1. Kartet er en liste med lister

```python
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 2, 1, 0],
    [1, 0, 0, 0, 2],
]
```

| Tall | Betyr |
| --- | --- |
| `0` | Gulv |
| `1` | Hindring (du kan ikke gå hit) |
| `2` | Fiende |

Hver indre liste er **én rad**. For å hente en celle skriver du først raden, så kolonnen:

```python
grid[3][2]   # rad 3, kolonne 2 → 2 (en fiende)
```

> **Vanlig feil:** Mange tenker `(x, y)`, altså kolonne først. Men i en liste med lister kommer **raden først**: `grid[rad][kolonne]`. Derfor bruker eksempelet navnene `row` og `col` i stedet for `x` og `y`, så det er lettere å holde styr på.

Rad 0 er øverst. Å gå **opp** betyr derfor at raden blir **mindre** (`-1`).

---

## 2. Klassen `Map`

`Map` tar vare på rutenettet og svarer på spørsmål om det:

| Metode | Svarer på |
| --- | --- |
| `is_inside(row, col)` | Er denne posisjonen innenfor kartet? |
| `is_blocked(row, col)` | Er det en hindring her? |
| `describe(row, col)` | Hva står jeg på? (f.eks. «en gulvcelle») |
| `show(player)` | Skriver ut kartet med `P` der spilleren står |

Klassen heter `Map` med stor M. Klasser skrives med stor forbokstav i Python, og `map` med liten m er dessuten allerede en innebygd funksjon i Python. Av samme grunn heter objektet `game_map`, ikke `map`.

---

## 3. Klassen `Player`

Spilleren vet bare **hvor den står** (`row` og `col`). Når den skal flytte seg, regner den ut den nye posisjonen og spør kartet om det er lov:

```python
def move(self, d_row, d_col, game_map):
    new_row = self.row + d_row
    new_col = self.col + d_col

    if not game_map.is_inside(new_row, new_col):
        print("Du kan ikke gå utenfor kartet.")
    elif game_map.is_blocked(new_row, new_col):
        print("Det står en hindring i veien.")
    else:
        self.row = new_row
        self.col = new_col
```

Rekkefølgen er viktig: vi må sjekke `is_inside` **før** `is_blocked`. Ellers prøver vi å lese en celle som ikke finnes, og får `IndexError`. (Prøv selv: hva skjer med `grid[-1][0]`? Hvorfor er det lurt å sjekke `0 <= row`?)

---

## 4. Retninger som tall

I stedet for fire `if`-tester for w/a/s/d, lagrer vi hvor mye rad og kolonne skal endres:

```python
RETNINGER = {
    "w": (-1, 0),  # opp
    "s": (1, 0),   # ned
    "a": (0, -1),  # venstre
    "d": (0, 1),   # høyre
}
```

Da trenger `Player` bare én `move`-metode, uansett retning.

---

## 5. Versjon 2: kamp mot fiender

I [main-v2.py](main-v2.py) skjer det noe når du går på en fiende (`2`): du havner i en kamp. Vinner du, blir cellen til gulv og du kan utforske videre. Taper du, er spillet over.

### Nye ting i klassene

| Klasse | Nytt | Hva det gjør |
| --- | --- | --- |
| `Map` | `has_enemy(row, col)` | Står det en fiende her? |
| `Map` | `remove_enemy(row, col)` | Gjør cellen om til gulv (`0`) når fienden er beseiret |
| `Player` | `hp`, `max_hp` | Hvor mye liv spilleren har nå, og maks |
| `Player` | `attack(enemy)` | Gjør 4–8 skade på fienden |
| `Player` | `defend()` | Neste angrep fra fienden gjør bare halv skade |
| `Player` | `heal()` | Får tilbake 6 HP, men aldri mer enn `max_hp` |
| `Player` | `take_damage(damage)` | Trekker fra skade, og halverer den hvis spilleren forsvarer seg |
| `Enemy` | ny klasse | Har `name` og `hp`, og kan angripe spilleren (3–7 skade) |

Skaden er tilfeldig med `random.randint(a, b)`, som gir et heltall fra og med `a` til og med `b`. Derfor blir ikke to kamper like.

### Hvem passer på forsvaret?

Det er `Player` som vet om den forsvarer seg (`self.defending`). Fienden bryr seg ikke om det, den kaller bare `player.take_damage(damage)`, og så regner spilleren selv ut hvor mye skade den faktisk tar:

```python
def take_damage(self, damage):
    if self.defending:
        damage = damage // 2  # halv skade når vi forsvarer oss
        self.defending = False
    self.hp -= damage
    return damage
```

`defending` settes tilbake til `False` med en gang, slik at forsvaret bare gjelder **ett** angrep. Metoden returnerer den faktiske skaden, så fienden kan skrive ut riktig tall.

### Kampen er en egen løkke

Funksjonen `fight(player, enemy)` har sin egen `while`-løkke, inne i hovedløkka. Hver runde har to deler:

1. **Spillerens tur:** velg angrip (`a`), forsvar (`f`) eller heal (`h`).
2. **Fiendens tur:** fienden angriper, men **bare hvis den fortsatt lever**. Ellers kunne en død fiende slått tilbake.

Løkka går så lenge begge lever. Etterpå returnerer funksjonen `True` (spilleren vant) eller `False` (spilleren tapte). Ved ugyldig valg bruker vi `continue`, slik at spilleren blir spurt på nytt uten at fienden får en gratis runde.

### Koble kampen til kartet

I hovedløkka sjekker vi om spilleren har gått på en fiende etter hvert trekk:

```python
if game_map.has_enemy(spiller.row, spiller.col):
    fiende = Enemy("Goblin", 15)
    if fight(spiller, fiende):
        game_map.remove_enemy(spiller.row, spiller.col)
    else:
        print("Spillet er over.")
        break
```

Legg merke til at kartet fortsatt bare inneholder tall. `Enemy`-objektet lages først **når kampen starter**. Det fungerer her fordi alle fiendene er like, og fordi cellen blir gulv etter at du har vunnet. Skal fiendene være forskjellige, eller skal en fiende huske skaden den har fått, må objektet ligge i kartet (se neste del).

Spilleren beholder HP-en sin mellom kampene. Har du lite HP igjen etter første goblin, går du inn i neste kamp svekket.

---

## 6. Versjon 3: pikselgrafikk med rich-pixels

I [main-v3.py](main-v3.py) er spillet det samme som i v2, men kartet og kampene tegnes med fargede ruter i terminalen:

- Kartet: gulv er grått, vegger er svarte, fiender er røde og spilleren er grønn.
- I kampen står spilleren og goblinen på bakken ved siden av hverandre. Den som dør, blir tegnet liggende.

All tegning skjer i klassen `Graphics` i en egen fil, [graphics.py](graphics.py). `main-v3.py` henter den med `from graphics import Graphics`, akkurat som i [importering](../importering/README.md).

### Tegne med bokstaver

rich-pixels har en metode, `Pixels.from_ascii(tekst, mapping)`, som går gjennom en tekst tegn for tegn og bytter hvert tegn ut med noe annet. Vi bytter hver bokstav ut med en farget rute. En figur er derfor bare en liste med tekstlinjer:

```python
SPILLER = [
    "...HHH...",   # H = hud
    "...KHK...",   # K = øyne
    "...HHH...",
    "..GGGGG..",   # G = grønn trøye
    ".H.GGG.H.",
    "...B.B...",   # B = blå bukse
    "...B.B...",
]
```

Og hvilken farge hver bokstav skal ha, står i en dictionary:

```python
FIGURFARGER = {
    "H": "#f1c27d",  # hud
    "K": "#000000",  # øyne
    "G": "#00b000",  # grønn trøye
    ...
}
```

`.` betyr gjennomsiktig, altså ingen farge. Hver rute tegnes som **to** mellomrom med bakgrunnsfarge, fordi et tegn i terminalen er omtrent dobbelt så høyt som det er bredt. Med to tegn blir rutene nesten kvadratiske.

Fargene er skrevet som hex-koder (`#rrggbb`), som du kanskje kjenner fra CSS. Vil du ha andre farger eller nye figurer, endrer du bare tekstene og dictionaryene øverst i `graphics.py`.

### Klassen `Graphics`

| Metode | Hva den gjør |
| --- | --- |
| `draw_map(game_map, player)` | Tegner kartet, med spilleren som en grønn rute |
| `draw_fight(player, enemy)` | Tegner spilleren og fienden ved siden av hverandre, levende eller døde |
| `clear()` | Tømmer terminalen (brukes i v4) |
| `draw_sprite(sprite)` | Tegner én figur, f.eks. `graphics.draw_sprite(SPILLER)` (kan brukes etter behov) |
| `_draw(text, colors)` | Hjelpemetode som de andre bruker. Gjør om bokstaver til farger og skriver ut |

Understreken i `_draw` er en vanlig måte å si «denne metoden er bare ment for bruk inne i klassen».

`draw_fight` velger figur ut fra om karakteren lever:

```python
if player.is_alive():
    left = SPILLER
else:
    left = SPILLER_DØD
```

Deretter limes figurene sammen linje for linje, med litt luft imellom og en linje med bakke (`g`) under. Det fungerer fordi alle figurene er like store (9 × 7 ruter). De døde figurene har tomme linjer øverst, slik at de ligger nede på bakken.

### Hva ble endret i `main-v3.py`?

Ikke mye, og det er hele poenget:

- `Map.show()` er fjernet. `Map` vet hva som ligger på kartet, og `Graphics` vet hvordan det skal **se ut**. Når hver klasse har sin egen oppgave, kan du bytte ut grafikken uten å røre spillogikken.
- `graphics.draw_map(game_map, spiller)` erstatter `game_map.show(spiller)`.
- `fight()` tar imot `graphics` og kaller `graphics.draw_fight(player, enemy)` i starten av hver runde, og én gang til etter kampen, når en av dem ligger død.

> **Tips:** Svarte vegger kan bli vanskelige å se hvis terminalen har mørk bakgrunn. Bytt til en annen farge i `KARTFARGER` om du vil.

---

## 7. Versjon 4: tømme skjermen mellom hver tegning

I v3 blir hver nye tegning skrevet ut under den forrige, så terminalen fylles opp nedover. I [main-v4.py](main-v4.py) tømmer vi skjermen før hver tegning med `graphics.clear()`. Da står kartet alltid øverst, og det ser mer ut som et spill og mindre som en logg.

### Problemet: meldingene forsvinner

Det holder ikke å bare legge inn `graphics.clear()` øverst i løkka. I v3 skriver `move()` ut en melding, for eksempel «Det står en hindring i veien.», rett **før** neste runde i løkka. Med en gang løkka starter på nytt, tømmes skjermen, og meldingen forsvinner før du rekker å lese den.

### Løsningen: returner meldingen i stedet for å printe den

I v4 bruker metodene `return` i stedet for `print()`:

```python
def attack(self, enemy):
    damage = random.randint(4, 8)
    enemy.hp -= damage
    return f"{self.name} angriper og gjør {damage} skade."
```

Hovedløkka tar vare på meldingen i en variabel og skriver den ut **etter** at skjermen er tømt og kartet er tegnet:

```python
message = "Velkommen! Finn og beseir fiendene."

while True:
    graphics.clear()
    graphics.draw_map(game_map, spiller)
    print(message)
    valg = input("Gå med w/a/s/d (q for å avslutte): ").lower()
    ...
    message = spiller.move(d_row, d_col, game_map)
```

Rekkefølgen i hver runde blir: **tøm → tegn → vis melding → spør**.

Dette gjør også klassene ryddigere. `Player` bestemmer hva som skal skje, men ikke hvordan det skal vises. Det er det samme poenget som da `Graphics` fikk ansvaret for tegningen i v3.

### Kampen

I kampen skjer det to ting hver runde: spilleren gjør noe, og fienden angriper. Meldingene settes sammen med `"\n"`, slik at de havner på hver sin linje:

```python
message = player.attack(enemy)
if enemy.is_alive():
    message += "\n" + enemy.attack(player)
```

Tegningen av kampen (tøm, tegn figurene, vis HP og melding) ligger i en egen funksjon, `draw_fight_screen()`, fordi den brukes to steder: i hver runde og én gang til når kampen er over.

Etter kampen venter spillet på at du trykker Enter. Ellers ville kartet blitt tegnet med en gang, og du hadde ikke sett hvem som vant.

> **Merk:** `clear()` virker i vanlige terminaler, også den i VS Code. Kjører du programmet et sted som ikke er en ekte terminal, for eksempel i noen nettbaserte editorer, kan det hende skjermen ikke blir tømt.

---

## Trenger vi en egen klasse for celler?

Ikke i dette eksempelet. Så lenge en celle bare er «gulv», «hindring» eller «fiende», holder det med et tall.

En `Cell`-klasse blir nyttig (men ikke nødvendig) når cellene skal **huske noe**, for eksempel:

- en fiende som har egne HP og kan dø (da kan cellen inneholde et `Enemy`-objekt)
- en kiste som er åpnet eller ikke
- en celle som er besøkt (for «tåke» over ukjente deler av kartet)

Da kan rutenettet inneholde objekter i stedet for tall: `grid[rad][kolonne]` gir et `Cell`-objekt, og du kan skrive f.eks. `cell.is_blocked()` eller `cell.enemy`.

---

## Videre arbeid

Dette er bare **én** måte å gjøre det på. Noen ting du kan prøve, eller gjøre annerledes:

- Legg til flere celletyper, f.eks. `3` for en skatt eller en dør.
- Bytt ut tallene med bokstaver (`"."`, `"#"`, `"E"`) så kartet blir lettere å lese.
- Hva skal skje når du går på en fiende? Kan du koble dette til `Player` og `Enemy` fra [dungeon_crawler_rpg](../dungeon_crawler_rpg/README.md)?
- I `main-v2.py` kan du heale så mye du vil. Gi spilleren et begrenset antall healing-drikker i stedet.
- Gi fiendene ulike navn og styrke, f.eks. ved å la tallet `3` bety en sterkere fiende.
- Gjør det mulig å vinne spillet: skriv en melding og avslutt når alle fiendene er beseiret.
- La fienden også velge mellom flere handlinger, for eksempel tilfeldig med `random.choice`.
- Lag din egen figur i `graphics.py`, f.eks. en skattekiste, og tegn den med `draw_sprite` når spilleren finner en skatt.
- Gi spilleren en annen figur når den forsvarer seg (med skjold) eller healer.
- Les kartet fra en tekstfil i stedet for å skrive det i koden.
- Flytt klassene til en egen fil, slik som i [importering](../importering/README.md).
