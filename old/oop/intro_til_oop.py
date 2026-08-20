'''
    Dette er eit eksempel på korleis ein kan bruke objektorientert programmering (OOP) i Python.
    Koden viser korleis ein kan definere ein klasse, og korleis ein kan bruke denne klassen til å lage instansar av klassen.

    Alternativ 1:
    Det første eksempelet viser ein klasse med private attributtar, og korleis ein kan bruke getters og setters for å endre attributtar.
    Les meir om denne metoden her: https://realpython.com/python-getter-setter/ - her kan du lese litt diskusjon om korleis det er 
    vanleg å gjere dette i Python.
'''

class Character:
    ''' 
        Dette er ein klasse for å representere ein karakter i eit spel. 
        Klassen har fire attributt: name, level, hp og mana. 
        ...
    '''
    def __init__(self, name, hp):
        self.__name = name # Dette er eit privat attributt, kjenneteikna med underscore.
        self.__hp = hp

    def __str__(self):
        return f"\nNavn: {self.get_name()}, HP: {self.get_hp()}\n"

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        self.__hp = new_hp
    
    def is_alive(self):
        return self.__hp > 0

print("------------------------\n")
print("VERSJON 1:")

# Opprettar ein instans av klassen Character, og printar ut informasjonen om denne.    
fiende = Character("Rektor", 100)
print(fiende)

# Ser på ulike måtar å endre attributter på.
# 1. Direkte manipulasjon av attributtet hp, som er privat.
fiende.__hp = 0 # Dette vil ikkje endre attributtet hp, fordi hp er privat.
print(f"Direkte manipulasjon av attributtet hp: {fiende.get_hp()}")

# 2. Endring ved bruk av name mangling (ikkje anbefalt)
fiende._Character__hp = 50
print(f"Direkte manipulasjon av attributtet hp ved bruk av name mangling: {fiende.get_hp()}")

# 3. Endring av attributtet hp via metode.
fiende.set_hp(0)
print(f"Endring av attributtet hp via metode: {fiende.get_hp()}")

# Sjekkar om instansen er i live.
print(f"Fienden er i live: {fiende.is_alive()}")

print("\n------------------------\n")

print("VERSJON 2:")

''' 
    Alternativ måte å definere klassen på:
    Her nyttar me ikkje getters og setters, og me har ikkje private attributt.
    Her brukar me ein decorator for å definere ein property. Dette betyr at me kan aksessere metoden som om 
    det var eit attributt. Eksempelvis: fiende.is_alive. 
    Til slutt er det lagt til typeannotasjonar, som kan gjere koden meir lesbar og hjelpe med statisk typekontroll. NB: Valfritt!
'''
import random

class Character_v2:
    def __init__(self, name: str, level: int, hp: int, mana: int):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana

    def __str__(self) -> str:
        return f"\nNavn: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}\n"

    @property
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def attack(self) -> int:
        # Angrepsstyrken kan vere basert på level eller andre attributt
        return random.randint(1, self.level * 2)
    
    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

# Opprettar ein instans av klassen Character_v2, og printar ut informasjonen om instansen.
fiende2 = Character_v2("ASS Rektor", 1, 100, 100)
print(fiende2)
# Endrar hp-attributtet for instansen, og sjekkar om instansen er i live.
fiende2.hp = 50
print(f"Fienden er i live etter direkte manipulasjon: {fiende2.is_alive} ({fiende2.hp} hp)")

'''
    Om å arve frå Character_v2:
'''

# Eksempel på en subklasse av Character_v2
class Player(Character_v2):
    '''
        Dette er helten i spelet, som arvar frå den meir generelle klassen Character_v2.
    '''
    def __init__(self, name: str, level: int, hp: int, mana: int, strength: int, dexterity: int, intelligence: int):
        super().__init__(name, level, hp, mana)
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        
    def __str__(self) -> str:
        return (f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, "
                f"Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}")
    
    def attack(self):
        return random.randint(1, self.strength)

# Opprettar ein helt i spelet, og printar ut informasjon om denne.
spiller = Player("Jo Bjørnar", 1, 100, 100, 10, 10, 10)
print(spiller)

# Gjer eit angrep med helten, og printar ut kor mykje skade angrepet gjer.
skade = spiller.attack()
print(f"Spelaren gjorde {skade} skade!")
fiende2.take_damage(skade)
print(f"Fienden har {fiende2.hp} hp igjen.")

print("\n------------------------")