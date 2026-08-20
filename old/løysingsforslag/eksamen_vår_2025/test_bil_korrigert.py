import pytest
from batteri_korrigert import Batteri

def test_opprett_batteri():
    batteri = Batteri("TEST001", 20.0)
    assert batteri._Batteri__batteriID == "TEST001"
    assert batteri._Batteri__energikapasitet == 20.0
    assert batteri._Batteri__energinivå == 0.0

def test_lad_opp_positiv_energi():
    batteri = Batteri("TEST002", 15.0)
    assert batteri.ladOpp(10.0) is True
    assert batteri._Batteri__energinivå == 10.0

def test_lad_opp_over_kapasitet():
    batteri = Batteri("TEST003", 10.0)
    assert batteri.ladOpp(12.0) is True
    assert batteri._Batteri__energinivå == 10.0  # Skal være fulladet

def test_lad_opp_negativ_energi(capsys):
    batteri = Batteri("TEST004", 20.0)
    assert batteri.ladOpp(-5.0) is False
    assert batteri._Batteri__energinivå == 0.0  # Skal ikke endres
    captured = capsys.readouterr()
    assert "Ugyldig ladeverdi" in captured.out

def test_lad_opp_null_energi(capsys):
    batteri = Batteri("INFO001", 10.0)
    assert batteri.ladOpp(0.0) is False
    captured = capsys.readouterr()
    assert "Ugyldig ladeverdi" in captured.out

def test_lad_opp_ikke_tall_energi(capsys):
    batteri = Batteri("TYPE001", 10.0)
    assert batteri.ladOpp("abc") is False
    captured = capsys.readouterr()
    assert "Ugyldig ladeverdi" in captured.out

def test_bruk_energi_nok_energi():
    batteri = Batteri("TEST005", 25.0)
    batteri._Batteri__energinivå = 15.0  # Setter initielt nivå for testen
    assert batteri.brukEnergi(7.0) is True
    assert batteri._Batteri__energinivå == 8.0

def test_bruk_energi_ikke_nok_energi(capsys):
    batteri = Batteri("TEST006", 10.0)
    batteri._Batteri__energinivå = 3.0
    assert batteri.brukEnergi(5.0) is False
    assert batteri._Batteri__energinivå == 3.0  # Skal ikke endres
    captured = capsys.readouterr()  # Fang output her
    assert "Ikke nok energi" in captured.out

def test_bruk_energi_negativ_energi(capsys):
    batteri = Batteri("TEST007", 18.0)
    batteri._Batteri__energinivå = 9.0
    assert batteri.brukEnergi(-2.0) is False
    assert batteri._Batteri__energinivå == 9.0  # Skal ikke endres
    captured = capsys.readouterr()
    assert "Ugyldig energibruk" in captured.out

def test_bruk_energi_null_energi(capsys):
    batteri = Batteri("INFO002", 10.0)
    assert batteri.brukEnergi(0.0) is False
    captured = capsys.readouterr()
    assert "Ugyldig energibruk" in captured.out

def test_bruk_energi_ikke_tall_energi(capsys):
    batteri = Batteri("TYPE002", 10.0)
    assert batteri.brukEnergi([1, 2]) is False
    captured = capsys.readouterr()
    assert "Ugyldig energibruk" in captured.out

def test_vis_energiniva():
    batteri = Batteri("TEST008", 30.0)
    batteri._Batteri__energinivå = 22.5
    assert batteri.visEnergiNivå() == 22.5

def test_opprett_batteri_med_negativ_kapasitet():
    with pytest.raises(ValueError) as excinfo:
        Batteri("ERROR001", -5.0)
    assert "Energikapasitet må være et positivt tall." in str(excinfo.value)

def test_opprett_batteri_med_ingen_id():
    with pytest.raises(TypeError) as excinfo:
        Batteri(None, 10.0)
    assert "Batteri-ID må være en streng." in str(excinfo.value)

def test_opprett_batteri_med_tom_id():
    with pytest.raises(ValueError) as excinfo:
        Batteri("", 10.0)
    assert "Batteri-ID kan ikke være en tom streng." in str(excinfo.value)