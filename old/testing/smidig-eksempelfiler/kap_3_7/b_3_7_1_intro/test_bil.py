# test_bil.py
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bil import Bil
import pytest

class TestBil:
    def test_start_motor(self):
        bil = Bil()
        bil.start_motor()
        assert bil.motor_status == 'startet'

    def test_stopp_motor(self):
        bil = Bil()
        bil.start_motor()
        bil.stopp_motor()
        assert bil.motor_status == 'stoppet'

# Smidig IT-2 © TIP AS 2024