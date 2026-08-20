"""Program med tilfeldige verdier som skal testes med etterligning."""

import random


def tilfeldig_farge() -> str:
    """Returner en vilkårlig farge."""
    farger = ["Rød", "Grønn", "Blå"]
    return random.choice(farger)


if __name__ == "__main__":
    print(tilfeldig_farge())

# Smidig IT-2 © TIP AS 2024
