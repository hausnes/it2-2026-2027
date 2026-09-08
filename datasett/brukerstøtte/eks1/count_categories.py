import csv
from collections import Counter

FILE = "aa_dataset-tickets-multi-lang-5-2-50-version.csv"

# Nøkkelord per kategori. Datasettet inneholder billetter på engelsk (en) og tysk (de),
# så vi må lete etter ord på begge språk for å ikke miste tyske billetter.
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
        "usb storage", "usb drive", "usb stick", "usb-stick",
        "usb-speicher",
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
    reader = csv.DictReader(f)
    for row in reader:
        total_rows += 1
        text = normalize((row.get("subject") or "") + " " + (row.get("body") or ""))
        for category, keywords in CATEGORIES.items():
            if any(normalize(kw) in text for kw in keywords):
                counts[category] += 1

print(f"Totalt antall billetter: {total_rows}\n")
for category in CATEGORIES:
    n = counts[category]
    pct = 100 * n / total_rows
    print(f"{category:22s}: {n:5d}  ({pct:5.2f} %)")
