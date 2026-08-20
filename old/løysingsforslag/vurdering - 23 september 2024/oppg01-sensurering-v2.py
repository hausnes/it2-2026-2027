'''
    Oppgåve 1: Sensurering, v2
    Omtrent den same tilnærminga som i v1, men no med funksjon.
'''

# Problematiske ord som skal sensurast:
problematiske_ord = ["fis", "stygtord1", "stygtord2", "stygtord3", "stygtord4"]

# Setning som skal sensurerast:
setning = "Dette er ein tekst med fisen og stygtord1 og stygtord2 og stygtord3 og stygtord4."

# Funksjon som skal sensurere setningar:
def sensurer(setning, problematiske_ord):
    for ord in problematiske_ord:
        setning = setning.replace(ord, "*" * len(ord))

    # Returner den sensurerte setninga:
    return setning

# Sensurerer setninga:
print(sensurer(setning, problematiske_ord))