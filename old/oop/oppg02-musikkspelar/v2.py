import pygame

class Track:
    """A class to represent a track (a song or sound file)."""

    def __init__(self, title, filename):
        self.title = title
        self.filename = filename

    def get_title(self):
        return self.title

    def get_filename(self):
        return self.filename

class Player:
    """A class to control the playback of tracks."""

    def __init__(self):
        pygame.mixer.init()
        self.current_track = None
        self.paused = False

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
    print("5: Avslutt")
    print()

# Opprettar liste med songar ("tracks")
tracks = []
tracks.append(Track("Horror hit", "lyd/horror-hit-logo-142395.mp3"))
tracks.append(Track("Sunflower Street Drumloop", "lyd/sunflower-street-drumloop-85bpm-163900.mp3"))
tracks.append(Track("Science Documentary", "lyd/science-documentary-169621.mp3"))
tracks.append(Track("Trap Future Bass", "lyd/trap-future-bass-royalty-free-music-167020.mp3"))

# Opprettar musikkspelarobjektet
player = Player()

# Ønsker brukaren velkomen
print("-----------------------------")
print("Velkomen til musikkspelaren!")
print("-----------------------------")

val = 0

while val != 5:
    show_menu()
    if player.get_current_track() is None:
        print("Gjeldande lydfil: Ingen lydfil valt.")
    else:
        print("Gjeldande lydfil:", player.get_current_track().get_title())
    val = int(input("\nKva vil du gjere? "))
    match val:
        case 1:
            # Lar brukaren velge lydfil
            print("Vel lydfil:")
            for i, track in enumerate(tracks):
                print(f"{i}: {track.get_title()}")
            valgt_nr = int(input("Vel lydfil: "))
            valgt_track = tracks[valgt_nr]
            player.load_track(valgt_track)
        case 2:
            player.play()
        case 3:
            player.pause()
        case 4:
            player.stop()
        case 5:
            print("\nAvsluttar...")
            player.stop()
        case _:
            print("\nUgyldig val.")
