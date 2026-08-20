class Organisme:
    def __init__(self, navn):
        self.navn = navn
    
    def leve(self):
        return f"{self.navn} er en levende organisme."
    
    def bevege_seg(self):
        return f"{self.navn} beveger seg på en eller annen måte."

class Dyr(Organisme):  
    def __init__(self, navn, antall_bein):
        super().__init__(navn)  # Kaller superklassens init-metode
        self.antall_bein = antall_bein

    def bevege_seg(self):
        return f"{self.navn} kan bevege seg med sine {self.antall_bein} bein."

class Fugl(Dyr):  
    def __init__(self, navn, vingespenn):
        super().__init__(navn, 2)  # Fugl har alltid to bein
        self.vingespenn = vingespenn

    def fly(self):
        return f"{self.navn} kan fly med et vingespenn på {self.vingespenn} meter."

    def bevege_seg(self):
        return f"{self.navn} flyr gjennom luften."