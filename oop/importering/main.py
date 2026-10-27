from karakterer import Player, Enemy

spiller = Player("Kari", 1, 100, 10)
fiende = Enemy("Rektor", 3, 60, "linjal")

print(spiller)
print(fiende)

while spiller.is_alive() and fiende.is_alive():
    skade = spiller.attack()
    fiende.take_damage(skade)
    print(f"{spiller.name} gjør {skade} skade. {fiende.name} har {fiende.hp} HP igjen.")

    if not fiende.is_alive():
        print(f"{fiende.name} er beseiret!")
        break

    skade = fiende.attack()
    spiller.take_damage(skade)
    print(f"{fiende.name} slår med {fiende.weapon} og gjør {skade} skade. {spiller.name} har {spiller.hp} HP igjen.")

    if not spiller.is_alive():
        print(f"{spiller.name} er beseiret!")
