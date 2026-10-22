# Løysingsforslag oppgåve 5: Klassen Playlist
# Bygger vidare på v3-4-neste-forrige.py
#
# I staden for ei vanleg liste får vi eit Playlist-objekt som tek vare på låtane.
# Player og hovudprogrammet spør spelelista i staden for å bruke lista direkte.

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

class Playlist:
    """A class to represent a list of tracks."""

    def __init__(self, name):
        self.name = name
        self.tracks = []

    def get_name(self):
        return self.name

    def add_track(self, track):
        """Adds a track to the end of the playlist."""
        self.tracks.append(track)

    def get_track(self, nr):
        """Returns the track with number nr."""
        return self.tracks[nr]

    def get_number_of_tracks(self):
        """Returns how many tracks the playlist has."""
        return len(self.tracks)

class Player:
    """A class to control the playback of tracks."""

    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist    # Endra: spelaren får ei speleliste i staden for ei liste
        self.current_nr = None
        self.paused = False
        self.volume = 100

    def load_track(self, nr):
        """Loads the track with number nr from the playlist."""
        self.current_nr = nr
        self.paused = False
        track = self.playlist.get_track(nr)
        pygame.mixer.music.load(track.get_filename())

    def play(self):
        """Plays the current track from the start."""
        if self.current_nr is None:
            print("Du må velje ei lydfil først.")
            return
        self.paused = False
        pygame.mixer.music.play()

    def next_track(self):
        """Loads and plays the next track. Starts from the beginning after the last track."""
        if self.current_nr is None:
            nr = 0
        else:
            nr = self.current_nr + 1
            if nr >= self.playlist.get_number_of_tracks():
                nr = 0
        self.load_track(nr)
        self.play()

    def previous_track(self):
        """Loads and plays the previous track. Goes to the last track before the first one."""
        if self.current_nr is None:
            nr = 0
        else:
            nr = self.current_nr - 1
            if nr < 0:
                nr = self.playlist.get_number_of_tracks() - 1
        self.load_track(nr)
        self.play()

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
        if self.current_nr is None:
            return None
        return self.playlist.get_track(self.current_nr)

def show_menu():
    '''Shows the menu.'''
    print("\nFunksjonar:")
    print("1: Vel lydfil")
    print("2: Spele lydfil")
    print("3: Pause/unpause lydfil")
    print("4: Stopp lydfil")
    print("5: Endre volum")
    print("6: Neste lydfil")
    print("7: Førre lydfil")
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
            print("Du må skrive eit heilt tal.")

# Opprettar spelelista og legg til låtar
playlist = Playlist("Mine favorittar")
playlist.add_track(Track("Horror hit", "lyd/horror-hit-logo-142395.mp3", "Skrekk"))
playlist.add_track(Track("Sunflower Street Drumloop", "lyd/sunflower-street-drumloop-85bpm-163900.mp3", "Hiphop"))
playlist.add_track(Track("Science Documentary", "lyd/science-documentary-169621.mp3", "Dokumentar"))
playlist.add_track(Track("Trap Future Bass", "lyd/trap-future-bass-royalty-free-music-167020.mp3", "Trap"))

# Opprettar musikkspelarobjektet med spelelista
player = Player(playlist)

# Ønsker brukaren velkomen
print("-----------------------------")
print("Velkomen til musikkspelaren!")
print("-----------------------------")

val = -1

while val != 0:
    show_menu()
    print("Speleliste:", playlist.get_name())
    if player.get_current_track() is None:
        print("Gjeldande lydfil: Ingen lydfil valt.")
    else:
        track = player.get_current_track()
        print(f"Gjeldande lydfil: {track.get_title()} ({track.get_genre()})")
    print("Volum:", player.get_volume())
    val = ask_number("\nKva vil du gjere? ", 0, 7)
    match val:
        case 1:
            # Lar brukaren velge lydfil
            print("Vel lydfil:")
            for i in range(playlist.get_number_of_tracks()):
                track = playlist.get_track(i)
                print(f"{i}: {track.get_title()} ({track.get_genre()})")
            valgt_nr = ask_number("Vel lydfil: ", 0, playlist.get_number_of_tracks() - 1)
            player.load_track(valgt_nr)
        case 2:
            player.play()
        case 3:
            player.pause()
        case 4:
            player.stop()
        case 5:
            nytt_volum = ask_number("Nytt volum (0-100): ", 0, 100)
            player.set_volume(nytt_volum)
        case 6:
            player.next_track()
        case 7:
            player.previous_track()
        case 0:
            print("\nAvsluttar...")
            player.stop()
