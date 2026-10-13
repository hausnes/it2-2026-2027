"""
Steg 2: Metoder
En metode er en funksjon som hører til en klasse.
Nå flytter vi funksjonene fra del 1 INN i klassen, slik at
dataene (saldo) og det man kan gjøre med dem (sett inn, ta ut) ligger samlet.
"""


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
        # Gjenbruker metodene vi allerede har laget
        self.ta_ut(belop)
        annen_konto.sett_inn(belop)


# Test klassen
ola = Konto("1001", "Ola Nordmann", 1500)
kari = Konto("1002", "Kari Nordmann", 3200)

ola.vis_saldo()
ola.sett_inn(500)
ola.ta_ut(10000)  # Skal gi feilmelding
ola.overfor_til(kari, 1000)

ola.vis_saldo()
kari.vis_saldo()

# Sammenlign med del 1:
#   sett_inn(kunder, "1001", 500)   ->   ola.sett_inn(500)
# Vi slipper å sende med hele kunder-dictionaryen og kontonummeret hver gang.
# Kontoen "vet" selv hvem den er (self).
