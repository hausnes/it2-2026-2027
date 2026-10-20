"""
Steg 4: Sparekonto med arv
- Konto: en vanlig brukskonto (nå med historikk, fra utfordringen)
- Sparekonto: ER en Konto, men med maks 3 uttak og renter
Alt som er spesielt for sparekontoen, står samlet i Sparekonto-klassen.
"""


class Konto:
    def __init__(self, kontonummer, navn, saldo=0):
        self.kontonummer = kontonummer
        self.navn = navn
        self._saldo = saldo
        self.historikk = []

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
        # En vanlig konto får ingen renter. Sparekonto overstyrer denne.
        pass


class Sparekonto(Konto):  # Sparekonto arver alt fra Konto
    RENTE = 0.02
    MAKS_UTTAK = 3

    def __init__(self, kontonummer, navn, saldo=0):
        super().__init__(kontonummer, navn, saldo)  # Kjør __init__ fra Konto først
        self.uttak = 0  # Bare sparekontoer har denne attributten

    def vis_saldo(self):
        super().vis_saldo()
        print(f"Uttak igjen: {self.MAKS_UTTAK - self.uttak}")

    def ta_ut(self, belop):
        if self.uttak >= self.MAKS_UTTAK:
            print("Du har brukt opp uttakene på sparekontoen.")
            return False
        if super().ta_ut(belop):  # La Konto gjøre resten av sjekkene og selve uttaket
            self.uttak += 1
            return True
        return False

    def legg_til_renter(self):
        renter = round(self._saldo * self.RENTE)
        self._saldo += renter
        self.historikk.append(f"Renter: {renter} kr")
        self.uttak = 0


class Bank:
    def __init__(self):
        self.kontoer = {}  # kontonummer -> Konto- eller Sparekonto-objekt

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
        # Ingen typesjekk! Hver konto vet selv hvordan den skal få renter.
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
    bank = Bank()
    bank.legg_til(Konto("1001", "Ola Nordmann", 1500))
    bank.legg_til(Sparekonto("1002", "Kari Nordmann", 3200))
    bank.legg_til(Konto("1003", "Per Hansen", 250))

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
            navn = input("Navn på ny kunde: ")
            svar = input("Sparekonto? (j/n): ")
            bank.opprett_konto(navn, sparekonto=(svar == "j"))

        elif valg == "6":
            bank.vis_alle()

        elif valg == "7":
            konto = bank.finn_konto(input("Kontonummer: "))
            if konto:
                konto.vis_historikk()

        elif valg == "8":
            bank.legg_til_renter()

        elif valg == "0":
            print("Ha en fin dag!")
            break

        else:
            print("Ugyldig valg.")


meny()
