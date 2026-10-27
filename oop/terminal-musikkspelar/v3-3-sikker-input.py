# Løysingsforslag oppgåve 3: Programmet skal ikkje krasje ved ugyldig input
# Bygger vidare på v3-2-sjanger.py

import pygame

class Track:
    """A class to represent a track (a song or sound file)."""

    def __init__(self, title, filename, genre):
        self.title = title
        self.filename = filename
        self.genre = genre

    def get_title(self):
        return self.title

    def get_filename(self):
        return self.filename

    def get_genre(self):
        return self.genre

class Player:
    """A class to control the playback of tracks."""

    def __init__(self):
        pygame.mixer.init()
        self.current_track = None
        self.paused = False
        self.volume = 100

    def load_track(self, track):
        """Loads a track into the player."""
        self.current_track = track
        self.paused = False
        pygame.mixer.music.load(track.get_filename())

    def play(self):
        """Plays the current track from the start."""
        if self.current_track is None:
            print("Du må velje ei lydfil først.")
            return
        self.paused = False
        pygame.mixer.music.play()

    def pause(self):
        """Pauses or unpauses the current track."""
        if self.paused:
            self.paused = False
            pygame.mixer.music.unpause()
        else:
            self.paused = True
            pygame.mixer.music.pause()

    def stop(self):
        """Stops the current track."""
        self.paused = False
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        """Sets the volume. volume is a number from 0 to 100."""
        if volume < 0 or volume > 100:
            print("Volumet må vere mellom 0 og 100.")
            return
        self.volume = volume
        pygame.mixer.music.set_volume(volume / 100)

    def get_volume(self):
        """Returns the volume (0-100)."""
        return self.volume

    def is_playing(self):
        """Returns True if the current track is playing, False otherwise."""
        return pygame.mixer.music.get_busy()

    def get_current_track(self):
        """Returns the current track, or None if no track is loaded."""
        return self.current_track

def show_menu():
    '''Shows the menu.'''
    print("\nFunksjonar:")
    print("1: Vel lydfil")
    print("2: Spele lydfil")
    print("3: Pause/unpause lydfil")
    print("4: Stopp lydfil")
    print("5: Endre volum")
    print("0: Avslutt")
    print()

def ask_number(question, lowest, highest):
    '''Asks for a whole number between lowest and highest. Keeps asking until the answer is valid.'''
    while True:
        try:
            number = int(input(question))
            if number >= lowest and number <= highest:
                return number
            print(f"Talet må vere mellom {lowest} og {highest}.")
        except ValueError:
            # int() gir ValueError dersom brukaren skriv noko som ikkje er eit heilt tal
            print("Du må skrive eit heilt tal.")

# Opprettar liste med songar ("tracks")
tracks = []
tracks.append(Track("Horror hit", "lyd/horror-hit-logo-142395.mp3", "Skrekk"))
tracks.append(Track("Sunflower Street Drumloop", "lyd/sunflower-street-drumloop-85bpm-163900.mp3", "Hiphop"))
tracks.append(Track("Science Documentary", "lyd/science-documentary-169621.mp3", "Dokumentar"))
tracks.append(Track("Trap Future Bass", "lyd/trap-future-bass-royalty-free-music-167020.mp3", "Trap"))

# Opprettar musikkspelarobjektet
player = Player()

# Ønsker brukaren velkomen
print("-----------------------------")
print("Velkomen til musikkspelaren!")
print("-----------------------------")

val = -1

while val != 0:
    show_menu()
    if player.get_current_track() is None:
        print("Gjeldande lydfil: Ingen lydfil valt.")
    else:
        track = player.get_current_track()
        print(f"Gjeldande lydfil: {track.get_title()} ({track.get_genre()})")
    print("Volum:", player.get_volume())
    # ask_number sørgjer for at val alltid er 0-5, så vi treng ikkje lenger "case _"
    val = ask_number("\nKva vil du gjere? ", 0, 5)
    match val:
        case 1:
            # Lar brukaren velge lydfil
            print("Vel lydfil:")
            for i, track in enumerate(tracks):
                print(f"{i}: {track.get_title()} ({track.get_genre()})")
            valgt_nr = ask_number("Vel lydfil: ", 0, len(tracks) - 1)
            valgt_track = tracks[valgt_nr]
            player.load_track(valgt_track)
        case 2:
            player.play()
        case 3:
            player.pause()
        case 4:
            player.stop()
        case 5:
            nytt_volum = ask_number("Nytt volum (0-100): ", 0, 100)
            player.set_volume(nytt_volum)
        case 0:
            print("\nAvsluttar...")
            player.stop()
