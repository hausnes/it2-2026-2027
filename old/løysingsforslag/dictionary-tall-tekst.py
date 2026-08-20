# Opprett en ordbok som inneholder tallene som nøkler og tekstene som verdier
tall_tekst = {
    1: "en", 
    2: "to", 
    3: "tre", 
    4: "fire", 
    5: "fem", 
    6: "seks", 
    7: "syv", 
    8: "åtte", 
    9: "ni", 
    10: "ti"
}

# Skriv ut alle tallene med sine tilhørende tekster i tabellform
print("Tall | Tekst")
print("-----|------")
for tall, tekst in tall_tekst.items():
    print(f"{tall:<5}| {tekst}")

# Test ordboka ved å la en bruker skrive inn et tall
tall_inn = int(input("Skriv inn et tall mellom 1 og 10: "))
if tall_inn in tall_tekst:
    print(f"Teksten for {tall_inn} er {tall_tekst[tall_inn]}.")
else:
    print(f"Ugyldig tall. Prøv igjen.")

'''
    # Oppgåve: utvidelse av konseptet over.
    # Du skal no legge til skrivemåten på fleire språk. 
'''
tall_tekst = {
    1: {"norsk": "en", "engelsk": "one", "spansk": "uno"},
    2: {"norsk": "to", "engelsk": "two", "spansk": "dos"},
    3: {"norsk": "tre", "engelsk": "three", "spansk": "tres"},
    4: {"norsk": "fire", "engelsk": "four", "spansk": "cuatro"},
    5: {"norsk": "fem", "engelsk": "five", "spansk": "cinco"},
    6: {"norsk": "seks", "engelsk": "six", "spansk": "seis"},
    7: {"norsk": "syv", "engelsk": "seven", "spansk": "siete"},
    8: {"norsk": "åtte", "engelsk": "eight", "spansk": "ocho"},
    9: {"norsk": "ni", "engelsk": "nine", "spansk": "nueve"},
    10: {"norsk": "ti", "engelsk": "ten", "spansk": "diez"}
}

# Eksempel på korleis du kan bruke dictionaryen i dette tilfellet
tall = 3
språk = "engelsk"
print(f"Tallet {tall} på {språk} er '{tall_tekst[tall][språk]}'")