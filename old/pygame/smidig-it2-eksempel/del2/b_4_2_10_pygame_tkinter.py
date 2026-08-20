import threading
import tkinter as tk
from tkinter import ttk
import pygame as pg
import queue
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '1'
PG_WIDTH, PG_HEIGHT = 300, 125
FPS = 24
color_dict = {
    'oransje': '#f14829',
    'gul'    : '#fde013',
    'grønn'  : '#17af65',
    'rosa'   : '#e0038c'
}


class SharedResources:
    def __init__(self):
        self.color_queue = queue.Queue()
        self.speed_queue = queue.Queue()
        self.bounces = 0
        self.bounces_lock = threading.Lock()
        self.stop_event = threading.Event()

    def get_color(self):
        try:
            return self.color_queue.get_nowait()
        except queue.Empty:
            return None

    def get_speed(self):
        try:
            return self.speed_queue.get_nowait()
        except queue.Empty:
            return None

    def increment_bounces(self):
        with self.bounces_lock:
            self.bounces += 1

    def get_bounces(self):
        with self.bounces_lock:
            return self.bounces

    def set_stop(self):
        self.stop_event.set()

    def should_stop(self):
        return self.stop_event.is_set()


class TkinterApp(tk.Tk):
    def __init__(self, resources):
        super().__init__()
        self.resources = resources
        self.position_window()
        self.title("Tkinter tråd")
        self.setup_widgets()
        self.update_bounces()
        self.check_for_stop()

    def setup_widgets(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10)
        ttk.Label(self.frame, text="Hastighet:").grid(
            row=0, column=0, sticky="w", padx=5, pady=5)
        self.speed_slider = ttk.Scale(
            self.frame, from_=3, to=9, orient="horizontal", command=self.speed_changed)
        self.speed_slider.set(6)
        self.speed_slider.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self.frame, text="Farge:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5)
        self.color_var = tk.StringVar(value="Gul")
        color_combo = ttk.Combobox(
            self.frame, textvariable=self.color_var, values=list(color_dict.keys()))
        color_combo.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.color_var.trace_add("write", self.color_changed)
        ttk.Label(self.frame, text="Antall sprett:").grid(
            row=3, column=0, sticky="w", padx=5, pady=5)
        self.bounces_value = ttk.Label(self.frame, text="0")
        self.bounces_value.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    def speed_changed(self, event):
        speed = self.speed_slider.get()
        self.resources.speed_queue.put(speed)

    def color_changed(self, *args):
        color = self.color_var.get()
        self.resources.color_queue.put(color_dict[color])

    def update_bounces(self):
        if not self.resources.should_stop():
            self.bounces_value.config(text=str(self.resources.get_bounces()))
            self.after(100, self.update_bounces)

    def check_for_stop(self):
        if self.resources.should_stop():
            self.quit()
        else:
            self.after(100, self.check_for_stop)

    def position_window(self):
        x = (self.winfo_screenwidth() - PG_WIDTH) // 2 - PG_WIDTH - 20
        y = (self.winfo_screenheight() - PG_HEIGHT) // 2 - 35
        self.geometry(f"{PG_WIDTH}x{PG_HEIGHT}+{x}+{y}")

    def destroy(self):
        self.resources.set_stop()
        super().destroy()

    def start(self):
        self.mainloop()


class PygameApp:
    def __init__(self, resources):
        self.resources = resources
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((PG_WIDTH, PG_HEIGHT))
        pg.display.set_caption("Pygame tråd")
        self.ball = Ball(self.resources)
        self.all_sprites = pg.sprite.Group(self.ball)

    def run(self):
        while not self.resources.should_stop():
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.resources.set_stop()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pg.display.update()


class Ball(pg.sprite.Sprite):
    def __init__(self, resources):
        super().__init__()
        self.resources = resources
        self.dx = 5
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.color = "#fde013"  # Default color
        self.update_color()
        self.rect.x = 0
        self.rect.y = (PG_HEIGHT - self.rect.height) / 2

    def update_color(self):
        self.image.fill((0, 0, 0, 0))
        pg.draw.circle(self.image, pg.Color(self.color), (25, 25), 25)

    def update(self):
        new_speed = self.resources.get_speed()
        if new_speed is not None:
            self.dx = abs(new_speed) if self.dx > 0 else -abs(new_speed)

        new_color = self.resources.get_color()
        if new_color is not None:
            self.color = new_color
            self.update_color()

        self.rect.x += self.dx
        if self.rect.left < 0 or self.rect.right > PG_WIDTH:
            self.dx *= -1
            self.resources.increment_bounces()


def start_app():
    resources = SharedResources()
    tk_thread = threading.Thread(target=lambda: TkinterApp(resources).start())
    pg_thread = threading.Thread(target=lambda: PygameApp(resources).run())
    tk_thread.start()
    pg_thread.start()
    tk_thread.join()
    pg_thread.join()


if __name__ == "__main__":
    start_app()

# Smidig IT-2 © TIP AS, 2024