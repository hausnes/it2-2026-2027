# Eksempel på tidsstyring i Pygame
import pygame as pg
from pygame.locals import *
from random import randint

WIDTH, HEIGHT = 500, 600
FPS = 24


class Ball(pg.sprite.Sprite):
    def __init__(self, color, x):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, color, (10, 10), 10)
        self.rect.x = x
        self.rect.y = 0

    def update(self):
        self.rect.y += 5

        # Fjern ballen fra sprite-gruppen når den går utenfor vinduet
        if self.rect.top > HEIGHT:
            self.kill()


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tidsstyrte handlinger")
        self.timer = pg.time.get_ticks()
        self.running = True
        self.all_sprites = pg.sprite.Group()
        # ALTERNATIV 3a (Fast tidsintervall)
        # lag en burkerdefinert hendelse hvert 2. sekund
        pg.time.set_timer(pg.USEREVENT, 2000)
        # ALTERNATIV 3b (Fast tidsintervall, men en annen hendelse)
        # lag en annen burkerdefinert hendelse hvert 0.5. sekund
        pg.time.set_timer(pg.USEREVENT + 1, 500)
        # ALTERNATIV 4 (Tilfeldig tidsintervall, også en annen hendelse)
        # lag en annen burkerdefinert hendelse ved tilfeldig tispunkt
        # i snitt hvert 1. sekund
        pg.time.set_timer(pg.USEREVENT + 2, randint(500, 1500), loops=1)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.USEREVENT:
                self.all_sprites.add(Ball("green", 245))
            elif event.type == pg.USEREVENT + 1:
                self.all_sprites.add(Ball("orange", 330))
            elif event.type == pg.USEREVENT + 2:
                self.all_sprites.add(Ball("purple", 415))
                pg.time.set_timer(pg.USEREVENT + 2, randint(500, 1500), loops=1)

    def update(self):
        # ALTERNATIV 1 (Tilfeldig tidsintervall)
        # legg til en ny rød ball ved tilfeldig tidspunkt
        # i snitt  hvert sekund
        if randint(0, FPS - 1) == 0:
            self.all_sprites.add(Ball("red", 75))

        # ALTERNATIV 2 (Fast tidsintervall)
        # legg til en ny blå ball hvert sekund
        # Husk å sette self.timer = pg.time.get_ticks() i __init__
        if pg.time.get_ticks() - self.timer > 1000:
            self.timer = pg.time.get_ticks()
            self.all_sprites.add(Ball("blue", 160))

        # Kun for å sjekke at ballene fjernes fra minnet
        # når de er utenfor vinduet.
        print(len(self.all_sprites))

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