# Del 2: Fra funksjoner til objekter

Forrige time laget vi en bank med dictionaries og funksjoner (se [løsningsforslaget i `vanlig/`](../vanlig/bank.py)). Den fungerer, men nå skal vi se på hvorfor den blir tungvint å jobbe med, og hvordan **objektorientert programmering (OOP)** kan hjelpe oss.

---

## 1. Diskusjon: Hva var tungvint?

Diskuter to og to, og deretter i klassen:

1. Hvor mange ganger skrev du `kunder[kontonummer]["saldo"]` eller noe lignende?
2. Hva skjer om du skriver `"Saldo"` eller `"sado"` i stedet for `"saldo"`? Når oppdager du feilen?
3. Hvor mange funksjoner måtte få `kunder` (og `kontonummer`) som parameter?
4. Hva hindrer noen i å skrive `kunder["1001"]["saldo"] = 1000000` et sted i koden?
5. Tenk deg at vi vil legge til **transaksjonshistorikk**. Hvilke steder i koden må endres?
6. Tenk deg at banken vokser til 50 funksjoner og 5 programmerere. Hvordan vet alle hva en "kunde" består av?

<details>
<summary>👩‍🏫 Typiske svar (for læreren)</summary>

- **Mye gjentakelse:** `kunder[kontonummer]["saldo"]` overalt. Lang og lite lesbar kode.
- **Skrivefeil oppdages sent:** En feil nøkkel gir `KeyError` først når akkurat den linjen kjøres. VS Code kan ikke hjelpe, fordi det bare er tekst.
- **Alt må sendes rundt:** Nesten alle funksjoner trenger `kunder` *og* `kontonummer`. Dataene og funksjonene som jobber med dem ligger hver for seg.
- **Ingen beskyttelse:** Reglene (ikke negativ saldo, ikke negative beløp) ligger i funksjonene, men ingenting tvinger oss til å bruke dem. Hvem som helst kan endre saldoen direkte.
- **Endringer sprer seg:** Ny informasjon om en kunde (f.eks. historikk) må legges inn i `opprett_kunde`, i JSON-fila, i `sett_inn`, i `ta_ut`, i `overfor` ...
- **Ingen tydelig "mal":** Det står ingen steder i koden hva en kunde *er*. Man må lese JSON-fila eller gjette.

**Kjernen:** Data (saldo, navn) og oppførsel (sett inn, ta ut) hører sammen, men i del 1 lever de hver for seg. OOP samler dem.

</details>

---

## 2. Nye begreper

| Begrep | Forklaring | I banken vår |
|---|---|---|
| **Klasse** | En mal/oppskrift som beskriver hva noe *er* og hva det *kan gjøre* | `Konto` |
| **Objekt** | Én konkret ting laget fra klassen | Olas konto, Karis konto |
| **Attributt** | En variabel som hører til objektet | `navn`, `saldo`, `kontonummer` |
| **Metode** | En funksjon som hører til objektet | `sett_inn()`, `ta_ut()` |
| **`__init__`** | Spesiell metode som kjøres når et nytt objekt lages | Gir kontoen navn og startsaldo |
| **`self`** | "Meg selv" — objektet metoden jobber med | `self.saldo` = *denne* kontoens saldo |

En god sammenligning: **Klassen** er tegningen av et hus. **Objektene** er husene som bygges fra tegningen. Alle husene har samme oppbygning, men hvert hus har sine egne møbler (attributter).

---

## 3. Steg for steg

Åpne og kjør filene i rekkefølge. Hvert steg bygger på det forrige.

### Steg 1: Vår første klasse — [steg1_klasse.py](steg1_klasse.py)

Vi lager en klasse `Konto` med bare `__init__` og tre attributter, og lager to objekter fra den.

```python
class Konto:
    def __init__(self, kontonummer, navn, saldo):
        self.kontonummer = kontonummer
        self.navn = navn
        self.saldo = saldo


konto1 = Konto("1001", "Ola Nordmann", 1500)
print(konto1.saldo)
```

**Sammenlign:** `kunder["1001"]["saldo"]` blir til `konto1.saldo`. Kortere, og VS Code foreslår attributtene for deg når du skriver `konto1.` — og sier fra om du skriver feil.

✏️ **Prøv selv:** Lag en tredje konto for deg selv, og skriv ut navn og saldo.

### Steg 2: Metoder — [steg2_metoder.py](steg2_metoder.py)

Nå flytter vi funksjonene fra del 1 *inn i* klassen. De blir da **metoder**.

| Del 1 (funksjon) | Del 2 (metode) |
|---|---|
| `def sett_inn(kunder, kontonummer, belop):` | `def sett_inn(self, belop):` |
| `kunder[kontonummer]["saldo"] += belop` | `self.saldo += belop` |
| `sett_inn(kunder, "1001", 500)` | `ola.sett_inn(500)` |

Legg merke til at vi ikke lenger trenger å sende med `kunder` og `kontonummer`. Kontoen *vet* hvem den er gjennom `self`. Når vi skriver `ola.sett_inn(500)`, sender Python automatisk `ola` inn som `self`.

✏️ **Prøv selv:** Lag kontoer for Ola og Kari. Sett inn, ta ut og overfør penger mellom dem. Prøv å ta ut mer enn det som står på kontoen.

### Steg 3: En Bank-klasse og JSON — [steg3_bank.py](steg3_bank.py)

Nå har vi én klasse for **én konto**. Men vi trenger også noe som holder styr på **alle** kontoene, og som leser og skriver JSON-fila. Det blir klassen `Bank`.

- `Bank` har en attributt `self.kontoer`, som er en dictionary: kontonummer → `Konto`-objekt.
- `les_fra_fil()` leser JSON (som vanlig) og gjør hver kunde om til et `Konto`-objekt.
- `lagre_til_fil()` gjør det motsatt: hvert `Konto`-objekt gjøres om til en dictionary med `til_dict()`, og så lagres alt med `json.dump()`.

**Hvorfor `til_dict()`?** JSON kan bare lagre tekst, tall, lister og dictionaries — ikke våre egne objekter. Vi må derfor "pakke ut" objektet til en dictionary før vi lagrer, og "pakke det inn" igjen når vi leser.

```
kunder.json  --json.load-->  dictionary  --Konto(...)-->   Konto-objekter
kunder.json  <--json.dump--  dictionary  <--til_dict()--   Konto-objekter
```

Se også hvordan menyen har blitt enklere:

```python
konto = bank.finn_konto(input("Kontonummer: "))
if konto:
    konto.sett_inn(les_belop())
    bank.lagre_til_fil()
```

✏️ **Prøv selv:** Kjør programmet, gjør noen endringer, avslutt og start på nytt. Er endringene lagret?

---

## 4. Utfordring: Transaksjonshistorikk

Husker du spørsmål 5 fra diskusjonen? Nå skal vi legge til historikk i OOP-versjonen og se hvor mange steder vi må endre koden.

Lag en kopi av `steg3_bank.py` og gjør dette:

1. Gi `Konto` en ny attributt `historikk`, som er en liste.
2. La `sett_inn()` og `ta_ut()` legge til en linje i historikken, f.eks. `"Innskudd: 500 kr"`.
3. Lag en metode `vis_historikk()`.
4. Husk å få med historikken i `til_dict()` og når du leser fra fil.
5. Legg til et menyvalg for å vise historikken.

<details>
<summary>💡 Løsningsforslag (endringene i Konto)</summary>

```python
class Konto:
    def __init__(self, kontonummer, navn, saldo=0, historikk=None):
        self.kontonummer = kontonummer
        self.navn = navn
        self.saldo = saldo
        if historikk is None:
            historikk = []
        self.historikk = historikk

    def sett_inn(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        self.saldo += belop
        self.historikk.append(f"Innskudd: {belop} kr")
        print(f"Satte inn {belop} kr.")

    def ta_ut(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        if belop > self.saldo:
            print("Det er ikke nok penger på kontoen.")
            return
        self.saldo -= belop
        self.historikk.append(f"Uttak: {belop} kr")
        print(f"Tok ut {belop} kr.")

    def vis_historikk(self):
        for linje in self.historikk:
            print(linje)

    def til_dict(self):
        return {"navn": self.navn, "saldo": self.saldo, "historikk": self.historikk}
```

I `Bank.les_fra_fil()` bruker vi `.get()`, slik at gamle kontoer uten historikk i fila fortsatt fungerer:

```python
self.kontoer[kontonummer] = Konto(kontonummer, info["navn"], info["saldo"], info.get("historikk"))
```

Hvorfor `historikk=None` og ikke `historikk=[]`? Se "Obs!" om standardparametere i [funksjoner-intro](../../../grunnleggande-python/14-funksjonar-intro.md).

Legg merke til at `overfor_til()` **ikke** måtte endres i det hele tatt — den bruker `ta_ut()` og `sett_inn()`, så historikken kommer med automatisk!

</details>

---

## 5. Oppsummering

| | Del 1: Funksjoner og dictionaries | Del 2: OOP |
|---|---|---|
| Hente saldo | `kunder["1001"]["saldo"]` | `konto.saldo` |
| Sette inn | `sett_inn(kunder, "1001", 500)` | `konto.sett_inn(500)` |
| Hva er en kunde? | Må lese JSON-fila eller gjette | Står i `Konto.__init__` |
| Skrivefeil i navn | Oppdages når programmet krasjer | VS Code sier fra med en gang |
| Ny funksjonalitet | Endringer mange steder | Endringer samlet i klassen |
| Lese/skrive JSON | Enkelt — dictionaryen lagres direkte | Litt mer jobb — må gjøre om til/fra objekter |

OOP er ikke alltid enklere å *skrive* — men det blir enklere å *forstå, endre og utvide* koden etter hvert som programmet vokser.
