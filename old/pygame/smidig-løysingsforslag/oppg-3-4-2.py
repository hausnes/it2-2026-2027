'''
3.4.2
Lag et program med følgende spesifikasjoner
• Vinduet skal ha størrelsen 500x500
• En ball med diameter 40 piksler skal gå rundt i sirkel inni
vinduet
• Sirkelen skal ha en diameter på 400 piksler og være sentrert i
vindue
'''

import pygame as pg
from pygame.locals import *
import math

WIDTH, HEIGHT = 500, 500
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40,40))
        self.image.set_colorkey('black')
        pg.draw.circle(self.image, "darkblue", (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vinkel  = 0
        self.vinkelhastighet = 2*math.pi/(2*FPS)

    def update(self):
        self.vinkel += self.vinkelhastighet
        self.rect.x = WIDTH/2 + 200 * math.cos(self.vinkel) -20
        self.rect.y = HEIGHT/2 + 200 * math.sin(self.vinkel) -20

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Ball som går i sirkel")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        ball = Ball()
        self.all_sprites.add(ball)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("lightblue")
        self.all_sprites.draw(self.screen)
        pg.draw.circle(self.screen, "black", (WIDTH//2, HEIGHT//2), 200, 1)
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