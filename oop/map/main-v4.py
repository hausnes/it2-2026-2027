import random

# Grafikken ligger i en egen fil, graphics.py (krever: pip install rich-pixels)
from graphics import Graphics

# Tallene i rutenettet betyr:
# 0 = gulv, 1 = hindring, 2 = fiende
CELLETYPER = {
    0: "en gulvcelle",
    1: "en hindring",
    2: "en fiende",
}


class Map:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)  # antall rader
        self.width = len(grid[0])  # antall kolonner

    def is_inside(self, row, col):
        return 0 <= row < self.height and 0 <= col < self.width

    def is_blocked(self, row, col):
        return self.grid[row][col] == 1

    def has_enemy(self, row, col):
        return self.grid[row][col] == 2

    def remove_enemy(self, row, col):
        # Fienden er beseiret, så cellen blir vanlig gulv
        self.grid[row][col] = 0

    def describe(self, row, col):
        return CELLETYPER[self.grid[row][col]]


# Nytt i v4: metodene returnerer meldingen i stedet for å printe den.
# Skjermen tømmes før hver tegning, så en print() her ville blitt
# slettet med en gang. Hovedløkka skriver ut meldingen etter tegningen.


class Player:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        self.max_hp = 30
        self.hp = self.max_hp
        self.defending = False

    def is_alive(self):
        return self.hp > 0

    def move(self, d_row, d_col, game_map):
        new_row = self.row + d_row
        new_col = self.col + d_col

        if not game_map.is_inside(new_row, new_col):
            message = "Du kan ikke gå utenfor kartet.\n"
        elif game_map.is_blocked(new_row, new_col):
            message = "Det står en hindring i veien.\n"
        else:
            self.row = new_row
            self.col = new_col
            message = ""

        return message + f"Du står nå på {game_map.describe(self.row, self.col)}."

    def attack(self, enemy):
        damage = random.randint(4, 8)
        enemy.hp -= damage
        return f"{self.name} angriper og gjør {damage} skade."

    def defend(self):
        # Gjelder bare for neste angrep fra fienden
        self.defending = True
        return f"{self.name} hever skjoldet."

    def heal(self):
        amount = 6
        # min() sørger for at vi ikke får mer enn max_hp
        self.hp = min(self.hp + amount, self.max_hp)
        return f"{self.name} healer seg og har nå {self.hp} HP."

    def take_damage(self, damage):
        if self.defending:
            damage = damage // 2  # halv skade når vi forsvarer oss
            self.defending = False
        self.hp -= damage
        return damage


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def attack(self, player):
        damage = random.randint(3, 7)
        actual_damage = player.take_damage(damage)
        return f"{self.name} angriper og gjør {actual_damage} skade."


# Hva spilleren kan gjøre i en kamp
KAMPVALG = {
    "a": "angrip",
    "f": "forsvar",
    "h": "heal",
}


def draw_fight_screen(player, enemy, graphics, message):
    # Tømmer skjermen og tegner hele kampbildet på nytt
    graphics.clear()
    graphics.draw_fight(player, enemy)
    print(f"{player.name}: {player.hp} HP   {enemy.name}: {enemy.hp} HP")
    print(message)


def fight(player, enemy, graphics):
    # Returnerer True hvis spilleren vinner, og False hvis spilleren taper
    message = f"En {enemy.name} dukker opp! Kampen starter."

    while player.is_alive() and enemy.is_alive():
        draw_fight_screen(player, enemy, graphics, message)
        valg = input("Angrip (a), forsvar (f) eller heal (h): ").lower()

        if valg not in KAMPVALG:
            message = "Ugyldig valg."
            continue  # spør på nytt, fienden får ikke angripe

        # Spillerens tur
        if valg == "a":
            message = player.attack(enemy)
        elif valg == "f":
            message = player.defend()
        elif valg == "h":
            message = player.heal()

        # Fiendens tur, men bare hvis den fortsatt lever.
        # "\n" gjør at meldingene havner på hver sin linje.
        if enemy.is_alive():
            message += "\n" + enemy.attack(player)

    # Tegner en siste gang, nå ligger en av dem død på bakken
    if player.is_alive():
        message += f"\n\nDu beseiret {enemy.name}!"
    else:
        message += f"\n\n{player.name} ble beseiret ..."
    draw_fight_screen(player, enemy, graphics, message)

    # Venter, ellers blir resultatet slettet med en gang kartet tegnes igjen
    input("Trykk Enter for å fortsette ...")
    return player.is_alive()


# Hver indre liste er én rad. grid[rad][kolonne]
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 2, 1, 0],
    [1, 0, 0, 0, 2],
]

game_map = Map(grid)
spiller = Player("Kari", 0, 0)
graphics = Graphics()

# Hvor mye rad og kolonne endres for hver tast
RETNINGER = {
    "w": (-1, 0),  # opp
    "s": (1, 0),  # ned
    "a": (0, -1),  # venstre
    "d": (0, 1),  # høyre
}

# Meldingen fra forrige trekk, som skrives ut under kartet
message = "Velkommen! Finn og beseir fiendene."

while True:
    # Tømmer skjermen og tegner alt på nytt, slik at kartet alltid står øverst
    graphics.clear()
    graphics.draw_map(game_map, spiller)
    print(f"{spiller.name}: {spiller.hp}/{spiller.max_hp} HP")
    print(message)
    valg = input("Gå med w/a/s/d (q for å avslutte): ").lower()

    if valg == "q":
        break
    elif valg in RETNINGER:
        d_row, d_col = RETNINGER[valg]
        message = spiller.move(d_row, d_col, game_map)

        if game_map.has_enemy(spiller.row, spiller.col):
            fiende = Enemy("Goblin", 15)
            if fight(spiller, fiende, graphics):
                game_map.remove_enemy(spiller.row, spiller.col)
                message = f"Du beseiret {fiende.name}. Ruta er nå gulv."
            else:
                print("Spillet er over.")
                break
    else:
        message = "Ugyldig valg."
