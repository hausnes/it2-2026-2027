# Kart: gå rundt i et rutenett

Et lite eksempel på hvordan en spillkarakter kan gå rundt på et kart. Kartet er en **todimensjonal liste** (en liste med lister), og hver celle inneholder et tall som forteller hva som ligger der.

| Fil | Hva den inneholder |
| --- | --- |
| [main.py](main.py) | Klassene `Map` og `Player`, og en løkke der du styrer med w/a/s/d |

Kjør med:

```
python main.py
```

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

## Trenger vi en egen klasse for celler?

Ikke i dette eksempelet. Så lenge en celle bare er «gulv», «hindring» eller «fiende», holder det med et tall.

En `Cell`-klasse blir nyttig når cellene skal **huske noe**, for eksempel:

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
- Les kartet fra en tekstfil i stedet for å skrive det i koden.
- Flytt klassene til en egen fil, slik som i [importering](../importering/README.md).
