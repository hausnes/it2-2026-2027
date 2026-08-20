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

    def __init__(self, paused=False):
        pygame.mixer.init()
        self.current_song = None
        self.paused = False

    def load_song(self, song):
        """Loads a song into the player."""
        self.current_song = song
        pygame.mixer.music.load(song.get_filename())

    def play(self):
        """Plays the current song."""
        pygame.mixer.music.play()

    def pause(self):
        """Pauses or unpauses the current song."""
        if self.paused:
            self.paused = False
            pygame.mixer.music.unpause()
        else:
            self.paused = True
            pygame.mixer.music.pause()

    def stop(self):
        """Stops the current song."""
        pygame.mixer.music.stop()

    def is_playing(self):
        """Returns True if the current song is playing, False otherwise."""
        return pygame.mixer.music.get_busy()

    def get_current_song(self):
        """Returns the current song that is being played, or None if no song is playing."""
        return self.current_song
    
    def show_menu(self):
        '''Shows the menu.'''
        print("\nFunksjonar:")
        print("1: Vel lydfil")
        print("2: Spele lydfil")
        print("3: Pause lydfil")
        print("4: Stopp lydfil")
        print("5: Avslutt")
        print()

song1 = Song("Horror hit", "lyd/horror-hit-logo-142395.mp3")
song2 = Song("Sunflower Street Drumloop", "lyd/sunflower-street-drumloop-85bpm-163900.mp3")
song3 = Song("Science Documentary", "lyd/science-documentary-169621.mp3")
song4 = Song("Trap Future Bass", "lyd/trap-future-bass-royalty-free-music-167020.mp3")

# Oppretter musikkspelarobjektet
player = Player()

# Ønsker brukeren velkomen
print("-----------------------------")
print("Velkomen til musikkspelaren!")
print("-----------------------------")

val = 0

while val != 5:
    player.show_menu()
    print("Gjeldande lydfil:", player.get_current_song().get_title() if player.get_current_song() else "Ingen lydfil valt.")
    val = int(input("\nKva vil du gjere? "))
    match val:
        case 1:
            # Lar brukaren velge lydfil
            print("Vel lydfil:")
            for i, song in enumerate([song1, song2, song3, song4]):
                print(f"{i}: {song.get_title()}")
            valSong = int(input("Vel lydfil: "))
            song = [song1, song2, song3, song4][valSong]
            player.load_song(song)
        case 2:
            player.play()
        case 3:
            player.pause()
        case 4:
            player.stop()
        case 5:
            print("\nAvsluttar...")
            player.stop()
            break
        case _:
            print("\nUgyldig val.")
            pass