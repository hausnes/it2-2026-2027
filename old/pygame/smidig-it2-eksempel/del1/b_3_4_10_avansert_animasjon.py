import pygame as pg
from pygame.locals import *
from random import randint, choice

WIDTH, HEIGHT = 500, 500
FPS = 24
ANTALL_BALLER = 25


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.diameter = randint(25, 100)
        self.image = pg.Surface([self.diameter, self.diameter])
        farge = [randint(0, 255) for _ in range(3)]
        self.image.set_colorkey('black')
        radius = self.diameter//2
        pg.draw.circle(self.image, farge, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WIDTH-self.diameter)
        self.rect.y = randint(0, HEIGHT-self.diameter)
        self.dx = choice((-1, 1)) * randint(2, 8)
        self.dy = choice((-1, 1)) * randint(2, 8)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Sjekk om ballen er utenfor skjermen
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1
            self.rect.x = max(0, min(WIDTH - self.diameter, self.rect.x))

        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1
            self.rect.y = max(0, min(HEIGHT - self.diameter, self.rect.y))


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Avansert animasjon")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.timer = pg.time.get_ticks()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):

        # Lag nye baller hvert 2. sekund inntil ANTALL_BALLER
        if pg.time.get_ticks()-self.timer > 2000:
            self.timer = pg.time.get_ticks()
            if len(self.all_sprites) < ANTALL_BALLER:
                self.all_sprites.add(Ball())

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