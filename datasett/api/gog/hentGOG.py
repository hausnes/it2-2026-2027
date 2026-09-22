"""
hentGOG.py

Henter hvor mange spill du eier på GOG (Good Old Games), og skriver
tallet ut i terminalen.

VIKTIG - GOG har ingen offisiell, offentlig "utvikler-API" slik som
Steam og TMDB har. Det finnes ingen side der du kan registrere en app
og få en enkel API-nøkkel. I stedet bruker vi det samme (uoffisielle)
grensesnittet som GOG Galaxy-klienten selv snakker med. Dette er godt
dokumentert og brukt av flere åpne kildekode-prosjekter (bl.a.
lgogdownloader, minigalaxy og Heroic Games Launcher), men Google/GOG
kan i teorien endre det uten varsel.

Fordi det ikke finnes en enkel API-nøkkel, må du logge inn i en
nettleser og hente en engangskode. Slik gjør du det:

  1. Kopier denne lenken inn i nettleseren din:

     https://auth.gog.com/auth?client_id=46899977096215655&redirect_uri=https%3A%2F%2Fembed.gog.com%2Fon_login_success%3Forigin%3Dclient&response_type=code&layout=client2

  2. Logg inn med din vanlige GOG-konto.
  3. Etter innlogging blir du sendt til en (tom/feil-utseende) side
     med en adresse omtrent slik:

     https://embed.gog.com/on_login_success?origin=client&code=ABCDEF123456...

     Kopier verdien etter "code=" (og ingenting mer - stopp ved en
     eventuell "&").
  4. Lim koden inn i GOG_LOGIN_CODE nedenfor og kjør scriptet med en
     gang - koden er kun gyldig i noen få minutter.
  5. Kjør: python hentGOG.py

Krever biblioteket "requests" (installer med: pip install requests).
"""

import requests

# ---- FYLL INN DENNE ----
GOG_LOGIN_CODE = "KODEN_DU_KOPIERTE_FRA_NETTLESEREN_HER"
# -------------------------

# Disse to er IKKE hemmelige nøkler du selv skal skaffe - det er de
# offentlige ID-ene som GOG Galaxy-klienten selv bruker, og som er
# kjent fra åpen kildekode-prosjekter som snakker med GOG sitt API.
GOG_CLIENT_ID = "46899977096215655"
GOG_CLIENT_SECRET = "9d85c43b1482497dbbce61f6e4aa173a433796eeae2ca8c5f6129f2dc4de46d"
GOG_REDIRECT_URI = "https://embed.gog.com/on_login_success?origin=client"


def hent_tilgangstoken():
    """Bytter engangskoden fra nettleseren mot et ekte tilgangstoken."""
    parametre = {
        "client_id": GOG_CLIENT_ID,
        "client_secret": GOG_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": GOG_LOGIN_CODE,
        "redirect_uri": GOG_REDIRECT_URI,
    }

    response = requests.get("https://auth.gog.com/token", params=parametre)
    response.raise_for_status()  # Gir feilmelding hvis koden er ugyldig/utløpt

    return response.json()["access_token"]


def hent_gog_spill():
    if "KODEN_DU" in GOG_LOGIN_CODE:
        print("Feil: Du må fylle inn GOG_LOGIN_CODE øverst i fila før du kjører scriptet (se instruksjonene i toppen av fila).")
        return

    print("Bytter innloggingskode mot tilgangstoken...")

    try:
        access_token = hent_tilgangstoken()
    except requests.exceptions.RequestException as feil:
        print(f"Klarte ikke å logge inn mot GOG: {feil}")
        print("Vanligste årsak: koden er utløpt (de varer bare noen få minutter) - hent en ny kode og prøv igjen.")
        return

    print("Henter spillbiblioteket ditt fra GOG...")

    try:
        response = requests.get(
            "https://embed.gog.com/user/data/games",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as feil:
        print(f"Klarte ikke å hente data fra GOG sitt API: {feil}")
        return

    data = response.json()
    spill_ider = data.get("owned", [])

    print(f"Ferdig! Du eier {len(spill_ider)} spill på GOG.")


hent_gog_spill()
