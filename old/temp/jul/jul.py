import pygame
import os
import time

# Initialiser Pygame
pygame.init()
pygame.mixer.init()

# Skjermoppsett
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Julestemning")

# Farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Last inn julesangen
pygame.mixer.music.load('haohaohao.mp3')

# Spill av julesangen
pygame.mixer.music.play(-1)  # -1 betyr at sangen spilles i loop

# Tekstinnstillinger
font = pygame.font.SysFont('Arial', 48)
text = font.render('God jol!', True, RED)
text_rect = text.get_rect()
text_rect.y = HEIGHT // 2 - text_rect.height // 2

# Hovedløkken for animasjonen
running = True
x_pos = -text_rect.width  # Start utenfor venstre kant
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyll skjermen med hvit farge
    screen.fill(WHITE)

    # Tegn teksten på skjermen
    screen.blit(text, (x_pos, text_rect.y))

    # Oppdater skjermen
    pygame.display.flip()

    # Flytt teksten til høyre
    x_pos += 5
    if x_pos > WIDTH:
        x_pos = -text_rect.width  # Start på nytt fra venstre side

    # Vent litt før neste oppdatering
    pygame.time.delay(50)

# Avslutt Pygame
pygame.quit()