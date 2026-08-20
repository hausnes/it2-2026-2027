"""
Oppgave 6d, IT-2 Eksamen, Vår 2024
En liten kalkulator med fire regnearter
og håndtering av mulige feil og unntak.
"""


class Kalkulator:
    def sjekk_input(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Feil: Inndata må være tall.")

    def pluss(self, a: float, b: float) -> float:
        self.sjekk_input(a, b)
        return a + b

    def minus(self, a: float, b: float) -> float:
        self.sjekk_input(a, b)
        return a - b

    def gange(self, a: float, b: float) -> float:
        self.sjekk_input(a, b)
        return a * b

    def dele(self, a: float, b: float) -> float:
        self.sjekk_input(a, b)
        if b == 0:
            raise ZeroDivisionError("Feil: Divisjon med null er ikke tillatt.")
        return a / b


# Eksempel på bruk
if __name__ == "__main__":
    kalkulator = Kalkulator()
    try:
        print(f"Addisjon: 2 + 3 = {kalkulator.pluss(2, 3)}")
        print(f"Subtraksjon: 5 - 3 = {kalkulator.minus(5, 3)}")
        print(f"Multiplikasjon: 5 * 8 = {kalkulator.gange(5, 8)}")
        print(f"Divisjon: 13 / 8 = {kalkulator.dele(13, 8):.2f}")
        print(f"Divisjon: 5 / 0 = {kalkulator.dele(5, 0)}")
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    try:
        print(f"Ugyldig inndata: 5 + 'a' = {kalkulator.pluss(5, 'a')}")
    except TypeError as e:
        print(e)
    try:
        print(f"Feil antall argumenter: 2 - = {kalkulator.minus(2)}")
    except TypeError as e:
        print("Feil: Kalkulator.minus() mangler 1 argument: 'b'")


# Smidig IT-2 © TIP AS, 2024