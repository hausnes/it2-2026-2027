class Batteri:
    def __init__(self, batteriID: str, energikapasitet: float):
        """
        Konstruktør for Batteri-klassen.

        Args:
            batteriID (str): En unik identifikator for batteriet.
            energikapasitet (float): Batteriets totale energikapasitet i en passende enhet (f.eks. kWh).
        """
        self.__batteriID = batteriID
        self.__energikapasitet = energikapasitet
        self.__energinivå = 0.0  # Initialiserer energinivået til 0 ved opprettelse

    def ladOpp(self, energi: float):
        """
        Lader opp batteriet med en gitt mengde energi.

        Args:
            energi (float): Mengden energi som skal legges til batteriet.
        """
        if energi > 0:
            nytt_energinivå = self.__energinivå + energi
            if nytt_energinivå <= self.__energikapasitet:
                self.__energinivå = nytt_energinivå
                print(f"Batteri {self.__batteriID}: Ladet opp med {energi} enheter. Nytt energinivå: {self.__energinivå:.2f} / {self.__energikapasitet:.2f}")
            else:
                self.__energinivå = self.__energikapasitet
                print(f"Batteri {self.__batteriID}: Kunne ikke lade med {energi} enheter. Batteriet er fullt ({self.__energinivå:.2f} / {self.__energikapasitet:.2f}).")
        else:
            print(f"Batteri {self.__batteriID}: Ugyldig ladeverdi. Må være et positivt tall.")

    def brukEnergi(self, energi: float):
        """
        Bruker en gitt mengde energi fra batteriet.

        Args:
            energi (float): Mengden energi som skal brukes fra batteriet.
        """
        if energi > 0:
            nytt_energinivå = self.__energinivå - energi
            if nytt_energinivå >= 0:
                self.__energinivå = nytt_energinivå
                print(f"Batteri {self.__batteriID}: Brukt {energi} enheter. Nytt energinivå: {self.__energinivå:.2f} / {self.__energikapasitet:.2f}")
            else:
                print(f"Batteri {self.__batteriID}: Ikke nok energi til å bruke {energi} enheter. Gjeldende energinivå: {self.__energinivå:.2f} / {self.__energikapasitet:.2f}")
        else:
            print(f"Batteri {self.__batteriID}: Ugyldig energibruk. Må være et positivt tall.")

    def visEnergiNivå(self) -> float:
        """
        Viser gjeldende energinivå i batteriet.

        Returns:
            float: Gjeldende energinivå.
        """
        return self.__energinivå

# Eksempel på bruk av klassen:
if __name__ == "__main__":
    batteri1 = Batteri("BATT001", 10.0)  # Oppretter et batteri med ID "BATT001" og kapasitet 10.0

    print(f"Initialt energinivå for {batteri1._Batteri__batteriID}: {batteri1.visEnergiNivå():.2f} / {batteri1._Batteri__energikapasitet:.2f}")

    batteri1.ladOpp(5.0)
    batteri1.brukEnergi(2.0)
    batteri1.ladOpp(8.0)
    batteri1.brukEnergi(12.0)

    print(f"Endelig energinivå for {batteri1._Batteri__batteriID}: {batteri1.visEnergiNivå():.2f} / {batteri1._Batteri__energikapasitet:.2f}")