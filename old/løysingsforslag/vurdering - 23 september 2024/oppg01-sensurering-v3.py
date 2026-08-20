'''
    Oppgåve 1: Sensurering, v3
    Har lagt til ein dictionary med erstatningsord, slik at me kan velge å erstatte ord med søte erstatningsord i staden for *.
    Legg merke til at dette er implementert med ein valgfri parameter i funksjonen, som default er True.
'''
import random

# Problematiske ord som skal sensurast:
problematiske_ord = ["fis", "stygtord1", "stygtord2", "stygtord3", "stygtord4"]

# Erstatningsord, dersom me ikkje ynskjer å sensurere med *
erstatningsord = ["promp", "erstatningsord2", "erstatningsord3", "erstatningsord4"]

# Setning som skal sensurerast:
setning = "Dette er ein tekst med fisen og stygtord1 og stygtord2 og stygtord3 og stygtord4. Eg likar fisk!"

# Funksjon som skal sensurere setningar:
def sensurer(setning, problematiske_ord, erstatningTegn = True): # erstatningTegn er ein valgfri parameter, som default er True
    for ord in problematiske_ord:
        if erstatningTegn: # Som i at me ynskjer å erstatte stygge ord med *
            setning = setning.replace(ord, "*" * len(ord))
        else: # Som i at me ynskjer å erstatte stygge ord med "søte erstatningsord"
            setning = setning.replace(ord, random.choice(erstatningsord))

    # Returner den sensurerte setninga:
    return setning

# Sensurerer setninga:
print(sensurer(setning, problematiske_ord))
print(sensurer(setning, problematiske_ord, False))