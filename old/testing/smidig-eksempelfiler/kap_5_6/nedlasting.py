"""Program med nedlasting fra Internett som skal testes med etterligning."""

import requests
from bs4 import BeautifulSoup


def hent_tittel(url: str) -> str:
    """Last ned en valgfri webside og returner tittelen."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return response.reason
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string
    except requests.exceptions.RequestException as e:
        raise SystemExit(e) from e


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Unit_testing"
    print(hent_tittel(url))


# Smidig IT-2 © TIP AS 2024
