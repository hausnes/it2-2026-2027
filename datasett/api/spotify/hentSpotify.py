"""
hentSpotify.py

Henter hvilken artist du har hørt mest på i det siste, via Spotifys
offisielle Web API, og skriver navnet ut i terminalen.

Spotify krever at du logger inn (Spotify vet jo bare hva DU har hørt
på hvis du sier hvem du er), så oppsettet har noen flere steg enn
Steam-eksempelet. Slik gjør du det:

  1. Gå til https://developer.spotify.com/dashboard og logg inn med
     din vanlige Spotify-konto (gratis-konto er nok).
  2. Klikk "Create app". Fyll inn et navn og en beskrivelse (valgfritt
     hva).
  3. Under "Redirect URIs", legg til nøyaktig denne adressen:

     http://127.0.0.1:8888/callback

     (Dette er en lokal adresse på din egen maskin - appen din
     trenger den for å ta imot svaret fra Spotify etter innlogging.)
  4. Lagre appen. Gå inn på "Settings" for appen din, og du finner
     "Client ID" og "Client secret" (du må trykke "View" for å se
     secreten).
  5. Fyll inn CLIENT_ID og CLIENT_SECRET nedenfor.
  6. Installer biblioteket "spotipy", som gjør selve innloggingen
     (OAuth) enkel for oss:

     pip install spotipy

  7. Kjør: python hentSpotify.py

     Første gang åpnes en nettleser der du må logge inn og godkjenne
     at scriptet får lese lyttehistorikken din. Etter det husker
     spotipy innloggingen din lokalt (i en .cache-fil), så du slipper
     å logge inn på nytt hver gang.
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---- FYLL INN DISSE TO ----
CLIENT_ID = "DIN_CLIENT_ID_HER"
CLIENT_SECRET = "DIN_CLIENT_SECRET_HER"
# ----------------------------

REDIRECT_URI = "http://127.0.0.1:8888/callback"

# "Scope" forteller Spotify hva scriptet ber om lov til å gjøre.
# user-top-read gir lov til å lese hvilke artister/låter du har hørt mest på.
SCOPE = "user-top-read"


def hent_mest_spilte_artist():
    if "DIN_" in CLIENT_ID or "DIN_" in CLIENT_SECRET:
        print("Feil: Du må fylle inn CLIENT_ID og CLIENT_SECRET øverst i fila før du kjører scriptet.")
        return

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    ))

    print("Henter toppartisten din fra Spotify...")

    try:
        # time_range kan også være "short_term" (siste 4 uker) eller
        # "long_term" (flere år) - "medium_term" er omtrent siste 6 måneder.
        resultat = sp.current_user_top_artists(limit=1, time_range="medium_term")
    except spotipy.SpotifyException as feil:
        print(f"Klarte ikke å hente data fra Spotify sitt API: {feil}")
        return

    artister = resultat.get("items")

    if not artister:
        print("Fant ingen topp-artister. Vanligste årsak: du har ikke lyttet nok på Spotify ennå til at de har nok data om deg.")
        return

    toppartist = artister[0]
    print(f"Artisten du har hørt mest på (siste ca. 6 måneder): {toppartist['name']}")


hent_mest_spilte_artist()
