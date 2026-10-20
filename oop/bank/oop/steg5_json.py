"""
Steg 5: Lagre objektene i en JSON-fil
JSON kan bare lagre tekst, tall, lister og dictionaries - ikke våre egne objekter.
Derfor må vi gjøre objektene om til dictionaries (til_dict) før vi lagrer,
og tilbake til objekter (Konto(...) / Sparekonto(...)) når vi leser.
"""

import json
from pathlib import Path

FILSTI = Path(__file__).resolve().parent.joinpath("kunder.json")


class Konto:
    def __init__(self, kontonummer, navn, saldo=0, historikk=None):
        self.kontonummer = kontonummer
        self.navn = navn
        self._saldo = saldo
        if historikk is None:
            historikk = []
        self.historikk = historikk

    def vis_saldo(self):
        print(f"{self.navn} har {self._saldo} kr på konto {self.kontonummer}.")

    def sett_inn(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        self._saldo += belop
        self.historikk.append(f"Innskudd: {belop} kr")
        print(f"Satte inn {belop} kr.")

    def ta_ut(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return False
        if belop > self._saldo:
            print("Det er ikke nok penger på kontoen.")
            return False
        self._saldo -= belop
        self.historikk.append(f"Uttak: {belop} kr")
        print(f"Tok ut {belop} kr.")
        return True

    def overfor_til(self, annen_konto, belop):
        if self.ta_ut(belop):
            annen_konto.sett_inn(belop)

    def vis_historikk(self):
        for linje in self.historikk:
            print(linje)

    def legg_til_renter(self):
        pass

    def til_dict(self):
        # JSON kan ikke lagre objekter direkte, så vi gjør kontoen om til en dictionary
        return {
            "type": "brukskonto",
            "navn": self.navn,
            "saldo": self._saldo,
            "historikk": self.historikk,
        }


class Sparekonto(Konto):
    RENTE = 0.02
    MAKS_UTTAK = 3

    def __init__(self, kontonummer, navn, saldo=0, historikk=None, uttak=0):
        super().__init__(kontonummer, navn, saldo, historikk)
        self.uttak = uttak

    def vis_saldo(self):
        super().vis_saldo()
        print(f"Uttak igjen: {self.MAKS_UTTAK - self.uttak}")

    def ta_ut(self, belop):
        if self.uttak >= self.MAKS_UTTAK:
            print("Du har brukt opp uttakene på sparekontoen.")
            return False
        if super().ta_ut(belop):
            self.uttak += 1
            return True
        return False

    def legg_til_renter(self):
        renter = round(self._saldo * self.RENTE)
        self._saldo += renter
        self.historikk.append(f"Renter: {renter} kr")
        self.uttak = 0

    def til_dict(self):
        data = super().til_dict()  # Start med det Konto lagrer ...
        data["type"] = "sparekonto"  # ... og legg til det som er spesielt for sparekontoen
        data["uttak"] = self.uttak
        return data


class Bank:
    def __init__(self, filsti):
        self.filsti = filsti
        self.kontoer = {}  # kontonummer -> Konto- eller Sparekonto-objekt
        self.les_fra_fil()

    def les_fra_fil(self):
        with open(self.filsti, encoding="utf-8") as fil:
            data = json.load(fil)
        # Gjør hver dictionary fra fila om til riktig type objekt.
        # Dette er det eneste stedet vi må sjekke kontotypen!
        for kontonummer, info in data.items():
            if info["type"] == "sparekonto":
                konto = Sparekonto(kontonummer, info["navn"], info["saldo"], info["historikk"], info["uttak"])
            else:
                konto = Konto(kontonummer, info["navn"], info["saldo"], info["historikk"])
            self.legg_til(konto)

    def lagre_til_fil(self):
        data = {}
        for kontonummer, konto in self.kontoer.items():
            data[kontonummer] = konto.til_dict()
        with open(self.filsti, "w", encoding="utf-8") as fil:
            json.dump(data, fil, indent=4, ensure_ascii=False)

    def legg_til(self, konto):
        self.kontoer[konto.kontonummer] = konto

    def finn_konto(self, kontonummer):
        if kontonummer not in self.kontoer:
            print("Fant ingen konto med det kontonummeret.")
            return None
        return self.kontoer[kontonummer]

    def opprett_konto(self, navn, sparekonto=False):
        kontonummer = str(1001 + len(self.kontoer))
        if sparekonto:
            self.legg_til(Sparekonto(kontonummer, navn))
        else:
            self.legg_til(Konto(kontonummer, navn))
        print(f"Opprettet konto {kontonummer} for {navn}.")

    def vis_alle(self):
        for konto in self.kontoer.values():
            konto.vis_saldo()

    def legg_til_renter(self):
        for konto in self.kontoer.values():
            konto.legg_til_renter()
        print("Renter er lagt til.")


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
        print("7: Vis historikk")
        print("8: Legg til renter")
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
            navn = input("Navn på ny kunde: ")
            svar = input("Sparekonto? (j/n): ")
            bank.opprett_konto(navn, sparekonto=(svar == "j"))
            bank.lagre_til_fil()

        elif valg == "6":
            bank.vis_alle()

        elif valg == "7":
            konto = bank.finn_konto(input("Kontonummer: "))
            if konto:
                konto.vis_historikk()

        elif valg == "8":
            bank.legg_til_renter()
            bank.lagre_til_fil()

        elif valg == "0":
            print("Ha en fin dag!")
            break

        else:
            print("Ugyldig valg.")


meny()
