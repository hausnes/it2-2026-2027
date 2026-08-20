# elbil.py

class Elbil:
    def __init__(self, batteri_nivaa, forbruk_per_mil):
        self.batteri_nivaa = batteri_nivaa  # i kWh
        self.forbruk_per_mil = forbruk_per_mil  # i kWh per mil

    def beregn_rekkevidde(self):
        return self.batteri_nivaa / self.forbruk_per_mil

    def kjør(self, mil):
        if not isinstance(mil, (int, float)):
            raise TypeError("Antall mil må være en int eller float")
        if mil < 0:
            raise ValueError("Antall mil kan ikke være negativt")
        rekkevidde = self.beregn_rekkevidde()
        if mil > rekkevidde:
            raise ValueError("Ikke nok strøm på batteriet til å kjøre så langt")
        forbruk = self.forbruk_per_mil * mil
        self.batteri_nivaa -= forbruk

    def koble_til_lader(self):
        ikke_implementert = True
        if ikke_implementert:
            raise NotImplementedError("Lader ikke implementert")
        return "Koblet til lader"

# Eksempel på bruk av Elbil klassen:
if __name__ == "__main__":
    elbil = Elbil(100, 2.0)
    try:
        elbil.kjør(60)
        print(f"Etter å ha kjørt 60 mil, har bilen {elbil.batteri_nivaa} kWh igjen.")
    except (ValueError, TypeError) as e:
        print(f"Feil: {e}")

    try:
        elbil.kjør(-5)
    except (ValueError, TypeError) as e:
        print(f"Feil: {e}")

    try:
        elbil.kjør("ti")
    except (ValueError, TypeError) as e:
        print(f"Feil: {e}")

    try:
        elbil.kjør(10)
        print(f"Etter å ha kjørt 10 mil, har bilen {elbil.batteri_nivaa} kWh igjen.")
    except (ValueError, TypeError) as e:
        print(f"Feil: {e}")

    try:
        elbil.koble_til_lader()
    except NotImplementedError as e:
        print(f"Feil: {e}")

# Smidig IT-2 © TIP AS 2024
