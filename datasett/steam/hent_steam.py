"""
hent_steam.py

Henter hele Steam-biblioteket ditt (via Steams offisielle Web API)
og lagrer det som en lokal JSON-fil.

Bruk:
  1. Fyll inn STEAM_API_KEY og STEAM_ID64 nedenfor.
     https://steamcommunity.com/dev/apikey og https://steamid.io/ for steamid64
  2. Kjør: python hent_steam.py
  3. Resultatet havner i games.json i samme mappe.

Krever biblioteket "requests" (installer med: pip install requests).
"""

import json
import requests

# ---- FYLL INN DISSE TO ----
STEAM_API_KEY = "DIN_API_NØKKEL_HER"
STEAM_ID64 = "DIN_STEAMID64_HER"
# ---------------------------

OUTPUT_FILE = "games.json"


def hent_steam_spill():
    if "DIN_" in STEAM_API_KEY or "DIN_" in STEAM_ID64:
        print("Feil: Du må fylle inn STEAM_API_KEY og STEAM_ID64 øverst i fila før du kjører scriptet.")
        return

    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    parametre = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID64,
        "format": "json",
        "include_appinfo": True,
        "include_played_free_games": True,
    }

    print("Henter spilldata fra Steam...")

    try:
        response = requests.get(url, params=parametre)
        response.raise_for_status()  # Gir en feilmelding hvis Steam svarer med feilkode
    except requests.exceptions.RequestException as feil:
        print(f"Klarte ikke å hente data fra Steam sitt API: {feil}")
        return

    data = response.json()
    spill = data.get("response", {}).get("games")

    if not spill:
        print("Fant ingen spill i svaret. Vanligste årsak: profilen/spilldetaljene er ikke satt til offentlig i Steam-innstillingene.")
        return

    # Legg til spilletid i timer i tillegg til minutter, som en liten bonus for elevene
    for s in spill:
        s["playtime_forever_hours"] = round(s["playtime_forever"] / 60, 1)

    resultat = {
        "antall_spill": len(spill),
        "spill": spill,
    }

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(resultat, f, indent=2, ensure_ascii=False)
    except OSError as feil:
        print(f"Klarte ikke å lagre fila: {feil}")
        return

    print(f"Ferdig! {len(spill)} spill lagret i {OUTPUT_FILE}")


hent_steam_spill()
