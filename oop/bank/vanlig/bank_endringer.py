"""
Del 1b: Banksystemet etter endringsrunden
Nye krav: transaksjonshistorikk og sparekonto (maks 3 uttak, renter).

Legg merke til hvor mange steder vi må sjekke kunde["type"],
og at en kunde-dictionary ser forskjellig ut avhengig av typen.
"""

import json
from pathlib import Path

FILSTI = Path(__file__).resolve().parent.joinpath("kunder_endringer.json")

RENTE = 0.02
MAKS_UTTAK_SPAREKONTO = 3


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
    print(f"{kunde['navn']} har {kunde['saldo']} kr på {kunde['type']} {kontonummer}.")
    if kunde["type"] == "sparekonto":  # ENDRET: typesjekk
        print(f"Uttak igjen: {MAKS_UTTAK_SPAREKONTO - kunde['uttak']}")


def sett_inn(kunder, kontonummer, belop):
    if belop <= 0:
        print("Beløpet må være større enn 0.")
        return
    kunder[kontonummer]["saldo"] += belop
    kunder[kontonummer]["historikk"].append(f"Innskudd: {belop} kr")  # ENDRET
    print(f"Satte inn {belop} kr.")
    vis_saldo(kunder, kontonummer)


def ta_ut(kunder, kontonummer, belop):
    kunde = kunder[kontonummer]
    if belop <= 0:
        print("Beløpet må være større enn 0.")
        return False
    if belop > kunde["saldo"]:
        print("Det er ikke nok penger på kontoen.")
        return False
    # ENDRET: typesjekk
    if kunde["type"] == "sparekonto" and kunde["uttak"] >= MAKS_UTTAK_SPAREKONTO:
        print("Du har brukt opp uttakene på sparekontoen.")
        return False
    kunde["saldo"] -= belop
    kunde["historikk"].append(f"Uttak: {belop} kr")  # ENDRET
    if kunde["type"] == "sparekonto":  # ENDRET: typesjekk igjen
        kunde["uttak"] += 1
    print(f"Tok ut {belop} kr.")
    vis_saldo(kunder, kontonummer)
    return True


def overfor(kunder, fra_konto, til_konto, belop):
    # Uendret, fordi den gjenbruker ta_ut() og sett_inn()
    if ta_ut(kunder, fra_konto, belop):
        sett_inn(kunder, til_konto, belop)


def opprett_kunde(kunder, navn, kontotype):
    kontonummer = str(1001 + len(kunder))
    # ENDRET: hva en kunde består av, avhenger av typen
    kunde = {"navn": navn, "saldo": 0, "type": kontotype, "historikk": []}
    if kontotype == "sparekonto":  # ENDRET: typesjekk
        kunde["uttak"] = 0
    kunder[kontonummer] = kunde
    print(f"Opprettet {kontotype} {kontonummer} for {navn}.")


def vis_alle_kunder(kunder):
    for kontonummer in kunder:
        vis_saldo(kunder, kontonummer)


def vis_historikk(kunder, kontonummer):  # NY
    for linje in kunder[kontonummer]["historikk"]:
        print(linje)


def legg_til_renter(kunder):  # NY
    for kunde in kunder.values():
        if kunde["type"] == "sparekonto":  # typesjekk
            renter = round(kunde["saldo"] * RENTE)
            kunde["saldo"] += renter
            kunde["historikk"].append(f"Renter: {renter} kr")
            kunde["uttak"] = 0
    print("Renter er lagt til på alle sparekontoer.")


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


def les_kontotype():  # NY
    while True:
        svar = input("Kontotype (1: brukskonto, 2: sparekonto): ")
        if svar == "1":
            return "brukskonto"
        if svar == "2":
            return "sparekonto"
        print("Ugyldig valg.")


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
        print("7: Vis historikk")
        print("8: Legg til renter")
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
            opprett_kunde(kunder, navn, les_kontotype())
            lagre_data(kunder)

        elif valg == "6":
            vis_alle_kunder(kunder)

        elif valg == "7":
            kontonummer = les_kontonummer(kunder)
            if kontonummer:
                vis_historikk(kunder, kontonummer)

        elif valg == "8":
            legg_til_renter(kunder)
            lagre_data(kunder)

        elif valg == "0":
            print("Ha en fin dag!")
            break

        else:
            print("Ugyldig valg.")


meny()
