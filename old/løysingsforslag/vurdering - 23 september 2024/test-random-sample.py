# Ein kjapp test for å leike litt med konseptet om å hente ut tilfeldige element frå ei ordbok/dictionary.

fakta = {
    "Norway" : {
        "capital" : "Oslo",
        "population" : 5378857,
        "neighbors" : ["Sweden", "Finland", "Russia"]
    },
    "Sweden" : {
        "capital" : "Stockholm",
        "population" : 10099265,
        "neighbors" : ["Norway", "Finland"]
    },
    "Finland" : {
        "capital" : "Helsinki",
        "population" : 5540720,
        "neighbors" : ["Sweden", "Norway", "Russia"]
    },
    "Russia" : {
        "capital" : "Moscow",
        "population" : 144526636,
        "neighbors" : ["Finland", "Norway"]
    }
}

import random

land_liste = list(fakta.keys())

tilfeldige_land = random.sample(land_liste, 3)

print(tilfeldige_land)

# Velg eit tilfeldig spørsmål for kvart land
sporsmal_liste = []
for land in tilfeldige_land:
    nøkkel = random.choice(list(fakta[land].keys()))
    sporsmal_liste.append((land, nøkkel, fakta[land][nøkkel]))

# Skriv ut spørsmåla
for land, nøkkel, verdi in sporsmal_liste:
    print(f"Land: {land}, Spørsmål: {nøkkel}, Svar: {verdi}")