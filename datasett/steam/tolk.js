const fs = require("fs");

const fil = "games.json";

function lesInn(fil) {
    const data = JSON.parse(fs.readFileSync(fil, "utf-8"));

    console.log(data.spill[0]);
    
    console.log(`Det første spillet i datasettet er ${data.spill[0].name}`);
    
    console.log(`Jeg finner ${data.spill.length} spill i datasettet.`);
    
    // Manuell måte å finne det mest spelte spelet
    let maksSpilletid = 0;
    let popSpill = "";

    for (spill of data.spill) {
        // console.log(`Vurderer ${spill.name} med speletid ${spill.playtime_forever_hours}.`)
        if (spill.playtime_forever_hours > maksSpilletid) {
            popSpill = spill.name;
            maksSpilletid = spill.playtime_forever_hours;
        }
    }

    console.log(`Det mest populære spelet er ${popSpill}, som du har spelt i ${maksSpilletid} timar.`);

    // Eksempel på korleis du kan vise eit bilete av eit gitt spel
    let biletsti = `https://cdn.cloudflare.steamstatic.com/steam/apps/${data.spill[3].appid}/header.jpg`;
    console.log(biletsti);
}

lesInn(fil);