'''
Ta utgangspunkt i filen b_3_4_6_enkel_animasjon.py og gjør følgende
endringer:
• Endre bevegelsen til å bruke easeInOutExpo-tween for jevnere animasjon.
• La ballen animere frem og tilbake gjentatte ganger, uten avbrudd.
'''

import pygame as pg
from pygame.locals import *
import pytweening as tween
WIDTH, HEIGHT = 400, 100
FPS = 24

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "yellow", (25, 25), 25)
        pg.draw.circle(self.image, "red", (25, 25), 25, 5)
        self.rect.x = -self.rect.width
        self.rect.y = (HEIGHT-self.rect.height)/2
        self.dx = 5
        self.bilder = FPS * 2
        self.teller = 0

    def update(self):
        # La en runde være fram og tilbake
        total_distance = WIDTH - self.rect.width
        self.teller += 1
        if self.teller >=  2*self.bilder:
            self.teller = 0

        # Bestem retning ved å sjekke om vi er halvveis
        direction = 1 if self.teller/self.bilder < 1 else -1

        # Beregn relativ framgang

        # Alt 1: Kortversjon
        # progress = (self.teller % self.bilder)/self.bilder
        # Alt 2: Langversjon, steg for steg
        # Antall bilder i animasjonen
        antall_bilder = self.bilder
        # Teller som øker med tiden eller antall iterasjoner
        teller = self.teller
        # Finn resten når teller deles på antall bilder
        resten = teller % antall_bilder
        # Beregn fremdriften som en brøkdel av den totale lengden
        fremdrift = resten / antall_bilder
        # Tilordne fremdriften til progress
        progress = fremdrift

        x = total_distance * tween.easeInOutExpo(progress)
        self.rect.x = x if direction == 1 else WIDTH - x - self.rect.width

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tweening")
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