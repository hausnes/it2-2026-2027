from datetime import datetime
from typing import Dict
ANTALL_PLASSER = 20
PRIS_PER_MINUTT = 1.5

class Bil:
    def __init__(self, reg_nr: str, modell: str, farge: str):
        self.reg_nr: str = reg_nr
        self.modell: str = modell
        self.farge: str = farge
        self.innkjøringstid: datetime = None
        print(f"Opprettet {farge} {modell} med reg.nr. {reg_nr}")

class PHus:
    def __init__(self):
        self.parkerte_biler: Dict[str, Bil] = {}
        print(
            f"Opprettet parkingshus med {ANTALL_PLASSER} plasser", end='\n\n')

    def innkjøring(self, bil: Bil, tid: datetime) -> None:
        bil.innkjøringstid = tid
        self.parkerte_biler[bil.reg_nr] = bil
        print(f"{bil.reg_nr} kjørte inn {tid.strftime('%H:%M')}")
        self.vis_ledige_plasser()

    def utkjøring(self, reg_nr: str, tid: datetime) -> None:
        bil: Bil = self.parkerte_biler.pop(reg_nr)
        minutter_parkert = (tid - bil.innkjøringstid).total_seconds()/60
        parkeringsavgift = minutter_parkert * PRIS_PER_MINUTT
        print(
            f"{bil.reg_nr} {bil.farge} {bil.modell} kjørte ut {tid.strftime('%H:%M')}")
        print(
            f"Parkeringstid: {minutter_parkert:.0f} min., avgift kr {parkeringsavgift:.2f}")
        self.vis_ledige_plasser()

    def vis_ledige_plasser(self) -> None:
        antall_ledige_plasser = ANTALL_PLASSER - len(self.parkerte_biler)
        print(f'Antall ledige plasser: {antall_ledige_plasser}', end='\n\n')

    def vis_biler_med_farge(self, farge: str) -> None:
        print(f'Parkerte biler som er {farge.lower()}e:')
        for reg_nr, bil in self.parkerte_biler.items():
            if bil.farge.lower() == farge.lower():
                print(f"   {reg_nr} {bil.modell}")

if __name__ == "__main__":
    phus = PHus()

    bil = Bil("AB12345", "Tesla", "rød")
    tid = datetime(2023, 11, 29, 13, 37)
    phus.innkjøring(bil, tid)

    bil = Bil("EK13002", "eGolf", "hvit")
    tid = datetime(2023, 11, 29, 13, 45)
    phus.innkjøring(bil, tid)

    tid = datetime(2023, 11, 29, 14, 41)
    phus.utkjøring("AB12345", tid)

    bil = Bil("TV12345", "Ford", "hvit")
    tid = datetime(2023, 11, 29, 14, 50)
    phus.innkjøring(bil, tid)

    bil = Bil("VD77077", "Ford", "blå")
    tid = datetime(2023, 11, 29, 14, 55)
    phus.innkjøring(bil, tid)

    phus.vis_biler_med_farge("hvit")