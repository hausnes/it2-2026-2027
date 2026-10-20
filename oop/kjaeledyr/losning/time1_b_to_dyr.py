"""
Time 1, del B: To kjæledyr med vanlige variabler
Slik ser det typisk ut når vi bygger videre på del A.
Legg merke til hvor mye som må dupliseres!
"""

navn1 = "Fido"
sult1 = 5
energi1 = 5
glede1 = 5

navn2 = "Pusur"
sult2 = 5
energi2 = 5
glede2 = 5


def begrens(verdi):
    return max(0, min(10, verdi))


def vis_status(navn, sult, energi, glede):
    # Denne fungerer for begge, men vi må sende inn ALLE verdiene hver gang
    print(f"{navn}: sult {sult}, energi {energi}, glede {glede}")
    if sult >= 8:
        print(f"{navn} er sulten!")
    if energi <= 2:
        print(f"{navn} er trøtt!")


def mate(hvilket):
    global sult1, glede1, sult2, glede2
    if hvilket == "1":
        sult1 = begrens(sult1 - 3)
        glede1 = begrens(glede1 + 1)
        print(f"Du ga {navn1} mat.")
    else:
        sult2 = begrens(sult2 - 3)
        glede2 = begrens(glede2 + 1)
        print(f"Du ga {navn2} mat.")


def leke(hvilket):
    global sult1, energi1, glede1, sult2, energi2, glede2
    if hvilket == "1":
        if energi1 < 2:
            print(f"{navn1} er for trøtt til å leke.")
            return
        glede1 = begrens(glede1 + 3)
        energi1 = begrens(energi1 - 2)
        sult1 = begrens(sult1 + 1)
        print(f"Du lekte med {navn1}.")
    else:
        if energi2 < 2:
            print(f"{navn2} er for trøtt til å leke.")
            return
        glede2 = begrens(glede2 + 3)
        energi2 = begrens(energi2 - 2)
        sult2 = begrens(sult2 + 1)
        print(f"Du lekte med {navn2}.")


def sove(hvilket):
    global sult1, energi1, sult2, energi2
    if hvilket == "1":
        energi1 = begrens(energi1 + 4)
        sult1 = begrens(sult1 + 1)
        print(f"{navn1} sov godt.")
    else:
        energi2 = begrens(energi2 + 4)
        sult2 = begrens(sult2 + 1)
        print(f"{navn2} sov godt.")


def tiden_gaar():
    # Tiden går for ALLE dyrene
    global sult1, glede1, sult2, glede2
    sult1 = begrens(sult1 + 1)
    glede1 = begrens(glede1 - 1)
    sult2 = begrens(sult2 + 1)
    glede2 = begrens(glede2 - 1)


while True:
    print()
    vis_status(navn1, sult1, energi1, glede1)
    vis_status(navn2, sult2, energi2, glede2)
    print("1: Mate  2: Leke  3: Sove  0: Avslutt")
    valg = input("Velg: ")

    if valg == "0":
        break
    if valg not in ["1", "2", "3"]:
        print("Ugyldig valg.")
        continue

    hvilket = input(f"Hvilket dyr? (1: {navn1}, 2: {navn2}): ")
    if valg == "1":
        mate(hvilket)
    elif valg == "2":
        leke(hvilket)
    elif valg == "3":
        sove(hvilket)

    tiden_gaar()
