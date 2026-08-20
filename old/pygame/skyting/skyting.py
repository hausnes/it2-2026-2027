'''
Enkelt eksempel for å skyte skudd basert på kor spelaren er.
Du navigerer med WASD på tastaturet, og skyt med å trykke med muspeikaren
på skjermen i den retningen du ynskjer.
Nyttar Vector2 frå PyGame og normalize for å handtere retning og fart.
'''

import pygame
import sys
import math

# Initialiser Pygame
pygame.init()

# Skjermoppsett
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skyting ved å bruke vektorar")

# Fargar
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Spelarklassen
class Player:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = BLUE
        self.speed = 5

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Skudd-klassen
class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.color = RED
        self.speed = 10
        self.direction = direction

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Lagar spelarinstans
player = Player(WIDTH // 2, HEIGHT // 2, 50)

# Liste for å halde på skudda
bullets = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Hent mus-posisjon
            mouse_x, mouse_y = event.pos
            # Kalkuler retningsvektoren https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
            direction = pygame.math.Vector2(mouse_x - player.rect.centerx, mouse_y - player.rect.centery)
            print("direction:",direction)
            direction = direction.normalize() # Dette gjer me for skalere lengden (til 1), medan retningen forblir lik
            print("direction, etter normalize:",direction)
            # Lage eit nytt skudd
            bullet = Bullet(player.rect.centerx, player.rect.centery, direction)
            bullets.append(bullet)

    # Handterer spelaren sin bevegelse
    player.handle_keys()

    # Oppdaterer skudda
    for bullet in bullets[:]:
        bullet.update()
        # Fjern skudd som er utanfor skjermen
        if bullet.rect.x < 0 or bullet.rect.x > WIDTH or bullet.rect.y < 0 or bullet.rect.y > HEIGHT:
            bullets.remove(bullet)

    # For testing, kor mange skudd er "aktive"
    # print(len(bullets))

    # Clear skjerm
    screen.fill(WHITE)

    # Teikn spelar
    player.draw(screen)

    # Teikn skudda
    for bullet in bullets:
        bullet.draw(screen)

    # Vis alt på display
    pygame.display.flip()

    # Begrens FPS
    pygame.time.Clock().tick(60)

# Avslutt Pygame
pygame.quit()
sys.exit()