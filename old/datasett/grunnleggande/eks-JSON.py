import json

filnavn = "data/land.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

print(data) # Alt
# print(json.dumps(data, indent=4)) # "Finare" utskrift til terminalen, eventuelt i nettlesar eller VS Code
# print(data["region"]) # Berre Skandinavia
# print(data["land"]) # Alt som ligg under land
# print(data["land"][0]["navn"]) # ..fordi det under land ligg ei liste..

# for x in data["land"]:
#     print(f'Landet {x["navn"]} har fylgjande byar:')
#     for y in range(len(x["byer"])):
#         print(f'\t{x["byer"][y]}')