import pandas as pd
import matplotlib.pyplot as plt

file_path = 'sikkerheit_utf8.csv'
# df = pd.read_csv(file_path, delimiter=';', skipinitialspace=True, encoding='windows-1252')
df = pd.read_csv(file_path, delimiter=';', skipinitialspace=True)

# Litt innleiande uttesting
# print(df.head())
# print()
# print(df.info())
# print()
# print(df.describe())
# print()
# print("--------------------------------------------")

# 1: -	Kva for tre (3) protokollar («Protocol») er brukt oftast i datasettet, og kor mange gonger blir desse brukt (forekomst)?
protocol_counts = df['Protocol'].value_counts().head(3)
print("De tre vanligste protokollene:")
print(protocol_counts)

# 2: 
#   - Finn ut, og skriv ut, kor mange ulike typar «Attack Type» det er.
#   - Finn ut, og skriv ut, kor stor prosentandel «DDoS» utgjer av totalen.
#   - Lag ein graf/visualisering som viser fordelinga av dei ulike typane «Attack Type».

print()
unique_attack_types = df['Attack Type'].nunique()
print(f"Antall ulike typer 'Attack Type': {unique_attack_types}")
unique_alt = df['Attack Type'].value_counts()
print(unique_alt)

# Kor mykje utgjer DDoS
ddos_count = df[df['Attack Type'] == 'DDoS'].shape[0]
print(f"ddos_count = {ddos_count}")
total_attacks = df.shape[0]
print(f"total_attacks = {total_attacks}")
'''
Om shape i koden over:
DataFramen ddos_count inneheld rader med DDoS som angrepstype.
shape er ein eigenskap i Pandas som gjer dimensjonane til ein dataframe, 
og den returnerer ein tuple i formatet (antall_rader, antall_kolonner)
shape[0] hentar det første elementet i tuplen, som er antall rader i den
filtrerte DataFrame.
'''
ddos_percentage = (ddos_count / total_attacks) * 100
print(f"'DDoS' utgjør {ddos_percentage:.2f}% av totalen.")

attack_type_counts = df['Attack Type'].value_counts()
attack_type_counts.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Fordeling av ulike typer "Attack Type"')
plt.xlabel('Attack Type')
plt.ylabel('Antall forekomster')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3: - Finn ut kva type operativsystem som blir angripe oftast, av «Macintosh» og «Windows», og visualiser dette.

# Filtrer rader som inneholder "Macintosh" eller "Windows" i kolonnen "Device Information"
# Alternativ 1, kort, effektivt, elegant .. og lite logisk før du har sett det?
macintosh_count = df['Device Information'].str.contains('Macintosh', na=False).sum()
windows_count = df['Device Information'].str.contains('Windows', na=False).sum()

# Alternativ 2: Steg-for-steg..
# Sjå fila sikkerheit-vanilla.py

# Skriv ut resultata
print()
print(f"Antall angrep på Macintosh: {macintosh_count}")
print(f"Antall angrep på Windows: {windows_count}")

# Visualiser resultata
# Alternativ 1, "vanilla" Python
# os_counts = {'Macintosh': macintosh_count, 'Windows': windows_count}
# plt.bar(os_counts.keys(), os_counts.values(), color=['blue', 'green'])
# Alternativ 2, Pandas series
'''
pd.Series er ein funksjon frå Pandas-biblioteket som lagar ein éin-dimensjonal datastruktur (liknar på ei liste eller dictionary).
{'Macintosh': macintosh_count, 'Windows': windows_count} er ei Python-dictionary der nøklane er navna på operativsystema 
('Macintosh' og 'Windows'), og verdiane (macintosh_count og windows_count) representerer antall angrep på kvart operativsystem.
Resultatet er ein "Series" der nøklane i dictionaryen blir indeksane, og verdiane blir data i Series.
'''
os_counts = pd.Series({'Macintosh': macintosh_count, 'Windows': windows_count})
os_counts.plot(kind='bar', color=['blue', 'green'], figsize=(8, 5))
plt.title('Antall angrep per operativsystem')
plt.xlabel('Operativsystem')
plt.ylabel('Antall angrep')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()