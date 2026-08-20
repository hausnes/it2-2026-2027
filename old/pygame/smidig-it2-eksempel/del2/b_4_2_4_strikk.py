# En linje (strikk) fra midten av skjermen til musepekeren
import pygame as pg
from pygame.locals import *

BREDDE, HØYDE = 500, 500
FPS = 25


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((BREDDE, HØYDE))
        pg.display.set_caption("Strikk")
        self.clock = pg.time.Clock()
        self.running = True
        self.pos = (250, 250)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEMOTION:
                self.pos = event.pos

    def update(self):
        pass

    def draw(self):
        self.screen.fill("grey")
        pg.draw.line(self.screen, "black", (250, 250), self.pos, width=5)
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