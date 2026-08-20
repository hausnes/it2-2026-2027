import pytest
from batteri import Batteri

def test_opprett_batteri():
    batteri = Batteri("TEST001", 20.0)
    assert batteri._Batteri__batteriID == "TEST001"
    assert batteri._Batteri__energikapasitet == 20.0
    assert batteri._Batteri__energinivå == 0.0

def test_lad_opp_positiv_energi():
    batteri = Batteri("TEST002", 15.0)
    batteri.ladOpp(10.0)
    assert batteri._Batteri__energinivå == 10.0

def test_lad_opp_over_kapasitet():
    batteri = Batteri("TEST003", 10.0)
    batteri.ladOpp(12.0)
    assert batteri._Batteri__energinivå == 10.0  # Skal være fulladet

def test_lad_opp_negativ_energi():
    batteri = Batteri("TEST004", 20.0)
    batteri.ladOpp(-5.0)
    assert batteri._Batteri__energinivå == 0.0  # Skal ikke endres

def test_bruk_energi_nok_energi():
    batteri = Batteri("TEST005", 25.0)
    batteri._Batteri__energinivå = 15.0  # Setter initielt nivå for testen
    batteri.brukEnergi(7.0)
    assert batteri._Batteri__energinivå == 8.0

def test_bruk_energi_ikke_nok_energi():
    batteri = Batteri("TEST006", 10.0)
    batteri._Batteri__energinivå = 3.0
    batteri.brukEnergi(5.0)
    assert batteri._Batteri__energinivå == 3.0  # Skal ikke endres

def test_bruk_energi_negativ_energi():
    batteri = Batteri("TEST007", 18.0)
    batteri._Batteri__energinivå = 9.0
    batteri.brukEnergi(-2.0)
    assert batteri._Batteri__energinivå == 9.0  # Skal ikke endres

def test_vis_energiniva():
    batteri = Batteri("TEST008", 30.0)
    batteri._Batteri__energinivå = 22.5
    assert batteri.visEnergiNivå() == 22.5

# Mulige feil og ett unntak:

# 1. Feil: Manglende validering av energikapasitet ved opprettelse.
#    Hvis energikapasiteten som sendes inn er negativ, vil batteriet fortsatt opprettes
#    med en negativ kapasitet, noe som er ulogisk. Vi kan legge til en sjekk i __init__.
def test_opprett_batteri_med_negativ_kapasitet():
    with pytest.raises(ValueError):
        Batteri("ERROR001", -5.0)

# 2. Feil: Utydelig håndtering av null-energi ved lading/bruk.
#    Hvis man forsøker å lade eller bruke 0 energi, skjer det ingen endring, men det gis
#    ingen eksplisitt tilbakemelding om at ingenting skjedde. Selv om det ikke er en
#    direkte feil, kan det være forvirrende. Vi kan velge å legge til en melding.
def test_lad_opp_null_energi(capsys):
    batteri = Batteri("INFO001", 10.0)
    batteri.ladOpp(0.0)
    captured = capsys.readouterr()
    assert "Ugyldig ladeverdi" in captured.out # Programmet skriver ut en melding

def test_bruk_energi_null_energi(capsys):
    batteri = Batteri("INFO002", 10.0)
    batteri.brukEnergi(0.0)
    captured = capsys.readouterr()
    assert "Ugyldig energibruk" in captured.out # Programmet skriver ut en melding

# 3. Unntak: Forsøk på å opprette et batteri uten gyldig ID (f.eks. None eller tom streng).
#    Dette kan føre til problemer senere hvis ID brukes for identifisering. Vi kan
#    velge å heve et TypeError eller ValueError hvis ID er ugyldig.
def test_opprett_batteri_med_ingen_id():
    with pytest.raises(TypeError): # Eller ValueError, avhengig av ønsket håndtering
        Batteri(None, 10.0)

def test_opprett_batteri_med_tom_id():
    with pytest.raises(ValueError): # Eller TypeError, avhengig av ønsket håndtering
        Batteri("", 10.0)