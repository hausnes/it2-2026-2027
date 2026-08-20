import pygame as pg
from pygame.locals import *
from random import choice

WIDTH, HEIGHT = 400, 600
FPS = 24
TID_PER_RUNDE = 2000 # Endre denne for å endre tiden du gir brukeren på å klikke

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Klikke i vinkel!")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        # Her kommer nye ting jeg la til for å lage til dette løsningsforslaget (basert på mal fra Smidig):
        self.timer = pg.time.get_ticks() # Denne skal brukes i sammenheng med å restarte spillet så ofte som TID_PER_RUNDE tilsier
        self.fargeliste = ["blue","red","green","pink","purple","brown"] # For å kunne endre bakgrunnsfargen underveis
        self.background_color = self.fargeliste[3]  # Startfarge
        self.antall_klikk = 0 # Teller for antall klikk
        # self.antall_klikk_rekord = 0 # Holde styr på rekorden i antall klikk
        # Under initialisering/oppstart henter vi en eventuell rekord fra rekord.txt
        try:
            with open("rekord.txt", "r") as file:
                self.antall_klikk_rekord = int(file.read())
        except FileNotFoundError: # Dersom vi ikke finner rekord.txt, ..
            self.antall_klikk_rekord = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.antall_klikk += 1
                print(f"Antall klikk: {self.antall_klikk}")

    def update(self):
        self.all_sprites.update()

        # Denne koden kjører så ofte som TID_PER_RUNDE tilsier
        if pg.time.get_ticks() - self.timer > TID_PER_RUNDE:
            print(f"Det har gått {TID_PER_RUNDE/1000} sekunder, runden er ferdig!")
            
            # Håndterer det å VELGE en ny, tilfeldig farge (settes i draw-funksjonen)
            fargeNy = choice(self.fargeliste)
            while self.background_color == fargeNy:
                fargeNy = choice(self.fargeliste)
            self.background_color = fargeNy

            # Håndterer det å sette en ny rekord, dersom det er tilfelle
            if self.antall_klikk > self.antall_klikk_rekord:
                self.antall_klikk_rekord = self.antall_klikk
            print(f"Rekord: {self.antall_klikk_rekord}")

            # Nullstiller antall klikk etter en runde
            self.antall_klikk = 0

            self.timer = pg.time.get_ticks() # Når en runde er ferdig, nullstill timeren


    def draw(self):
        self.screen.fill(self.background_color) # Setter den nye fargen som blir valgt i update-funksjonen

        self.all_sprites.draw(self.screen)

        # Vis antall klikk i pågående runde i spillvinduet (NB: ikke en del av oppgaveteksten)
        font = pg.font.Font(None, 36)
        text = font.render(f"Antall klikk denne runden: {self.antall_klikk}", True, pg.Color("white"))
        self.screen.blit(text, (10, 10))

        # Vis beste resultat i spillvinduet (heller ikke en del av den originale oppgaveteksten)
        text_highscore = font.render(f"Rekord: {self.antall_klikk_rekord}", True, pg.Color("Black"))
        self.screen.blit(text_highscore, (10, 40))

        pg.display.update()

    def run(self):
        # Gameloopen
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        # Når programmet er ferdig (brukeren lukker vindu), skrives rekorden til en tekstfil
        if self.antall_klikk_rekord > 0:
            with open("rekord.txt", "w") as file:
                file.write(str(self.antall_klikk_rekord))

        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()