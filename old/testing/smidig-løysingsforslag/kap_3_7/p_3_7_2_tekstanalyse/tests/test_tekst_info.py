import pytest
from tekst_info import TekstInfo

# Uten fixtures
def test_finn_antall_karakterer():
    ti = TekstInfo()
    tekst = "Dette er en testsetning"
    assert ti.finn_antall_karakterer(tekst) == 23

# Opprett en tekst vi kan bruke i testene
@pytest.fixture
def tekst():
    return "Dette er en setningen vi skal bruke i resten av testene"

def test_finn_antall_ord(tekst):
    ti = TekstInfo()
    assert ti.finn_antall_ord(tekst) == 11

# Opprett en instans vi kan bruke i testene
@pytest.fixture
def tekstinfo():
    return TekstInfo()

def test_finn_lengste_ordet(tekstinfo, tekst):
    assert tekstinfo.finn_lengste_ordet(tekst) == "setningen"

# Med statiske metoder slipper vi å opprette en instans
def test_finn_korteste_ordet(tekst):
    assert TekstInfo.finn_korteste_ordet(tekst) == "i"

# Smidig IT-2 © TIP AS 2024