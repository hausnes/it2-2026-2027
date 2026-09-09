// Enkel start: les CSV-filen linje for linje og tell hvor mange
// linjer som inneholder ordet "connectivity".

const fs = require("fs");

const FIL = "aa_dataset-tickets-multi-lang-5-2-50-version.csv";
const ORD = "connectivity";

const innhold = fs.readFileSync(FIL, "utf-8");
const linjer = innhold.split("\n");
console.log(`Det finnes ${linjer.length} linjer i datasettet.`);

let antall = 0;

for (const linje of linjer) {
  if (linje.toLowerCase().includes(ORD)) {
    antall++;
  }
}

console.log(`Ordet "${ORD}" ble funnet i ${antall} linjer.`);