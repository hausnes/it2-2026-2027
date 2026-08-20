import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 200, 100
FPS = 24


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Last inn lydfilene
        pg.mixer.init()
        self.PING = pg.mixer.Sound("ping.mp3")
        self.PONG = pg.mixer.Sound("pong.mp3")
        
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "yellow", (25, 25), 25)
        pg.draw.circle(self.image, "red", (25, 25), 25, 5)
        self.rect.x = 0
        self.rect.y = (HEIGHT-self.rect.height)/2
        self.dx = 5

    def update(self):
        self.rect.x += self.dx

        # Sjekk om ballen treffer kanten
        if self.rect.left < 0 or self.rect.right > WIDTH:
            # Snu fartsretningen
            self.dx *= -1

            # Spill av lyd
            if self.dx < 0:
                self.PING.play()  # Traff høyre kant
            else:
                self.PONG.play()  # Traff venstre kant


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
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