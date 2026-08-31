# Konsept til eit særs enkelt tekstbasert eventyrspel

spillerLever = True
spillerVant = False

valg = input("Du står ved et veikryss. Går du til høyre (h) eller venstre (v)? ")

while spillerLever and not spillerVant:
    if valg == 'h':
        print("Du finner en skatt! Spillet er ferdig.")
        spillerVant = True
        # break # Hopper ut av while-loopen
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