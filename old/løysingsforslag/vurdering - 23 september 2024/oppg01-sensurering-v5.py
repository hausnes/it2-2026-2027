'''
    Oppgåve: Sensurering, v5
    -
    Denne gongen skal me bruke regex for å sensurere ord.
    Me lagar eit regex-mønster for kvart problematiske ord som matchar ordet og variasjonane. 
    For eksempel, for ordet "fis", vil mønsteret matche "fis", "fisen", "fisens", "fisar", "fisane", osv., men ikkje "fisk".
    Me brukar re.sub for å erstatte dei matcha orda med enten stjerner eller erstatningsord.

    Forklaring til linje 58 (regex-mønsteret):
    -
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
    "Fiskal (fis fis fis!) blir benyttet om det som har med statskassen eller regnskap å gjøre, som for eksempel «fiskale avgifter» (statlige avgifter), eller «det fiskale året 2005» (regnskapsåret 2005). Fiskale skatter og avgifter har til formål å skaffe inntekter til staten.",
    "Oppskrifter med fisk og sjømat for alle, til middag, lunsj og fest. Lær om behandling av fisk og sjømat."
]

# Funksjon som skal sensurere setningar:
def sensurer(setning, problematiske_ord, erstatningTegn=True): # erstatningTegn er ein valgfri parameter, som default er True
    for ord in problematiske_ord:
        # Lag regex-mønster for å matche ordet og dets variasjoner
        mønster = re.compile(r'\b' + re.escape(ord) + r'(en|ens|ene|er|ers|et|ets|e|es)?\b', re.IGNORECASE) # Sjå eigen kommentar på toppen
        
        def erstatning(match):
            funnet_ord = match.group(0)
            if erstatningTegn:
                return '*' * len(funnet_ord)
            else:
                return erstatningsord.get(ord, funnet_ord)
        
        setning = mønster.sub(erstatning, setning)
    
    return setning

# Sensurerer setningane:
for setning in setningar:
    print("-"*50)
    print(sensurer(setning, problematiske_ord))
    print(sensurer(setning, problematiske_ord, False))