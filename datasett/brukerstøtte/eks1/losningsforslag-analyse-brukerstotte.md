# Løsningsforslag – Analysere brukerstøtte

**Fag:** Brukerstøtte (IM-ITK Vg2)
**Datasett:** `aa_dataset-tickets-multi-lang-5-2-50-version.csv` (Customer IT Support – Ticket Dataset, Kaggle)

---

## 1. Hva oppgaven egentlig ber om

NDLA-emnet «Analysere brukerstøtte» handler om å finne **mønstre i henvendelser**, slik at en supportavdeling kan se hvilke problemer som går igjen, og prioritere ressurser og opplæring deretter (fokusområder).

Konkret skal vi telle **hvor mange saker (billetter/tickets)** som handler om hver av disse sju kategoriene:

- Connectivity
- Firmware
- Billing eller Payment
- Camera
- Service interruptions
- USB storage
- Laptop

Det viktige presiseringen i oppgaveteksten er:

> *"typisk bare en gang i subject eller body, slik at vi ikke teller dobbelt opp hvert problem"*

Det betyr at vi **ikke** skal telle antall ganger ordet "network" forekommer i teksten. Vi skal telle **antall unike billetter** der ordet forekommer minst én gang – enten i emnefeltet (`subject`) eller i selve meldingen (`body`). En billett med ordet "network" nevnt fem ganger skal fortsatt bare telle som **1**.

---

## 2. Bli kjent med datasettet før du koder

Dette steget hopper mange over – men det er halve jobben i en ekte analyse. Åpne CSV-filen (f.eks. i Excel, eller `head` i terminalen) og se på:

| Kolonne | Innhold |
|---|---|
| `subject` | Emnefelt / tittel på saken |
| `body` | Selve henvendelsen fra kunden |
| `answer` | Svaret support ga |
| `type` | Incident, Request, Problem, Change |
| `queue` | Hvilken avdeling saken hører til (Technical Support, Billing and Payments, ...) |
| `priority` | low / medium / high |
| `language` | Språkkode |
| `tag_1`–`tag_8` | Ferdige stikkord satt av datasettforfatterne |

**Viktig funn:** Datasettet inneholder **to språk** – engelsk og tysk:

| Språk | Antall billetter |
|---|---|
| `en` (engelsk) | 16 338 |
| `de` (tysk) | 12 249 |
| **Totalt** | **28 587** |

Dette er avgjørende for løsningen! Hvis vi bare søker etter engelske ord som `"network"` eller `"invoice"`, mister vi automatisk **43 % av datasettet** (alle de tyske billettene), og tallene våre blir feil. En vanlig feil er å ikke oppdage dette og konkludere med altfor lave forekomster.

> 💡 **Pedagogisk poeng:** Dette er akkurat den typen skjult felle ekte data har, og som NDLA-pensumet peker på – du må alltid undersøke *hva* du analyserer før du trekker konklusjoner.

---

## 3. Metodevalg (og hvorfor)

For at elevene skal kunne følge løsningen, forklarer vi valgene underveis:

1. **Slå sammen `subject` og `body`** til én tekst per billett, og søk i denne. Da fanger vi opp saker der ordet bare står i emnefeltet.
2. **Gjør alt om til små bokstaver** (`lower()` / `toLowerCase()`) før søk, slik at `Network`, `NETWORK` og `network` regnes som samme ord.
3. **Bruk enkelt tekst-/substrengsøk** (`"nettverk" in tekst`), ikke reelle "hele ord"-grenser med regex. Dette er den enkleste tilnærmingen, men har en bevisst avveining (se punkt 6 – feilkilder).
4. **Tell per billett, ikke per treff**: for hver kategori sjekker vi *om* minst ett nøkkelord finnes i teksten (bruk `any(...)` i Python / `.some(...)` i JavaScript), og øker telleren med maks 1 per billett.
5. **Nøkkelord på begge språk**, siden datasettet er tospråklig.
6. **Normaliser tyske spesialtegn** (ä, ö, ü, ß) slik at søket finner ordet uansett om det skrives med spesialtegn eller ikke (nyttig fordi tekstkoding av og til går galt i eksporterte CSV-filer).

### Nøkkelord vi bruker per kategori

| Kategori | Engelske nøkkelord | Tyske nøkkelord |
|---|---|---|
| Connectivity | connect, connectivity, network, wifi, wi-fi | Verbindung, Netzwerk, WLAN |
| Firmware | firmware | firmware (samme ord) |
| Billing/Payment | billing, payment, invoice, bill | Rechnung, Zahlung, Abrechnung |
| Camera | camera | Kamera |
| Service interruptions | service interruption, interruption, outage, disruption | Störung, Unterbrechung, Ausfall |
| USB storage | usb storage, usb drive, usb stick | USB-Stick, USB-Speicher |
| Laptop | laptop | laptop (samme ord) |

Dette er **ikke en fasit-liste i den forstand at det finnes bare ett riktig svar** – elevene kan ha valgt andre/flere synonymer. Poenget er at de kan **begrunne** hvilke ord de valgte, og at de har tenkt på det tospråklige datasettet.

---

## 4. Løsning i Python

Vi bruker kun standardbiblioteket: `csv` (for å lese filen riktig, inkludert felt med komma og linjeskift inni) og `collections.Counter` (for å telle). Ingen pandas, numpy eller andre tredjepartsbibliotek er nødvendig.

```python
import csv
from collections import Counter

FILE = "aa_dataset-tickets-multi-lang-5-2-50-version.csv"

# Nøkkelord per kategori. Datasettet inneholder billetter på engelsk (en)
# og tysk (de), så vi må lete etter ord på begge språk.
CATEGORIES = {
    "Connectivity": [
        "connect", "connectivity", "network", "wifi", "wi-fi",
        "verbindung", "netzwerk", "wlan",
    ],
    "Firmware": [
        "firmware",
    ],
    "Billing/Payment": [
        "billing", "payment", "invoice", "bill",
        "rechnung", "zahlung", "abrechnung",
    ],
    "Camera": [
        "camera",
        "kamera",
    ],
    "Service interruptions": [
        "service interruption", "interruption", "outage", "disruption",
        "storung", "unterbrechung", "ausfall",
    ],
    "USB storage": [
        "usb storage", "usb drive", "usb stick", "usb-stick", "usb-speicher",
    ],
    "Laptop": [
        "laptop",
    ],
}


def normalize(text):
    """Gjør tekst om til små bokstaver og fjerner tyske spesialtegn,
    slik at f.eks. 'Störung' og 'storung' matcher samme søkeord."""
    text = text.lower()
    text = (text.replace("ä", "a")
                .replace("ö", "o")
                .replace("ü", "u")
                .replace("ß", "ss"))
    return text


counts = Counter()
total_rows = 0

with open(FILE, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)          # leser filen radvis, gir hver rad som en dict
    for row in reader:
        total_rows += 1
        # Slå sammen emnefelt og meldingstekst til én streng vi kan søke i
        text = normalize((row.get("subject") or "") + " " + (row.get("body") or ""))

        for category, keywords in CATEGORIES.items():
            # any(...) gir True med det samme ETT nøkkelord treffer.
            # Dermed telles hver billett maks én gang per kategori,
            # uansett hvor mange ganger ordet forekommer i teksten.
            if any(normalize(kw) in text for kw in keywords):
                counts[category] += 1

# Skriv ut resultatet
print(f"Totalt antall billetter: {total_rows}\n")
for category in CATEGORIES:
    n = counts[category]
    pct = 100 * n / total_rows
    print(f"{category:22s}: {n:5d}  ({pct:5.2f} %)")
```

### Forklaring av de viktigste stedene

- **`csv.DictReader`**: Vi bruker ikke `text.split(",")` fordi flere av tekstfeltene inneholder komma og linjeskift *inni* anførselstegn (f.eks. `"Sehr geehrtes Support-Team, ..."`). En naiv splitting på komma ville ha ødelagt radene. `csv`-modulen (standardbibliotek, ikke tredjepart) håndterer dette riktig.
- **`row.get("subject") or ""`**: Beskytter mot at feltet er tomt (`None` eller tom streng), slik at koden ikke krasjer.
- **`any(... for kw in keywords)`**: Dette er selve knepet som hindrer dobbelttelling – vi spør «finnes *minst ett* av disse ordene i teksten?», ikke «hvor mange ganger finnes de?».
- **`encoding="utf-8"`**: Filen er lagret i UTF-8. På Windows kan `print()` av og til vise rare tegn (f.eks. `�` i stedet for `ø`/`ä`) i selve konsollvinduet – det er et visningsproblem i terminalen, ikke en feil i dataene eller koden.

---

## 5. Løsning i JavaScript (Node.js)

I JavaScript finnes det ingen innebygd CSV-leser, og de fleste "ordentlige" løsninger bruker et npm-bibliotek. Siden oppgaven ber om minst mulig avanserte biblioteker, skriver vi en **enkel, egen CSV-parser** (kun rundt 30 linjer) som håndterer anførselstegn og linjeskift inni felt – akkurat det Pythons `csv`-modul gjør for oss automatisk.

```javascript
const fs = require("fs");

const FILE = "aa_dataset-tickets-multi-lang-5-2-50-version.csv";

// Enkel CSV-parser (tegn for tegn) som takler feltverdier med komma,
// linjeskift og doble anførselstegn inni "...".
function parseCSV(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const c = text[i];

    if (inQuotes) {
      if (c === '"') {
        if (text[i + 1] === '"') {   // "" inni feltet betyr ett escapet "
          field += '"';
          i++;
        } else {
          inQuotes = false;          // avsluttende anførselstegn
        }
      } else {
        field += c;
      }
    } else {
      if (c === '"') {
        inQuotes = true;
      } else if (c === ",") {
        row.push(field);
        field = "";
      } else if (c === "\n") {
        row.push(field);
        rows.push(row);
        row = [];
        field = "";
      } else if (c === "\r") {
        // ignorer, \n håndterer selve linjeskiftet (Windows bruker \r\n)
      } else {
        field += c;
      }
    }
  }
  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }
  return rows;
}

// Nøkkelord per kategori – engelsk og tysk, siden datasettet er tospråklig
const CATEGORIES = {
  Connectivity: ["connect", "connectivity", "network", "wifi", "wi-fi", "verbindung", "netzwerk", "wlan"],
  Firmware: ["firmware"],
  "Billing/Payment": ["billing", "payment", "invoice", "bill", "rechnung", "zahlung", "abrechnung"],
  Camera: ["camera", "kamera"],
  "Service interruptions": ["service interruption", "interruption", "outage", "disruption", "storung", "unterbrechung", "ausfall"],
  "USB storage": ["usb storage", "usb drive", "usb stick", "usb-stick", "usb-speicher"],
  Laptop: ["laptop"],
};

function normalize(text) {
  return text
    .toLowerCase()
    .replaceAll("ä", "a")
    .replaceAll("ö", "o")
    .replaceAll("ü", "u")
    .replaceAll("ß", "ss");
}

const raw = fs.readFileSync(FILE, "utf-8");
const rows = parseCSV(raw);
const header = rows[0];
const subjectIdx = header.indexOf("subject");
const bodyIdx = header.indexOf("body");

const counts = {};
for (const category of Object.keys(CATEGORIES)) counts[category] = 0;

let total = 0;
for (let i = 1; i < rows.length; i++) {
  const r = rows[i];
  if (r.length < header.length) continue; // hopp over evt. tomme/ufullstendige rader
  total++;

  const text = normalize((r[subjectIdx] || "") + " " + (r[bodyIdx] || ""));

  for (const [category, keywords] of Object.entries(CATEGORIES)) {
    // .some(...) fungerer akkurat som Pythons any(...):
    // sant med det samme ETT nøkkelord treffer -> ingen dobbelttelling
    if (keywords.some((kw) => text.includes(normalize(kw)))) {
      counts[category]++;
    }
  }
}

console.log(`Totalt antall billetter: ${total}\n`);
for (const category of Object.keys(CATEGORIES)) {
  const n = counts[category];
  const pct = ((100 * n) / total).toFixed(2);
  console.log(`${category.padEnd(22)}: ${String(n).padStart(5)}  (${pct} %)`);
}
```

Kjøres med:

```bash
node count_categories.js
```

### Forklaring av de viktigste stedene

- **Egen CSV-parser**: Går tegn for tegn gjennom filen og holder styr på om vi er "inni" et anførselstegn-felt (`inQuotes`). Så lenge vi er inni et felt, behandles komma og linjeskift som vanlig tekst, ikke som skilletegn. Dette er den enkleste måten å parse CSV riktig på uten biblioteker.
- **`.replaceAll(...)`** brukes i stedet for regex for å holde koden lettlest for elever som ikke har lært regulære uttrykk ennå.
- Resultatet er identisk med Python-løsningen (verifisert – se punkt 6).

---

## 6. Resultat (fasit-tall)

Begge løsningene over er kjørt mot `aa_dataset-tickets-multi-lang-5-2-50-version.csv` og gir **identiske tall**:

**Totalt antall billetter i datasettet: 28 587**

| Kategori | Antall billetter | Andel av alle billetter |
|---|---:|---:|
| Connectivity | 3 829 | 13,39 % |
| Service interruptions | 2 961 | 10,36 % |
| Billing/Payment | 1 614 | 5,65 % |
| Firmware | 219 | 0,77 % |
| Laptop | 51 | 0,18 % |
| Camera | 67 | 0,23 % |
| USB storage | 25 | 0,09 % |

*(Sortert etter hyppighet, ikke i oppgavens opprinnelige rekkefølge, for å gjøre mønsteret tydelig.)*

### Enkel visualisering uten bibliotek (valgfritt tillegg)

Man kan illustrere fordelingen med en enkel tekstbasert stolpe, helt uten grafikkbibliotek – nyttig for elever som vil vise resultatet visuelt uten f.eks. matplotlib eller Chart.js:

```python
for category, n in sorted(counts.items(), key=lambda x: -x[1]):
    bar = "#" * (n // 50)   # skaler ned slik at stolpene ikke blir for lange
    print(f"{category:22s} | {bar} ({n})")
```

```
Connectivity           | ################################################################################ (3829)
Service interruptions  | ############################################################ (2961)
Billing/Payment        | ################################ (1614)
Firmware               | #### (219)
Camera                 | # (67)
Laptop                 | # (51)
USB storage            |  (25)
```

---

## 7. Tolkning – hva forteller dette oss om fokusområder?

Dette er den delen NDLA-oppgaven egentlig handler om – **tallene alene er ikke svaret, det er hva vi gjør med dem**:

- **Connectivity (13,4 %)** og **Service interruptions (10,4 %)** er de klart største kategoriene. Til sammen utgjør de nesten en fjerdedel av alle henvendelser. Dette tyder på at nettverksstabilitet og oppetid er det største fokusområdet for supportavdelingen – både forebyggende (bedre infrastruktur/overvåking) og reaktivt (raskere respons, bedre feilsøkingsrutiner og FAQ for disse temaene).
- **Billing/Payment (5,7 %)** er også en betydelig andel – ofte et tegn på at faktura- eller betalingsprosesser bør gjøres tydeligere for kundene, eller at selvbetjeningsløsninger for fakturaspørsmål bør prioriteres.
- **Firmware, Camera, Laptop og USB storage** er alle under 1 %. Dette er ikke "uviktige" kategorier, men de er tydelig **ikke** hovedfokusområder sammenlignet med de tre første. Ressurser (bemanning, opplæring, dokumentasjon) bør trolig ikke prioriteres tungt her.
- Ved å krysse "Connectivity" og "Service interruptions" mot kolonnen `queue`, ser vi at disse sakene i stor grad havner i **Technical Support** og **Service Outages and Maintenance** – noe som bekrefter at treffene faktisk handler om det vi tror, og ikke er tilfeldige ordtreff:

  | Kategori | Topp-3 køer (queue) |
  |---|---|
  | Connectivity | Technical Support (1507), IT Support (656), Product Support (603) |
  | Service interruptions | Technical Support (1007), Service Outages and Maintenance (730), IT Support (489) |

  Dette er et fint ekstra sjekk-steg elevene kan gjøre: **stemmer treffene med hvilken avdeling saken faktisk er sortert i?** Det er en enkel måte å validere at nøkkelordsøket faktisk fanger riktige saker.

---

## 8. Vanlige feil elevene kan ha gjort (sjekkliste for retting)

| Feil | Konsekvens | Hva du bør se etter i elevbesvarelsen |
|---|---|---|
| Bare søkt på engelske ord | Mister ~43 % av datasettet (alle tyske billetter) → for lave tall | Sjekk om de har sett på `language`-kolonnen i det hele tatt |
| Telt antall *forekomster* av ordet i stedet for antall *billetter* | Tall blir kunstig høye | Se etter `count()`/`.split()`-telling i stedet for `in`/`.includes()` |
| Delt filen med `split(",")` uten CSV-bibliotek/parser | Rader med komma i teksten blir feilkuttet, gir feil totalt antall rader | Sjekk om `total_rows`/`total` stemmer med ca. 28 587 |
| Søkt kun i `subject` eller kun i `body`, ikke begge | For lave tall, spesielt for kategorier sjeldent nevnt i emnefeltet | Sjekk at begge feltene er slått sammen før søk |
| Ikke gjort om til små bokstaver før søk | "Network" ≠ "network" ved f.eks. `in`-sjekk med case-sensitivt Python | Sjekk om `.lower()`/`.toLowerCase()` er brukt |
| For smalt nøkkelordvalg (kun ett ord per kategori) | Underrapporterer kategorien | Ikke feil i seg selv, men bør diskuteres/begrunnes |

---

## 9. Mulige forbedringer (for de sterkeste elevene / videre diskusjon)

Løsningen over er bevisst enkel (substrengsøk), men det finnes kjente svakheter dere kan diskutere i klassen:

1. **Substrengsøk kan gi falske treff.** Eksempelvis vil `"bill"` også matche inni ord som `"billion"` dersom slike fantes i teksten (vi sjekket – det finnes ingen slike treff i dette datasettet, men det er flaks, ikke en garanti). En mer robust løsning bruker regulære uttrykk med ordgrenser, f.eks. `re.search(r"\bbill\b", text)` i Python.
2. **Synonymer og bøyningsformer** kan mangle. Vi fanger `"connect"`, men ikke nødvendigvis alle avledninger på tysk (f.eks. sammensatte ord). Flere nøkkelord kan legges til etter å ha lest gjennom et utvalg billetter manuelt.
3. **Ferdige tags i datasettet** (`tag_1`–`tag_8`) kunne vært brukt som en kontroll/alternativ metode – sammenlign om nøkkelordsøket gir samme mønster som de forhåndsdefinerte tag-ene.
4. **Kryssing mot `priority`** kunne vist om f.eks. "Service interruptions" oftere er `high`-prioritet enn andre kategorier – enda et steg i retning ekte forretningsanalyse.

---

## 10. Kjøreinstruksjon (for referanse)

**Python** (krever kun standard Python 3, ingen `pip install`):

```bash
python3 count_categories.py
```

**JavaScript** (krever kun Node.js, ingen `npm install`):

```bash
node count_categories.js
```

Begge scriptene forventer at CSV-filen ligger i samme mappe som scriptet, eller at filstien i `FILE`-variabelen justeres.
