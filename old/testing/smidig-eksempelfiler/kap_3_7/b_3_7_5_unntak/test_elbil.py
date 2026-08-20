# test_elbil.py
import pytest
from elbil import Elbil

class TestElbil:
    def test_kjør_negativ_mil(self):
        elbil = Elbil(100, 2.0)
        # Metode 1: Bruker match-parameteren
        with pytest.raises((ValueError,TypeError), match="Antall mil kan ikke være negativt"):
            elbil.kjør(-5)

    def test_kjør_ikke_nok_strom(self):   
        elbil = Elbil(100, 2.0)
        # Metode 2: Bruker e.value for å sjekke feilmeldingen
        with pytest.raises(ValueError) as e:
            elbil.kjør(60)
        assert "Ikke nok strøm på batteriet til å kjøre så langt" in str(e.value)

    def test_kjør_ugyldig_mil_type(self):
        elbil = Elbil(100, 2.0)
        with pytest.raises(TypeError, match="Antall mil må være en int eller float"):
            elbil.kjør("ti")

    @pytest.mark.xfail(reason="Ikke implementert")
    def test_koble_til_lader_ikke_implementert(self):
        elbil = Elbil(batteri_nivaa=100, forbruk_per_mil=2)
        assert elbil.koble_til_lader() == "Koblet til lader"

    def test_kjør_gyldig(self):
        elbil = Elbil(100, 2.0)
        elbil.kjør(10)
        assert elbil.batteri_nivaa == 80        # 100 - (2.0 * 10) = 80 kWh

    def test_beregn_rekkevidde(self):
        elbil = Elbil(100, 2.0)
        assert elbil.beregn_rekkevidde() == 50  # 100 kWh / 2.0 kWh per mil = 50 mil


# Smidig IT-2 © TIP AS 2024
