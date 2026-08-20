# elbil.py

class Elbil:
    def __init__(self, batteri_nivaa, forbruk_per_mil):
        self.batteri_nivaa = batteri_nivaa      # i kWh
        self.forbruk_per_mil = forbruk_per_mil  # i kWh per mil

    def beregn_rekkevidde(self)->float:
        return self.batteri_nivaa / self.forbruk_per_mil

# # Eksempel på bruk av Elbil-klassen
if __name__ == '__main__':
    elbil = Elbil(40, 1.5)
    print(f'Rekkevidde: {elbil.beregn_rekkevidde():.1f} mil')

# Smidig IT-2 © TIP AS 2024