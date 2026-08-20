# poengsystem.py
class PoengSystem:
    def __init__(self):
        self.poeng = 0

    def oppdater_poeng(self, handling):
        if handling == "levert_sau":
            self.poeng += 1

    def hent_poeng(self):
        return self.poeng

# Smidig IT-2 © TIP AS 2024
