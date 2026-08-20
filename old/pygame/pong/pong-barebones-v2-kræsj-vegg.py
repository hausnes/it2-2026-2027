'''
"Barebones"-eksempel på Pong, der me ikkje nyttar OOP.
Per no er det berre ein ball og to "paddlar". Ballen
blir ikkje stoppa av paddlane, men i denne versjonen blir
kræsj med kantane handtert. Neste steg er å kræsje med paddle...
Klarar du det?
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

    # Sjekk kollisjon med veggene
    if ball.top <= 0 or ball.bottom >= 600:
        ball_y_velocity = -ball_y_velocity
    if ball.left <= 0 or ball.right >= 800:
        ball_x_velocity = -ball_x_velocity

    # Teikn alt
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Oppdater skjermen
    pygame.display.flip()

    # Avgrens bildefrekvensen
    clock.tick(60)