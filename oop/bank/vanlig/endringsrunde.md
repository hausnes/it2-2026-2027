# Endringsrunde: Banken har nye ønsker

Gratulerer, prototypen din fungerer! 🎉 Banken er fornøyd, men har allerede to nye ønsker. Slik er det nesten alltid i ekte programvareutvikling: kravene endrer seg etter at koden er skrevet.

Bygg ønskene inn i **din egen kode** fra del 1. Ikke start på nytt!

> 📝 **Før du begynner:** Ta en kopi av fila di (f.eks. `bank_v1.py`), slik at du kan sammenligne før og etter.

---

## Ønske 1: Transaksjonshistorikk

1. Hver konto skal ha en **historikk**: en liste over alle innskudd og uttak, f.eks. `"Innskudd: 500 kr"` og `"Uttak: 200 kr"`.
2. Legg til et menyvalg der brukeren kan se historikken til en konto.

## Ønske 2: Sparekonto

Banken skal nå ha to typer kontoer:

| | Brukskonto | Sparekonto |
|---|---|---|
| Uttak | Så mange du vil | **Maks 3 uttak** |
| Renter | Nei | **2 %** når banken legger til renter |

1. Hver kunde skal ha en **kontotype**: `"brukskonto"` eller `"sparekonto"`. Gi Kari en sparekonto, og de andre brukskonto.
2. En sparekonto kan bare ha **3 uttak**. Prøver man et fjerde, skal programmet si nei.
3. Legg til et menyvalg **«Legg til renter»**. Da får alle sparekontoer 2 % rente (rund av til hele kroner), og telleren for uttak nullstilles.
4. Når man oppretter en ny kunde, skal programmet spørre om kontotype.
5. Når man viser saldoen til en sparekonto, skal det også stå hvor mange uttak som er igjen.

> 💡 Bruker du JSON-fil, må du også oppdatere `kunder.json`. Hva skjer med kunder som ble lagret *før* du la til de nye feltene?

---

## Etterpå: Tell endringene

Sammenlign koden din før og etter, og fyll ut tabellen. Ta den med til neste time.

| Spørsmål | Ditt svar |
|---|---|
| Hvilke funksjoner måtte du endre for ønske 1? | |
| Hvilke funksjoner måtte du endre for ønske 2? | |
| Hvor mange steder i koden sjekker du om en konto er en sparekonto? | |
| Hvor i koden står det hvilke nøkler en sparekonto har (og en brukskonto)? | |
| Fikk du noen `KeyError` underveis? Hva var årsaken? | |
| Hvis banken kommer med en tredje kontotype (f.eks. *BSU*), hvor mye må endres da? | |
