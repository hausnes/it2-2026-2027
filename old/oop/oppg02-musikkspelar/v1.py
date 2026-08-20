import pygame

class Song:
    """A class to represent a song."""

    def __init__(self, title, filename):
        self.title = title
        self.filename = filename

    def get_title(self):
        return self.title

    def get_filename(self):
        return self.filename

class Player:
    """A class to control the playback of songs."""

    def __init__(self):
        pygame.mixer.init()
        self.current_song = None

    def load_song(self, song):
        """Loads a song into the player."""
        self.current_song = song
        pygame.mixer.music.load(song.get_filename())

    def play(self):
        """Plays the current song."""
        pygame.mixer.music.play()

    def pause(self):
        """Pauses the current song."""
        pygame.mixer.music.pause() # NB: Motsetningen er pygame.mixer.music.unpause(), som ikkje er implementert i denne versjonen av programmet

    def stop(self):
        """Stops the current song."""
        pygame.mixer.music.stop()

    def is_playing(self):
        """Returns True if the current song is playing, False otherwise."""
        return pygame.mixer.music.get_busy()

    def get_current_song(self):
        """Returns the current song that is being played, or None if no song is playing."""
        return self.current_song

song1 = Song("Horror hit", "lyd/horror-hit-logo-142395.mp3")
song2 = Song("Sunflower Street Drumloop", "lyd/sunflower-street-drumloop-85bpm-163900.mp3")

# Oppretter musikkspelarobjektet
player = Player()

# Ønsker brukeren velkomen
print("-----------------------------")
print("No skal du få høyre to låtar!")
print("-----------------------------")

player.load_song(song1)
player.play()

# Ventar til songen er ferdig
while player.is_playing():
    pass

# Play the next song
player.load_song(song2)
player.play()

# Ventar til songen er ferdig
while player.is_playing():
    pass