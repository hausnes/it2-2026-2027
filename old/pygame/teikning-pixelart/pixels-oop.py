import pygame

class PixelArtApp:
    def __init__(self, screen_width, screen_height, pixel_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pixel_size = pixel_size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        # self.pixels = [["white" for _ in range(screen_width // pixel_size)] for _ in range(screen_height // pixel_size)]
        # Alternative way to create the pixels list (more readable)
        self.pixels = []
        # Calculate the number of pixels in width and height
        num_pixels_width = self.screen_width // self.pixel_size
        num_pixels_height = self.screen_height // self.pixel_size

        # Loop over the height of the screen
        for _ in range(num_pixels_height):
            # Initialize an empty row
            row = []
            
            # Loop over the width of the screen
            for _ in range(num_pixels_width):
                # Add a "white" pixel to the row
                row.append("white")
    
            # Add the row to the pixels
            self.pixels.append(row)

        self.drawing_color = "black"
        self.mouse_button_down = False
        self.help_shown = False

    def change_color(self, key):
        if key == pygame.K_1:
            return "black"
        elif key == pygame.K_2:
            return "red"
        elif key == pygame.K_3:
            return "green"
        elif key == pygame.K_4:
            return "blue"
        elif key == pygame.K_5:
            return "white"
        else:
            return self.drawing_color

    def clear_pixels(self):
        for y in range(self.screen_height // self.pixel_size):
            for x in range(self.screen_width // self.pixel_size):
                self.pixels[y][x] = "white"

    def draw_help(self):
        self.screen.fill(pygame.Color("white"))
        font = pygame.font.Font(None, 36)
        text_color = pygame.Color("black")
        commands = [
            ("1", "Change color to black"),
            ("2", "Change color to red"),
            ("3", "Change color to green"),
            ("4", "Change color to blue"),
            ("5", "Change color to white"),
            ("c", "Clear the screen"),
            ("s", "Save the screen to a PNG file"),
            ("h", "Toggle this help screen"),
        ]
        for i, (key, description) in enumerate(commands):
            text = font.render(f"{key}: {description}", True, text_color)
            self.screen.blit(text, (50, 25 + i * 40))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.pixels[y // self.pixel_size][x // self.pixel_size] = self.drawing_color
                    self.mouse_button_down = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_button_down = False
                elif event.type == pygame.MOUSEMOTION:
                    if self.mouse_button_down:
                        x, y = event.pos
                        self.pixels[y // self.pixel_size][x // self.pixel_size] = self.drawing_color
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.help_shown = not self.help_shown
                    elif not self.help_shown:
                        self.drawing_color = self.change_color(event.key)
                        if event.key == pygame.K_c:
                            self.clear_pixels()
                        elif event.key == pygame.K_s:
                            pygame.image.save(self.screen, "pixelart.png")
            if self.help_shown:
                self.draw_help()
            else:
                self.draw_pixels()
            pygame.display.flip()

    def draw_pixels(self):
        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                pygame.draw.rect(self.screen, pygame.Color(color), pygame.Rect(x * self.pixel_size, y * self.pixel_size, self.pixel_size, self.pixel_size))

if __name__ == "__main__":
    pygame.init()
    app = PixelArtApp(800, 600, 10)
    app.run()
    pygame.quit()