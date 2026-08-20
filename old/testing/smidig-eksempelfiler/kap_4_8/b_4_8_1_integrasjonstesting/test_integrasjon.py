# test_integrasjon.py
import pytest
from spiller import Spiller


@pytest.fixture
def spiller_ola():
    return Spiller("Ola")


def test_poeng_for_å_levere_sau(spiller_ola):
    spiller_ola.oppdater_poeng("levert_sau")
    assert spiller_ola.poengsystem.hent_poeng() == 1


def test_poeng_for_ingen_handling(spiller_ola):
    spiller_ola.oppdater_poeng("ingen_handling")
    assert spiller_ola.poengsystem.hent_poeng() == 0


if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS 2024
