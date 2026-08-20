'''
    Typeannotasjoner i Python er meint for å gje informasjon om kva typar verdiar som forventast, 
    men dei handterast ikkje av sjølve Python-språket ved køyring. Dei er primært meint for å 
    hjelpe utviklarar og verktøy som typekontrollere (f.eks. mypy) med å oppdage potensielle feil.

    Du kan eventuelt skrive din eigen implementasjon av ein enkel typekontroller, slik som i 
    klassen under.
'''

class Character:
    def __init__(self, name: str, level: int, hp: int, mana: int):
        if not isinstance(name, str):
            raise TypeError(f"Expected name to be a string, got {type(name).__name__}")
        if not isinstance(level, int):
            raise TypeError(f"Expected level to be an int, got {type(level).__name__}")
        if not isinstance(hp, int):
            raise TypeError(f"Expected hp to be an int, got {type(hp).__name__}")
        if not isinstance(mana, int):
            raise TypeError(f"Expected mana to be an int, got {type(mana).__name__}")

        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana

# Eksempel på bruk
try:
    character = Character("Gandalf", "high", 100, 50)  # Dette vil kaste en TypeError
except TypeError as e:
    print(e)