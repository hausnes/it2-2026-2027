'''
    Oppgåve 1: Sensurering, v4
    Dette er ein vidareutvikling av v3, der me no har lagt til ein dictionary med erstatningsord.
'''
import random

# Problematiske ord som skal sensurast:
problematiske_ord = ["fis", "stygtord1", "stygtord2", "stygtord3", "stygtord4"]

# Dictionary med ord og kva som er korrekt erstatningsord:
erstatningsord = {
    "fis": "promp",
    "stygtord1": "erstatningsord2",
    "stygtord2": "erstatningsord3",
    "stygtord3": "erstatningsord4",
    "stygtord4": "erstatningsord5"
}

# Setning som skal sensurerast:
setningar = [
    "Den som fisen først er var, den er fisens rette far Fis fis fis!.",
    "FIS globally governs skiing and snowboarding and oversees over 7000 events annually in Alpine, Cross-Country, Ski Jumping, Nordic Combined and many more.",
    "Fiskal blir benyttet om det som har med statskassen eller regnskap å gjøre, som for eksempel «fiskale avgifter» (statlige avgifter), eller «det fiskale året 2005» (regnskapsåret 2005). Fiskale skatter og avgifter har til formål å skaffe inntekter til staten.",
    "Oppskrifter med fisk og sjømat for alle, til middag, lunsj og fest. Lær om behandling av fisk og sjømat."
]

# Funksjon som skal sensurere setningar:
def sensurer(setning, problematiske_ord, erstatningTegn=True): # erstatningTegn er ein valgfri parameter, som default er True
    ord_liste = setning.split()
    sensurert_liste = []

    for ord in ord_liste:
        ord_lower = ord.lower()
        if any(problematisk_ord in ord_lower for problematisk_ord in problematiske_ord):
            if erstatningTegn:
                sensurert_ord = '*' * len(ord)
            else:
                # Finn det problematiske ordet som er en del av ordet
                for problematisk_ord in problematiske_ord:
                    if problematisk_ord in ord_lower:
                        erstatning = erstatningsord.get(problematisk_ord, problematisk_ord)
                        sensurert_ord = ord_lower.replace(problematisk_ord, erstatning)
                        break
            sensurert_liste.append(sensurert_ord)
        else:
            sensurert_liste.append(ord)

    # Returner den sensurerte setninga:
    return ' '.join(sensurert_liste)

# Sensurerer setninga:
for setning in setningar:
    print("-"*50)
    print(sensurer(setning, problematiske_ord))
    print(sensurer(setning, problematiske_ord, False))