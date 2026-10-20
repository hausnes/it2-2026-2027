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
        # Understrek = "intern, ikke rør utenfor klassen". Bruk metodene i stedet.
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
        # Returnerer True/False, slik at overfor_til() vet om uttaket gikk bra
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
        # Gjenbruker metodene vi allerede har laget
        if self.ta_ut(belop):
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

# Python stopper deg ikke om du skriver ola._saldo = 1000000,
# men understreken gjør det tydelig for alle som leser koden at det er juks.
