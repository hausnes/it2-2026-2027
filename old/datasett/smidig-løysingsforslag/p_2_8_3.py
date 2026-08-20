import json
with open('p_2_8_3.json', encoding='utf-8') as fil:
    obj = json.load(fil)

# a
print('\nBilmerker:')
for merke in obj.keys():
    print(f'  {merke}')

# b
print('\nEn utvalgt Ford modell:')
for n,v in obj['Ford'][1].items():
    print(f'  {n:10}: {v}')

#c
print('\nHele listen:')
for n,v in obj.items():
    print(n)
    for e in v:
        for n2,v2 in e.items(): 
            print(f'  {n2:6}: {v2}')
        print()

def biler_med_farge(farge:str)->None:
    print('\nModeller med fargen: ' + farge.title())
    funnet = False
    for n,v in obj.items(): # merker
        for e in v:         # liste med modeller
            if e['farge'].lower()==farge.lower():
                funnet = True
                print('\n' + n)
                for n2,v2 in e.items(): 
                    print(f'  {n2:6}: {v2}')
    if not funnet: 
        print('Ingen funnet')

biler_med_farge('Rød')