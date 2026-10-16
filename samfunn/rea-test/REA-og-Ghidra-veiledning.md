# Se inni et Windows-program med REA og Ghidra

En trinnvis veiledning i *reverse engineering*: å finne ut hva et ferdig
kompilert program gjør, uten tilgang til kildekoden.

Vi lager et bitte lite Windows-program (en `.exe`-fil) selv, slik at vi vet
fasiten på forhånd. Så ser vi på filen utenfra, og til slutt bruker vi REA og
Ghidra til å se inni den og gjenskape koden.

> Alle utskrifter i denne veiledningen er ekte, kjørt på en Mac med
> REA 6.5.0 og Ghidra 12.1.4.

---

## Innhold

1. [Verktøyene](#1-verktøyene)
2. [Installasjon](#2-installasjon)
3. [Lag en test-EXE](#3-lag-en-test-exe)
4. [Se på filen utenfra](#4-se-på-filen-utenfra)
5. [Se inni med REA og Ghidra](#5-se-inni-med-rea-og-ghidra)
6. [Sammenlign med fasiten](#6-sammenlign-med-fasiten)
7. [Oppgaver](#7-oppgaver)
8. [Feilsøking](#8-feilsøking)
9. [Ordliste](#9-ordliste)

---

## 1. Verktøyene

| Verktøy | Hva det er |
|---|---|
| **Ghidra** | Et gratis reverse engineering-verktøy fra NSA (åpen kildekode). Det leser maskinkode og gjør den om til assembly og C-lignende kode (*dekompilering*). |
| **REA** | «Reverse Engineer Anything». Et kommandolinjeverktøy og en MCP-server som styrer Ghidra (og andre verktøy) for deg, og gir resultatene i et ryddig format. |
| **MCP** | *Model Context Protocol*. En standard som lar en AI-agent (som Claude Code) bruke eksterne verktøy. Gjennom MCP kan du be agenten på vanlig norsk om å analysere en fil. |
| **Java (OpenJDK 21)** | Ghidra er skrevet i Java og trenger det for å kjøre. |

Sammenhengen:

```
  Du  ──spør──▶  AI-agent (Claude Code)  ──MCP──▶  REA  ──styrer──▶  Ghidra
                                                          │
  Du  ──────────────── kommandolinje (npx rea-agents …) ──┘
```

Du kan altså bruke REA på to måter: **gjennom en AI-agent** eller
**direkte fra terminalen**. Begge viser vi under.

---

## 2. Installasjon

Forutsetninger: macOS med [Homebrew](https://brew.sh) og Node.js 20 eller nyere.

**Steg 1 – Installer Ghidra** (Java 21 kommer med automatisk):

```bash
brew install ghidra
```

**Steg 2 – Fortell REA hvor Ghidra og Java ligger:**

```bash
export GHIDRA_INSTALL_DIR=/opt/homebrew/opt/ghidra/libexec
export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
```

Tips: legg disse to linjene i `~/.zshrc` så de gjelder i alle terminalvinduer.

**Steg 3 – Koble REA til AI-agenten.** Se først hva som vil skje (ingenting
endres):

```bash
npx rea-agents@latest setup --client claude_code --dry-run
```

Kjør det på ekte når du er fornøyd med planen:

```bash
npx rea-agents@latest setup --client claude_code
```

Setup tar sikkerhetskopi av konfigurasjonen før den endrer noe. Start
Claude Code på nytt etterpå.

**Steg 4 – Sjekk at alt virker:**

```bash
npx rea-agents@latest doctor --client claude_code --provider ghidra
```

Se etter `healthy: true`. (`environment_healthy: false` er normalt så lenge
verktøy du ikke trenger, som Hopper og IDA, ikke er installert.)

---

## 3. Lag en test-EXE

Vi har ingen Windows-kompilator på Macen, så vi bygger EXE-filen **byte for
byte** med et Python-skript: `eksempel/lag_exe.py`.

> **Hvor enkelt er det egentlig?** `eksempel/make_pe.py` er det opprinnelige
> skriptet: bare 33 linjer, uten forklarende kommentarer. Det lager nøyaktig
> samme fil (samme SHA-256) som `lag_exe.py`, som er den kommenterte
> versjonen for undervisning.

Programmet tilsvarer denne C-koden:

```c
int add(int a, int b) { return a + b; }
int main(void)        { return add(2, 3); }
```

Kjør skriptet:

```bash
cd eksempel
python3 lag_exe.py hello.exe
```

```
Skrev 1024 byte til hello.exe
```

Hele programmet er 1024 byte. Til sammenligning er et vanlig «Hello world» fra
en C-kompilator gjerne 50–100 KB, fordi kompilatoren legger til mye støttekode.
Vår fil inneholder bare det aller nødvendigste:

| Del | Innhold |
|---|---|
| DOS-header | Starter med `MZ`, og peker videre til PE-headeren |
| PE-header | Sier at dette er et 64-bits Windows-program, hvor koden starter osv. |
| Seksjonstabell | Én seksjon, `.text`, som inneholder koden |
| `.text` | 36 byte maskinkode – selve programmet |

Den egentlige koden er bare disse 36 bytene (se kommentarene i skriptet):

```
48 83 EC 28      sub  rsp, 0x28        ; gjør plass på stakken
B9 02 00 00 00   mov  ecx, 2           ; første argument = 2
BA 03 00 00 00   mov  edx, 3           ; andre argument  = 3
E8 0D 00 00 00   call add              ; kall add
48 83 C4 28      add  rsp, 0x28        ; rydd opp
C3               ret                   ; ferdig
CC CC … CC       (utfylling)
8D 04 11         lea  eax, [rcx+rdx]   ; add: eax = a + b
C3               ret
```

---

## 4. Se på filen utenfra

Før vi bruker spesialverktøy: hva kan vi finne ut med vanlige verktøy?

### 4.1 Hva slags fil er det?

```bash
file hello.exe
```

```
hello.exe: MS-DOS executable PE32+ executable (console) x86-64, for MS Windows
```

`file` ser på de første bytene og kjenner igjen formatet: et 64-bits
Windows-konsollprogram.

### 4.2 Kan vi kjøre den?

```bash
chmod +x hello.exe
./hello.exe
```

```
zsh: exec format error: ./hello.exe
```

Nei. macOS forstår ikke Windows-formatet (PE). Dobbeltklikker du på filen i
Finder, vet ikke macOS hvilket program som skal åpne den. Det er faktisk en
fordel: **statisk analyse** (å se på filen uten å kjøre den) er trygt, selv
med programmer vi ikke stoler på.

### 4.3 Finnes det lesbar tekst?

```bash
strings -a hello.exe
```

```
.text
```

Bare navnet på seksjonen. Programmet vårt skriver ikke ut noe, så det har
ingen tekst. I ekte programmer gir `strings` ofte nyttige spor: feilmeldinger,
nettadresser, filnavn.

### 4.4 De rå bytene

```bash
xxd -l 0x190 hello.exe
```

```
00000000: 4d5a 0000 0000 0000 0000 0000 0000 0000  MZ..............
...
00000030: 0000 0000 0000 0000 0000 0000 4000 0000  ............@...
00000040: 5045 0000 6486 0100 0000 0000 0000 0000  PE..d...........
00000050: 0000 0000 f000 2200 0b02 0e00 0002 0000  ......".........
00000060: 0000 0000 0000 0000 0010 0000 0010 0000  ................
00000070: 0000 0040 0100 0000 0010 0000 0002 0000  ...@............
...
00000140: 0000 0000 0000 0000 2e74 6578 7400 0000  .........text...
```

Slik leser vi det (merk: tall lagres **little-endian**, minst signifikante
byte først, så `6486` betyr `0x8664`):

| Posisjon | Byte | Betydning |
|---|---|---|
| `0x00` | `4d 5a` | «MZ» – alle Windows-programmer starter slik |
| `0x3C` | `40 00 00 00` | PE-headeren ligger på posisjon `0x40` |
| `0x40` | `50 45 00 00` | «PE\0\0» – her starter PE-headeren |
| `0x44` | `64 86` | `0x8664` = x86-64-prosessor |
| `0x46` | `01 00` | 1 seksjon |
| `0x58` | `0b 02` | `0x20B` = PE32+ (64-bits) |
| `0x68` | `00 10 00 00` | Inngangspunkt: `0x1000` byte etter image base |
| `0x70` | `00 00 00 40 01 00 00 00` | Image base: `0x140000000` |
| `0x148` | `2e 74 65 78 74` | «.text» – navnet på kodeseksjonen |

Og selve koden, på posisjon `0x200` i filen:

```bash
xxd -s 0x200 -l 0x30 hello.exe
```

```
00000200: 4883 ec28 b902 0000 00ba 0300 0000 e80d  H..(............
00000210: 0000 0048 83c4 28c3 cccc cccc cccc cccc  ...H..(.........
00000220: 8d04 11c3 0000 0000 0000 0000 0000 0000  ................
```

Dette er de samme bytene som i skriptet. Men å lese et ekte program slik, med
millioner av byte, er umulig for hånd. Det er her Ghidra kommer inn.

---

## 5. Se inni med REA og Ghidra

### Alternativ A: Spør AI-agenten

Med REA koblet til Claude Code kan du bare skrive, for eksempel:

> Åpne `/full/sti/til/eksempel/hello.exe` med REA og Ghidra. Gi meg en
> oversikt, list funksjonene, og forklar hva de gjør.

Agenten velger selv riktige REA-verktøy. Under ser du hvert verktøy den
brukte og hva det svarte (forkortet – de ekte svarene inneholder også
bevisinformasjon som sjekksum og begrensninger).

### Alternativ B: Kommandolinjen

Samme analyse uten AI-agent (husk `GHIDRA_INSTALL_DIR` og `JAVA_HOME` fra
steg 2):

```bash
npx rea-agents@latest analyze   hello.exe --provider ghidra
npx rea-agents@latest decompile hello.exe entry --provider ghidra
```

Hver kommando bruker ca. 20–30 sekunder, mest fordi Ghidra må starte og
analysere filen.

---

### 5.1 `open_binary` – åpne filen

REA sjekker filen og gir den til Ghidra:

```json
{ "format": "pe", "kind": "executable", "architecture": "x86_64",
  "sha256": "771fd388a4f9843cfb0b84a2f29f7d4cd1e14465ec9735d475fe1495c4461d96" }
```

**SHA-256-sjekksummen** er et «fingeravtrykk» av filen. Lager du filen med
skriptet, får du nøyaktig samme sjekksum. Slik kan dere kontrollere at alle
analyserer samme fil.

Ghidra jobber på en midlertidig kopi. **Den opprinnelige filen blir aldri
endret, og programmet blir aldri kjørt.**

### 5.2 `binary_overview` – oversikt

```
image_base:      0x140000000
segmenter:       2   (Headers, .text)
funksjoner:      2
tekststrenger:   0
```

### 5.3 `list_segments` – minneområder

| Navn | Start | Slutt | Lese | Skrive | Kjøre |
|---|---|---|---|---|---|
| Headers | `0x140000000` | `0x140000200` | ja | nei | nei |
| .text | `0x140001000` | `0x140001200` | ja | nei | **ja** |

Legg merke til at koden lå på posisjon `0x200` i **filen**, men havner på
adresse `0x140001000` i **minnet** når Windows laster programmet
(image base `0x140000000` + `0x1000`). Ghidra bruker minneadresser.

### 5.4 `list_procedures` – finn funksjonene

| Adresse | Navn |
|---|---|
| `0x140001000` | `entry` |
| `0x140001020` | `FUN_140001020` |

Ghidra fant begge funksjonene på egen hånd:

- `entry` er inngangspunktet fra PE-headeren.
- Den andre fant Ghidra fordi `entry` kaller den. Den har ikke noe navn i
  filen, så Ghidra kaller den `FUN_` + adressen.

### 5.5 `procedure_assembly` – maskinkoden som assembly

```
0x140001000: SUB RSP, 0x28
0x140001004: MOV ECX, 0x2
0x140001009: MOV EDX, 0x3
0x14000100e: CALL 0x140001020
0x140001013: ADD RSP, 0x28
0x140001017: RET
```

Ghidra har oversatt bytene til instruksjoner (*disassembly*). Sammenlign med
bytene i avsnitt 3: `B9 02 00 00 00` ble `MOV ECX, 0x2`, og `E8 0D 00 00 00`
ble `CALL 0x140001020`. Ghidra har regnet ut selve måladressen for oss.

### 5.6 `procedure_pseudo_code` – tilbake til C

Dette er Ghidras viktigste funksjon, **dekompilatoren**:

```c
void entry(void)
{
  FUN_140001020(2,3);
  return;
}
```

```c
int FUN_140001020(int param_1, int param_2)
{
  return param_1 + param_2;
}
```

Ghidra har sett at `ECX` og `EDX` brukes som argumenter (Windows' kallkonvensjon
for 64-bit), og at `LEA EAX, [RCX+RDX]` betyr «returner summen».

### 5.7 `procedure_callers` – hvem kaller hvem?

Hvem kaller `FUN_140001020`?

```
0x140001000   (entry)
```

I store programmer er dette et nøkkelverktøy: Finner du en interessant
funksjon, kan du nøste deg bakover og se hvor den brukes.

### 5.8 `set_address_name` – gi funksjonen et bedre navn

Når vi har forstått hva en funksjon gjør, gir vi den et navn:

```
set_address_name  adresse=0x140001020  navn=add   →  true
```

Dekompiler `entry` på nytt:

```c
void entry(void)
{
  add(2,3);
  return;
}
```

Navnet slår igjennom overalt. Slik jobber man i praksis: forstå litt, gi navn,
og koden blir gradvis lettere å lese. (Navnene lagres bare i Ghidras
midlertidige database, ikke i EXE-filen.)

### 5.9 `close_binary` – lukk

Ghidra-økten og den midlertidige databasen slettes.

---

## 6. Sammenlign med fasiten

| Opprinnelig (vår C-kode) | Ghidra |
|---|---|
| `int add(int a, int b)` | `int FUN_140001020(int param_1, int param_2)` |
| `return a + b;` | `return param_1 + param_2;` |
| `int main(void)` | `void entry(void)` |
| `return add(2, 3);` | `FUN_140001020(2,3); return;` |

Hva lærer vi?

- **Logikken kommer tilbake**, men **navn forsvinner** ved kompilering. Det
  er analytikerens jobb å gi navnene tilbake.
- **Dekompilert kode er en rekonstruksjon, ikke originalen.** Ghidra tror
  `entry` ikke returnerer noe (`void`). Egentlig ligger svaret 5 igjen i
  `EAX`, men ingen kode bruker det etterpå, så Ghidra gjetter `void`.
  Sjekk alltid assembly når detaljene er viktige.
- Ekte programmer har mye mer: importerte Windows-funksjoner (`kernel32.dll`
  osv.), tekststrenger, ressurser (ikoner, menyer) og tusenvis av funksjoner.
  Verktøyene og arbeidsmåten er de samme.

---

## 8. Feilsøking

| Problem | Løsning |
|---|---|
| `GHIDRA_INSTALL_DIR is not set` | Kjør `export`-linjene fra steg 2 i installasjonen. |
| Agenten ser ingen REA-verktøy | Start Claude Code på nytt etter `setup`. Sjekk med `claude mcp get rea`. |
| `doctor` sier `healthy: false` | Les `remediation`-feltet i utskriften – det sier hva som mangler. |
| Analysen tar lang tid | Normalt: 20–30 sekunder for små filer, mer for store. |
| Feil etter `brew upgrade` | REA forventer Ghidra 12.1.x. Kjør `setup` på nytt, eller lås versjonene med `brew pin ghidra openjdk@21`. |

---

## 9. Ordliste

| Ord | Forklaring |
|---|---|
| **Reverse engineering** | Å finne ut hvordan noe virker ved å ta det fra hverandre. |
| **PE (Portable Executable)** | Filformatet for Windows-programmer (`.exe`, `.dll`). |
| **Maskinkode** | Bytene prosessoren faktisk utfører. |
| **Assembly** | Maskinkode skrevet som lesbare instruksjoner (`MOV`, `CALL`, `RET`). |
| **Disassembler** | Oversetter maskinkode til assembly. |
| **Dekompilator** | Oversetter maskinkode til C-lignende kode. |
| **Statisk analyse** | Å analysere et program uten å kjøre det. |
| **Inngangspunkt (entry point)** | Adressen der programmet begynner å kjøre. |
| **Image base** | Adressen Windows ønsker å laste programmet til i minnet. |
| **Seksjon** | En del av programfilen, f.eks. `.text` (kode) eller `.data` (data). |
| **Little-endian** | Tall lagres med minst signifikante byte først. |
| **SHA-256** | En sjekksum som fungerer som et unikt fingeravtrykk for en fil. |
| **MCP** | Protokoll som lar AI-agenter bruke eksterne verktøy. |
