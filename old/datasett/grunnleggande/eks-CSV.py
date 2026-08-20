'''
Kjelde: Aunivers, IT2
https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/3b-reelle-datasett/lese-og-bruke-csv-filer

NB: Ikkje bruk av OOP, Pandas eller andre bibliotek enn matplotlib for enkel oppteikning.
'''

import csv
import matplotlib.pyplot as plt # pip install matplotlib
from matplotlib.ticker import ScalarFormatter

filnavn = "data/befolkning_1951_2022.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil: # sig handterer mellom anna æ, ø og å
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
        aarstall.append(int(rad[0]))
        befolkning.append(int(rad[1]))

# Tegner grafen
plt.plot(aarstall, befolkning) # Utgangspunkt i listene, x- og y-akse
plt.grid()

# ALTERNATIVT: Bruk ScalarFormatter for å vise reelle tall på y-aksen (iike vitenskapelig notasjon, eks. 1e6)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.get_major_formatter().set_scientific(False)

plt.show()