# Oppgåve: Lag stein, saks og papir. La spelaren spele mot datamaskina

'''
Tips:

La spelet gå heilt til spelaren eller datamaskina har 3 "wins":
while poengSpelar < 3 and poengDatamaskin < 3:
...

valMaskin  = random.choice(["stein", "saks", "papir"])

'''

import random

# Sjølve spelet -- tips til å kome i gang med ein litt meir avansert løysning
poengSpelar = 0
poengDatamaskin = 0
uavgjort = 0

print(f"""
-------------------------------
Velkommen til stein-saks-papir!
Forklar reglar...
--------------------------------
""")

while poengSpelar < 3 and poengDatamaskin < 3:
    valSpelar = input("Stein, saks eller papir? ").lower()
    valMaskin  = random.choice(["stein", "saks", "papir"])

    # Valider brukaren sin input
    while valSpelar not in ["stein", "saks", "papir"]:
        print("Ugyldig val. Forsøk på ny.")
        valSpelar = input("Stein, saks eller papir? ").lower()
    
    if valSpelar == valMaskin:
        uavgjort += 1
        resultat = "Uavgjort!"
    elif (valSpelar == "stein" and valMaskin == "saks") or \
         (valSpelar == "saks" and valMaskin == "papir") or \
         (valSpelar == "papir" and valMaskin == "stein"):
        poengSpelar += 1
        resultat = "Du vann!"
    else:
        poengDatamaskin += 1
        resultat = "Datamaskina vann!"

    print(f"Du valte {valSpelar}, datamaskina valte {valMaskin}. {resultat}")
    print(f"Stilling: Spiller {poengSpelar} - Datamaskin {poengDatamaskin} - Uavgjort {uavgjort}\n")

print(f"""...
-------------------------------
Spelet er over! {resultat}
Endeleg stilling: Spelar {poengSpelar} - Datamaskin {poengDatamaskin} - Uavgjort {uavgjort}
-------------------------------
""")

# Til seinare (les: du treng ikkje studere dette før seinare kapittel)
# Definer vinnende kombinasjoner
# vinnande_kombinasjoner = {
#     "stein": "saks",
#     "saks": "papir",
#     "papir": "stein"
# }

# if valSpelar == valMaskin:
#     uavgjort += 1
#     resultat = "Uavgjort!"
# elif vinnande_kombinasjoner[valSpelar] == valMaskin:
#     poengSpelar += 1
#     resultat = "Du vann!"
# else:
#     poengDatamaskin += 1
#     resultat = "Datamaskina vann!"