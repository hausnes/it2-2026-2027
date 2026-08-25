# Typer i Python

Vi har typisk bare definert variabler på denne måten:

```python
tall = 3
print(type(tall))
```

Det ligger i kortene at den som skriver koden har `tenkt` at man skulle lagre tall i denne variabelen, men det er IKKE gitt at faktisk blir tilfelle. Kanskje man ikke skriver på norsk? Kanskje man ikke bryr seg?

Et enkelt grep du kan gjøre er å spesifisere at du ønsker at denne variabelen skal inneholde en spesifikk type, som dette:

```python
alder: int = 16
print(type(alder))

lengde: float = 4.5
print(type(lengde))

navn: str = "Ola"
print(type(navn))

gammelNok: bool = True
print(type(gammelNok))

```

Videre, for mer avanserte datatyper kan du bruke:

```python
listeNavn: list = ["Ola", "Kari", "Per"]
print(type(listeNavn))

dictPersoner: dict = {"Ola": 16, "Kari": 17, "Per": 18}
print(type(dictPersoner))
```

..eller enda bedre:

```python
# Ny og bedre måte (spesifiserer innholdet):
liste_navn: list[str] = ["Ola", "Kari", "Per"]
dict_personer: dict[str, int] = {"Ola": 16, "Kari": 17, "Per": 18}
```

Python sjekker derimot ikke typer automatisk når koden kjører (runtime). Det betyr at dette ikke vil gi en feilmelding i Python når du kjører skriptet:

```python
alder: int = "sytten"  # Python tillater dette ved kjøring
```

VS Code vil derimot gi deg en rød strek eller advarsel dersom du sender inn feil datatype.

Dersom du eksempelvis bruker `mypy`, så er dette et verktøy du kan kjøre i terminalen for å sjekke at alle typer i prosjektet stemmer før du kjører koden.