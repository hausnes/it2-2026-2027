import random

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.magi_angrep = {
            "fireball": 30,
            "lightning": 25,
            "ice shard": 20,
            "earthquake": 35
        }

    def is_alive(self):
        return self.hp > 0

    def velg_magi_angrep(self):
        print("\nVelg et magi-angrep:")
        angrep_liste = list(self.magi_angrep.keys())
        for i in range(len(angrep_liste)):
            print(f"{i + 1}. {angrep_liste[i].capitalize()} (Skade: {self.magi_angrep[angrep_liste[i]]})")
        valg = int(input("Skriv inn nummeret på angrepet du vil bruke: ")) - 1
        angrep_navn = angrep_liste[valg]
        skade = self.magi_angrep[angrep_navn]
        return angrep_navn, skade

    def utfør_magi_angrep(self, angrep_navn, skade, mål):
        print(f"\n{self.name} bruker {angrep_navn} på {mål.name} og gjør {skade} skade!")
        mål.hp -= skade
        if mål.hp < 0:
            mål.hp = 0

# Eksempel på bruk
helt = Character("Tor", 200)
fiende = Character("Loke", 150)

print(f"{helt.name} har {helt.hp} HP.")
print(f"{fiende.name} har {fiende.hp} HP.")

while helt.is_alive() and fiende.is_alive():
    angrep_navn, skade = helt.velg_magi_angrep()
    helt.utfør_magi_angrep(angrep_navn, skade, fiende)
    print(f"{fiende.name} har nå {fiende.hp} HP.")
    if not fiende.is_alive():
        print(f"{fiende.name} er beseiret!")
        break

    # Fienden angriper tilbake (for enkelhetens skyld velger vi et tilfeldig angrep)
    angrep_navn, skade = random.choice(list(fiende.magi_angrep.items()))
    fiende.utfør_magi_angrep(angrep_navn, skade, helt)
    print(f"{helt.name} har nå {helt.hp} HP.")
    if not helt.is_alive():
        print(f"{helt.name} er beseiret!")
        break