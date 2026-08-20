# Kanon som kan flyttes med piltastene
# og avfyre granater med mellomromstasten
import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 600
FPS = 24


class Kanon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bredde = 60
        self.høyde = 40
        self.image = pg.Surface((self.bredde, self.høyde), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, "grey", (0, 20, 60, 20))
        pg.draw.rect(self.image, "grey", (25, 0, 10, 20))
        self.rect.bottom = HEIGHT
        self.rect.centerx = WIDTH // 2
        self.fart = 5

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.fart
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.fart

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pygame med Kanon")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.kanon = Kanon()
        self.all_sprites.add(self.kanon)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
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