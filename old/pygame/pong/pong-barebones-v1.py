'''
"Barebones"-eksempel på Pong, der me ikkje nyttar OOP.
Per no er det berre ein ball og to "paddlar", og ballen
blir ikkje stoppa av paddlane, ei heller blir kræsj med
kantane handtert. Dette kjem me tilbake til seinare.
'''

import pygame

# Initialiser spelet
pygame.init()

# Set opp skjermen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Set opp fargane
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set opp paddlane og ballen
paddle1 = pygame.Rect(50, 250, 20, 100)
paddle2 = pygame.Rect(730, 250, 20, 100)
ball = pygame.Rect(390, 290, 20, 20)

# Set opp ballens fart
ball_x_velocity = 1
ball_y_velocity = 1

# Set opp klokka
clock = pygame.time.Clock()

# Spelets løkke
running = True

while running:
    # Handter hendingar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oppdater spelets tilstand
    ball.x += ball_x_velocity
    ball.y += ball_y_velocity

    # Teikn alt
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Oppdater skjermen
    pygame.display.flip()

    # Avgrens bildefrekvensen
    clock.tick(60)