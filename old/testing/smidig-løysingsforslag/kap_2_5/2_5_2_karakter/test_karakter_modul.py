from karakter_modul import karakter
import pytest

@pytest.mark.parametrize("poengsum, forventet", [
    ( 30, 'Ikke bestått'),
    ( 65, 'Bestått'),
    ( 82, 'Godt bestått'),
    ( 97, 'Meget godt bestått'),
    (102, 'Ikke gyldig poengsum!'),
    (  0, 'Ikke bestått'),
    ( 50, 'Bestått'),
    ( 69, 'Bestått'),
    ( 70, 'Godt bestått'),
    ( 89, 'Godt bestått'),
    ( 90, 'Meget godt bestått'),
    (100, 'Meget godt bestått'),
    ( -1, 'Ikke gyldig poengsum!'),
])
def test_karakter(poengsum, forventet):
    assert(karakter(poengsum) == forventet)

# Smidig IT-2 © TIP AS 2024