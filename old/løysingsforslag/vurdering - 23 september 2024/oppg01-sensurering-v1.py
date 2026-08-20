'''
    Oppgåve 1: Sensurering, v1
    Enkel tilnærming.
'''

# Problematiske ord som skal sensurast:
problematiske_ord = ["fis", "stygtord1", "stygtord2", "stygtord3", "stygtord4"]

# Setning som skal sensurerast:
setning = "Dette er ein tekst med fis og stygtord1 og stygtord2 og stygtord3 og stygtord4."

# Sensurerer setninga:
for ord in problematiske_ord:
    setning = setning.replace(ord, "*" * len(ord))

# Skriv ut den sensurerte setninga:
print(setning)