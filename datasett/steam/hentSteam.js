/**
 * hent-steam-spill.js
 *
 * Henter hele Steam-biblioteket ditt (via Steams offisielle Web API)
 * og lagrer det som en lokal JSON-fil.
 *
 * Bruk:
 *   1. Fyll inn STEAM_API_KEY og STEAM_ID64 nedenfor. https://steamcommunity.com/dev/apikey og https://steamid.io/ for steamid64
 *   2. Kjør: node hent-steam-spill.js
 *   3. Resultatet havner i games.json i samme mappe.
 *
 * Krever Node.js 18 eller nyere (bruker innebygd fetch).
 */

const fs = require("fs");

// ---- FYLL INN DISSE TO ----
const STEAM_API_KEY = "DIN_API_NØKKEL_HER";
const STEAM_ID64 = "DIN_STEAMID64_HER";
// ---------------------------

const OUTPUT_FILE = "games.json";

async function hentSteamSpill() {
  if (STEAM_API_KEY.includes("DIN_") || STEAM_ID64.includes("DIN_")) {
    console.error(
      "Feil: Du må fylle inn STEAM_API_KEY og STEAM_ID64 øverst i fila før du kjører scriptet."
    );
    process.exit(1);
  }

  const url =
    `https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/` +
    `?key=${STEAM_API_KEY}` +
    `&steamid=${STEAM_ID64}` +
    `&format=json` +
    `&include_appinfo=true` +
    `&include_played_free_games=true`;

  console.log("Henter spilldata fra Steam...");

  let response;
  try {
    response = await fetch(url);
  } catch (err) {
    console.error("Klarte ikke å kontakte Steam sitt API:", err.message);
    process.exit(1);
  }

  if (!response.ok) {
    console.error(
      `Steam svarte med feilkode ${response.status}. ` +
        `Sjekk at API-nøkkelen og SteamID64 er riktige, og at spilllisten er satt til offentlig.`
    );
    process.exit(1);
  }

  const data = await response.json();
  const games = data?.response?.games; // Med ?. blir games i stedet undefined hvis noe mangler, og det fanges opp rett under

  if (!games) {
    console.error(
      "Fant ingen spill i svaret. Vanligste årsak: profilen/spilldetaljene er ikke satt til offentlig i Steam-innstillingene."
    );
    process.exit(1);
  }

  // Legg til spilletid i timer i tillegg til minutter, som en liten bonus for elevene
  const bearbeidet = games.map((spill) => ({
    ...spill,
    playtime_forever_hours: Math.round((spill.playtime_forever / 60) * 10) / 10,
  }));

  const resultat = {
    antall_spill: bearbeidet.length,
    hentet_dato: new Date().toISOString(),
    spill: bearbeidet,
  };

  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(resultat, null, 2), "utf-8");

  console.log(`Ferdig! ${bearbeidet.length} spill lagret i ${OUTPUT_FILE}`);
}

hentSteamSpill();