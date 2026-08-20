'''
    Versjon 0 av quizen.
    Dette er ein særs forenkla versjon der ein 
    - lagrar innbyggjartal som streng, ikkje som heiltal
    - ikkje har støtte for fleire svaralternativ for naboland
    - ikkje har støtte for å godta eit svar innan +-10% av det korrekte svaret
    - ikkje klarar å velgje eit tilfeldig spørsmål

    Det denne besvarelsen klarar å vise er derimot god bruk av dictionary, og 
    funksjonar med parameter. I tillegg er det godkjent å skrive eit svar med
    store og små bokstavar (oslo vs Oslo vs oSLo).
'''

fakta = {
    "Norge" : {
        "hovudstad" : "Oslo",
        "innbyggjartal" : "5378857",
        "naboland" : ["Sverige", "Finland", "Russland"]
    },
    "Sverige" : {
        "hovudstad" : "Stockholm",
        "innbyggjartal" : "10099265",
        "naboland" : ["Norge", "Finland"]
    },
    "Finland" : {
        "hovudstad" : "Helsinki",
        "innbyggjartal" : "5540720",
        "naboland" : ["Sverige", "Norge", "Russland"]
    },
    "Russland" : {
        "hovudstad" : "Moskva",
        "innbyggjartal" : "144526636",
        "naboland" : ["Finland", "Norge"]
    }
}

# Funksjon som stiller eit spørsmål, med parameter gitt spørsmålsnummer
def still_sporsmal(land, sporsmal):
    # Henter det korrekte svaret frå data-dictionaryen
    korrekt_svar = fakta[land][sporsmal]
    
    # Printar spørsmålet
    print(f"Kva er {sporsmal} i {land}?")
    
    # Henter brukarinput
    svar = input().capitalize()

    # Sjekker om brukarinput er likt det korrekte svaret
    if svar == korrekt_svar or svar in korrekt_svar:
        print("Riktig!")
    else:
        # Opplyser om at svaret er feil, og viser det korrekte svaret
        print(f"Feil. Det korrekte svaret er {korrekt_svar}.")

# Still spørsmål
land = "Norge"
# spm = "innbyggjartal"
spm = "hovudstad"
still_sporsmal(land, spm)