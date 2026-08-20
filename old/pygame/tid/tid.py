import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 600
FPS = 24


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tidsstyring")
        self.timer = pg.time.get_ticks()
        self.timer_20 = pg.time.get_ticks()
        self.running = True
        self.all_sprites = pg.sprite.Group()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        if pg.time.get_ticks() - self.timer > 5000:
            self.timer = pg.time.get_ticks()
            print("Fem sekund har gått.")

        if pg.time.get_ticks() - self.timer_20 > 20000:
            self.timer_20 = pg.time.get_ticks()
            print("Tjue sekund har gått, restarter!")

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        print("Programmet avsluttes.")
        pg.quit()


if __name__ == "__main__":
    app = App()
    app.run()