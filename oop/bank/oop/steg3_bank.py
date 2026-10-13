"""
Steg 3: En Bank-klasse som holder på alle kontoene og tar seg av JSON
- Konto: én konto (samme som i steg 2, pluss til_dict)
- Bank: har en dictionary med Konto-objekter, og kan lese/lagre fra fil
"""

import json
from pathlib import Path

FILSTI = Path(__file__).resolve().parent.joinpath("kunder.json")


class Konto:
    def __init__(self, kontonummer, navn, saldo=0):
        self.kontonummer = kontonummer
        self.navn = navn
        self.saldo = saldo

    def vis_saldo(self):
        print(f"{self.navn} har {self.saldo} kr på konto {self.kontonummer}.")

    def sett_inn(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        self.saldo += belop
        print(f"Satte inn {belop} kr.")

    def ta_ut(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        if belop > self.saldo:
            print("Det er ikke nok penger på kontoen.")
            return
        self.saldo -= belop
        print(f"Tok ut {belop} kr.")

    def overfor_til(self, annen_konto, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        if belop > self.saldo:
            print("Det er ikke nok penger på kontoen.")
            return
        self.ta_ut(belop)
        annen_konto.sett_inn(belop)

    def til_dict(self):
        # JSON kan ikke lagre objekter direkte, så vi gjør kontoen om til en dictionary
        return {"navn": self.navn, "saldo": self.saldo}


class Bank:
    def __init__(self, filsti):
        self.filsti = filsti
        self.kontoer = {}  # kontonummer -> Konto-objekt
        self.les_fra_fil()

    def les_fra_fil(self):
        with open(self.filsti, encoding="utf-8") as fil:
            data = json.load(fil)
        # Gjør hver dictionary fra fila om til et Konto-objekt
        for kontonummer, info in data.items():
            self.kontoer[kontonummer] = Konto(kontonummer, info["navn"], info["saldo"])

    def lagre_til_fil(self):
        data = {}
        for kontonummer, konto in self.kontoer.items():
            data[kontonummer] = konto.til_dict()
        with open(self.filsti, "w", encoding="utf-8") as fil:
            json.dump(data, fil, indent=4, ensure_ascii=False)

    def finn_konto(self, kontonummer):
        if kontonummer not in self.kontoer:
            print("Fant ingen konto med det kontonummeret.")
            return None
        return self.kontoer[kontonummer]

    def opprett_konto(self, navn):
        kontonummer = str(1001 + len(self.kontoer))
        self.kontoer[kontonummer] = Konto(kontonummer, navn)
        print(f"Opprettet konto {kontonummer} for {navn}.")

    def vis_alle(self):
        for konto in self.kontoer.values():
            konto.vis_saldo()


# ---------- Hjelpefunksjon for input ----------

def les_belop():
    try:
        return int(input("Beløp: "))
    except ValueError:
        print("Du må skrive et heltall.")
        return 0


# ---------- Hovedprogram ----------

def meny():
    bank = Bank(FILSTI)

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
            konto = bank.finn_konto(input("Kontonummer: "))
            if konto:
                konto.vis_saldo()

        elif valg == "2":
            konto = bank.finn_konto(input("Kontonummer: "))
            if konto:
                konto.sett_inn(les_belop())
                bank.lagre_til_fil()

        elif valg == "3":
            konto = bank.finn_konto(input("Kontonummer: "))
            if konto:
                konto.ta_ut(les_belop())
                bank.lagre_til_fil()

        elif valg == "4":
            fra_konto = bank.finn_konto(input("Fra kontonummer: "))
            til_konto = bank.finn_konto(input("Til kontonummer: "))
            if fra_konto and til_konto:
                fra_konto.overfor_til(til_konto, les_belop())
                bank.lagre_til_fil()

        elif valg == "5":
            bank.opprett_konto(input("Navn på ny kunde: "))
            bank.lagre_til_fil()

        elif valg == "6":
            bank.vis_alle()

        elif valg == "0":
            print("Ha en fin dag!")
            break

        else:
            print("Ugyldig valg.")


meny()
