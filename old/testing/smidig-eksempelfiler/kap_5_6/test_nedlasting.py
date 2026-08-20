"""
5.6 Etterligning (mocking) med pytest
Vi bruker pytest-mock for å få tilgang til mocker-fixturen
Installer pytest-mock med kommandoen: pip install pytest-mock
"""

import nedlasting
import requests
import pytest
from pathlib import Path


@pytest.fixture
def mock_response(mocker):
    """
    Fixture for å etterligne requests.get responsen med innhold fra en lokal HTML-fil.
    Dette sikrer at testen ikke avhenger av en faktisk nettverksforbindelse.
    """
    fil = Path(__file__).parent.resolve().joinpath("Unit_testing.htm")
    with open(fil, encoding="utf-8") as f:
        mock_html_content = f.read()

    # MagicMock brukes til å lage et mock-objekt som etterligner requests.Response
    mock_response = mocker.MagicMock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.text = mock_html_content
    mock_response.raise_for_status = mocker.MagicMock()

    # mocker.patch erstatter returverdien fra requests.get med vår mock_response
    mocker.patch("requests.get", return_value=mock_response)


def test_hent_tittel(mock_response):
    """
    Selv om mock_response ikke brukes direkte i denne funksjonen,
    er argumentet nødvendig for å sikre at requests.get blir mocket korrekt
    av pytest-fixturen. Dette gjør at testen kan kjøre uavhengig av
    nettverksforbindelse.
    """
    url = "https://en.wikipedia.org/wiki/Unit_testing"
    expected_title = "Unit testing - Wikipedia"
    tittel = nedlasting.hent_tittel(url)
    assert tittel == expected_title


if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS 2024
