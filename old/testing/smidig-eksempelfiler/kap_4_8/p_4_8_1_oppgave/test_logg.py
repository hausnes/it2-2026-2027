from logg import Logg
import pytest

class TestLogg:

    def test_init(self):
        logg = Logg()
        assert logg is not None
        assert isinstance(logg, Logg)
        assert logg.transaksjoner == []

    def test_legg_til(self):
        logg = Logg()
        logg.legg_til("Innskudd: 1000")
        assert logg.transaksjoner == ["Innskudd: 1000"]
        logg.legg_til("Uttak: 500")
        assert logg.transaksjoner == ["Innskudd: 1000", "Uttak: 500"]
        logg.legg_til("Uttak feilet: 700")
        assert logg.transaksjoner == ["Innskudd: 1000", "Uttak: 500", "Uttak feilet: 700"]

    def test_hent_transaksjoner(self):
        logg = Logg()
        logg.legg_til("Innskudd: 1000")
        logg.legg_til("Uttak: 500")
        logg.legg_til("Uttak feilet: 700")
        assert logg.hent_transaksjoner() == ["Innskudd: 1000", "Uttak: 500", "Uttak feilet: 700"]

if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS, 2024