class TekstInfo:
    """En klasse for å analysere tekst"""

    def finn_antall_karakterer(self,tekst:str)->int:
        """ Finner og returnerer antall karakterer i teksten"""
        return len(tekst)
    
    def finn_antall_ord(self, tekst:str)->int:
        """Finner og returnerer antall ord i teksten."""
        ord_liste = tekst.split()
        return len(ord_liste)
        
    def finn_lengste_ordet(self, tekst:str)->str:
        """Finner og returnerer det lengste ordet i teksten."""
        ord_liste = tekst.split()
        return max(ord_liste, key=len)
    
    @staticmethod
    def finn_korteste_ordet(tekst:str)->str:
        """Finner og returnerer det korteste ordet i teksten."""
        ord_liste = tekst.split()
        return min(ord_liste, key=len)
    
# Smidig IT-2 © TIP AS 2024