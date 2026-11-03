# Enkel pikselgrafikk i terminalen med rich-pixels.
# Installer først: pip install rich-pixels
# Dokumentasjon: https://pypi.org/project/rich-pixels/
#
# Ideen: vi tegner med bokstaver i en tekststreng, og hver bokstav byttes ut
# med en farget rute. "R" kan for eksempel bety en rød rute.

from rich.console import Console
from rich.segment import Segment
from rich.style import Style
from rich_pixels import Pixels

# Fargene på kartet. Nøkkelen er det som står i rutenettet (som tekst),
# pluss "P" for spilleren.
KARTFARGER = {
    "0": "#808080",  # gulv: grått
    "1": "#000000",  # vegg: svart
    "2": "#d00000",  # fiende: rød
    "P": "#00b000",  # spiller: grønn
}

# Fargene i figurene. "." betyr gjennomsiktig (ingen farge).
FIGURFARGER = {
    "H": "#f1c27d",  # hud
    "K": "#000000",  # øyne
    "G": "#00b000",  # grønn trøye
    "B": "#3050c0",  # blå bukse
    "R": "#d00000",  # rød goblin
    "Y": "#ffff00",  # gule goblinøyne
    "g": "#6b4f2a",  # bakken
}

# Alle figurene er 9 ruter brede og 7 ruter høye, slik at de er lette å sette
# ved siden av hverandre. De døde figurene ligger nederst, altså på bakken.
SPILLER = [
    "...HHH...",
    "...KHK...",
    "...HHH...",
    "..GGGGG..",
    ".H.GGG.H.",
    "...B.B...",
    "...B.B...",
]

SPILLER_DØD = [
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    "HH..H....",
    "KHGGGGBBB",
]

GOBLIN = [
    "R..RRR..R",
    ".RRYRYRR.",
    "...RRR...",
    "..RRRRR..",
    ".R.RRR.R.",
    "...R.R...",
    "...R.R...",
]

GOBLIN_DØD = [
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    "....R..RR",
    "RRRRRRRYR",
]


class Graphics:
    def __init__(self):
        self.console = Console()

    def _draw(self, text, colors):
        # Gjør om fargene til Segment-er: to mellomrom med bakgrunnsfarge.
        # To tegn per rute gjør rutene omtrent kvadratiske i terminalen.
        # "." får to mellomrom uten farge, altså en gjennomsiktig rute
        mapping = {".": Segment("  ")}
        # Resten av tegnene får to mellomrom med bakgrunnsfargen sin,
        # f.eks. blir "1" til to svarte mellomrom med KARTFARGER
        for char, color in colors.items():
            mapping[char] = Segment("  ", Style(bgcolor=color))

        # from_ascii slår opp hvert tegn i text i mapping og bytter det ut
        # med segmentet, så skriver console.print resultatet til terminalen
        self.console.print(Pixels.from_ascii(text, mapping))

    def clear(self):
        # Tømmer terminalen, slik at neste tegning havner øverst
        self.console.clear()

    def draw_map(self, game_map, player):
        # Bygger opp kartet som én tekststreng, ett tegn per rute
        text = ""
        for row in range(game_map.height):
            for col in range(game_map.width):
                # Står spilleren her, tegner vi "P" i stedet for det som er i ruta
                if row == player.row and col == player.col:
                    text += "P"
                else:
                    # Tallet i rutenettet gjøres om til tekst, f.eks. 1 -> "1"
                    text += str(game_map.grid[row][col])
            text += "\n"  # ny linje etter hver rad
        # Hvert tegn byttes ut med fargen sin fra KARTFARGER
        self._draw(text, KARTFARGER)

    def draw_sprite(self, sprite):
        # Tegner én figur, f.eks. graphics.draw_sprite(SPILLER)
        self._draw("\n".join(sprite), FIGURFARGER)

    def draw_fight(self, player, enemy):
        # Velger levende eller død figur for hver av dem
        if player.is_alive():
            left = SPILLER
        else:
            left = SPILLER_DØD

        if enemy.is_alive():
            right = GOBLIN
        else:
            right = GOBLIN_DØD

        # Setter figurene ved siden av hverandre, linje for linje
        lines = []
        for i in range(len(left)):
            lines.append(left[i] + "...." + right[i])
        lines.append("g" * len(lines[0]))  # bakken under begge

        self._draw("\n".join(lines), FIGURFARGER)


# Testkode: kjører bare når du starter denne fila direkte (python graphics.py),
# ikke når en annen fil gjør "from graphics import Graphics".
if __name__ == "__main__":

    # Enkle stand-in-klasser med akkurat det Graphics trenger.
    # I spillet bruker du de ekte Map-, Player- og Enemy-klassene i stedet.
    class TestMap:
        def __init__(self, grid):
            self.grid = grid
            self.height = len(grid)
            self.width = len(grid[0])

    class TestPlayer:
        def __init__(self, row, col, hp):
            self.row = row
            self.col = col
            self.hp = hp

        def is_alive(self):
            return self.hp > 0

    class TestEnemy:
        def __init__(self, hp):
            self.hp = hp

        def is_alive(self):
            return self.hp > 0

    graphics = Graphics()

    # 1) draw_sprite: tegner én figur
    print("draw_sprite(SPILLER):")
    graphics.draw_sprite(SPILLER)

    print("draw_sprite(GOBLIN):")
    graphics.draw_sprite(GOBLIN)

    # 2) draw_map: tegner kartet med spilleren som en grønn rute
    #    0 = gulv, 1 = vegg, 2 = fiende
    grid = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    game_map = TestMap(grid)
    player = TestPlayer(row=1, col=1, hp=10)

    print("draw_map(game_map, player):")
    graphics.draw_map(game_map, player)

    # 3) draw_fight: tegner spiller og fiende ved siden av hverandre.
    #    Figuren som har hp <= 0, tegnes som død.
    print("draw_fight: begge lever")
    graphics.draw_fight(player, TestEnemy(hp=5))

    print("draw_fight: goblinen er død")
    graphics.draw_fight(player, TestEnemy(hp=0))

    print("draw_fight: spilleren er død")
    graphics.draw_fight(TestPlayer(row=1, col=1, hp=0), TestEnemy(hp=5))
