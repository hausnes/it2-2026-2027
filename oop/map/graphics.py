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
        mapping = {".": Segment("  ")}
        for char, color in colors.items():
            mapping[char] = Segment("  ", Style(bgcolor=color))

        self.console.print(Pixels.from_ascii(text, mapping))

    def draw_map(self, game_map, player):
        text = ""
        for row in range(game_map.height):
            for col in range(game_map.width):
                if row == player.row and col == player.col:
                    text += "P"
                else:
                    text += str(game_map.grid[row][col])
            text += "\n"
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
