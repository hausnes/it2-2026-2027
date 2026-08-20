""" Oppgave 4.8.1 Logging av banktransaksjoner """


class Logg:
    def __init__(self):
        self.transaksjoner = []

    def legg_til(self, melding):
        self.transaksjoner.append(melding)

    def hent_transaksjoner(self):
        return self.transaksjoner


if __name__ == "__main__":
    logg = Logg()
    logg.legg_til("Innskudd: 1000")
    logg.legg_til("Uttak: 500")
    logg.legg_til("Uttak feilet: 700")
    for transaksjon in logg.hent_transaksjoner():
        print(transaksjon)


# Smidig IT-2 © TIP AS 2024
