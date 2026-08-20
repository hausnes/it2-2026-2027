class Spillfigur:
    def __init__(self, navn, helse, hemmelig_styrke):
        self.navn = navn
        self._helse = helse  # Indikerer beskyttet
        self.__hemmelig_styrke = hemmelig_styrke  # Indikerer privat

    def angrip(self, mål):
        print(f"{self.navn} angriper {mål.navn}!")
        # Den hemmelige styrken kan påvirke angrepet internt
        skade = 10 + self.__hemmelig_styrke // 5
        mål.motta_skade(skade)

    def _sjekk_om_levende(self):
        return self._helse > 0

    def motta_skade(self, skade):
        if self._sjekk_om_levende():
            self._helse -= skade
            print(f"{self.navn} mottar {skade} skade. Gjenværende helse: {self._helse}")
            if not self._sjekk_om_levende():
                print(f"{self.navn} er beseiret!")
        else:
            print(f"{self.navn} er allerede beseiret.")

    def helbred(self, mengde):
        if self._sjekk_om_levende():
            self._helse += mengde
            print(f"{self.navn} helbredes med {mengde}. Ny helse: {self._helse}")
        else:
            print(f"{self.navn} kan ikke helbredes.")

    def avslor_hemmelig_styrke(self, kode):
        if kode == "topphemmelig":
            return self.__hemmelig_styrke
        else:
            return "Tilgang nektet."