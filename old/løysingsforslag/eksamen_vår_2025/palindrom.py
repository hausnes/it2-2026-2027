def er_palindrom(s):
    # Fjerner mellomrom og gjør strengen til små bokstaver
    s = s.replace(" ", "").lower()
    # Sjekker om strengen er lik sin reverserte versjon
    return s == s[::-1]

def er_palindrom_alternativ(s):
    # Fjerner mellomrom og gjør strengen til små bokstaver
    s = s.replace(" ", "").lower()
    
    # Initialiserer to pekere, en på starten og en på slutten av strengen
    start = 0
    slutt = len(s) - 1
    
    # Sjekker tegnene fra start og slutt mot midten
    while start < slutt:
        if s[start] != s[slutt]:
            return False
        start += 1
        slutt -= 1
    
    return True

# Eksempel på bruk
test_streng = "A man a plan a canal Panama"
print(er_palindrom(test_streng))  # Output: True
print(er_palindrom_alternativ(test_streng)) # Output: True

def tal_er_palindrom(n):
    """
    Sjekkar om eit positivt heiltall er eit palindrom.

    Args:
        n: Eit positivt heiltal.

    Returns:
        True dersom n er eit palindrom, False ellers.
    """
    if n < 0:
        return False  # Palindrom definerast vanlegvis for ikkje-negative tal

    original_tall = n
    reversert_tall = 0

    while n > 0:
        siste_siffer = n % 10
        reversert_tall = (reversert_tall * 10) + siste_siffer
        n //= 10

    return original_tall == reversert_tall

# Eksempel på bruk:
tall = int(input("Skriv inn eit positivt heiltal: "))
if tal_er_palindrom(tall):
    print("True")
else:
    print("False")

# Kor mange tresifra palindromtal er det?
antall_palindrom = 0
for h in range(100, 1000):  # Går gjennom alle tresifra tall
    if tal_er_palindrom(h):
        antall_palindrom += 1

print(f"Antall tresifrede palindromtall: {antall_palindrom}")