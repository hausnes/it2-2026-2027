# Konsept til eit særs enkelt tekstbasert eventyrspel

spillerLever = True

valg = input("Du står ved et veikryss. Går du til høyre (h) eller venstre (v)? ")

while spillerLever:
    if valg == 'h':
        print("Du finner en skatt! Spillet er ferdig.")
        break # Hopper ut av while-loopen
    elif valg == 'v':
        print("Du møter en drage. Vil du kjempe (k) eller flykte (f)?")
        valg2 = input()
        if valg2 == 'k':
            print("Du tapte kampen.")
            spillerLever = False
        elif valg2 == 'f':
            print("Du slapp unna.")
        else:
            print("Det kan du ikke gjøre..")
    else:
        print("Ugyldig valg.")