# Kollisjon mellom to baller
import pygame as pg
from pygame.locals import *
from random import randint

WIDTH, HEIGHT = 400, 100
FPS = 24


class Ball(pg.sprite.Sprite):
    def __init__(self, color, speed, pos="left"):
        super().__init__()
        self.dx = speed
        self.image = pg.Surface([50, 50], pg.SRCALPHA)

        self.rect = self.image.get_rect()
        self.rect.x = 0 if pos == "left" else WIDTH - self.rect.width
        self.rect.y = (HEIGHT - self.rect.height) / 2
        pg.draw.circle(self.image, color, (25, 25), 25)
        pg.draw.circle(self.image, "yellow", (25, 25), 25, 5)
        self.radius = 25
        self.dx = speed

    def update(self):
        self.rect.x += self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

    def collide(self):
        self.dx *= -1
        self.rect.x += self.dx


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Baller som kolliderer")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.ball_1 = Ball("red", 5, "left")
        self.all_sprites.add(self.ball_1)
        self.ball_2 = Ball("blue", -2, "right")
        self.all_sprites.add(self.ball_2)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        if pg.sprite.collide_circle(self.ball_1, self.ball_2):
            self.ball_1.collide()
            self.ball_2.collide()
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