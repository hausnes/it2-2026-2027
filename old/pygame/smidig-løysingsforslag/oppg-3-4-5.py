''' 
Oppgave 3.4.5 Multipong Del 1
IT-2 eksamen, eksempeloppgave 13. Se neste side
• Foreløpig holder det med å lage baller som beveger seg nedover
skjermen.
• Ballene skal endre retning når de treffer sideveggene (sprette
ilbake inn i banen).
• Lag en ny ball hvert sekund.
• Padden og kollisjonene programmerer vi når vi kommer til 4.2
Hendelser , kollisjoner, tidsstyring og GUI-integrering i Pygame
'''

import pygame as pg
from pygame.locals import *
from random import choice, randint

WIDTH, HEIGHT = 300, 500
FPS = 24


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
        pg.display.set_caption("Multipong Del 1")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.timer = pg.time.get_ticks()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        if pg.time.get_ticks() - self.timer >= 1000: # Kvart sekund gen. ein ny ball
            self.timer = pg.time.get_ticks()
            self.all_sprites.add(Ball())

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