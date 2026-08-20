'''
Oppgave 6b, IT-2 Eksamen, Vår 2024
Kjør testene med pytest
Mer omfattende tester ville inkludert:
* Tester med negative tall
* Grenseverdier (veldig små og veldig store tall)
* Tester for 'nan' og 'inf'
Disse er utelatt for å holde testene innenfor tilgjengelig tidsramme.
'''
from kalkulator import Kalkulator
import pytest
import math


@pytest.fixture(scope="class")
def kalkulator():
    return Kalkulator()


class TestKalkulator:

    def test_kalkulator(self, kalkulator):
        assert kalkulator is not None
        assert isinstance(kalkulator, Kalkulator)

    def test_pluss(self, kalkulator):
        assert kalkulator.pluss(1, 2) == 3
        # Feil type
        with pytest.raises(TypeError):
            kalkulator.pluss(2, "3")

    def test_minus(self, kalkulator):
        assert kalkulator.minus(5, 2) == 3
        # For få argumenter
        with pytest.raises(TypeError):
            kalkulator.minus(8)

    def test_gange(self, kalkulator):
        assert kalkulator.gange(8, 13) == 104
        assert kalkulator.gange(math.pi, 2) \
            == pytest.approx(6.28, rel=0.001)

    def test_dele(self, kalkulator):
        assert kalkulator.dele(10, 2) == 5
        # Divisjon med 0
        with pytest.raises(ZeroDivisionError):
            kalkulator.dele(5, 0)

# Smidig IT-2 © TIP AS, 2024
