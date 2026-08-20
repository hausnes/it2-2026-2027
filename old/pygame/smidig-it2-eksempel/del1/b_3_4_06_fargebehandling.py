import pygame as pg
from pygame.locals import *
import math

WIDTH, HEIGHT = 550, 100
FPS = 24


class SolidBall(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "yellow", (25, 25), 25)
        self.rect.x = self.rect.width
        self.rect.y = (HEIGHT-self.rect.height)/2


class TransparentBall(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50), SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "red", (25, 25), 25)
        self.rect.x = 3*self.rect.width
        self.rect.y = (HEIGHT-self.rect.height)/2


class ColorShiftBall(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50), SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = 5 * self.rect.width
        self.rect.y = (HEIGHT - self.rect.height) / 2
        self.time = 0  # Teller for å skifte farge

    def update(self):
        # Regnbuefarger
        self.time += 1 / FPS  # øk tiden med 1/FPS sekunder
        cycle_time = 10       # sekunder
        # Lar fargene skifte med sinusbølger
        # Faseforskyver fargene med 120 grader
        r = int((math.sin(self.time * 2 * math.pi / cycle_time) * 0.5 + 0.5) * 255)
        g = int((math.sin(self.time * 2 * math.pi /
                cycle_time + 2 * math.pi / 3) * 0.5 + 0.5) * 255)
        b = int((math.sin(self.time * 2 * math.pi /
                cycle_time + 4 * math.pi / 3) * 0.5 + 0.5) * 255)
        self.color = pg.Color(r, g, b)
        self.image.fill((0, 0, 0, 0))  # Clear with full transparency
        pg.draw.circle(self.image, self.color, (25, 25), 25)


class OpacityBall(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50), SRCALPHA)
        self.rect = self.image.get_rect()
        self.color = pg.Color("blue")
        pg.draw.circle(self.image, self.color, (25, 25), 25)
        self.rect.x = 7*self.rect.width
        self.rect.y = (HEIGHT-self.rect.height)/2
        self.direction = 'down'

    def update(self):
        if self.direction == 'down':
            self.color.a = max(0, self.color.a - 4)
            if self.color.a <= 0:
                self.direction = 'up'
        else:
            self.color.a = min(255, self.color.a + 4)
            if self.color.a >= 255:
                self.direction = 'down'
        pg.draw.circle(self.image, self.color, (25, 25), 25)


class LerpBall(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50), SRCALPHA)
        self.rect = self.image.get_rect()
        self.color = pg.Color("yellow")
        pg.draw.circle(self.image, self.color, (25, 25), 25)
        self.rect.x = 9*self.rect.width
        self.rect.y = (HEIGHT-self.rect.height)/2
        self.lerp_factor = 1
        self.direction = 1

    def update(self):
        self.lerp_factor += 0.015 * self.direction
        if self.lerp_factor >= 1.0 or self.lerp_factor <= 0.0:
            self.direction *= -1
            self.lerp_factor = max(0, min(1, self.lerp_factor))
        self.color = pg.Color('darkgreen').lerp(
            pg.Color('purple'), self.lerp_factor)
        pg.draw.circle(self.image, self.color, (25, 25), 25)


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Fargebehanling i Pygame")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(SolidBall())
        self.all_sprites.add(TransparentBall())
        self.all_sprites.add(ColorShiftBall())
        self.all_sprites.add(OpacityBall())
        self.all_sprites.add(LerpBall())

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("gray50")
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
