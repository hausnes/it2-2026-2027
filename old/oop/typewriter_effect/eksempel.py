# from typewriter_effect import *
# eller
import typewriter_effect as jbh # Gjer det tydelegare at det er ditt eige..?

setning = "Jo Bjørnar Hausnes elskar OOP."

langSetning = '''
    ... og setningar
    som går 
    over fleire linjer.
'''

# Eksempel 1
print("Standard bruk av print:")
print(setning)
print(langSetning)

# Eksempel 2
print("Eigendefinert 'typewriter', med kjapp standardinnstilling:")
jbh.skrivUt(setning) # Kjapt er satt som standard, kunne skrive ", True" om me ville vere tydeleg
jbh.skrivUt(langSetning)

# Eksempel 3
print("Eigendefinert 'typewriter', med spesifisert treig innstilling:")
jbh.skrivUt(setning, False)
jbh.skrivUt(langSetning, False)