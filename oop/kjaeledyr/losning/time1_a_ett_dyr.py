"""
Time 1, del A: Ett kjæledyr med vanlige variabler
"""

navn = "Fido"
sult = 5
energi = 5
glede = 5


def begrens(verdi):
    # Holder verdien mellom 0 og 10
    return max(0, min(10, verdi))


def vis_status():
    print(f"\n{navn}: sult {sult}, energi {energi}, glede {glede}")
    if sult >= 8:
        print(f"{navn} er sulten!")
    if energi <= 2:
        print(f"{navn} er trøtt!")


def mate():
    global sult, glede
    sult = begrens(sult - 3)
    glede = begrens(glede + 1)
    print(f"Du ga {navn} mat.")


def leke():
    global sult, energi, glede
    if energi < 2:
        print(f"{navn} er for trøtt til å leke.")
        return
    glede = begrens(glede + 3)
    energi = begrens(energi - 2)
    sult = begrens(sult + 1)
    print(f"Du lekte med {navn}.")


def sove():
    global sult, energi
    energi = begrens(energi + 4)
    sult = begrens(sult + 1)
    print(f"{navn} sov godt.")


def tiden_gaar():
    global sult, glede
    sult = begrens(sult + 1)
    glede = begrens(glede - 1)


while True:
    vis_status()
    print("1: Mate  2: Leke  3: Sove  0: Avslutt")
    valg = input("Velg: ")

    if valg == "1":
        mate()
    elif valg == "2":
        leke()
    elif valg == "3":
        sove()
    elif valg == "0":
        break
    else:
        print("Ugyldig valg.")
        continue

    tiden_gaar()
