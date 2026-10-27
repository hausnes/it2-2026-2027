# Importering: del koden opp i flere filer

Når et program blir stort, blir det fort uoversiktlig å ha alt i én fil. En vanlig løsning er å legge klassene i en egen fil og **importere** dem i hovedfila. Da blir hovedfila kort og handler bare om selve spillet.

| Fil | Hva den inneholder |
| --- | --- |
| [karakterer.py](karakterer.py) | Klassene `Character`, `Player` og `Enemy` |
| [main.py](main.py) | Hovedfila: importerer klassene og kjører en enkel kamp |

Eksempelet bygger på [dungeon_crawler_rpg](../dungeon_crawler_rpg/README.md).

---

## 1. Lag en fil med klassene

I [karakterer.py](karakterer.py) ligger alle klassene samlet. `Player` og `Enemy` arver fra `Character`:

```python
import random


class Character:
    def __init__(self, name, level, hp):
        ...

class Player(Character):
    def __init__(self, name, level, hp, strength):
        ...

class Enemy(Character):
    def __init__(self, name, level, hp, weapon):
        ...
```

Legg merke til at `import random` står i denne fila, fordi det er her `random` brukes. Hovedfila trenger ikke å importere `random`.

---

## 2. Importer klassene i hovedfila

I [main.py](main.py) henter vi klassene med én linje:

```python
from karakterer import Player, Enemy

spiller = Player("Kari", 1, 100, 10)
fiende = Enemy("Rektor", 3, 60, "linjal")
```

- `karakterer` er filnavnet **uten** `.py`.
- Etter `import` skriver du navnet på det du vil hente, skilt med komma.
- Du trenger ikke importere `Character`, så lenge du ikke lager `Character`-objekter direkte i hovedfila. `Player` og `Enemy` vet selv at de arver fra den.

Kjør programmet ved å starte **hovedfila**:

```
python main.py
```

### En annen måte å importere på

Du kan også importere hele fila. Da må du skrive filnavnet foran klassenavnet:

```python
import karakterer

spiller = karakterer.Player("Kari", 1, 100, 10)
```

Begge måtene virker. `from ... import ...` gir kortere kode, mens `import karakterer` gjør det tydelig hvor klassen kommer fra.

---

## 3. Test-kode med `if __name__ == "__main__":`

Nederst i [karakterer.py](karakterer.py) står dette:

```python
if __name__ == "__main__":
    test_spiller = Player("Test", 1, 100, 10)
    print(test_spiller)
```

Når Python importerer en fil, kjøres **all** koden i fila. Uten denne `if`-testen ville test-koden blitt kjørt hver gang du startet `main.py`.

- Kjører du `python karakterer.py`, kjøres test-koden.
- Kjører du `python main.py`, hoppes test-koden over.

Slik kan du teste klassene dine i samme fil som de er skrevet i, uten at det forstyrrer hovedprogrammet.

---

## 4. Vanlige feil

- **`ModuleNotFoundError: No module named 'karakterer'`**: Filene må ligge i samme mappe, og du må kjøre programmet fra den mappa. I VS Code kan du åpne selve mappa (`File → Open Folder`).
- **`ImportError: cannot import name 'Enemy'`**: Sjekk at navnet er stavet likt, med stor og liten bokstav, i begge filene.
- **Ikke gi fila samme navn som et bibliotek.** Kaller du fila `random.py`, vil `import random` hente din fil i stedet for Python sitt bibliotek.
- **Mappa `__pycache__`** dukker opp når du importerer. Den lager Python selv for å starte raskere, og du kan trygt ignorere den.

---

## 5. Prøv selv

- Legg til en ny klasse `Boss(Enemy)` i [karakterer.py](karakterer.py) og bruk den i [main.py](main.py).
- Flytt grafikken fra [dungeoncrawler_grafikk.py](../dungeon_crawler_rpg/dungeoncrawler_grafikk.py) inn i en egen fil `grafikk.py` og importer `logo` i hovedfila.
