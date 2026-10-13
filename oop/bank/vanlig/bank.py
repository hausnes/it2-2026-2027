"""
Del 1: Banksystem med "vanlig" Python
Data: dictionary i dictionary, lagret i kunder.json
Logikk: funksjoner som får kunde-dictionaryen som parameter
"""

import json
from pathlib import Path

# Finn kunder.json i samme mappe som denne Python-fila
FILSTI = Path(__file__).resolve().parent.joinpath("kunder.json")


# ---------- Lese og skrive JSON ----------

def les_data():
    with open(FILSTI, encoding="utf-8") as fil:
        return json.load(fil)


def lagre_data(kunder):
    with open(FILSTI, "w", encoding="utf-8") as fil:
        json.dump(kunder, fil, indent=4, ensure_ascii=False)


# ---------- Bankoperasjoner ----------

def vis_saldo(kunder, kontonummer):
    kunde = kunder[kontonummer]
    print(f"{kunde['navn']} har {kunde['saldo']} kr på konto {kontonummer}.")


def sett_inn(kunder, kontonummer, belop):
    if belop <= 0:
        print("Beløpet må være større enn 0.")
        return
    kunder[kontonummer]["saldo"] += belop
    print(f"Satte inn {belop} kr.")
    vis_saldo(kunder, kontonummer)


def ta_ut(kunder, kontonummer, belop):
    if belop <= 0:
        print("Beløpet må være større enn 0.")
        return
    if belop > kunder[kontonummer]["saldo"]:
        print("Det er ikke nok penger på kontoen.")
        return
    kunder[kontonummer]["saldo"] -= belop
    print(f"Tok ut {belop} kr.")
    vis_saldo(kunder, kontonummer)


def overfor(kunder, fra_konto, til_konto, belop):
    if belop <= 0:
        print("Beløpet må være større enn 0.")
        return
    if belop > kunder[fra_konto]["saldo"]:
        print("Det er ikke nok penger på kontoen.")
        return
    kunder[fra_konto]["saldo"] -= belop
    kunder[til_konto]["saldo"] += belop
    print(f"Overførte {belop} kr fra {fra_konto} til {til_konto}.")


def opprett_kunde(kunder, navn):
    # Enkel måte å lage et nytt, unikt kontonummer på (så lenge ingen slettes)
    kontonummer = str(1001 + len(kunder))
    kunder[kontonummer] = {"navn": navn, "saldo": 0}
    print(f"Opprettet konto {kontonummer} for {navn}.")


def vis_alle_kunder(kunder):
    for kontonummer in kunder:
        vis_saldo(kunder, kontonummer)


# ---------- Hjelpefunksjoner for input ----------

def les_kontonummer(kunder):
    kontonummer = input("Kontonummer: ")
    if kontonummer not in kunder:
        print("Fant ingen konto med det kontonummeret.")
        return None
    return kontonummer


def les_belop():
    try:
        return int(input("Beløp: "))
    except ValueError:
        print("Du må skrive et heltall.")
        return 0


# ---------- Hovedprogram ----------

def meny():
    kunder = les_data()

    while True:
        print("\n--- BANKEN ---")
        print("1: Vis saldo")
        print("2: Sett inn penger")
        print("3: Ta ut penger")
        print("4: Overfør penger")
        print("5: Opprett ny kunde")
        print("6: Vis alle kunder")
        print("0: Avslutt")
        valg = input("Velg: ")

        if valg == "1":
            kontonummer = les_kontonummer(kunder)
            if kontonummer:
                vis_saldo(kunder, kontonummer)

        elif valg == "2":
            kontonummer = les_kontonummer(kunder)
            if kontonummer:
                sett_inn(kunder, kontonummer, les_belop())
                lagre_data(kunder)

        elif valg == "3":
            kontonummer = les_kontonummer(kunder)
            if kontonummer:
                ta_ut(kunder, kontonummer, les_belop())
                lagre_data(kunder)

        elif valg == "4":
            print("Fra konto:")
            fra_konto = les_kontonummer(kunder)
            print("Til konto:")
            til_konto = les_kontonummer(kunder)
            if fra_konto and til_konto:
                overfor(kunder, fra_konto, til_konto, les_belop())
                lagre_data(kunder)

        elif valg == "5":
            navn = input("Navn på ny kunde: ")
            opprett_kunde(kunder, navn)
            lagre_data(kunder)

        elif valg == "6":
            vis_alle_kunder(kunder)

        elif valg == "0":
            print("Ha en fin dag!")
            break

        else:
            print("Ugyldig valg.")


meny()
