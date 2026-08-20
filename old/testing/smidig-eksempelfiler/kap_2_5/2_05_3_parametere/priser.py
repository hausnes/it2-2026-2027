def billettpris(alder:int)->int:
    if    6 <= alder <= 17: return  63 # Barn/Ungdom
    elif 18 <= alder <= 66: return 157 # Voksen
    else                  : return  79 # Honnør

# Smidig IT-2 © TIP AS, 2024