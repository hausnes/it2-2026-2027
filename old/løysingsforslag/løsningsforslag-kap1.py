'''
Oppgave 15 fra kapittel 1A:
---------------------------
Vi har en rettvinklet trekant.
Vi kjenner en vinkel (60 grader) og den hosliggende kateten (7).
Vi ønsker å finne hypotenusen (x).
Python's math-bibliotek bruker radianer, så vi må konvertere grader til radianer.
'''

import math

# Gitt informasjon
vinkel_grader = 60
hosliggende_katet = 7

# Konverter grader til radianer
vinkel_radianer = math.radians(vinkel_grader)

# Bruk cosinus for å finne hypotenusen
# cos(vinkel) = hosliggende_katet / hypotenus
# Dermed: hypotenus = hosliggende_katet / cos(vinkel)
hypotenus = hosliggende_katet / math.cos(vinkel_radianer)

print("Hypotenusen er:", hypotenus)

'''
Oppgåve 1 frå kapittel 1C
'''
# Tala frå og med 1 til og med 30:
for tall in range(1, 31):
    print(tall)
# 100 første partala:
for tall in range(2, 201, 2):
    print(tall)
# 5-ganger (frå og med 5, til og med 50):
for tall in range(5, 51, 5):
    print(tall)
# Talsekvensen 21, 28, 35, 42:
for tall in range(21, 43, 7):
    print(tall)
# Talsekvensen 100, 90, 80, 70, 50, 40, 30, 20, 10:
for tall in range(100, 9, -10):
    print(tall)

'''
Oppgåve 22 frå kapittel 1C
'''
def print_gangetabell(size):
    """Printar ein gangetabell med gitt størrelse.

    Args:
        size: Størrelsen på gangetabellen (antall rader og kolonner).
    """

    # Skriv ut overskrifta med tala frå 1 til "size"
    print("    ", end="")  # Legg til ekstra mellomrom for å justere overskrifta
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()

    # Skriv ut ei horisontal linje
    print("    ", "-" * (size * 4 + 1))

    # Skriv ut sjølve gangetabellen
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")  # Juster radetikettar
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()

# Kallar funksjonen for å printe ein size x size gangetabell
print_gangetabell(7)

'''
Oppgåve 24 frå kapittel 1C
'''
while True:
    maanednr = input("Oppgi nummeret til måneden vi er i ")

    try:
        maanednr = int(maanednr)
        if maanednr >= 1 and maanednr <= 12:
            print(f"Du skrev inn {maanednr}.")
            break
        else:
            print("Du må oppgi et tall mellom 1 og 12.")
    except ValueError:
        print("Du må oppgi et gyldig tall.")