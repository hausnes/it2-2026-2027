# test_bil.py
from bil import Bil

class TestBil:
    def test_init(self):
        bil = Bil()
        assert bil is not None
        assert isinstance(bil, Bil)
        assert bil.motor_status == 'stoppet'

# Smidig IT-2 © TIP AS 2024