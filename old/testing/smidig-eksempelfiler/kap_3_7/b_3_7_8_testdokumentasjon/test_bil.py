# test_bil.py
import pytest
from bil import Bil

@pytest.fixture(scope="class")
def cls():
    print("\nClass setUp")
    yield
    print("Class tearDown")

@pytest.fixture
def bil(cls):
    print("Function setUp")
    bil = Bil()
    yield bil
    print("\nFunction tearDown")

class TestBil:
    def test_start_motor(self, bil):
        print("Tester start av motor")
        bil.start_motor()
        assert bil.motor_status == 'i gang'

    def test_stopp_motor(self, bil):
        print("Tester stopp av motor")
        bil.start_motor()
        bil.stopp_motor()
        assert bil.motor_status == 'stoppet'

# Smidig IT-2 © TIP AS 2024



