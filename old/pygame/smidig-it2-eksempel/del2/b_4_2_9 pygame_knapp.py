import pygame as pg

WIDTH, HEIGHT = 350, 200
FPS = 24


class Button:
    def __init__(self, text, pos):
        self.font = pg.font.SysFont("Verdana", 18)
        self.ts = self.font.render(text, True, "black")
        self.text_rect = self.ts.get_rect(center=pos)
        self.rect = self.text_rect.inflate(20, 20)
        self.clicked = False

    def draw(self, surface):
        color = pg.Color("grey" if not self.rect.collidepoint(pg.mouse.get_pos()) else "lightgrey")
        pg.draw.rect(surface, color, self.rect)
        pg.draw.rect(surface, pg.Color("black"), self.rect, 2)
        surface.blit(self.ts, self.text_rect)

    def handle_event(self, event):
        if (event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)):
            self.clicked = True


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("GUI komponenter i Pygame")
        self.running = True
        self.button = Button("Klikk meg.", (WIDTH // 2, 50))
        self.click_count = 0
        self.font = pg.font.SysFont("Verdana", 18)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            self.button.handle_event(event)
            if self.button.clicked:
                self.click_count += 1
                self.button.clicked = False

    def draw(self):
        self.screen.fill("white")
        self.button.draw(self.screen)
        click_text = self.font.render(f"Antall Klikk: {self.click_count}", True, "black")
        click_rect = click_text.get_rect(centerx=WIDTH // 2, top=self.button.rect.bottom + 10)
        self.screen.blit(click_text, click_rect)
        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pg.time.Clock().tick(FPS)
        pg.quit()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS, 2024