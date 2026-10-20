# Time 1: Lag et virtuelt kjæledyr 🐶

Du skal lage et lite kjæledyrspill i terminalen — som en Tamagotchi. Du skal bare bruke det du allerede kan: variabler, funksjoner, valgsetninger, løkker, lister og dictionaries.

Oppgaven har tre deler. **Bygg videre på din egen kode** fra del til del, ikke start på nytt!

---

## Del A: Ett kjæledyr (ca. 15 min)

Kjæledyret har et **navn** og tre verdier som alltid er mellom **0 og 10**. Alle starter på 5.

| Verdi | Betyr |
|---|---|
| `sult` | 10 = skrubbsulten |
| `energi` | 0 = helt utslitt |
| `glede` | 10 = superglad |

Programmet viser status og en meny, helt til brukeren avslutter:

```
Fido: sult 5, energi 5, glede 5
1: Mate  2: Leke  3: Sove  0: Avslutt
Velg:
```

| Handling | Effekt |
|---|---|
| **Mate** | sult −3, glede +1 |
| **Leke** | glede +3, energi −2, sult +1 (men bare hvis energi er minst 2 — ellers er dyret for trøtt) |
| **Sove** | energi +4, sult +1 |
| **Tiden går** (etter hver handling) | sult +1, glede −1 |

Når du viser status, skal programmet også si fra hvis dyret er sultent (sult 8 eller mer) eller trøtt (energi 2 eller mindre).

**Hint:** Lag én funksjon per handling: `mate()`, `leke()`, `sove()`, `tiden_gaar()` og `vis_status()`. Denne hjelpefunksjonen holder en verdi mellom 0 og 10:

```python
def begrens(verdi):
    return max(0, min(10, verdi))


sult = begrens(sult - 3)
```

> 💡 Vil du endre en variabel som er laget utenfor funksjonen, må du skrive `global sult` øverst i funksjonen.

---

## Del B: To kjæledyr (ca. 15 min)

Nytt ønske: Spilleren vil ha **to** kjæledyr, Fido og Pusur!

- Vis status for begge dyrene.
- Når brukeren velger en handling, skal programmet spørre *hvilket* dyr det gjelder.
- Tiden går for **begge** dyrene etter hver handling.

Bygg videre på koden fra del A. Gjør det på den måten som føles mest naturlig for deg.

---

## Del C: Så mange dyr du vil (ca. 20 min)

Nytt ønske: Spilleren skal kunne **adoptere nye dyr** — så mange som spilleren vil.

- Legg til menyvalget `4: Adopter nytt dyr`. Det nye dyret starter med 5 på alle verdiene.
- Alle dyrene skal vises, og tiden går for alle.

<details>
<summary>💡 Hint (ikke åpne før du har tenkt litt selv)</summary>

Med vanlige variabler (`sult1`, `sult2`, `sult3` ...) er dette nesten umulig, fordi vi ikke vet hvor mange dyr det blir. Prøv i stedet en **liste med dictionaries**:

```python
dyrene = [
    {"navn": "Fido", "sult": 5, "energi": 5, "glede": 5},
    {"navn": "Pusur", "sult": 5, "energi": 5, "glede": 5},
]


def mate(dyr):
    dyr["sult"] = begrens(dyr["sult"] - 3)
    ...


mate(dyrene[0])  # Mat Fido
```

</details>

---

## Tenk over før slutten av timen 🤔

Skriv ned korte svar. Vi diskuterer dem i plenum.

1. Hvor mange ganger skrev du `global`? Hva var irriterende med det?
2. Hvor mye kode måtte du kopiere i del B? Hva om det var 10 dyr?
3. Hvor mange parametere måtte `vis_status` ha i del B?
4. I del C: Hva skjer om du skriver `dyr["slut"]` i stedet for `dyr["sult"]`? *Når* oppdager du feilen?
5. Hvor i koden din står det hva et kjæledyr *består av*?

**Løsningsforslag:** [del A](losning/time1_a_ett_dyr.py), [del B](losning/time1_b_to_dyr.py), [del C](losning/time1_c_mange_dyr.py).
