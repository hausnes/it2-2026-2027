import csv
import matplotlib.pyplot as plt

filnavn = "data/befolkning_1951_2022.csv"

# Ordbok for å lagre årstall og befolkningsstørrelser
data = {}

with open(filnavn, encoding="utf-8-sig") as fil:  # sig håndterer blant annet æ, ø og å
    filinnhold = csv.DictReader(fil, delimiter=";")

    # Iterer gjennom radene og hent data
    for rad in filinnhold:
        år = int(rad["Årstall"])  # Bruk kolonnenavnet som nøkkel
        befolkning = int(rad["Befolkning 1. januar"])  # Bruk kolonnenavnet som nøkkel
        data[år] = befolkning

# print(data)

# Konverter ordboken til to lister
aarstall = list(data.keys())
befolkning = list(data.values())

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.xlabel("År")
plt.ylabel("Befolkning")
plt.title("Befolkning i Norge 1951-2022")
plt.grid()
plt.show()