""" Oppgave 4.8.1 Bankkonto med transaksjoner """

from logg import Logg


class Konto:
    def __init__(self, saldo=0, logg=None):
        self.__saldo = saldo
        self.logg = Logg() if logg is None else logg

    @property
    def saldo(self):
        return self.__saldo

    def innskudd(self, belop):
        self.__saldo += belop
        self.logg.legg_til(f"Innskudd: {belop}")

    def uttak(self, belop):
        if belop <= self.__saldo:
            self.__saldo -= belop
            self.logg.legg_til(f"Uttak: {belop}")
            return True
        else:
            self.logg.legg_til(f"Uttak feilet: {belop}")
            return False


if __name__ == "__main__":
    konto = Konto()
    print(f"Startsaldo: {konto.saldo}")
    konto.innskudd(1000)
    print(f"Saldo etter innskudd: {konto.saldo}")
    konto.uttak(600)
    print(f"Saldo etter uttak: {konto.saldo}")
    konto.uttak(700)
    print(f"Saldo etter mislykket uttak: {konto.saldo}")
    for transaksjon in konto.logg.hent_transaksjoner():
        print(transaksjon)

# Smidig IT-2 © TIP AS 2024
