import random


class Character:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def __str__(self):
        return f"Navn: {self.name}, Level: {self.level}, HP: {self.hp}"

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        # Angrepsstyrken avhenger av level
        return random.randint(1, self.level * 2)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


class Player(Character):
    def __init__(self, name, level, hp, strength):
        super().__init__(name, level, hp)
        self.strength = strength

    def __str__(self):
        return f"{super().__str__()}, Styrke: {self.strength}"

    def attack(self):
        # Spilleren bruker styrke i stedet for level
        return random.randint(1, self.strength)


class Enemy(Character):
    def __init__(self, name, level, hp, weapon):
        super().__init__(name, level, hp)
        self.weapon = weapon

    def __str__(self):
        return f"{super().__str__()}, Våpen: {self.weapon}"


# Denne koden kjøres bare når du starter karakterer.py direkte,
# ikke når fila importeres fra en annen fil.
# Spesifisering: "Kjør dette bare hvis denne fila er den som ble startet."
# ..da __name__ er "__main__" for den filen du starter direkte (trenger ikke hete main.py).
if __name__ == "__main__":
    test_spiller = Player("Test", 1, 100, 10)
    test_fiende = Enemy("Testfiende", 2, 50, "pinne")
    print(test_spiller)
    print(test_fiende)
