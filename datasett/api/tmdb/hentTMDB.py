"""
hentTMDB.py

Henter de 5 mest populære filmene fra 2026 fra The Movie Database
(TMDB) sitt API, og skriver dem ut i terminalen.

Bruk:
  1. Lag en gratis konto på https://www.themoviedb.org/signup
  2. Gå til kontoinnstillingene dine -> "API" (eller direkte:
     https://www.themoviedb.org/settings/api), og be om en API-nøkkel
     ("Request an API Key"). Velg "Developer" og fyll ut det korte
     skjemaet - du får nøkkelen med en gang.
  3. Du kan få både en "API Key (v3 auth)" og et "API Read Access
     Token (v4 auth)". Vi bruker v3-nøkkelen her, siden den er
     enklest å bruke (sendes bare som en vanlig parameter i URL-en).
  4. Fyll inn TMDB_API_KEY nedenfor.
  5. Kjør: python hentTMDB.py

Krever biblioteket "requests" (installer med: pip install requests).
"""

import requests

# ---- FYLL INN DENNE ----
TMDB_API_KEY = "DIN_API_NØKKEL_HER"
# -------------------------

AAR = 2026
ANTALL_FILMER = 5


def hent_populaere_filmer():
    if "DIN_" in TMDB_API_KEY:
        print("Feil: Du må fylle inn TMDB_API_KEY øverst i fila før du kjører scriptet.")
        return

    url = "https://api.themoviedb.org/3/discover/movie"
    parametre = {
        "api_key": TMDB_API_KEY,
        "primary_release_year": AAR,
        "sort_by": "popularity.desc",
        "language": "no-NO",  # Norske titler/beskrivelser der de finnes
    }

    print(f"Henter de {ANTALL_FILMER} mest populære filmene fra {AAR}...")

    try:
        response = requests.get(url, params=parametre)
        response.raise_for_status()  # Gir en feilmelding hvis TMDB svarer med feilkode
    except requests.exceptions.RequestException as feil:
        print(f"Klarte ikke å hente data fra TMDB sitt API: {feil}")
        return

    data = response.json()
    filmer = data.get("results", [])

    if not filmer:
        print(f"Fant ingen filmer fra {AAR}.")
        return

    # "results" kommer allerede sortert etter popularitet (mest populær først),
    # så vi trenger bare å ta de 5 første med vanlig listeindeksering.
    topp_filmer = filmer[:ANTALL_FILMER]

    print(f"\nDe {len(topp_filmer)} mest populære filmene fra {AAR}:")
    for i, film in enumerate(topp_filmer, start=1):
        tittel = film["title"]
        popularitet = film["popularity"]
        utgivelsesdato = film.get("release_date", "ukjent dato")
        print(f"{i}. {tittel} (utgitt: {utgivelsesdato}, popularitet: {popularitet})")


hent_populaere_filmer()
