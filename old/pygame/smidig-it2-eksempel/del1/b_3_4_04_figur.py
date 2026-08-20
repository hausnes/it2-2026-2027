import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 300, 200
FPS = 24


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "yellow", (25, 25), 25)
        pg.draw.circle(self.image, "red", (25,25), 25, 5)
        self.rect.x = (WIDTH-self.rect.width)/2
        self.rect.y = (HEIGHT-self.rect.height)/2


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Figurer")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.ball = Ball()
        self.all_sprites.add(self.ball)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

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
        pg.quit()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS, 2024