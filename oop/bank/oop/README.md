# Del 2: Fra funksjoner til objekter

Forrige time laget vi en bank med dictionaries og funksjoner, og bygde inn bankens nye ønsker i [endringsrunden](../vanlig/endringsrunde.md) (se løsningsforslagene [bank.py](../vanlig/bank.py) og [bank_endringer.py](../vanlig/bank_endringer.py)). Den fungerer, men nå skal vi se på hva som ble tungvint, og hvordan **objektorientert programmering (OOP)** kan hjelpe oss.

---

## 1. Diskusjon: Hva var tungvint?

Ta fram tabellen fra endringsrunden. Diskuter to og to, og deretter i klassen:

1. Hvor mange ganger skrev du `kunder[kontonummer]["saldo"]` eller noe lignende?
2. Hva skjer om du skriver `"Saldo"` eller `"sado"` i stedet for `"saldo"`? Når oppdager du feilen?
3. Hvor mange funksjoner måtte få `kunder` (og `kontonummer`) som parameter?
4. Hvilke funksjoner måtte du endre for historikken? Og for sparekontoen?
5. Hvor mange steder sjekker du om en konto er en sparekonto? Hva skjer når banken vil ha en tredje kontotype?
6. En sparekonto har nøkkelen `"uttak"`, en brukskonto har den ikke. Hvor i koden står det? Hvordan skal en ny programmerer på teamet vite det?
7. Hva hindrer noen i å skrive `kunder["1001"]["saldo"] = 1000000` et sted i koden, forbi alle reglene?

<details>
<summary>👩‍🏫 Typiske svar (for læreren)</summary>

- **Mye gjentakelse:** `kunder[kontonummer]["saldo"]` overalt. Lang og lite lesbar kode.
- **Skrivefeil oppdages sent:** En feil nøkkel gir `KeyError` først når akkurat den linjen kjøres. VS Code kan ikke hjelpe, fordi det bare er tekst.
- **Alt må sendes rundt:** Nesten alle funksjoner trenger `kunder` *og* `kontonummer`. Dataene og funksjonene som jobber med dem ligger hver for seg.
- **Historikken:** `opprett_kunde`, `sett_inn`, `ta_ut`, ny funksjon, menyen — og startdataene/JSON-fila. Gamle kunder uten `"historikk"` gir `KeyError`.
- **Sparekontoen er den store smerten:** `if kunde["type"] == "sparekonto"` dukker opp i `vis_saldo`, `ta_ut` (to ganger!), `opprett_kunde` og `legg_til_renter`. En ny kontotype betyr å lete opp og endre alle disse stedene.
- **Ingen tydelig "mal":** Det står ingen steder hva en kunde *er*. Svaret er «det kommer an på typen», og det ser man bare ved å lese `opprett_kunde` eller JSON-fila.
- **Ingen beskyttelse:** Reglene ligger i funksjonene, men ingenting tvinger oss til å bruke dem. Ærlig svar: Python-klasser hindrer det ikke *helt* heller, men vi kan gjøre det tydelig hva som er internt (se steg 2).

**Kjernen:** Data (saldo, navn) og oppførsel (sett inn, ta ut) hører sammen, men i del 1 lever de hver for seg. OOP samler dem — og lar oss samle alt som er spesielt for én *type* konto på ett sted.

</details>

---

## 2. Nye begreper

| Begrep | Forklaring | I banken vår |
|---|---|---|
| **Klasse** | En mal/oppskrift som beskriver hva noe *er* og hva det *kan gjøre* | `Konto` |
| **Objekt** | Én konkret ting laget fra klassen | Olas konto, Karis konto |
| **Attributt** | En variabel som hører til objektet | `navn`, `kontonummer`, `_saldo` |
| **Metode** | En funksjon som hører til objektet | `sett_inn()`, `ta_ut()` |
| **`__init__`** | Spesiell metode som kjøres når et nytt objekt lages | Gir kontoen navn og startsaldo |
| **`self`** | "Meg selv" — objektet metoden jobber med | `self._saldo` = *denne* kontoens saldo |

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
| `kunder[kontonummer]["saldo"] += belop` | `self._saldo += belop` |
| `sett_inn(kunder, "1001", 500)` | `ola.sett_inn(500)` |

Legg merke til at vi ikke lenger trenger å sende med `kunder` og `kontonummer`. Kontoen *vet* hvem den er gjennom `self`. Når vi skriver `ola.sett_inn(500)`, sender Python automatisk `ola` inn som `self`.

**Hvorfor `_saldo` med understrek?** I Python betyr en understrek foran et navn: *«dette er internt — ikke rør det utenfor klassen»*. Saldoen skal bare endres gjennom `sett_inn()` og `ta_ut()`, slik at reglene alltid følges. Python stopper deg ikke om du skriver `ola._saldo = 1000000`, men alle som leser koden ser at det er juks. Med en dictionary finnes det ingen slik måte å skille mellom «offentlig» og «internt».

✏️ **Prøv selv:** Lag kontoer for Ola og Kari. Sett inn, ta ut og overfør penger mellom dem. Prøv å ta ut mer enn det som står på kontoen.

### Steg 3: En Bank-klasse — [steg3_bank.py](steg3_bank.py)

Nå har vi én klasse for **én konto**. Men vi trenger også noe som holder styr på **alle** kontoene. Det blir klassen `Bank`, som har en attributt `self.kontoer`: en dictionary fra kontonummer til `Konto`-objekt.

Se hvordan menyen har blitt enklere:

```python
konto = bank.finn_konto(input("Kontonummer: "))
if konto:
    konto.sett_inn(les_belop())
```

Foreløpig lagrer vi ingenting til fil. Det venter vi med til steg 5.

---

## 4. Utfordring: Transaksjonshistorikk

Husker du ønske 1 fra endringsrunden? Nå skal du legge til historikk i OOP-versjonen og sammenligne med det du gjorde i del 1.

Lag en kopi av `steg3_bank.py` og gjør dette:

1. Gi `Konto` en ny attributt `historikk`, som er en liste.
2. La `sett_inn()` og `ta_ut()` legge til en linje i historikken, f.eks. `"Innskudd: 500 kr"`.
3. Lag en metode `vis_historikk()`.
4. Legg til et menyvalg for å vise historikken.

<details>
<summary>💡 Løsningsforslag (endringene i Konto)</summary>

```python
class Konto:
    def __init__(self, kontonummer, navn, saldo=0):
        self.kontonummer = kontonummer
        self.navn = navn
        self._saldo = saldo
        self.historikk = []

    def sett_inn(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        self._saldo += belop
        self.historikk.append(f"Innskudd: {belop} kr")
        print(f"Satte inn {belop} kr.")

    def ta_ut(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return False
        if belop > self._saldo:
            print("Det er ikke nok penger på kontoen.")
            return False
        self._saldo -= belop
        self.historikk.append(f"Uttak: {belop} kr")
        print(f"Tok ut {belop} kr.")
        return True

    def vis_historikk(self):
        for linje in self.historikk:
            print(linje)
```

</details>

**Sammenlign ærlig:** Antall endringer er omtrent det samme som i del 1. Forskjellen er *hvor* de er: Alt utenom menyen skjedde inne i `Konto`-klassen. I del 1 måtte du også huske `opprett_kunde`, startdataene og eventuelt JSON-fila — alle stedene der en kunde-dictionary *lages*. Her lages alle kontoer av `__init__`, så historikken kommer automatisk med på alle kontoer, også nye.

---

## 5. Steg 4: Sparekonto med arv — [steg4_sparekonto.py](steg4_sparekonto.py)

Det var ønske 2 som virkelig gjorde vondt i del 1: `if kunde["type"] == "sparekonto"` spredt rundt i koden. OOP har et verktøy for akkurat dette: **arv**.

En sparekonto *er* en konto — den kan alt en konto kan — men med noen ekstra regler. Da lager vi en ny klasse som **arver** fra `Konto`:

```python
class Sparekonto(Konto):  # Sparekonto arver alt fra Konto
    MAKS_UTTAK = 3

    def __init__(self, kontonummer, navn, saldo=0):
        super().__init__(kontonummer, navn, saldo)  # Kjør __init__ fra Konto først
        self.uttak = 0

    def ta_ut(self, belop):
        if self.uttak >= self.MAKS_UTTAK:
            print("Du har brukt opp uttakene på sparekontoen.")
            return False
        if super().ta_ut(belop):  # La Konto gjøre resten
            self.uttak += 1
            return True
        return False
```

| Begrep | Forklaring |
|---|---|
| **Arv** | `class Sparekonto(Konto)` betyr at `Sparekonto` får alle attributtene og metodene til `Konto` |
| **Overstyring** | `Sparekonto` lager sin egen versjon av `ta_ut()`, som brukes i stedet for den i `Konto` |
| **`super()`** | Kaller metoden i klassen vi arver fra, slik at vi slipper å skrive den på nytt |

Se hvordan banken legger til renter — **uten en eneste typesjekk**:

```python
def legg_til_renter(self):
    for konto in self.kontoer.values():
        konto.legg_til_renter()
```

Hver konto vet selv hva den skal gjøre: `Sparekonto.legg_til_renter()` gir 2 % rente, mens `Konto.legg_til_renter()` ikke gjør noe. `sett_inn()`, `overfor_til()` og `vis_historikk()` måtte ikke endres i det hele tatt.

✏️ **Prøv selv:** Banken vil ha en **BSU-konto**: 5 % rente, og ingen uttak i det hele tatt. Lag klassen `BSU`. Hvor mange steder i koden måtte du endre? Sammenlign med hvor mye du måtte endret i del 1.

---

## 6. Steg 5: Objekter og JSON — [steg5_json.py](steg5_json.py)

Til slutt vil vi at dataene skal lagres mellom hver gang programmet kjører. I del 1 var dette nesten gratis, fordi en dictionary kan lagres rett i JSON. Med objekter er det litt mer jobb.

**Problemet:** JSON kan bare lagre tekst, tall, lister og dictionaries — ikke våre egne objekter. Vi må derfor "pakke ut" objektet til en dictionary før vi lagrer, og "pakke det inn" igjen når vi leser.

```
kunder.json  --json.load-->  dictionary  --Konto(...)-->   Konto-objekter
kunder.json  <--json.dump--  dictionary  <--til_dict()--   Konto-objekter
```

- Hver klasse får en metode `til_dict()`. `Sparekonto` bruker `super().til_dict()` og legger bare til det som er spesielt for den.
- `Bank.les_fra_fil()` leser JSON-fila og lager riktig type objekt. Her *må* vi sjekke kontotypen — men det er det **eneste** stedet i hele programmet.
- `__init__` har fått parametere for `historikk` og `uttak`, slik at vi kan gjenskape kontoene akkurat slik de var.

Hvorfor `historikk=None` og ikke `historikk=[]`? Se "Obs!" om standardparametere i [funksjoner-intro](../../../grunnleggande-python/14-funksjonar-intro.md).

✏️ **Prøv selv:** Kjør programmet, gjør noen endringer, avslutt og start på nytt. Er endringene lagret? Åpne `kunder.json` og se hvordan objektene ser ut som dictionaries.

---

## 7. Oppsummering

| | Del 1: Funksjoner og dictionaries | Del 2: OOP |
|---|---|---|
| Hente data | `kunder["1001"]["navn"]` | `konto.navn` |
| Sette inn | `sett_inn(kunder, "1001", 500)` | `konto.sett_inn(500)` |
| Hva er en kunde? | Må lese `opprett_kunde` eller JSON-fila | Står i `__init__` |
| Skrivefeil i navn | Oppdages når programmet krasjer | VS Code sier fra med en gang |
| Ny funksjonalitet (historikk) | Endringer spredt i funksjoner og data | Endringer samlet i klassen |
| Ny kontotype | Nye `if type == ...` mange steder | Ny klasse som arver |
| Beskytte saldoen | Ingen måte å signalisere det på | `_saldo` + metoder |
| Lese/skrive JSON | Enkelt — dictionaryen lagres direkte | Mer jobb — må gjøre om til/fra objekter |

OOP er ikke alltid enklere å *skrive* — men det blir enklere å *forstå, endre og utvide* koden etter hvert som programmet vokser.
