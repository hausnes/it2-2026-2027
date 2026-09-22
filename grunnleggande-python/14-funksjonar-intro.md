# Undervisningsopplegg: Enkelt om funksjoner i Python

## Introduksjon
Her får du en oversikt over funksjoner i Python — det viktigste du bør vite, forklart med eksempler.

## Hva er en funksjon?
En funksjon er en blokk med kode som utfører en spesifikk oppgave. Funksjoner hjelper oss blant annet med å:

- **organisere** koden i mindre, forståelige biter
- **gjenbruke** kode, i stedet for å skrive den samme logikken flere ganger (DRY — *Don't Repeat Yourself*)
- **teste** koden lettere, siden en funksjon kan prøves ut isolert fra resten av programmet

En funksjon defineres med `def`, et navn, parenteser (som eventuelt inneholder parametere) og et kolon. Selve kodeblokken er innrykket under, akkurat som med `if`-setninger og løkker.

## Funksjoner uten parametere
En funksjon uten parametere tar ingen argumenter når den kalles.

```python
def hei_verden():
    print("Hei, verden!")

# Kalle funksjonen
hei_verden()
```

## Funksjoner med parametere
En funksjon med parametere tar ett eller flere argumenter når den kalles.

```python
def hei_namn(namn):
    print(f"Hei, {namn}!")

# Kalle funksjonen med et argument
hei_namn("Ola")
```

## Funksjoner med standardparametere
En funksjon med standardparametere har en forhåndsbestemt verdi for parameteren. Denne verdien brukes dersom du ikke oppgir noe annet når du kaller funksjonen.

```python
def hei_namn(namn="verden"):
    print(f"Hei, {namn}!")

# Kalle funksjonen med et argument
hei_namn("Ola") # Output: Hei, Ola!
# Kalle funksjonen uten argument
hei_namn()  # Output: Hei, verden!
```

**Obs!** Standardverdien regnes ut bare **én gang**, idet funksjonen defineres. Bruker du en liste eller dictionary som standardverdi, deler alle kallene samme objekt — noe som lett gir overraskende feil:

```python
def legg_til(element, liste=[]):  # FARLIG: samme liste gjenbrukes ved hvert kall
    liste.append(element)
    return liste

print(legg_til("a"))  # ['a']
print(legg_til("b"))  # ['a', 'b']  <- uventet! Listen fra forrige kall henger igjen
```

Den trygge løsningen er å bruke `None` som standardverdi, og heller opprette listen inni funksjonen:

```python
def legg_til(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

print(legg_til("a"))  # ['a']
print(legg_til("b"))  # ['b']  <- riktig, egen liste hver gang
```

## Posisjonelle argumenter og nøkkelordargumenter
Til nå har vi kalt funksjoner med argumenter i samme rekkefølge som parameterne er definert i — dette kalles **posisjonelle argumenter**. Du kan i stedet oppgi hvilken parameter du mener ved å bruke navnet dens, kalt **nøkkelordargumenter**. Da spiller ikke rekkefølgen noen rolle:

```python
def presenter(namn, alder):
    print(f"{namn} er {alder} år.")

presenter("Kari", 17)             # posisjonelt: namn="Kari", alder=17
presenter(alder=17, namn="Kari")  # nøkkelord: rekkefølgen betyr ikke noe her
```

## Funksjoner med flere parametere
En funksjon kan også ta flere argumenter.

```python
def legg_saman(a, b):
    return a + b
    print("Denne linjen kjører ikke!") # ..fordi return avslutter funksjonen

# Kalle funksjonen med to argumenter
resultat = legg_saman(3, 5)
print(resultat)  # Output: 8
```

## Arbitrære argumenter (*args og **kwargs)
En funksjon kan ta et ukjent antall argumenter ved hjelp av `*args` og `**kwargs`. `*args` samler ekstra **posisjonelle** argumenter i en tuple:

```python
def legg_saman(*args):
    return sum(args)

# Kalle funksjonen med flere argumenter
resultat = legg_saman(1, 2, 3, 4)
print(resultat)  # Output: 10
```

`**kwargs` samler på tilsvarende måte ekstra **nøkkelordargumenter** i en dictionary:

```python
def skriv_profil(**kwargs):
    for nokkel, verdi in kwargs.items():
        print(f"{nokkel}: {verdi}")

skriv_profil(navn="Ola", alder=17, klasse="3IM1")
# navn: Ola
# alder: 17
# klasse: 3IM1
```

Navnene `args` og `kwargs` er bare konvensjon — det er stjernene (`*` og `**`) som gjør jobben. Du kan i prinsippet kalle dem hva du vil, men det er lurt å følge konvensjonen slik at andre kjenner den igjen.

## Funksjoner med lister som parametere
Funksjoner kan også ta lister som argumenter.

```python
def summer_liste(tal_liste):
    return sum(tal_liste)

# Kalle funksjonen med en liste som argument
resultat = summer_liste([1, 2, 3, 4, 5])
print(resultat)  # Output: 15
```

## Flere returverdier
En funksjon kan returnere flere verdier samtidig, atskilt med komma. Python pakker dem faktisk sammen til en tuple, som du kan pakke ut igjen i flere variabler når du kaller funksjonen:

```python
def min_og_max(tal_liste):
    return min(tal_liste), max(tal_liste)

minste, storste = min_og_max([4, 8, 1, 9, 3])
print(minste, storste)  # 1 9

# Det som egentlig skjer:
resultat = min_og_max([4, 8, 1, 9, 3])
print(resultat)  # (1, 9)  <- en tuple med to verdier
```

## Funksjoner uten return
En funksjon trenger ikke alltid å returnere en verdi.

```python
def skriv_ut_liste(tal_liste):
    for tal in tal_liste:
        print(tal)

# Kalle funksjonen med en liste som argument
skriv_ut_liste([1, 2, 3, 4, 5])
```

Mangler funksjonen et `return`, returnerer den automatisk `None`:

```python
def skriv_hei():
    print("Hei!")

resultat = skriv_hei()  # Output: Hei!
print(resultat)         # Output: None
```

## Lokale og globale variabler (scope)
En variabel som defineres *inne i* en funksjon, kalles en **lokal variabel** — den finnes bare mens funksjonen kjører, og er ikke synlig utenfor. En variabel som defineres *utenfor* alle funksjoner, kalles en **global variabel**, og kan *leses* fra hvor som helst i filen:

```python
x = 10  # global variabel

def vis_x():
    print(x)  # kan lese globale variabler

vis_x()   # 10
```

Prøver du derimot å *tilordne* (`=`) en variabel inne i en funksjon, oppretter Python en **ny, lokal** variabel med samme navn — den globale variabelen blir ikke endret:

```python
def endre_x():
    x = 20  # dette er en NY, lokal variabel x
    print(x)  # 20

endre_x()
print(x)  # 10 - fortsatt uendret
```

Ønsker du å faktisk endre den globale variabelen inne i en funksjon, må du si ifra med nøkkelordet `global`:

```python
def endre_x_globalt():
    global x
    x = 20

endre_x_globalt()
print(x)  # 20 - nå endret
```

**Obs!** Det regnes som god praksis å unngå `global` der du kan. Send heller inn verdier som parametere, og ta dem ut igjen som returverdier — det gjør koden lettere å forstå og å teste.

## Rekursjon
En funksjon kan kalle seg selv. Dette kalles rekursjon. En rekursiv funksjon må alltid ha et **basistilfelle** (en betingelse som stopper rekursjonen) — ellers kaller funksjonen seg selv i det uendelige, og du får en feilmelding (`RecursionError`).

```python
def fak(n):
    if n == 0:      # basistilfelle
        return 1
    else:
        return n * fak(n-1)  # rekursivt steg

# Kalle funksjonen
print(fak(5))  # Output: 120
```

Et annet eksempel, en nedtelling:

```python
def nedtelling(n):
    if n == 0:          # basistilfelle
        print("Nå!")
    else:
        print(n)
        nedtelling(n - 1)  # rekursivt steg

nedtelling(3)
# 3
# 2
# 1
# Nå!
```

## Dokumentasjonsstrenger
Dokumentasjonsstrenger (docstrings) brukes til å dokumentere funksjoner.

```python
def hei_namn(namn):
    """
    Denne funksjonen skriver ut en hilsen til det gitte navnet.
    
    Parametre:
    namn (str): Navnet som skal hilses.
    """
    print(f"Hei, {namn}!")

# Kalle funksjonen
hei_namn("Ola")
```

I VS Code vil docstringen automatisk dukke opp som et tips når du holder musepekeren over funksjonsnavnet, eller mens du skriver et kall til funksjonen. Du kan også hente den fram i kode med `help(hei_namn)`.

## Type hints for funksjoner (bonus)
Du kan spesifisere hvilke typer en funksjon forventer og returnerer, med **type hints**. Dette er forklart i detalj i [typer.md](typer.md), men kort oppsummert:

```python
def hils(namn: str) -> str:
    return f"Hei, {namn}!"

print(hils("Ola"))
```

`namn: str` sier at parameteren skal være en streng, og `-> str` sier at funksjonen returnerer en streng. Dette sjekkes ikke automatisk når koden kjører, men verktøy som VS Code (Pylance) og mypy vil varsle deg dersom du bruker feil type.

## Oppsummering

| Mønster | Syntaks | Forklaring |
|---|---|---|
| Uten parametere | `def navn():` | Tar ingen argumenter |
| Med parametere | `def navn(param):` | Tar ett eller flere argumenter |
| Standardverdi | `def navn(param=verdi):` | Brukes hvis argumentet uteblir ved kall |
| Nøkkelordargument ved kall | `funksjon(param=verdi)` | Rekkefølgen på argumentene spiller ikke noen rolle |
| Vilkårlig antall posisjonsargumenter | `def navn(*args):` | `args` blir en tuple inne i funksjonen |
| Vilkårlig antall nøkkelordargumenter | `def navn(**kwargs):` | `kwargs` blir en dictionary inne i funksjonen |
| Returverdi | `return verdi` | Avslutter funksjonen og sender verdien tilbake |
| Flere returverdier | `return a, b` | Pakkes ut ved kall: `x, y = funksjon()` |
| Ingen return | (ingenting, eller `return` alene) | Funksjonen returnerer `None` |
| Lokal variabel | Definert inne i funksjonen | Finnes bare mens funksjonen kjører |
| Global variabel | Definert utenfor alle funksjoner | Kan leses overalt, men krever `global` for å endres inne i en funksjon |
| Rekursjon | Funksjonen kaller seg selv | Må ha et basistilfelle som stopper kallene |

## Øvingsoppgaver

**Vanskegrad:** ⭐ enkel · ⭐⭐ middels · ⭐⭐⭐ utfordring

### Oppgave 1 ⭐
Lag en funksjon `si_hei()` uten parametere, som skriver ut `"Hei og velkommen!"`.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def si_hei():
    print("Hei og velkommen!")

si_hei()
```

</details>

### Oppgave 2 ⭐
Lag en funksjon `kvadrat(tall)` som returnerer tallet opphøyd i andre potens.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def kvadrat(tall):
    return tall ** 2

print(kvadrat(4))  # 16
```

</details>

### Oppgave 3 ⭐
Lag en funksjon `hils(navn, tittel="elev")` med en standardparameter. Funksjonen skal skrive ut f.eks. `"Hei, elev Kari!"`. Kall den både med og uten `tittel`-argumentet.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def hils(navn, tittel="elev"):
    print(f"Hei, {tittel} {navn}!")

hils("Kari")              # Hei, elev Kari!
hils("Nordahl", "lærer")  # Hei, lærer Nordahl!
```

</details>

### Oppgave 4 ⭐⭐
Lag en funksjon som tar en streng som parameter og returnerer en ny streng der alle vokalene er fjernet.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def fjern_vokaler(tekst):
    vokaler = "aeiouyæøå"
    ny_tekst = ""
    for bokstav in tekst:
        if bokstav.lower() not in vokaler:
            ny_tekst += bokstav
    return ny_tekst

print(fjern_vokaler("Hei, verden!"))  # H, vrdn!
```

</details>

### Oppgave 5 ⭐⭐
Lag en funksjon som tar en streng som parameter og returnerer `True` hvis strengen er et palindrom, ellers `False`.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def er_palindrom(tekst):
    tekst = tekst.lower().replace(" ", "")
    return tekst == tekst[::-1]

print(er_palindrom("anna"))    # True
print(er_palindrom("Python"))  # False
```

</details>

### Oppgave 6 ⭐⭐
Lag en funksjon som tar en liste av tall som parameter og returnerer en ny liste der alle negative tall er fjernet.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def fjern_negative(tal_liste):
    ny_liste = []
    for tall in tal_liste:
        if tall >= 0:
            ny_liste.append(tall)
    return ny_liste

print(fjern_negative([3, -2, 5, -8, 0, 1]))  # [3, 5, 0, 1]
```

Alternativ løsning med list comprehension:

```python
def fjern_negative(tal_liste):
    return [tall for tall in tal_liste if tall >= 0]
```

</details>

### Oppgave 7 ⭐⭐
Lag en funksjon `produkt(*tall)` som bruker `*args` til å multiplisere sammen et vilkårlig antall tall, og returnerer resultatet.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def produkt(*tall):
    resultat = 1
    for t in tall:
        resultat *= t
    return resultat

print(produkt(2, 3, 4))  # 24
```

</details>

### Oppgave 8 ⭐⭐
Lag en funksjon `skriv_profil(**info)` som bruker `**kwargs` til å skrive ut alle nøkkel-verdi-parene du sender inn, på formen `nøkkel: verdi`.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def skriv_profil(**info):
    for nokkel, verdi in info.items():
        print(f"{nokkel}: {verdi}")

skriv_profil(navn="Ola", alder=17, klasse="3IM1")
```

</details>

### Oppgave 9 ⭐⭐
Lag en funksjon `min_og_max(tal_liste)` som returnerer både det minste og det største tallet i en liste (to returverdier). Pakk ut resultatet i to variabler når du kaller funksjonen.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def min_og_max(tal_liste):
    return min(tal_liste), max(tal_liste)

minste, storste = min_og_max([4, 8, 1, 9, 3])
print(minste, storste)  # 1 9
```

</details>

### Oppgave 10 ⭐⭐⭐
Se på koden under. Hva tror du skjer når den kjøres?

```python
teller = 0

def oke_teller():
    teller = teller + 1
    return teller

print(oke_teller())
```

Kjør koden og se om du hadde rett. Forklar deretter *hvorfor* det skjer, og rett opp funksjonen slik at den fungerer som forventet (økes med 1 for hvert kall), ved hjelp av `global`.

<details>
<summary>💡 Løsningsforslag</summary>

Koden gir en feilmelding av typen `UnboundLocalError` (den nøyaktige teksten varierer litt mellom Python-versjoner, men den sier i praksis at `teller` brukes før den har fått en verdi).

**Forklaring:** Siden `teller` blir tilordnet (`=`) inne i funksjonen, antar Python at `teller` er en *lokal* variabel i hele funksjonskroppen — også på høyresiden av `=`, altså før den i det hele tatt er satt en verdi. Dermed prøver Python å lese en lokal variabel som ennå ikke finnes.

**Rettet versjon:**

```python
teller = 0

def oke_teller():
    global teller
    teller = teller + 1
    return teller

print(oke_teller())  # 1
print(oke_teller())  # 2
```

</details>

### Oppgave 11 ⭐⭐⭐
Lag en **rekursiv** funksjon `summer_til(n)` som regner ut summen av alle heltall fra 1 til og med `n`, uten å bruke en løkke, `sum()` eller `range()`.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def summer_til(n):
    if n <= 0:              # basistilfelle
        return 0
    else:
        return n + summer_til(n - 1)  # rekursivt steg

print(summer_til(5))  # 15  (1+2+3+4+5)
```

</details>

### Oppgave 12 ⭐⭐⭐
Lag en **rekursiv** funksjon `er_palindrom_rekursiv(tekst)` som avgjør om en streng er et palindrom, ved hjelp av rekursjon i stedet for løkke eller slicing av hele strengen på én gang.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def er_palindrom_rekursiv(tekst):
    tekst = tekst.lower().replace(" ", "")
    if len(tekst) <= 1:            # basistilfelle: 0 eller 1 bokstav er alltid palindrom
        return True
    if tekst[0] != tekst[-1]:      # første og siste bokstav må være like
        return False
    return er_palindrom_rekursiv(tekst[1:-1])  # sjekk resten, rekursivt

print(er_palindrom_rekursiv("anna"))    # True
print(er_palindrom_rekursiv("Python"))  # False
```

</details>

### Oppgave 13 ⭐⭐⭐ (Bonus)
Ta utgangspunkt i `kvadrat`-funksjonen fra oppgave 2. Bruk [typer.md](typer.md) som referanse, og legg til type hints på parameteren og returverdien.

<details>
<summary>💡 Løsningsforslag</summary>

```python
def kvadrat(tall: int) -> int:
    return tall ** 2

print(kvadrat(4))  # 16
```

</details>
