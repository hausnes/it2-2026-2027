class Batteri:
    def __init__(self, batteriID: str, energikapasitet: float):
        """
        Konstruktør for Batteri-klassen.

        Args:
            batteriID (str): En unik identifikator for batteriet.
            energikapasitet (float): Batteriets totale energikapasitet.

        Raises:
            TypeError: Hvis batteriID ikke er en streng eller None.
            ValueError: Hvis energikapasitet ikke er positiv.
            ValueError: Hvis batteriID er en tom streng.
        """
        if not isinstance(batteriID, str):
            raise TypeError("Batteri-ID må være en streng.")
        if not batteriID:
            raise ValueError("Batteri-ID kan ikke være en tom streng.")
        if not isinstance(energikapasitet, (int, float)) or energikapasitet <= 0:
            raise ValueError("Energikapasitet må være et positivt tall.")

        self.__batteriID = batteriID
        self.__energikapasitet = energikapasitet
        self.__energinivå = 0.0  # Initialiserer energinivået til 0 ved opprettelse

    def ladOpp(self, energi: float):
        """
        Lader opp batteriet med en gitt mengde energi.

        Args:
            energi (float): Mengden energi som skal legges til batteriet.

        Returns:
            bool: True hvis ladingen ble utført, False ellers.
        """
        if not isinstance(energi, (int, float)):
            print(f"Batteri {self.__batteriID}: Ugyldig ladeverdi. Må være et tall.")
            return False
        if energi <= 0:
            print(f"Batteri {self.__batteriID}: Ugyldig ladeverdi. Må være et positivt tall.")
            return False

        nytt_energinivå = self.__energinivå + energi
        if nytt_energinivå <= self.__energikapasitet:
            self.__energinivå = nytt_energinivå
            print(f"Batteri {self.__batteriID}: Ladet opp med {energi:.2f} enheter. Nytt energinivå: {self.__energinivå:.2f} / {self.__energikapasitet:.2f}")
            return True
        else:
            self.__energinivå = self.__energikapasitet
            print(f"Batteri {self.__batteriID}: Kunne ikke lade med {energi:.2f} enheter. Batteriet er fullt ({self.__energinivå:.2f} / {self.__energikapasitet:.2f}).")
            return True

    def brukEnergi(self, energi: float):
        """
        Bruker en gitt mengde energi fra batteriet.

        Args:
            energi (float): Mengden energi som skal brukes fra batteriet.

        Returns:
            bool: True hvis energibruken ble utført, False ellers.
        """
        if not isinstance(energi, (int, float)):
            print(f"Batteri {self.__batteriID}: Ugyldig energibruk. Må være et tall.")
            return False
        if energi <= 0:
            print(f"Batteri {self.__batteriID}: Ugyldig energibruk. Må være et positivt tall.")
            return False

        nytt_energinivå = self.__energinivå - energi
        if nytt_energinivå >= 0:
            self.__energinivå = nytt_energinivå
            print(f"Batteri {self.__batteriID}: Brukt {energi:.2f} enheter. Nytt energinivå: {self.__energinivå:.2f} / {self.__energikapasitet:.2f}")
            return True
        else:
            print(f"Batteri {self.__batteriID}: Ikke nok energi til å bruke {energi:.2f} enheter. Gjeldende energinivå: {self.__energinivå:.2f} / {self.__energikapasitet:.2f}")
            return False

    def visEnergiNivå(self) -> float:
        """
        Viser gjeldende energinivå i batteriet.

        Returns:
            float: Gjeldende energinivå.
        """
        return self.__energinivå