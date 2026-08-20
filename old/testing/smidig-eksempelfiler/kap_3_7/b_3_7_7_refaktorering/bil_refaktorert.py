# bil_refaktorert.py
from pathlib import Path

class Bil:
    def __init__(self, loggfil):
        self.loggfil = Path(__file__).with_name(loggfil)
        self.motor_status = 'stoppet'

    def write_log(self, status):
        with open(self.loggfil, 'a') as f:
            f.write(f"Motor {status}\n")

    def start_motor(self):
        self.motor_status = 'startet'
        self.write_log('startet')

    def stopp_motor(self):
        self.motor_status = 'stoppet'
        self.write_log('stoppet')


# Eksempel på bruk av koden
if __name__ == "__main__":
    bil = Bil('bil.log')
    bil.start_motor()
    bil.stopp_motor()


# Smidig IT-2 © TIP AS 2024