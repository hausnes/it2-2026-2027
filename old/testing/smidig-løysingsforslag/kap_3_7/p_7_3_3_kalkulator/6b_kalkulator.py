'''
Oppgave 6b, IT-2 Eksamen, Vår 2024
En liten kalklutator med de fire regneartene
minus, pluss, gange og dele.
'''


class Kalkulator:
    def pluss(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def gange(self, a, b):
        return a * b

    def dele(self, a, b):
        return a / b


# Eksempel på bruk
if __name__ == '__main__':
    kalkulator = Kalkulator()
    print("Addisjon: 2 + 3 =", kalkulator.pluss(2, 3))
    print("Subtraksjon: 2 - 3 =", kalkulator.minus(2, 3))
    print("Multiplikasjon: 2 * 3 =", kalkulator.gange(2, 3))
    print("Divisjon: 5 / 3 =", kalkulator.dele(2, 3))

# Smidig IT-2 © TIP AS, 2024
