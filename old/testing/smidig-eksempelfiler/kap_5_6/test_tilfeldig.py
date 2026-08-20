"""
5.6 Etterligning (mocking) med pytest
Vi bruker pytest-mock for å få tilgang til mocker-fixturen
Installer pytest-mock med kommandoen: pip install pytest-mock
"""

import tilfeldig
import pytest


@pytest.fixture
def choice_mock(mocker):
    """Fixture for å mocke random.choice med forhåndsdefinerte verdier."""
    return mocker.patch("random.choice")


def test_tilfeldig_farge(choice_mock):
    choice_mock.return_value = "Rød"
    assert tilfeldig.tilfeldig_farge() == "Rød"

    choice_mock.return_value = "Grønn"
    assert tilfeldig.tilfeldig_farge() == "Grønn"

    choice_mock.return_value = "Blå"
    assert tilfeldig.tilfeldig_farge() == "Blå"


if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS 2024
