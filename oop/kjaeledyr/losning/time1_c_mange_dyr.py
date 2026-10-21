"""
Time 1, del C: Så mange kjæledyr du vil, med en liste av dictionaries
Mye bedre enn del B! Men:
- Alt er tekst-nøkler: dyr["slut"] gir KeyError først når linjen kjøres.
- Hva et dyr består av, står bare i nytt_dyr() (og må stemme med startlista).
- Dataene (dictionaryen) og funksjonene som jobber med dem, ligger hver for seg.
"""


def begrens(verdi):
    return max(0, min(10, verdi))


def nytt_dyr(navn):
    return {"navn": navn, "sult": 5, "energi": 5, "glede": 5}


def vis_status(dyr):
    print(f"{dyr['navn']}: sult {dyr['sult']}, energi {dyr['energi']}, glede {dyr['glede']}")
    if dyr["sult"] >= 8:
        print(f"{dyr['navn']} er sulten!")
    if dyr["energi"] <= 2:
        print(f"{dyr['navn']} er trøtt!")


def mate(dyr):
    dyr["sult"] = begrens(dyr["sult"] - 3)
    dyr["glede"] = begrens(dyr["glede"] + 1)
    print(f"Du ga {dyr['navn']} mat.")


def leke(dyr):
    if dyr["energi"] < 2:
        print(f"{dyr['navn']} er for trøtt til å leke.")
        return
    dyr["glede"] = begrens(dyr["glede"] + 3)
    dyr["energi"] = begrens(dyr["energi"] - 2)
    dyr["sult"] = begrens(dyr["sult"] + 1)
    print(f"Du lekte med {dyr['navn']}.")


def sove(dyr):
    dyr["energi"] = begrens(dyr["energi"] + 4)
    dyr["sult"] = begrens(dyr["sult"] + 1)
    print(f"{dyr['navn']} sov godt.")


def tiden_gaar(dyr):
    dyr["sult"] = begrens(dyr["sult"] + 1)
    dyr["glede"] = begrens(dyr["glede"] - 1)


def velg_dyr(dyrene):
    for i, dyr in enumerate(dyrene):
        print(f"{i + 1}: {dyr['navn']}")
    try:
        return dyrene[int(input("Hvilket dyr? ")) - 1]
    except (ValueError, IndexError):
        print("Ugyldig dyr.")
        return None


dyrene = [
    nytt_dyr("Fido"), 
    nytt_dyr("Pusur")
]

while True:
    print()
    for dyr in dyrene:
        vis_status(dyr)
    print("1: Mate  2: Leke  3: Sove  4: Adopter nytt dyr  0: Avslutt")
    valg = input("Velg: ")

    if valg == "0":
        break
    elif valg == "4":
        dyrene.append(nytt_dyr(input("Navn på det nye dyret: ")))
    elif valg in ["1", "2", "3"]:
        dyr = velg_dyr(dyrene)
        if dyr is None:
            continue
        if valg == "1":
            mate(dyr)
        elif valg == "2":
            leke(dyr)
        elif valg == "3":
            sove(dyr)
    else:
        print("Ugyldig valg.")
        continue

    for dyr in dyrene:
        tiden_gaar(dyr)
