# Reverse Engineer Anything

**Modding, rekompilering, dekompilering, reverse engineering og annet nytt fra IT-verden**

> Hvordan kan man finne ut hvordan et program virker, uten å ha kildekoden? Hva skjer når AI plutselig gjør dette mye enklere? Hvilke muligheter har vi?

Eksempel på video som oppsummerer litt av essensen i originalartiklene lenger nede (klikk på bildet for å se videoen):

[![Video på YouTube: oppsummering av temaet](https://img.youtube.com/vi/wajoP_5Cpw8/hqdefault.jpg)](https://www.youtube.com/watch?v=wajoP_5Cpw8)

---

## Om oppgaven

Du skal lese, se og prøve ut, og samtidig skrive svarene dine i en **Markdown-fil** (`fornavn-reverse-engineering.md`).

- Oppgavene merket **🔴 Obligatorisk** skal alle gjøre.
- Fra oppgavene merket **🔵 Valgfri** velger du **minst to**.
- Lever `.md`-filen sammen med en mappe med bildene du bruker (f.eks. `bilder/`).

Bruk gjerne denne guiden hvis du lurer på noe i Markdown: [Markdown Guide – Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

## Krav til Markdown

Besvarelsen din skal **minst** inneholde:

| Element | Eksempel på syntaks |
|---|---|
| Overskrifter av ulik størrelse | `#`, `##`, `###` |
| Paragrafer | Tom linje mellom avsnitt |
| Lenker | `[tekst](https://...)` |
| Uthevet tekst | `**fet**` og `*kursiv*` |
| Kode i linjen og kodeblokk | `` `kode` `` og ` ``` ` |
| Sitat | `> sitat` |
| Tabell | `\| kolonne \| kolonne \|` |
| Bilde | `![beskrivelse](bilder/skjermbilde.png)` |
| Punktliste og nummerert liste | `-` og `1.` |

**Bonus**:

- Sjekkliste: `- [x] Ferdig`
- Horisontal linje: `---`
- Fotnote: `Tekst[^1]` og `[^1]: Kilde`
- Innholdsfortegnelse med interne lenker: `[Begreper](#begreper)`

---

## Kilder

### Hovedtema: REA – Reverse Engineer Anything

- [rea.tools](https://rea.tools/) – nettsiden til verktøyet
- [Diskusjon på Hacker News](https://news.ycombinator.com/item?id=50028275) – hva sier utviklere om verktøyet?

### Spill

| Kilde | Type | Hva handler det om? |
|---|---|---|
| [Tek.no: «Sånn har du aldri sett Pokémon-spillene»](https://www.tek.no/nyheter/kommentar/i/M79rGR/saann-har-du-aldri-sett-pokemon-spillene) | Artikkel (norsk) | Gamle Pokémon-spill i ny drakt |
| [MVG: «Recomps and decomps have taken over retro gaming»](https://www.youtube.com/watch?v=mYZPHdKKMaI) | Video (engelsk) | Oversikt over recomp- og decomp-prosjekter |
| [Quiver Launcher](https://github.com/tgeorgiadis/quiver-launcher) | GitHub-prosjekt | Launcher for recomp-spill |
| [Ars Technica (2020): «Beyond emulation …»](https://arstechnica.com/gaming/2020/05/beyond-emulation-the-massive-effort-to-reverse-engineer-n64-source-code/) | Artikkel (engelsk) | Dekompileringen av *Super Mario 64* – slik det var for noen år siden |

### Programvare og firmware

| Kilde | Type | Hva handler det om? |
|---|---|---|
| [Ars Technica: «Software is over …»](https://arstechnica.com/ai/2026/10/software-is-over-bold-ai-developer-takes-aim-at-adobe-with-open-source-clones/) | Artikkel (engelsk) | AI-lagde open source-kloner av Adobe-programmer |
| [Tom's Hardware: Office-kloner](https://www.tomshardware.com/software/microsoft-office/creator-of-free-adobe-clones-unveils-open-source-microsoft-office-excel-powerpoint-and-word-replications-autodesk-tools-and-other-subscription-based-services-may-come-next) | Artikkel (engelsk) | Samme utvikler lager kloner av Word, Excel og PowerPoint |
| [PetaPixel: Office-kloner](https://petapixel.com/2026/10/12/there-are-free-open-source-versions-of-microsoft-office-apps-thanks-to-ai/) | Artikkel (engelsk) | Samme sak, annen vinkel |
| [Low Level: «Has AI solved reverse engineering?»](https://www.youtube.com/watch?v=wIe3eDfGKUo) | Video (engelsk) | Klarer AI egentlig å reverse-engineere? |

---

## 🔴 Obligatoriske oppgaver

### Oppgave 1 – Begreper

Forklar begrepene under **med egne ord**. Bruk gjerne et eksempel fra kildene til hvert begrep.

**Må være med:**

1. Kildekode og maskinkode
2. Kompilering
3. Dekompilering
4. Rekompilering (særlig *statisk rekompilering*, slik det brukes i «recomp»-prosjektene)
5. Reverse engineering
6. Modding
7. Emulering
8. Open source (og lisens)

**Ekstra (velg gjerne noen):** disassemblering, portering, *clean room*-reverse-engineering, firmware, klone.

> 💡 **Tips:** Lag en tabell med kolonnene *Begrep*, *Forklaring* og *Eksempel*.

<details>
<summary><strong>Løsningsforslag – begreper</strong> (prøv selv først!)</summary>

<br>

**Kildekode og maskinkode**
*Kildekode* er programmet slik utviklerne skriver det, i et språk mennesker kan lese (f.eks. C, Python eller JavaScript). *Maskinkode* er instruksjonene prosessoren faktisk kjører – bare tall (binært), som er svært vanskelig for mennesker å lese. Når du kjøper et spill eller et program, får du som regel bare maskinkoden.

**Kompilering**
Å oversette kildekode til maskinkode med et program som kalles en *kompilator*. Underveis forsvinner mye informasjon, som navn på variabler og funksjoner, og kommentarer. Det er derfor det er så vanskelig å gå tilbake igjen.

**Dekompilering**
Den motsatte veien: å gå fra maskinkode tilbake til kildekode som kan leses. Resultatet blir aldri helt likt originalen, så mennesker (og nå også AI) må gi navn til funksjoner og variabler og rydde i koden. *Eksempel:* Super Mario 64-prosjektet, der frivillige gjenskapte C-kode som gir *nøyaktig* samme maskinkode når den kompileres på nytt («matching decompilation»). Når man har kildekoden, kan spillet porteres til PC og andre plattformer.

**Rekompilering (statisk rekompilering)**
Å oversette maskinkode for én plattform direkte til et program som kjører på en annen plattform, uten å gå veien om lesbar kildekode. I «recomp»-prosjektene (f.eks. N64-spill som kjører rett på PC) oversettes hele spillet på forhånd («statisk»), i stedet for mens det kjører. Dette går ofte raskere å få til enn en full dekompilering, men koden blir ikke like lett å lese og endre.

**Reverse engineering**
Samlebegrepet for å finne ut hvordan noe virker ved å undersøke det ferdige produktet, når man ikke har tegningene eller kildekoden. Dekompilering, disassemblering og å studere hva et program gjør mens det kjører (f.eks. nettverkstrafikk) er alle former for reverse engineering. Det gjelder ikke bare programvare, også maskinvare og fysiske produkter.

**Modding**
Å endre et eksisterende spill eller program, f.eks. ny grafikk, nye baner, høyere oppløsning eller nye funksjoner. Modding er mye enklere når man har kildekode fra en dekompilering eller et recomp-prosjekt, men har også blitt gjort lenge ved å endre filer direkte.

**Emulering**
Å late som man er en annen maskin: en *emulator* er et program som etterligner maskinvaren til f.eks. en Nintendo 64, slik at det originale spillet kan kjøre uendret på en PC. Forskjellen fra decomp/recomp er at spillet selv ikke endres, det er «maskinen» som simuleres. Det krever mer regnekraft og gir mindre frihet til å endre spillet.

**Open source (og lisens)**
*Open source* (åpen kildekode) betyr at kildekoden er offentlig tilgjengelig, slik at hvem som helst kan lese den, lære av den, endre den og dele den videre. *Lisensen* bestemmer hva man har lov til: med MIT-lisensen kan du gjøre nesten hva du vil, mens GPL-lisensen krever at endrede versjoner også må deles som open source. Open source-programmer lages ofte av frivillige og er som regel gratis, men det betyr ikke at de er uten regler. *Eksempel:* GIMP, Inkscape og LibreOffice har vært gratis alternativer til Adobe og Microsoft Office i mange år. Det er derfor ikke det at alternativene er gratis som er nytt med de AI-lagde klonene, men hvor raskt de lages, og at de etterligner originalen så tett.

---

**Ekstra begreper**

| Begrep | Forklaring |
|---|---|
| Disassemblering | Å oversette maskinkode til *assembly* – en tekstversjon av maskininstruksjonene. Lesbart for eksperter, men mye mer lavnivå enn dekompilert kode. Ofte første steg i reverse engineering. |
| Portering | Å tilpasse et program slik at det kjører på en annen plattform, f.eks. fra konsoll til PC. |
| Clean room-reverse-engineering | En metode for å unngå brudd på opphavsretten: én gruppe undersøker originalen og skriver en beskrivelse av hvordan den virker, og en *annen* gruppe som aldri har sett originalkoden lager et nytt program ut fra beskrivelsen. |
| Klone | Et program som etterligner et annet programs funksjoner og utseende, men er laget med egen kode. En klone trenger ikke være laget med reverse engineering. |
| Firmware | Programvare som ligger innebygd i maskinvare, f.eks. i en ruter, et hovedkort, en skriver eller en spillkonsoll. |

</details>

### Oppgave 2 – Hva er REA?

Les [rea.tools](https://rea.tools/) og skum gjennom diskusjonen på [Hacker News](https://news.ycombinator.com/item?id=50028275).

1. Hva er REA, og hva kan det brukes til?
2. Hvordan installeres det? Vis kommandoen i en **kodeblokk**.
3. Hva slags programmer kan det analysere?
4. Finn **ett** positivt og **ett** kritisk innlegg på Hacker News, og gjengi dem som **sitat** (med lenke).

### Oppgave 3 – For og mot

Lag to lister (eller én tabell) med argumenter **for** og **mot** det som skjer i spill- og programvareverdenen nå. Tenk for eksempel på:

- Bevaring av gamle spill og programvare
- Opphavsrett og lisenser, hvem eier koden?
- Arbeidsplasser og selskaper som lever av abonnement
- Sikkerhet, både for og mot (kan verktøyene brukes til å finne sårbarheter, eller til å lage skadevare?)
- Kvalitet og brukerstøtte,  hvem hjelper deg når en gratis klone ikke virker?
- Open source: Hva er nytt nå, når gratis alternativer som GIMP og LibreOffice har fantes i mange år?
- ...

**Under listene:** Skriv din personlige mening i ett eller flere avsnitt. Er dette mest positivt eller negativt? Begrunn svaret.

### Oppgave 4 – Prøv det selv: Adobe-klonene

Prøv minst ett av de AI-lagde Adobe-alternativene som omtales i artikkelen.

> 💡 **Visste du?** Det har lenge eksistert gratis open source-alternativer til Adobe-programmene, laget av frivillige over mange år, uten AI og uten reverse engineering:
>
> | Adobe | Open source-alternativ |
> |---|---|
> | Photoshop | [GIMP](https://www.gimp.org/), [Krita](https://krita.org/) |
> | Illustrator | [Inkscape](https://inkscape.org/) |
> | InDesign | [Scribus](https://www.scribus.net/) |
> | Lightroom | [darktable](https://www.darktable.org/) |
> | Premiere Pro | [Kdenlive](https://kdenlive.org/), [Shotcut](https://shotcut.org/) |
> | After Effects | [Natron](https://natrongithub.github.io/) |
> | Audition | [Audacity](https://www.audacityteam.org/) |
> | Microsoft Office | [LibreOffice](https://www.libreoffice.org/) |

1. Hvilket program prøvde du, og hvilket Adobe-program skal det erstatte?
2. Hvor lastet du det ned fra, og hvordan installerte/startet du det?
3. Lag en **tabell** som sammenligner klonen med originalen (pris, funksjoner, brukervennlighet, ytelse, lisens).
4. Legg ved **minst to skjermbilder** av opplevelsen.
5. Gi en samlet vurdering: Ville du anbefalt dette til en vanlig bruker? Til en bedrift?
6. Sammenlign klonen med et av de etablerte open source-alternativene i tabellen over. Hva er forskjellen på en *klone* som etterligner Adobe, og et alternativ som har utviklet seg på egen hånd? Hvorfor tror du mange fortsatt betaler for Adobe, selv om gratis alternativer har eksistert lenge?

> ⚠️ **Husk:** Last kun ned fra den offisielle kilden (som lenkes i artiklene / GitHub).

---

## 🔵 Valgfrie oppgaver (velg minst to)

### Oppgave 5 – Super Mario 64: Da og nå

Les Ars Technica-artikkelen fra 2020 og se MVG-videoen. Sammenlign i en tabell: Hva var målet den gang, hvor lang tid tok det, og hva er mulig i dag? Hvilken rolle spiller AI nå?

### Oppgave 6 – Pokémon i ny drakt

Les Tek.no-artikkelen. Hva er det som gjør at Pokémon-spillene kan se så annerledes ut? Hvilke av begrepene fra oppgave 1 passer her?

### Oppgave 7 – Quiver Launcher

Se på GitHub-siden til [Quiver Launcher](https://github.com/tgeorgiadis/quiver-launcher). Hva gjør den, hvilke spill støtter den, og hva trenger man for å bruke den? Lovlig bruk krever at du eier originalspillet – hvorfor?

### Oppgave 8 – Har AI løst reverse engineering?

Se Low Level-videoen. Hva er hovedpoengene? Er du enig i konklusjonen? Bruk minst ett **sitat** fra videoen.

### Oppgave 9 – Brukerstøtte: Skriv en veiledning

Du jobber på en helpdesk, og en kollega vil bytte fra et Adobe-program til klonen du testet. Skriv en kort **steg-for-steg-veiledning** (nummerert liste) med skjermbilder, og en liten **FAQ** med vanlige problemer og løsninger.

### Oppgave 10 – Lov og etikk

Er det lov å dekompilere et program i Norge? Undersøk kort hva åndsverkloven sier, og forklar forskjellen på å lage en klone fra bunnen av og å kopiere kode direkte. Oppgi kildene dine.

### Oppgave 11 – Office-klonene

Prøv også en av Office-klonene. Klarer den å åpne en `.docx`- eller `.xlsx`-fil du har fra før? Hva fungerer, og hva fungerer ikke?

---

## Sjekkliste før innlevering

- [ ] Alle obligatoriske oppgaver (1–4) er besvart
- [ ] Minst to valgfrie oppgaver er besvart
- [ ] Alle påkrevde Markdown-elementer er brukt
- [ ] Bildene vises riktig (sjekk forhåndsvisningen!)
- [ ] Filen heter `fornavn-reverse-engineering.md`
