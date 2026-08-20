import sounddevice as sd
import numpy as np
import pygame
from time import sleep
# import keyboard

# Initialize Pygame
pygame.init()
# Initialize the Pygame mixer
pygame.mixer.init()
# Load the mp3 file
pygame.mixer.music.load('alarm-kort.mp3')

# Query devices, to see available outputs (and inputs), press enter to continue program
print("\nMoglege lydkjelder (trykk enter for å starte lydovervakning):\n")
input(sd.query_devices())
print()

# Function to play the alarm sound and print the volume
def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("Volume:", volume_norm)
    if volume_norm > 100 and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
        sleep(2) # Sleep for 2 seconds to prevent the alarm from repeating too quickly

with sd.InputStream(callback=audio_callback):
    while True:
        pass  # Do nothing and loop forever