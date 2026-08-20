# Røde baller "spiser" grønne baller
import pygame as pg
from random import choice, randint

# Innstillinger
WIDTH, HEIGHT = 600, 600
FPS = 24
RED = (255, 0, 0)
DARKGREEN = (0, 100, 0)
BG_COLOR = (200, 200, 200)


class Ball(pg.sprite.Sprite):
    def __init__(self, color=RED):
        super().__init__()
        self.color = color
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.radius = 25
        pg.draw.circle(self.image, self.color, self.rect.center, self.radius)

        # Sett tilfeldig startposisjon
        self.rect.top = randint(0, HEIGHT - self.rect.height)
        self.rect.left = randint(0, WIDTH - self.rect.width)

        # Sett tilfeldig hastighet
        self.speed = [choice([-1, 1]) * randint(1, 2), randint(1, 2)]

    def update(self):
        # Beveg ballen
        self.rect.move_ip(self.speed)

        # Sprett tilbake fra kantene
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
            self.rect.x = min(max(self.rect.x, 0), WIDTH - self.rect.width)
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] *= -1
            self.rect.y = min(max(self.rect.y, 0), HEIGHT - self.rect.height)


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Røde baller "spiser" grønne baller')

        # Opprett ballgrupper
        self.red_balls = pg.sprite.Group()
        self.green_balls = pg.sprite.Group()
        for _ in range(5):
            self.red_balls.add(Ball(RED))
            self.green_balls.add(Ball(DARKGREEN))
        self.running = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        # Sjekk for kollisjoner og fjern kolliderende grønne baller
        pg.sprite.groupcollide(
            self.red_balls,
            self.green_balls,
            False,
            True,
            collided=pg.sprite.collide_circle,
        )

        # Oppdater ballposisjoner
        self.red_balls.update()
        self.green_balls.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.red_balls.draw(self.screen)
        self.green_balls.draw(self.screen)
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