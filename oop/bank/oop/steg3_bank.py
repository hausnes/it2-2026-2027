"""
Steg 3: En Bank-klasse som holder styr på alle kontoene
- Konto: én konto (samme som i steg 2)
- Bank: har en dictionary med Konto-objekter
Foreløpig lagrer vi ingenting til fil. Det kommer i steg 5.
"""


class Konto:
    def __init__(self, kontonummer, navn, saldo=0):
        self.kontonummer = kontonummer
        self.navn = navn
        self._saldo = saldo

    def vis_saldo(self):
        print(f"{self.navn} har {self._saldo} kr på konto {self.kontonummer}.")

    def sett_inn(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return
        self._saldo += belop
        print(f"Satte inn {belop} kr.")

    def ta_ut(self, belop):
        if belop <= 0:
            print("Beløpet må være større enn 0.")
            return False
        if belop > self._saldo:
            print("Det er ikke nok penger på kontoen.")
            return False
        self._saldo -= belop
        print(f"Tok ut {belop} kr.")
        return True

    def overfor_til(self, annen_konto, belop):
        if self.ta_ut(belop):
            annen_konto.sett_inn(belop)


class Bank:
    def __init__(self):
        self.kontoer = {}  # kontonummer -> Konto-objekt

    def legg_til(self, konto):
        self.kontoer[konto.kontonummer] = konto

    def finn_konto(self, kontonummer):
        if kontonummer not in self.kontoer:
            print("Fant ingen konto med det kontonummeret.")
            return None
        return self.kontoer[kontonummer]

    def opprett_konto(self, navn):
        kontonummer = str(1001 + len(self.kontoer))
        self.legg_til(Konto(kontonummer, navn))
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
    bank = Bank()
    bank.legg_til(Konto("1001", "Ola Nordmann", 1500))
    bank.legg_til(Konto("1002", "Kari Nordmann", 3200))
    bank.legg_til(Konto("1003", "Per Hansen", 250))

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

        elif valg == "3":
            konto = bank.finn_konto(input("Kontonummer: "))
            if konto:
                konto.ta_ut(les_belop())

        elif valg == "4":
            fra_konto = bank.finn_konto(input("Fra kontonummer: "))
            til_konto = bank.finn_konto(input("Til kontonummer: "))
            if fra_konto and til_konto:
                fra_konto.overfor_til(til_konto, les_belop())

        elif valg == "5":
            bank.opprett_konto(input("Navn på ny kunde: "))

        elif valg == "6":
            bank.vis_alle()

        elif valg == "0":
            print("Ha en fin dag!")
            break

        else:
            print("Ugyldig valg.")


meny()
