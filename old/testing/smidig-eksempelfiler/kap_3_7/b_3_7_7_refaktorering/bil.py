# bil.py
from pathlib import Path

class Bil:
    def __init__(self, loggfil):
        sti = Path(__file__).parent.resolve()
        fil = sti.joinpath(loggfil)
        self.loggfil = fil
        self.motor_status = 'stoppet'

    def start_motor(self):
        self.motor_status = 'startet'
        with open(self.loggfil, 'a') as f:
            f.write(f"Motor startet\n")

    def stopp_motor(self):
        self.motor_status = 'stoppet'
        with open(self.loggfil, 'a') as f:
            f.write(f"Motor stoppet\n")


# Eksempel på bruk av Bil-kassen
if __name__ == "__main__":
    bil = Bil('bil.log')
    bil.start_motor()
    bil.stopp_motor()


# Smidig IT-2 © TIP AS 2024
