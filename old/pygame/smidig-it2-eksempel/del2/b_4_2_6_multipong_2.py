# Multipong Del 2 Kollisjoner med padden
import pygame as pg
from pygame.locals import *
from random import choice, randint

WIDTH, HEIGHT = 300, 500
FPS = 24


class Padde(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 80
        self.height = 15
        self.image = pg.Surface((self.width, self.height))
        self.image.fill("lightblue")
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 15
        self.rect.centerx = WIDTH / 2
        self.speed = 5


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.image.fill(choice(["red", "green", "blue"]))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = randint(0, WIDTH - self.rect.width)
        self.speed = [choice([-1, 1]) * randint(3, 5), randint(3, 5)]

    def update(self):
        self.rect.move_ip(self.speed)

        # Snu x-hastigheten hvis den treffer en sidevegg
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
            self.rect.x = min(max(self.rect.x, 0), WIDTH - self.rect.width)

        # Slett ballen når den er utenfor skjermen
        if self.rect.top > HEIGHT:
            self.kill()


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Multipong Del 2")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.padde = Padde()
        self.all_sprites.add(self.padde)
        self.timer = pg.time.get_ticks()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        # Plasser en ny ball på banen med jevne mellomrom
        if pg.time.get_ticks() - self.timer >= 1000:
            self.timer = pg.time.get_ticks()
            self.all_sprites.add(Ball())

        # Detekter kollisjon  mellom padden og ballene
        hits = pg.sprite.spritecollide(self.padde, self.all_sprites, False)
        for hit in hits:
            if isinstance(hit, Ball):
                hit.speed[1] *= -1
                # flytt ballen opp for å unngå umiddelbar ny kollisjon
                hit.rect.top = self.padde.rect.top - hit.rect.height

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