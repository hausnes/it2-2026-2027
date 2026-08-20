def karakter(poengsum:int)->str:
    if poengsum < 50:
        return('Ikke bestått')
    elif 50 < poengsum < 69:
        return('Bestått')
    elif 70< poengsum < 89:
        return('Godt bestått')
    elif 90 < poengsum < 100:
        return('Meget godt bestått')
    else:
        return('Ikke gyldig poengsum!')

assert(karakter(30) == 'Ikke bestått')
assert(karakter(65) == 'Bestått')
assert(karakter(82) == 'Godt bestått')
assert(karakter(97) == 'Meget godt bestått')
assert(karakter(102) == 'Ikke gyldig poengsum!')
assert(karakter(0) == 'Ikke bestått')
#assert(karakter(50) == 'Bestått')
print(f'7: {karakter(50)}')
#assert(karakter(69) == 'Bestått')
print(f'8: {karakter(69)}')
# assert(karakter(70) == 'Godt bestått')
print(f'9: {karakter(70)}')
# assert(karakter(89) == 'Godt bestått')
print(f'10: {karakter(89)}')
# assert(karakter(90) == 'Meget godt bestått')
print(f'11: {karakter(90)}')
# assert(karakter(100) == 'Meget godt bestått')
print(f'12: {karakter(100)}')
# assert(karakter(-1) == 'Ikke gyldig poengsum!')
print(f'13: {karakter(-1)}')

# Smidig IT-2 © TIP AS 2024