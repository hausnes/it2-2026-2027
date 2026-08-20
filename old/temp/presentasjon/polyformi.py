class Spillfigur:
    def __init__(self, navn, helse):
        self.navn = navn
        self.helse = helse

    def angrip(self, mål):
        print(f"{self.navn} angriper {mål.navn}!")

    def motta_skade(self, skade):
        self.helse -= skade
        print(f"{self.navn} mottar {skade} skade. Gjenværende helse: {self.helse}")
        if self.helse <= 0:
            print(f"{self.navn} er beseiret!")

class Helt(Spillfigur):
    def __init__(self, navn, helse, spesialangrep):
        super().__init__(navn, helse)
        self.spesialangrep = spesialangrep

    def angrip(self, mål):
        print(f"{self.navn} bruker {self.spesialangrep} og angriper {mål.navn}!")
        mål.motta_skade(15) # Heltens angrep gjør mer skade

class Fiende(Spillfigur):
    def __init__(self, navn, helse, type):
        super().__init__(navn, helse)
        self.type = type

    def angrip(self, mål):
        print(f"{self.navn} ({self.type}) gjør et vilt angrep mot {mål.navn}!")
        mål.motta_skade(10) # Fiendens angrep gjør moderat skade