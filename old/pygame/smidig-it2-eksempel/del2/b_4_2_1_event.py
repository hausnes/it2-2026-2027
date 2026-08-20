# Hendelser i Pygame: KEYDOWN og MOUSEBUTTONUP
import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 200
FPS = 24


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Hendelser")
        self.running = True
        self.font = pg.font.SysFont(None, 20)
        self.vis_tastetrykk = False
        self.vis_museklikk = False
        self.museklikk = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                self.vis_tastetrykk = True
                self.tast = pg.key.name(event.key)
            elif event.type == pg.MOUSEBUTTONUP:
                self.vis_museklikk = True
                self.museklikk += 1

    def update(self):
        pass

    def draw(self):
        self.screen.fill("grey")
        tekst_1 = self.font.render("Klikk på musa eller trykk en tast.", True, "black")
        self.screen.blit(tekst_1, (50, 50))
        if self.vis_tastetrykk:
            tekst_2 = self.font.render(
                "Du trykket på en tast: " + str(self.tast), True, "black"
            )
            self.screen.blit(tekst_2, (50, 100))
        if self.vis_museklikk:
            tekst_3 = self.font.render(
                "Du har klikket på musa "
                + str(self.museklikk)
                + (" ganger." if self.museklikk != 1 else " gang."),
                True,
                "black",
            )
            self.screen.blit(tekst_3, (50, 150))
        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS, 2024