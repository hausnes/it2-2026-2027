'''
    Ein kjapp test for å kunne bruke regex til å finne ordet "fis" og ulike variasjonar av dette, men ikkje "fisk".
    Kjelder:  
        - https://docs.python.org/3/library/re.html#module-re
        - https://www.w3schools.com/python/python_regex.asp
        - https://developers.google.com/edu/python/regular-expressions 
        - https://nowitsanurag.medium.com/regular-expression-in-python-f42483e80daa 
        - https://www.programiz.com/python-programming/regex
        - NB: Powertoys sin PowerRename funksjon har ein regex-modus som kan vere nyttig for å teste regex-uttrykk.

    re.compile blir brukt til å kompilere eit regulært uttrykk (regex) mønster til et regex-objekt. 
    Dette objektet kan deretter brukast til å utføre match-operasjonar på strengar.
    -
    r'\b': r før strengen er for å indikere at det er ein "raw string", som betyr at escape-tegn blir ignorert.
    \b er ein regex-spesialsekvens som representerer ei ordgrense. Det matchar posisjonen mmellom eit teikn som
    ikkje er ein del av eit ord (som mellomrom, punktum etc.) og eit teikn som er ein del av eit ord (alfanumeriske teikn).
    -
    re.escape(ord) blir brukt for å unngå alle spesialteikn i strengen ord. Dette sikrar at ord behandlast som ein
    bokstaveleg streng i regex-mønsteret.
    "ord" er variabelen som inneheld det problematiske ordet me ynskjer å matche.
    -
    r'(en|ens|ene|er|ers|et|ets|e|es)?':
    Dette er ei regex-gruppe som matchar flere moglege endingar på ordet.
    (...) er ei gruppe som inneheld fleire alternativ separert av | (eller).
    en|ens|ene|er|ers|et|ets|e|es er dei forskjellige endingane som me ynskjer å matche.
    ? etter gruppa indikerer at gruppa er valfri, dvs. at den kan dukke opp null eller ein gong.
    -
    re.IGNORECASE:
    Dette flagget gjer regex-mønsteret case-insensitive, slik at det matchar både store og små bokstavar.
'''

import re

setning = "Fis er eit flott ord, men når fisen kjem er det ikkje alltid like flott. Eg fiser ofte etter at eg har ete fisk."

ord = "fis"

mønster = re.compile(r'\b' + re.escape(ord) + r'(en|ens|ene|er|ers|et|ets|e|es)?\b', re.IGNORECASE)

# Finn alle forekomster av mønsteret i setningen
resultat = mønster.sub("***", setning)
# Finn alle forekomster av mønsteret i setningen
resultat_findall = mønster.findall(setning)

# Skriv ut resultatene
print(f"Sensurert setning: {resultat}")
print(resultat_findall)