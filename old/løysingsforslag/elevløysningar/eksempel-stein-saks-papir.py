#!/usr/bin/env python3
"""
Oppgave:
    - Lag et stein saks papir-spill.

Lisens: GNU General Public License v3.0

Skrevet av Olai Solsvik

Mulige forbedringer:
    - Ha en egen fil for locale slik at tekst ikke er hard-codet
    - Legge til en "interactive"-modus der spilleren kan velge valgene og antall runder
    - Gjøre koden for å farge teksten enklere å lese
    - Bruke verdien for antall uavgjort
"""

import random  # Brukes for å få datamaskinen til å velge


# ANSI-fargekoder
# Dette er det nærmeste jeg kommer en enum i python
# Å bruke disse fargene gjør at koden blir litt styggere, men jeg synes resultatet er verdt det.
# Du kan lese mer om det her: https://en.wikipedia.org/wiki/ANSI_escape_code
# Kilde for verdiene: https://gist.github.com/upsilun/4a85ab3bc7cf92e8acde720c6eb7ddea
# STORE BOKSTAVER fordi det er konstanter
class colors:
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"  # Brukes for å nullstille tilbake til normal tekst


# KlasserSkrivesSlikSomDette
class RockPaperScissorsGame:
    def __init__(self, choices=["stein", "saks", "papir"], rounds=3):
        """
        Sette variabler for spillet
        """
        # Interne variabler og metoder starter med _
        # jeg_skriver_variabler_slik
        self._computer_score = 0
        self._player_score = 0
        self._draws = 0
        self._rounds = rounds
        # "eksportert" variabel med leselig versjon av valgene, derfor uten "_"
        self.choices = choices
        self._choices = list(reversed(self.choices))

    def _input(self):
        """
        Spørre bruker om input og validere at det er et av de mulige valgene
        """
        choices = ", ".join(self.choices)
        prompt = f"Velg ({choices}): "
        err = f"Du må velge en av ({choices})!"
        # Spørre bruker om valg på nytt dersom det ikke er gyldig
        while True:
            ans = input(prompt)
            if ans in self._choices:
                # `return` stopper løkken på samme måte som break
                return ans
            else:
                print(err)

    def _play(self, player_choice, computer_choice):
        """
        Intern funksjon for å sjekke om man vinner når input er valgene
        Strengene er validert på forhånd
        """
        num_choices = len(self._choices)
        player = self._choices.index(player_choice)
        computer = self._choices.index(computer_choice)

        # Valgene er rangert i en liste slik at den med høyere indeks vinner over den med en lavere.
        # Et spesialtilfelle er hvis en har den første og en har den andre, men siden jeg bruker %
        # , blir det negative tallet positivt og alt virker :)
        if (computer - player) % num_choices == 1:
            return "computer"
        elif (player - computer) % num_choices == 1:
            return "player"
        # Trenger ikke else siden `return` stopper funksjonen
        return "draw"

    def play(self):
        """
        Eksportert funksjon for å gi brukeren tilbakemelding
        """
        player_choice = self._input()
        computer_choice = random.choice(self._choices)
        result = self._play(player_choice, computer_choice)
        match result:
            case "computer":
                # Denne print-koden er ikke veldig fin fordi jeg har lagt inn fargekoder
                # f-strings lar meg skrive verdier direkte inn
                print(
                    f"{colors.BOLD}{colors.RED}Du tapte!{colors.ENDC} Datamaskinen valgte {colors.BOLD}{colors.BLUE}{computer_choice}{colors.ENDC}."
                )
                self._computer_score += 1
            case "player":
                print(
                    f"{colors.BOLD}{colors.GREEN}Du vant!{colors.ENDC} Datamaskinen valgte {colors.BOLD}{colors.BLUE}{computer_choice}{colors.ENDC}."
                )
                self._player_score += 1
            case _:
                print(
                    f"{colors.BOLD}{colors.YELLOW}Det ble uavgjort!{colors.ENDC} Datamaskinen valgte {colors.BOLD}{colors.BLUE}{computer_choice}{colors.ENDC}."
                )
                self._draws += 1
        print(
            f"Din poengsum: {colors.BOLD}{colors.MAGENTA}{self._player_score}{colors.ENDC}, Datamaskinen sin poengsum: {colors.BOLD}{colors.MAGENTA}{self._computer_score}{colors.ENDC}"
        )

    def _game(self):
        """
        Løkke som kjører til spillet er ferdig og starter nye runder
        """
        # Sette sammen listen over valg med ", " mellom
        choices = ", ".join(self.choices)
        print(
            f"Spill {colors.ITALIC}{colors.BLUE}{choices}{colors.ENDC}! Målet er å vinne mot datamaskinen {colors.BOLD}{self._rounds}{colors.ENDC} ganger!"
        )
        print()
        # Løkke som går for alltid
        while True:
            self.play()
            # Stopp løkken og gi tilbakemelding til spilleren
            if self._computer_score >= self._rounds:
                print(
                    f"Spillet er over, {colors.BOLD}{colors.RED}du tapte!{colors.ENDC} Du vant {self._player_score} ganger."
                )
                break
            if self._player_score >= self._rounds:
                print(
                    f"Spillet er over, {colors.BOLD}{colors.GREEN}du vant!{colors.ENDC} Datamaskinen vant {self._computer_score} ganger."
                )
                break

    def game(self):
        """
        Wrapper rundt _game() for å starte på nytt dersom brukeren vil det.
        Jeg kunne brukt rekursjon (altså game() kjører seg selv hvis spillet skal starte på nytt)
        , men det ville ført til at spillet krasjet etter 1000 omspill, fordi det er grensen for rekursjon.
        https://stackoverflow.com/a/3323013
        """
        self._is_playing = True
        while self._is_playing:
            self._game()
            if not input("Vil du spille på nytt? (j/n) ").lower().strip() == "j":
                self._is_playing = False  # Stopper løkken
                break  # ikke nødvendig med break, `continue` hadde gjort det samme i dette tilfellet
            # Kjøre __init__ funksjonen, som i praksis vil nullstille klassen. Sende gjennom verdiene den hadde fra før.
            self.__init__(choices=self._choices, rounds=self._rounds)
            print()


# Gjøre at koden kjører kun når man kjører dette direkte, ikke hvis man prøver å importere den som et bibliotek
if __name__ == "__main__":
    # Lage en instance av klassen og starte spillet.
    game = RockPaperScissorsGame()
    game.game()

    # Kan også gjøre for eksempel:
    """
    choices = ["stein", "saks", "papir", "en annen ting", "enda en ting"]
    game = RockPaperScissorsGame(choices=choices, rounds=5)
    game.game()
    """
