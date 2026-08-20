from konto import Konto
from logg import Logg
import pytest

@pytest.fixture()
def mock_logg(mocker):
    return mocker.MagicMock(spec=Logg)

class TestKonto:

    def test_init(self, mock_logg):
        konto = Konto(saldo=0, logg=mock_logg)
        assert konto.saldo == 0
        assert konto.logg is not None
        assert isinstance(konto.logg, Logg)

    def test_innskudd(self, mock_logg):
        konto = Konto(saldo=0, logg=mock_logg)
        assert konto.saldo == 0
        konto.innskudd(700)
        assert konto.saldo == 700
        konto.logg.legg_til.assert_called_once_with("Innskudd: 700")
        konto.innskudd(400)
        assert konto.saldo == 1100
        konto.logg.legg_til.assert_called_with("Innskudd: 400")
        assert mock_logg.legg_til.call_count == 2

    def test_uttak(self, mock_logg):
        konto = Konto(saldo=1000, logg=mock_logg)
        assert konto.saldo == 1000
        assert konto.uttak(600) == True
        assert konto.saldo == 400
        konto.logg.legg_til.assert_called_once_with("Uttak: 600")

    def test_uttak_feilet(self, mock_logg):
        konto = Konto(saldo=400, logg=mock_logg)
        assert konto.saldo == 400
        assert konto.uttak(700) == False
        assert konto.saldo == 400
        konto.logg.legg_til.assert_called_once_with("Uttak feilet: 700")

if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS 2024
