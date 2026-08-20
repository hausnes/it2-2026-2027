import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360

# Define the size of the pixels
PIXEL_SIZE = 10

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a 2D array to store the pixel colors
pixels = [] # Create an empty list to store the rows of pixels

# Loop over the rows
for _ in range(SCREEN_HEIGHT // PIXEL_SIZE):
    # Create an empty list for this row
    row = []
    
    # Loop over the columns
    for _ in range(SCREEN_WIDTH // PIXEL_SIZE):
        # Add a white pixel to this row
        row.append("white")
    
    # Add this row to the pixels list
    pixels.append(row)

# An alternative way to draw the pixels
# pixels = [["white" for _ in range(SCREEN_WIDTH // PIXEL_SIZE)] for _ in range(SCREEN_HEIGHT // PIXEL_SIZE)]

# Function to draw the pixels
def draw_pixels():
    for y in range(SCREEN_HEIGHT // PIXEL_SIZE):
        for x in range(SCREEN_WIDTH // PIXEL_SIZE):
            color = pixels[y][x]
            pygame.draw.rect(screen, pygame.Color(color), pygame.Rect(x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

# Define the drawing color
drawing_color = "black"

def change_color(key):
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
        return drawing_color
    
# Function to clear the pixels
def clear_pixels():
    for y in range(SCREEN_HEIGHT // PIXEL_SIZE):
        for x in range(SCREEN_WIDTH // PIXEL_SIZE):
            pixels[y][x] = "white"

# Function to draw the help screen
def draw_help():
    # Clear the screen
    screen.fill(pygame.Color("white"))

    # Set the font and color for the text
    font = pygame.font.Font(None, 36)
    text_color = pygame.Color("black")

    # List of commands and their descriptions
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

    # Draw each command and its description
    for i, (key, description) in enumerate(commands):
        text = font.render(f"{key}: {description}", True, text_color)
        screen.blit(text, (50, 25 + i * 40))

# Add a variable to track whether the help screen is shown
help_shown = False

# Add a variable to track whether the mouse button is down
mouse_button_down = False

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            pixels[y // PIXEL_SIZE][x // PIXEL_SIZE] = drawing_color
            mouse_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button_down = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_button_down:
                x, y = event.pos
                pixels[y // PIXEL_SIZE][x // PIXEL_SIZE] = drawing_color
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Toggle the help screen when the "h" key is pressed
                help_shown = not help_shown
            elif not help_shown:  # Only process other key presses if the help screen is not shown
                drawing_color = change_color(event.key)
                if event.key == pygame.K_s:  # Save the screen when the "s" key is pressed
                    pygame.image.save(screen, "pixelart.png")
                if event.key == pygame.K_c:  # Clear the screen when the "c" key is pressed
                    clear_pixels()

    # Draw the pixels or the help screen
    if help_shown:
        draw_help()
    else:
        draw_pixels()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()