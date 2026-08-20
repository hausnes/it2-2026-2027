from s_2_5_1_bmi import bmi_klassifisering

def test_undervekt():
    assert bmi_klassifisering(1.80,48.6) == 'Undervekt'
    assert bmi_klassifisering(1.80,59.9) == 'Undervekt'
    assert bmi_klassifisering(1.75,55.0) == 'Undervekt'

def test_normalvekt():
    assert bmi_klassifisering(1.80,60.0) == 'Normalvekt'
    assert bmi_klassifisering(1.80,75.0) == 'Normalvekt'
    assert bmi_klassifisering(1.75,76.5) == 'Normalvekt'

def test_overvekt():
    assert bmi_klassifisering(1.72,74.0) == 'Overvekt'
    assert bmi_klassifisering(1.72,79.8) == 'Overvekt'
    assert bmi_klassifisering(1.85,102.6) == 'Overvekt'

def test_fedme_1():
    assert bmi_klassifisering(1.50,67.5) == 'Fedme, grad 1'
    assert bmi_klassifisering(1.50,72.5) == 'Fedme, grad 1'
    assert bmi_klassifisering(1.75,107.1) == 'Fedme, grad 1'

def test_fedme_2():
    assert bmi_klassifisering(1.80,113.4) == 'Fedme, grad 2'
    assert bmi_klassifisering(1.80,119.0) == 'Fedme, grad 2'
    assert bmi_klassifisering(1.75,108.5) == 'Fedme, grad 2'

def test_fedme_3():
    assert bmi_klassifisering(1.80,160.0) == 'Fedme, grad 3'
    assert bmi_klassifisering(1.80,152.3) == 'Fedme, grad 3'
    assert bmi_klassifisering(1.75,124.0) == 'Fedme, grad 3'

# Smidig IT-2 © TIP AS 2024