# test_elbil.py
from elbil import Elbil
import pytest

class TestElbil:
    def test_beregn_rekkevidde(self):
        elbil = Elbil(50, 2.0)
        # 50 kWh / 2.0 kWh per mil = 25 mil
        assert elbil.beregn_rekkevidde() == 25

    def test_beregn_rekkevidde_flatt_batteri(self):
        elbil = Elbil(0, 2.0)
        # 0 kWh / 2.0 kWh per mil = 0 mil
        assert elbil.beregn_rekkevidde() == 0

    def test_beregn_rekkevidde_effektiv(self):
        # 60 kWh / 1.5 kWh per mil ≈ 33.3 mil
        elbil = Elbil(50, 1.5)
        assert elbil.beregn_rekkevidde() == pytest.approx(33.3, abs=0.1)

    def test_beregn_rekkevidde_ineffektiv(self):
        # 50 kWh / 2,.5 kWh per mil = 20 mil
        elbil = Elbil(50, 2.5)
        assert elbil.beregn_rekkevidde() == 20


# Smidig IT-2 © TIP AS 2024
