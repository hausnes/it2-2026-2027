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

    def describe(self, row, col):
        return CELLETYPER[self.grid[row][col]]

    def show(self, player):
        # Skriver ut kartet. P viser hvor spilleren står.
        for row in range(self.height):
            line = ""
            for col in range(self.width):
                if row == player.row and col == player.col:
                    line += "P "
                else:
                    line += str(self.grid[row][col]) + " "
            print(line)


class Player:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

    def move(self, d_row, d_col, game_map):
        new_row = self.row + d_row
        new_col = self.col + d_col

        if not game_map.is_inside(new_row, new_col):
            print("Du kan ikke gå utenfor kartet.")
        elif game_map.is_blocked(new_row, new_col):
            print("Det står en hindring i veien.")
        else:
            self.row = new_row
            self.col = new_col

        print(f"Du står nå på {game_map.describe(self.row, self.col)}.")


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

# Hvor mye rad og kolonne endres for hver tast
RETNINGER = {
    "w": (-1, 0),  # opp
    "s": (1, 0),  # ned
    "a": (0, -1),  # venstre
    "d": (0, 1),  # høyre
}

while True:
    game_map.show(spiller)
    valg = input("Gå med w/a/s/d (q for å avslutte): ").lower()

    if valg == "q":
        break
    elif valg in RETNINGER:
        d_row, d_col = RETNINGER[valg]
        spiller.move(d_row, d_col, game_map)
    else:
        print("Ugyldig valg.")
    print()
