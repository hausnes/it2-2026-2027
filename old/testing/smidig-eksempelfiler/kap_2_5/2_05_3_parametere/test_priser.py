import priser
import pytest

@pytest.mark.parametrize('alder,billettpris',[
    (6,63),(10,63),(17,63),
    (18,157),(50,157),(66,157),
    (67,79),(80,79),(130,79)])
def test_billettpris(alder,billettpris):
    assert priser.billettpris(alder) == billettpris

# Smidig IT-2 © TIP AS, 2024