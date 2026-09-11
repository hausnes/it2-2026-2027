const fs = require("fs");

const fil = "games.json";

function lesInn(fil) {
    const data = JSON.parse(fs.readFileSync(fil, "utf-8"));
    
    console.log(`Det første spillet i datasettet er ${data.spill[0].name}`);
    
    console.log(`Jeg finner ${data.spill.length} spill i datasettet.`);
}

lesInn(fil);