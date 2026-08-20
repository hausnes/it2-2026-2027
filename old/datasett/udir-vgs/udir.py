# Datasettet, og moglegheit for filtrering av dette, finn du her:
# https://www.udir.no/tall-og-forskning/statistikk/statistikk-videregaende-skole/ 

import pandas as pd

df = pd.read_csv('eks.csv', sep='\t', encoding="utf-16")
# print(df.info())

unik_fagkode = df.value_counts("Vurderingsfagkode")
print(f"De ulike fagkodane er:\n {unik_fagkode}")

# Skriv ut fagkodene som ei liste
print("\nDei ulike fagkodane er:")
for fagkode, antall in unik_fagkode.items():
    print(f"- {fagkode}: {antall}")

# -------------------

# Fjern eventuelle rader der snittkarakteren er '*'
df = df[df['2023-24.Standpunkt.Alle eierformer.Alle kjønn.Snittkarakter'] != '*']

# Erstatt komma med punktum i snittkarakter-kolonna
df['2023-24.Standpunkt.Alle eierformer.Alle kjønn.Snittkarakter'] = df['2023-24.Standpunkt.Alle eierformer.Alle kjønn.Snittkarakter'].str.replace(',', '.')

# Konverter snittkarakter-kolonna til numerisk datatype
df['2023-24.Standpunkt.Alle eierformer.Alle kjønn.Snittkarakter'] = pd.to_numeric(
    df['2023-24.Standpunkt.Alle eierformer.Alle kjønn.Snittkarakter']
)

# Berekn gjennomsnitteleg snittkarakter for kvart fag
snittkarakter_per_fag = df.groupby('Vurderingsfagkode')['2023-24.Standpunkt.Alle eierformer.Alle kjønn.Snittkarakter'].mean()

# Skriv ut resultata
print("Gjennomsnitteleg snittkarakter for kvart fag:")
for fagkode, snitt in snittkarakter_per_fag.items():
    print(f"- {fagkode}: {snitt:.2f}")