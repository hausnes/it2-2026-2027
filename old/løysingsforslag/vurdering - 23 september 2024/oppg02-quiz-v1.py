'''
    Versjon 1 av quizen.
    Får til å hente ut tilfeldige spørsmål og svar, og sjekkar om brukarinput er likt det korrekte svaret.
    Dette er ein forenkla versjon der ein lagrar innbyggjartal som ein streng, og ikkje som heiltal.
    I tillegg har ein ikkje støtte for fleire svaralternativ for naboland, eller å godta eit svar innan +-10% av det korrekte svaret.
'''

fakta = {
    "Norway" : {
        "capital" : "Oslo",
        "population" : "5378857",
        "neighbors" : ["Sweden", "Finland", "Russia"]
    },
    "Sweden" : {
        "capital" : "Stockholm",
        "population" : "10099265",
        "neighbors" : ["Norway", "Finland"]
    },
    "Finland" : {
        "capital" : "Helsinki",
        "population" : "5540720",
        "neighbors" : ["Sweden", "Norway", "Russia"]
    },
    "Russia" : {
        "capital" : "Moscow",
        "population" : "144526636",
        "neighbors" : ["Finland", "Norway"]
    }
}

import random

# Funksjon som stiller eit spørsmål om eit tilfeldig land og eit tilfeldig faktaspørsmål
def ask_question():
    # Velger eit tilfeldig land frå data-dictionaryen
    country = random.choice(list(fakta.keys()))
    # Velger eit tilfeldig attributt/fakta frå landet
    attribute = random.choice(list(fakta[country].keys()))
    
    # Henter det korrekte svaret frå data-dictionaryen
    answer = fakta[country][attribute]
    
    # Printar spørsmålet
    print(f"What is the {attribute} of {country}?")
    
    # Henter brukarinput
    user_answer = input()

    # Sjekker om brukarinput er likt det korrekte svaret
    if user_answer == answer or user_answer in answer:
        print("Correct!")
    else:
        # Opplyser om at svaret er feil, og viser det korrekte svaret
        print(f"Wrong. The correct answer is {answer}.")

# Still spørsmål
ask_question()