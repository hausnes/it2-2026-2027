# OOP-prosjekt: Dungeon Crawler

I dette prosjektet skal du lage et lite rollespill (en *dungeon crawler*) i terminalen ved hjelp av **objektorientert programmering (OOP)**. Denne siden forklarer det du trenger om klasser og objekter, og viser eksempelfiler du kan hente idéer fra.

| Fil | Hva den viser |
| --- | --- |
| [dungeoncrawler_magi_dictionary.py](dungeoncrawler_magi_dictionary.py) | Et ferdig mini-spill: to karakterer kjemper med magi-angrep lagret i en dictionary |
| [dungeoncrawler_grafikk.py](dungeoncrawler_grafikk.py) | Tekstgrafikk (ASCII-art) av logo og fiender som du kan bruke i ditt eget spill |
| [richpixels_test.py](dungeoncrawler_richpixels.py) | Hvordan du viser et ekte bilde i terminalen med biblioteket `rich-pixels` |

---

## 1. Klasser og objekter

En **klasse** er en mal. Et **objekt** er én konkret ting laget fra malen. I et rollespill kan vi ha én klasse `Character`, og mange objekter: en helt, en rektor, et skjelett …

```python
import random


class Character:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def __str__(self):
        return f"Navn: {self.name}, Level: {self.level}, HP: {self.hp}"

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        # Angrepsstyrken avhenger av level
        return random.randint(1, self.level * 2)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
```

- `__init__` kjøres automatisk når vi lager et nytt objekt. Her gir vi objektet sine **attributter** (`name`, `level`, `hp`).
- `self` betyr «dette objektet». `self.hp` er HP-en til akkurat denne karakteren.
- Funksjoner inne i en klasse kalles **metoder**. De beskriver hva objektet kan *gjøre*.
- `__str__` bestemmer hva som skrives ut når vi bruker `print()` på objektet.

Slik lager og bruker vi objekter:

```python
fiende = Character("Rektor", 3, 100)
print(fiende)                    # Navn: Rektor, Level: 3, HP: 100

skade = fiende.attack()
print(f"Rektor angriper og gjør {skade} skade!")

fiende.take_damage(40)
print(fiende.hp)                 # 60
print(fiende.is_alive())         # True
```

> **Tips:** Du *kan* skrive `fiende.hp = 60` direkte, men å bruke en metode som `take_damage()` er ofte lurere, fordi metoden kan passe på reglene i spillet, for eksempel at HP aldri blir mindre enn 0.

---

## 2. Arv: en spiller er en karakter

Spilleren er også en karakter, men med noen ekstra egenskaper. I stedet for å skrive all koden på nytt kan `Player` **arve** fra `Character`:

```python
class Player(Character):
    def __init__(self, name, level, hp, strength):
        super().__init__(name, level, hp)   # Lar Character sette name, level og hp
        self.strength = strength            # Nytt attributt som bare spilleren har

    def __str__(self):
        return f"{super().__str__()}, Styrke: {self.strength}"

    def attack(self):
        # Spilleren bruker styrke i stedet for level
        return random.randint(1, self.strength)
```

- `class Player(Character):` betyr at `Player` får alle attributter og metoder fra `Character`.
- `super().__init__(...)` kaller `__init__` i `Character`, så vi slipper å gjenta koden.
- `Player` lager sin egen `attack()`. Da brukes den i stedet for den i `Character`. Dette kalles å **overstyre** en metode.
- `is_alive()` og `take_damage()` skriver vi ikke på nytt. De arves.

```python
spiller = Player("Kari", 1, 100, 10)
fiende = Character("Rektor", 3, 100)
print(spiller)                   # Navn: Kari, Level: 1, HP: 100, Styrke: 10

skade = spiller.attack()
fiende.take_damage(skade)
print(f"{spiller.name} gjorde {skade} skade. {fiende.name} har {fiende.hp} HP igjen.")
```

---

## 3. Alternative måter du kan møte (valgfritt)

Koden over er den enkleste og mest vanlige måten å skrive klasser på i Python. Når du leser kode på nettet, vil du også se andre måter. Du trenger ikke bruke dem, men det er greit å kjenne dem igjen.

### 3a. «Private» attributter med get- og set-metoder

I språk som Java er det vanlig å skjule attributtene og bare endre dem via metoder (*getters* og *setters*):

```python
class Character:
    def __init__(self, name, hp):
        self.__hp = hp       # To understreker: «ikke rør dette utenfra»
        self.__name = name

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        self.__hp = new_hp


fiende = Character("Rektor", 100)
fiende.set_hp(50)
print(fiende.get_hp())   # 50
```

Python har egentlig ikke ekte private attributter. To understreker (`__hp`) gjør bare at Python gir attributtet et annet navn bak kulissene (`_Character__hp`). Det gir noen overraskende resultater:

```python
fiende.__hp = 0                  # Lager et NYTT attributt med navnet __hp ...
print(fiende.get_hp())           # ... så den ekte HP-en er fortsatt 50

fiende._Character__hp = 0        # Dette endrer den ekte HP-en (men ikke gjør dette!)
print(fiende.get_hp())           # 0
```

I Python er det mer vanlig å bruke **én** understrek (`self._hp`). Det er bare en avtale mellom programmerere som betyr «dette er ment for bruk inne i klassen».

### 3b. `@property`

Med `@property` foran en metode kan du bruke metoden som om den var et attributt, altså uten parenteser:

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @property
    def is_alive(self):
        return self.hp > 0


fiende = Character("Rektor", 100)
print(fiende.is_alive)           # True (merk: ingen parenteser)
```

Dette er den «pythonske» erstatningen for get-metoder. Pass på at du ikke blander de to måtene: skriver du `fiende.is_alive()` her, får du en feilmelding.

Vil du lese mer, kan du se [Real Python: Getters and Setters](https://realpython.com/python-getter-setter/).

### 3c. Typeannotasjoner

Du kan skrive hvilken datatype parametere og returverdier skal ha. Python sjekker ikke dette når programmet kjører, men koden blir lettere å lese, og VS Code kan varsle deg om feil:

```python
class Character:
    def __init__(self, name: str, level: int, hp: int):
        self.name = name
        self.level = level
        self.hp = hp

    def is_alive(self) -> bool:
        return self.hp > 0
```

---

## 4. Eksempelfilene

### Magi-angrep med dictionary

[dungeoncrawler_magi_dictionary.py](dungeoncrawler_magi_dictionary.py) er et lite, ferdig spill der helten Tor kjemper mot Loke. Legg merke til:

- Hver karakter har en dictionary med magi-angrep, der nøkkelen er navnet og verdien er skaden.
- Metoden `utfør_magi_angrep()` tar imot et **annet objekt** (`mål`) og endrer HP-en til det. Slik kan objekter påvirke hverandre.
- En `while`-løkke kjører kampen til én av dem er beseiret.

### Tekstgrafikk

[dungeoncrawler_grafikk.py](dungeoncrawler_grafikk.py) inneholder bare grafikk lagret i variabler. Kjør fila for å se alt, eller importer det du trenger i ditt eget spill:

```python
from dungeoncrawler_grafikk import logo, enemy_list

print(logo)
print(enemy_list["skeleton"])
```

Fila må ligge i samme mappe som programmet ditt. Lager du egen grafikk med mange `\`-tegn, bør du skrive `r` foran strengen (`r"""..."""`), ellers kan Python tolke skråstrekene som spesialtegn.

### Bilder i terminalen med rich-pixels

[richpixels_test.py](dungeoncrawler_richpixels.py) viser bildet `skolebygget.webp` direkte i terminalen. Installer biblioteket først:

```
pip install rich-pixels
```

Hver piksel blir ett tegn i terminalen. Eksempelbildet er 300 × 198 piksler og blir derfor 300 tegn bredt, så du må kanskje gjøre terminalvinduet større eller bruke et mindre bilde.

---

## 5. Idéer til videre arbeid

- Gi `Player` en dictionary med magi-angrep, slik som i magi-eksempelet.
- Lag flere fiendetyper som arver fra `Character`, for eksempel `Skeleton` og `Dragon`, med hver sin `attack()`.
- Vis riktig ASCII-art fra `enemy_list` når spilleren møter en fiende.
- I magi-eksempelet krasjer programmet hvis du skriver noe annet enn et gyldig tall. Kan du fikse det?
- Legg til `mana` som brukes opp når spilleren kaster magi.
