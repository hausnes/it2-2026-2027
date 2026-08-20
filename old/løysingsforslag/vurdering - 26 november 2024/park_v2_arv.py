from datetime import datetime

ANTALL_PLASSER = 20
PRIS_PER_MINUTT = 1.5

class Bil:
    '''
    Klassen Bil representerer en bil med registreringsnummer, modell og farge.
    print_info er en valgfri parameter som bestemmer om informasjon om bilen skal printes ut
    når den opprettes.
    '''
    def __init__(self, reg_nr, modell, farge, print_info=True):
        self.reg_nr = reg_nr
        self.modell = modell
        self.farge = farge
        self.innkjøringstid = None
        if print_info:
            print(f"Opprettet {farge} {modell} med reg.nr. {reg_nr}")

    def antall_plasser(self):
        return 1

    def beregn_parkeringsavgift(self, minutter_parkert):
        return minutter_parkert * PRIS_PER_MINUTT * self.antall_plasser()

class Lastebil(Bil):
    '''
    Klassen Lastebil arver fra klassen Bil og representerer en lastebil.
    En lastebil tar to plasser.
    '''
    def __init__(self, reg_nr, modell, farge):
        super().__init__(reg_nr, modell, farge, print_info=False)
        print(f"Opprettet lastebil {farge} {modell} med reg.nr. {reg_nr}")

    def antall_plasser(self):
        return 2

class PHus:
    '''
    Klassen PHus representerer et parkeringhus med en viss mengde plasser.
    parkerte_biler er en dictionary med registreringsnummer som nøkkel og bilobjekt som verdi.
    opptatte_plasser er en teller for hvor mange plasser som er opptatt.
    '''
    def __init__(self):
        self.parkerte_biler = {}
        self.opptatte_plasser = 0
        print(f"Opprettet parkingshus med {ANTALL_PLASSER} plasser", end='\n\n')

    def innkjøring(self, bil, tid):
        if self.opptatte_plasser + bil.antall_plasser() > ANTALL_PLASSER:
            print(f"Ingen ledige plasser for {bil.reg_nr}")
            return
        bil.innkjøringstid = tid
        self.parkerte_biler[bil.reg_nr] = bil
        self.opptatte_plasser += bil.antall_plasser()
        print(f"{bil.reg_nr} kjørte inn {tid.strftime('%H:%M')}")
        self.vis_ledige_plasser()

    def utkjøring(self, reg_nr, tid):
        bil = self.parkerte_biler.pop(reg_nr)
        self.opptatte_plasser -= bil.antall_plasser()
        minutter_parkert = (tid - bil.innkjøringstid).total_seconds() / 60
        parkeringsavgift = bil.beregn_parkeringsavgift(minutter_parkert)
        print(f"{bil.reg_nr} {bil.farge} {bil.modell} kjørte ut {tid.strftime('%H:%M')}")
        print(f"Parkeringstid: {minutter_parkert:.0f} min., avgift kr {parkeringsavgift:.2f}")
        self.vis_ledige_plasser()

    def vis_ledige_plasser(self):
        antall_ledige_plasser = ANTALL_PLASSER - self.opptatte_plasser
        print(f'Antall ledige plasser: {antall_ledige_plasser}', end='\n\n')

    def vis_biler_med_farge(self, farge):
        for bil in self.parkerte_biler.values():
            if bil.farge == farge:
                print(f"{bil.reg_nr} {bil.farge} {bil.modell}")

if __name__ == "__main__":
    phus = PHus()

    bil = Bil("AB12345", "Tesla", "rød")
    tid = datetime(2023, 11, 29, 15, 0)
    phus.innkjøring(bil, tid)

    tid = datetime(2023, 11, 29, 16, 0)
    phus.utkjøring("AB12345", tid)

    bil = Bil("EK13002", "eGolf", "hvit")
    tid = datetime(2023, 11, 29, 13, 45)
    phus.innkjøring(bil, tid)

    # tid = datetime(2023, 11, 29, 14, 41)
    # phus.utkjøring("AB12345", tid)

    bil = Bil("TV12345", "Ford", "hvit")
    tid = datetime(2023, 11, 29, 14, 50)
    phus.innkjøring(bil, tid)

    bil = Bil("VD77077", "Ford", "blå")
    tid = datetime(2023, 11, 29, 14, 55)
    phus.innkjøring(bil, tid)

    phus.vis_biler_med_farge("hvit")

    # Opprett en lastebil og kjør den inn
    print("\n\nTester lastebil:")
    lastebil = Lastebil("XY98765", "Volvo", "rød")
    tid = datetime(2023, 11, 29, 15, 0)
    phus.innkjøring(lastebil, tid)

    # Kjør lastebilen ut etter en time
    tid = datetime(2023, 11, 29, 16, 0)
    phus.utkjøring("XY98765", tid)

    # Vis biler med en bestemt farge
    phus.vis_biler_med_farge("rød")