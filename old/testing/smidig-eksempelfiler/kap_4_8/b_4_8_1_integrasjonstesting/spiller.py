# spiller.py
from poengsystem import PoengSystem


class Spiller:
    def __init__(self, navn):
        self.navn = navn
        self.poengsystem = PoengSystem()

    def oppdater_poeng(self, handling):
        self.poengsystem.oppdater_poeng(handling)

# Smidig IT-2 © TIP AS 2024
