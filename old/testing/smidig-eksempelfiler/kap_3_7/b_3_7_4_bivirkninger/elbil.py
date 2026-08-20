# elbil.py
from pathlib import Path

class Elbil:
    def __init__(self, batteri_nivaa, forbruk_per_mil):
        self.batteri_nivaa = batteri_nivaa       # i kWh
        self.forbruk_per_mil = forbruk_per_mil   # i kWh per mil

    def kjør(self, mil):
        self.batteri_nivaa -= self.forbruk_per_mil * mil
        if self.batteri_nivaa < 0:
            self.batteri_nivaa = 0   #Batteriet kan ikke gå under 0.

    def skriv_til_fil(self, filnavn):
        sti = Path(__file__).parent.resolve()
        filnavn = sti.joinpath(filnavn)
        with open(filnavn, 'w', encoding='utf-8') as fil:
            fil.write(f'Batterinivå: {self.batteri_nivaa} kWh\n')

    def skriv_til_skjerm(self):
        print(f'Batterinivå: {self.batteri_nivaa} kWh')

# Eks# # Eksempel på bruk av Elbil-klassen
if __name__ == '__main__':
    elbil = Elbil(50, 2.0)
    print(f'Batterinivå: {elbil.batteri_nivaa} kWh')
    elbil.kjør(10)
    # 50 kWh - (2.0 kWh per mil * 10 mil) = 30 kWh
    elbil.skriv_til_fil('batterinivaa.txt')
    elbil.skriv_til_skjerm()

# Smidig IT-2 © TIP AS 2024