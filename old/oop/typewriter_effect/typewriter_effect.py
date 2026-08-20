# Kjelde (og diskusjon): https://stackoverflow.com/questions/20302331/typing-effect-in-python
# Her kan du altså bytte ut print() med din eigen effekt

import sys
from time import sleep

words = "This is just a test :P"

def skrivUt(ord, kjapt=True):
    sovetid = 0.03 # AKA kjapt

    if not kjapt: # Dersom brukaren spesifiserer False
        sovetid = 0.3

    # print(f"sovetid er satt til {sovetid}")

    for char in ord:
        sleep(sovetid)
        sys.stdout.write(char)
        sys.stdout.flush()

    print()
        
# print(words)
# skrivUt(words)