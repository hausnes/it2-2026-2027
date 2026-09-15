import json

FIL = "games.json"


def les_inn(fil):
    with open(fil, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(data["spill"][0])

    print(f"Det første spillet i datasettet er {data['spill'][0]['name']}")

    print(f"Jeg finner {len(data['spill'])} spill i datasettet.")

    # Manuell måte å finne det mest spelte spelet
    maks_spilletid = 0
    pop_spill = ""

    for spill in data["spill"]:
        # print(f"Vurderer {spill['name']} med speletid {spill['playtime_forever_hours']}.")
        if spill["playtime_forever_hours"] > maks_spilletid:
            pop_spill = spill["name"]
            maks_spilletid = spill["playtime_forever_hours"]

    print(f"Det mest populære spelet er {pop_spill}, som du har spelt i {maks_spilletid} timar.")

    # Eksempel på korleis du kan vise eit bilete av eit gitt spel
    biletsti = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{data['spill'][3]['appid']}/header.jpg"
    print(biletsti)


les_inn(FIL)
