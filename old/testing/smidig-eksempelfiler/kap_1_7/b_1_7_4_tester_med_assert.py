def aldersgruppe(alder):
    if alder < 17:
        return 'barn'
    elif alder < 67:
        return 'voksen'
    else:          
        return 'pensjonist'

assert aldersgruppe(10)=='barn'
assert aldersgruppe(15)=='barn'
assert aldersgruppe(16)=='voksen' # AssertionError
assert aldersgruppe(50)=='voksen'
assert aldersgruppe(66)=='voksen'
assert aldersgruppe(67)=='pensjonist'
assert aldersgruppe(80)=='pensjonist'

# Smidig IT-2 © TIP AS, 2024