"""
Steg 1: Vår første klasse
En klasse er en "oppskrift" (mal) for hvordan en konto ser ut.
Et objekt er én konkret konto laget fra oppskriften.
"""


class Konto:
    # __init__ kjøres automatisk hver gang vi lager en ny konto.
    # self er "denne kontoen" - objektet som blir laget.
    def __init__(self, kontonummer, navn, saldo):
        self.kontonummer = kontonummer
        self.navn = navn
        self.saldo = saldo


# Lag to objekter (to konkrete kontoer) fra samme klasse
konto1 = Konto("1001", "Ola Nordmann", 1500)
konto2 = Konto("1002", "Kari Nordmann", 3200)

# Hent ut attributter med punktum
print(konto1.navn, "har", konto1.saldo, "kr")
print(konto2.navn, "har", konto2.saldo, "kr")

# Hvert objekt har sine egne attributter
konto2.navn = "Kari Nordmann-Hansen"
print(konto1.navn)  # Uendret
print(konto2.navn)

# Sammenlign med del 1:
#   kunder["1001"]["saldo"]   ->   konto1.saldo
# Skriver du konto1.sado (skrivefeil), sier VS Code fra med en gang.
# Skriver du kunder["1001"]["sado"], merker du det først når programmet krasjer.
#
# Saldoen endrer vi IKKE direkte. Det skal skje via metoder (steg 2),
# slik at reglene (ikke negative beløp, ikke overtrekk) alltid følges.
