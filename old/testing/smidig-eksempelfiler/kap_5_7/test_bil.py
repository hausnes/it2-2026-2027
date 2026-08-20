# test_bil.py
import unittest
from bil import Bil


class TestBil(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        print("\ntearDownClass")
        return super().tearDownClass()

    def setUp(self) -> None:
        print("\nsetUp")
        self.bil = Bil()
        return super().setUp()

    def tearDown(self) -> None:
        print("tearDown")
        return super().tearDown()

    def test_start_motor(self):
        print("Tester start av motor")
        self.bil.start_motor()
        assert self.bil.motor_status == "startet"

    def test_stopp_motor(self):
        print("Tester stopp av motor")
        self.bil.start_motor()
        self.bil.stopp_motor()
        assert self.bil.motor_status == "stoppet"


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestBil("test_start_motor"))
    suite.addTest(TestBil("test_stopp_motor"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()

# Smidig IT-2 © TIP AS 2024
