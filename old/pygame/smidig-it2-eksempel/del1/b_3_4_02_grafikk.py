import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 350, 600
FPS = 24


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Geometriske figurer")
        self.running = True
        self.all_sprites = pg.sprite.Group()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)

        # gemometriske figurer
        pg.draw.line(self.screen, 'red', (50,50), (50,150),5)
        pg.draw.rect(self.screen, 'blue', (100,50,50,100))
        pg.draw.rect(self.screen, 'green', (50,200,100,50),10)
        pg.draw.circle(self.screen, 'yellow', (250,100), 50)
        pg.draw.circle(self.screen, 'purple', (250,225), 50,10)
        pg.draw.ellipse(self.screen, 'pink', (50,300,250,100))
        pg.draw.arc(self.screen, 'orange', (50,450,250,100), 0, 1.5*3.14, 5)

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