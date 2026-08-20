import json
with open('p_2_8_1.json', encoding='utf-8') as fil:
    o = json.load(fil)

# a
print(f'\nElise veier {o[1]["vekt"]} kg.')

# b
for e in o:
    print()
    for n,v in e.items():
        if n=='navn': print(v)
        else: print(f'  {n:8}: {v}')