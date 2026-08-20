# test_elbil.py
from elbil import Elbil

class TestElbil:
    def test_kjør(self):
        elbil = Elbil(50, 2.0)
        elbil.kjør(10)
        # 50 kWh - (2.0 kWh per mil * 10 mil) = 30 kWh
        assert elbil.batteri_nivaa == 30

    def test_skriv_til_fil(self, tmp_path):
        elbil = Elbil(50, 2.0)
        filnavn = tmp_path.joinpath('test_batterinivaa.txt')
        elbil.skriv_til_fil(filnavn)
        with open(filnavn, 'r', encoding='utf-8') as fil:
            innhold = fil.read()
            assert innhold == 'Batterinivå: 50 kWh\n'

    def test_skriv_til_skjerm(self, capsys):
        elbil = Elbil(50, 2.0)
        elbil.skriv_til_skjerm()
        captured = capsys.readouterr()
        assert captured.out == 'Batterinivå: 50 kWh\n'

# Smidig IT-2 © TIP AS 2024


