'''
Eksempel frå Aschehoug-boka, der det blir skrive ein eigen funksjon
for å handtere å finne avstand mellom to objekt.
'''

import pygame as pg
import math as m

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 800
VINDU_HOYDE  = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, x_fart, y_fart, radius, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.x_fart = x_fart
    self.y_fart = y_fart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.x_fart = -self.x_fart

    # Sjekker om ballen er utenfor toppen/bunnen
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.y_fart = -self.y_fart
       
    # Flytter ballen
    self.x += self.x_fart
    self.y += self.y_fart

def finnAvstand(obj1, obj2):
    xAvstand2 = (obj1.x - obj2.x)**2  # x-avstand i andre
    yAvstand2 = (obj1.y - obj2.y)**2  # y-avstand i andre
    avstand = m.sqrt(xAvstand2 + yAvstand2)

    return avstand
    
# Lager en liste med Ball-objekter
baller = [
    Ball(225, 100, 0.1, 0.1, 10, vindu),
    Ball(400, 300, 0.2, 0.2, 15, vindu),
    Ball(300, 300, 0.15, 0.15, 12, vindu),
    Ball(50, 40, 0.2, 0.2, 5, vindu),
    Ball(70, 140, 0.2, 0.2, 5, vindu)
    # Legg til flere baller her om ønskelig
]

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballene
    for ball in baller:
        ball.tegn()
        ball.flytt()

    # Sjekker om ballene treffer hverandre
    for i in range(len(baller)):
        for j in range(i + 1, len(baller)):
            if finnAvstand(baller[i], baller[j]) <= (baller[i].radius + baller[j].radius):
                print("Ballene treffer hverandre!")
                baller[i].x_fart = -baller[i].x_fart
                baller[i].y_fart = -baller[i].y_fart
                baller[j].x_fart = -baller[j].x_fart
                baller[j].y_fart = -baller[j].y_fart

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()