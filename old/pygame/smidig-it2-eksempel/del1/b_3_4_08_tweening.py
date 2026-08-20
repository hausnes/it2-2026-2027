import pygame as pg
from pygame.locals import *
import pytweening as tween

WIDTH, HEIGHT = 150, 400
FPS = 24


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "yellow", (25, 25), 25)
        pg.draw.circle(self.image, "red", (25, 25), 25, 5)
        self.rect.x = (WIDTH-self.rect.width)/2
        self.rect.y = 0
        self.bilder = FPS * 2  # Tweening i 2 sekunder
        self.teller = 0

    def update(self):
        self.teller += 1
        avstand = HEIGHT - self.rect.height

        # Tween i 2 sekunder
        if self.teller <= self.bilder:
            y = avstand * tween.easeOutBounce(self.teller / self.bilder)
        # La ballen ligge nede i 1 sekund
        elif self.teller <= FPS * 3:
            y = avstand
        # Start på nytt etter 3. sekunder
        else:
            y = 0
            self.teller = 0

        self.rect.y = y


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("EaseOutBounce Tweening")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.ball = Ball()
        self.all_sprites.add(self.ball)
        self.teller = FPS * 2

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