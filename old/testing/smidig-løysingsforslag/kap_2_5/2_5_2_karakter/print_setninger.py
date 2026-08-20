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

print(f'1: {karakter(30)}')
print(f'2: {karakter(65)}')
print(f'3: {karakter(82)}')
print(f'4: {karakter(97)}')
print(f'5: {karakter(102)}')
print(f'6: {karakter(0)}')
print(f'7: {karakter(50)}')
print(f'8: {karakter(69)}')
print(f'9: {karakter(70)}')
print(f'10: {karakter(89)}')
print(f'11: {karakter(90)}')
print(f'12: {karakter(100)}')
print(f'13: {karakter(-1)}')

# Smidig IT-2 © TIP AS 2024