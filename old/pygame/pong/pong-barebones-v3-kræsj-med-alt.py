'''
"Barebones"-eksempel på Pong, der me ikkje nyttar OOP.
I denne versjonen blir kræsj med både veggar og paddles
handtert. Merk at det er den enklaste (?) måten å handtere
kræsj som blir nytta for obj. mot obj.; "colliderect".
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
paddle1 = pygame.Rect(50, 150, 20, 100)
paddle2 = pygame.Rect(730, 250, 20, 100)
ball = pygame.Rect(290, 290, 20, 20)

# Set opp ballens fart
ball_x_velocity = 3
ball_y_velocity = 3

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

    # Sjekk kollisjon med paddlene
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
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