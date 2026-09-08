const fs = require("fs");

const FILE = "aa_dataset-tickets-multi-lang-5-2-50-version.csv";

// Enkel CSV-parser (tegn for tegn) som takler feltverdier med komma,
// linjeskift og doble anforselstegn inni "...".
function parseCSV(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const c = text[i];

    if (inQuotes) {
      if (c === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i++;
        } else {
          inQuotes = false;
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
        // hopp over, \n haandterer linjeskiftet
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
