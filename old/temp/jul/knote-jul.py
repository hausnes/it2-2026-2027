# Obfuskert kode for å skrive ein hemmeleg beskjed til terminalen

def _(_):
    __ = ""
    for ___ in _:
        __ += chr(___)
    return __

__ = [71, 111, 100, 32, 106, 111, 108, 33]
___ = _(__)
print(___)

# Forklaring (ikkje sjå på denne før du har prøvd å løyse oppgåva!):
# 1. Funksjonen _(_) tek ei liste med ASCII-verdier og konverterer dei til ein string.
# 2. Lista __ inneheld ASCII-verdiane for den hemmelege beskjeden.
# 3. Funksjonen _(_) kallast med lista __ som argument, og resultatet lagrast i variabelen ___.
# 4. Variabelen ___ inneheld den hemmelege beskjeden, som blir skrive ut til terminalen.