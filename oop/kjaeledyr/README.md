# Time 2: Kjæledyr med objekter

Forrige time laget du et kjæledyrspill med variabler, funksjoner og dictionaries ([oppgaven](time1_oppgave.md)). Det fungerte, men det ble tungvint: `global` overalt, kopiert kode, lange parameterlister og tekst-nøkler som lett får skrivefeil.

I denne guiden bygger du det samme spillet med **objektorientert programmering (OOP)**. Følg stegene i rekkefølge, og skriv koden selv i en ny fil, `kjaeledyr_oop.py`. Ikke kopier — skriv! Da lærer du mer.

---

## Steg 1: En klasse er en mal

I del C laget vi en funksjon som lager en dictionary for et nytt dyr:

```python
def nytt_dyr(navn):
    return {"navn": navn, "sult": 5, "energi": 5, "glede": 5}
```

En **klasse** er en mal for hva et kjæledyr *er*. Skriv dette:

```python
class Kjaeledyr:
    def __init__(self, navn):
        self.navn = navn
        self.sult = 5
        self.energi = 5
        self.glede = 5
```

- `class Kjaeledyr:` lager en ny klasse. Klassenavn skrives med stor forbokstav.
- `__init__` er en spesiell funksjon som kjøres **automatisk** hver gang vi lager et nytt dyr.
- `self` betyr «dette dyret» — det dyret som blir laget akkurat nå.
- `self.navn`, `self.sult` osv. er **attributter**: variabler som hører til dyret.

---

## Steg 2: Lag objekter fra klassen

Et **objekt** er ett konkret dyr laget fra malen. Legg til dette *under* klassen (ikke inne i den):

```python
fido = Kjaeledyr("Fido")
pusur = Kjaeledyr("Pusur")

print(fido.navn, fido.sult)
print(pusur.navn, pusur.sult)
```

Kjør programmet. Når du skriver `Kjaeledyr("Fido")`, kjører Python `__init__` og sender `"Fido"` inn som `navn`.

**Sammenlign:**

| Før | Nå |
|---|---|
| `dyr["sult"]` | `fido.sult` |
| `sult1`, `sult2` | `fido.sult`, `pusur.sult` |

Skriv `fido.` i VS Code og se at den foreslår attributtene. Prøv å skrive `fido.slut` — VS Code markerer feilen *før* du kjører programmet.

✏️ **Prøv selv:** Lag et tredje dyr med ditt eget navn, og skriv ut navnet og energien.

---

## Steg 3: Den første metoden

En **metode** er en funksjon som ligger *inne i* klassen. Legg til denne inne i klassen (rykket inn på samme nivå som `__init__`):

```python
    def vis_status(self):
        print(f"{self.navn}: sult {self.sult}, energi {self.energi}, glede {self.glede}")
        if self.sult >= 8:
            print(f"{self.navn} er sulten!")
        if self.energi <= 2:
            print(f"{self.navn} er trøtt!")
```

Bytt ut `print`-linjene fra steg 2 med:

```python
fido.vis_status()
pusur.vis_status()
```

**Hva er `self`?** Når du skriver `fido.vis_status()`, sender Python automatisk `fido` inn som `self`. Når du skriver `pusur.vis_status()`, er `self` Pusur. Derfor trenger metoden ingen andre parametere.

| Del B | Del C | OOP |
|---|---|---|
| `vis_status(navn1, sult1, energi1, glede1)` | `vis_status(dyrene[0])` | `fido.vis_status()` |

---

## Steg 4: Metoder som endrer dyret

Øverst i fila (over klassen) legger du inn hjelpefunksjonen fra forrige time:

```python
def begrens(verdi):
    return max(0, min(10, verdi))
```

Legg så til disse metodene inne i klassen:

```python
    def mate(self):
        self.sult = begrens(self.sult - 3)
        self.glede = begrens(self.glede + 1)
        print(f"Du ga {self.navn} mat.")

    def tiden_gaar(self):
        self.sult = begrens(self.sult + 1)
        self.glede = begrens(self.glede - 1)
```

Test dem:

```python
fido.mate()
fido.vis_status()
pusur.vis_status()  # Pusur er uendret!
```

Legg merke til: **Ingen `global`!** Metoden endrer `self.sult` — sulten til akkurat det dyret vi kalte metoden på.

✏️ **Prøv selv:** Skriv metodene `leke()` og `sove()` selv. Reglene står i del A i [oppgaven fra time 1](time1_oppgave.md). Husk at dyret ikke kan leke hvis energien er under 2.

---

## Steg 5: En liste med objekter

Nå kan vi ha så mange dyr vi vil i en liste. Bytt ut testkoden med:

```python
dyrene = [Kjaeledyr("Fido"), Kjaeledyr("Pusur"), Kjaeledyr("Rex")]

for dyr in dyrene:
    dyr.tiden_gaar()

for dyr in dyrene:
    dyr.vis_status()
```

Sammenlign med del B, der `tiden_gaar()` måtte nevne hver eneste variabel for hvert eneste dyr. Nå fungerer den samme løkka for 3 dyr eller 300.

---

## Steg 6: Hele spillet

Nå mangler bare menyen. Den er nesten lik den fra del C — men legg merke til at det er *dyret* som gjør ting: `dyr.mate()` i stedet for `mate(dyr)`.

```python
def velg_dyr(dyrene):
    for i, dyr in enumerate(dyrene):
        print(f"{i + 1}: {dyr.navn}")
    try:
        return dyrene[int(input("Hvilket dyr? ")) - 1]
    except (ValueError, IndexError):
        print("Ugyldig dyr.")
        return None


dyrene = [Kjaeledyr("Fido"), Kjaeledyr("Pusur")]

while True:
    print()
    for dyr in dyrene:
        dyr.vis_status()
    print("1: Mate  2: Leke  3: Sove  4: Adopter nytt dyr  0: Avslutt")
    valg = input("Velg: ")

    if valg == "0":
        break
    elif valg == "4":
        dyrene.append(Kjaeledyr(input("Navn på det nye dyret: ")))
    elif valg in ["1", "2", "3"]:
        dyr = velg_dyr(dyrene)
        if dyr is None:
            continue
        if valg == "1":
            dyr.mate()
        elif valg == "2":
            dyr.leke()
        elif valg == "3":
            dyr.sove()
    else:
        print("Ugyldig valg.")
        continue

    for dyr in dyrene:
        dyr.tiden_gaar()
```

Kjør og test spillet. Fullstendig løsning: [losning/time2_med_oop.py](losning/time2_med_oop.py).

---

## Steg 7: Test hvor lett det er å endre

Nå skal du merke gevinsten. Gjør disse endringene — og legg merke til *hvor* i koden du må endre:

1. **Ny handling:** Legg til metoden `bade()`: glede −1 og energi −1 (de fleste dyr liker ikke bad 😄). Legg den til i menyen.
2. **Ny verdi:** Gi alle dyr en `alder` som starter på 0 og øker med 1 hver gang tiden går. Vis den i statusen.

Hvor mange steder måtte du endre for punkt 2? Tenk på hvor mange steder du måtte endret i del B!

---

## Oppsummering

| Begrep | Forklaring | I spillet |
|---|---|---|
| **Klasse** | En mal som beskriver hva noe *er* og *kan gjøre* | `Kjaeledyr` |
| **Objekt** | Én konkret ting laget fra klassen | `fido`, `pusur` |
| **Attributt** | En variabel som hører til objektet | `self.sult` |
| **Metode** | En funksjon som hører til objektet | `mate()`, `leke()` |
| **`__init__`** | Kjøres automatisk når et objekt lages | Gir dyret navn og startverdier |
| **`self`** | Objektet metoden jobber med | `fido.mate()` → `self` er Fido |

| Problem i time 1 | Løsning med OOP |
|---|---|
| `global` overalt | Metodene endrer `self.sult` |
| Kopiert kode for hvert dyr | Én klasse, så mange objekter du vil |
| Lange parameterlister | `self` har alt dyret trenger |
| Skrivefeil i tekst-nøkler | VS Code sier fra om `fido.slut` |
| Hva *er* et kjæledyr? | Står i `__init__` |
| Data og funksjoner hver for seg | Samlet i klassen |

---

## Bonus: Hund og katt (arv)

Vil du ha forskjellige typer dyr? En hund *er* et kjæledyr, men med litt egen oppførsel. Da kan klassen **arve** fra `Kjaeledyr`:

```python
class Hund(Kjaeledyr):
    def leke(self):
        super().leke()  # Gjør alt et vanlig kjæledyr gjør når det leker ...
        print("Voff! 🐶")  # ... og litt til


class Katt(Kjaeledyr):
    def mate(self):
        super().mate()
        print("Mjau! 🐱")


dyrene = [Hund("Fido"), Katt("Pusur")]
```

- `class Hund(Kjaeledyr)` betyr at `Hund` får alle attributtene og metodene til `Kjaeledyr`.
- Når `Hund` har sin egen `leke()`, brukes den i stedet. Det kalles å **overstyre** en metode.
- `super().leke()` kaller `leke()` fra `Kjaeledyr`, slik at vi slipper å skrive reglene på nytt.

✏️ Gi `Katt` en egen regel: Katter gidder ikke leke hvis gleden er under 3.
