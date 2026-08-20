'''

NB: Uferdig - ikkje fungerandre eksempel!

'''

import pygame as pg
from pygame.locals import *
import random

WIDTH, HEIGHT = 400, 600
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, x_fart, y_fart, radius, color, vindusobjekt):
        super().__init__()
        self.image = pg.Surface((radius*2, radius*2), pg.SRCALPHA)
        pg.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x_fart = x_fart
        self.y_fart = y_fart
        self.vindusobjekt = vindusobjekt

    def update(self):
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart

        # Kollisjon med vegger
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.x_fart *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.y_fart *= -1

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()

        self.balls = pg.sprite.Group()
        # Opprett baller
        for i in range(5):
            ball = Ball(
                x=random.randint(50, WIDTH-50),
                y=random.randint(50, HEIGHT-50),
                x_fart=random.randint(-5, 5),
                y_fart=random.randint(-5, 5),
                radius=20,
                color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                vindusobjekt=self.screen,
            )
            self.balls.add(ball)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()
        # Oppdater alle baller
        self.balls.update()

        # Kollisjonsdeteksjon mellom baller
        collisions = pg.sprite.groupcollide(self.balls, self.balls, False, False)
        for ball1, collided_balls in collisions.items():
            for ball2 in collided_balls:
                ball1.x_fart *= -1
                ball1.y_fart *= -1
                ball2.x_fart *= -1
                ball2.y_fart *= -1

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        self.balls.draw(self.screen)
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