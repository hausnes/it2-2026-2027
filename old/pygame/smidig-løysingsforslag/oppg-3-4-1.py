'''
3.4.1
Lag et program med følgende spesifikasjoner
• Vinduet skal ha størrelsen 600x500
• Tegn et hus omtrent tilsvarende som vist i bildet [i læreboken].

TIPS:
o Se Pygame color list for fargenavn
o Bruk polygon til å tegne taket
'''

import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 600, 500
FPS = 24

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Hus")
        self.running = True
        self.all_sprites = pg.sprite.Group()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("darkblue") # Bakgrunn/himmel
        self.all_sprites.draw(self.screen)

        # Tegn et hus
        pg.draw.rect(self.screen, 'darkgreen', (0,350,600,150)) # Gress
        pg.draw.rect(self.screen, 'red', (100,200,300,200)) # Hus
        pg.draw.rect(self.screen, 'orange', (150,250,50,50)) # Vindu med lys
        pg.draw.rect(self.screen, 'black', (150,250,50,50),2) # Vindusramme
        pg.draw.line(self.screen, 'black', (175,250),(175,300),2) # Sprosse
        pg.draw.line(self.screen, 'black', (150,275),(200,275),2) # Sprosse
        pg.draw.rect(self.screen, 'black', (300,250,50,50)) # Mørkt vindu
        pg.draw.rect(self.screen, 'chocolate3', (225,300,50,100)) # Dør
        pg.draw.polygon(self.screen, 'black', ((75,200),(250,100),(425,200))) # Tak
        pg.draw.rect(self.screen, 'black', (300,100,50,100)) # Pipe
        pg.draw.circle(self.screen, 'grey', (500,100), 40) # Måne

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