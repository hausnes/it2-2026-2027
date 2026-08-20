# Dokumentasjon for datasett

## Om løysingsforslaga
- `tips.ipynb` er ei Notebook som løyser ein del oppgåver vha. Pandas og matplotlib.
- `tips.py` er ein Python-fil som løyser (mykje) dei same oppgåvene som `tips.ipynb`, men her blir "standardverktøya" frå Python brukt. Dette blir med andre ord mykje meir manuelle operasjonar enn i `tips.ipynb`. Argumentasjonen for å kunne gjere dette er å forstå kva som ligg bak "magien" i Pandas, og du får vist grunnleggjande Python- og programmeringskunnskapar.

## Offisiell lenke til dokumentasjon

[https://rdrr.io/cran/reshape2/man/tips.html](https://rdrr.io/cran/reshape2/man/tips.html)

## Informasjon om dei ulike kolonnene i datasettet

- tip in dollars,
- bill in dollars,
- sex of the bill payer,
- whether there were smokers in the party,
- day of the week,
- time of day,
- size of the party.

## Eksempel på spørsmål du kan finne ut av:

NB: I tillegg til oppgåvene under, så finn du ein del mindre og større vurderingar av datasettet i `tips.ipynb` og `tips.py`.

1) Vis hvor mange kolonner og rader det er i datasettet?
2) Vis kolonnenavnene til datasettet.
3) Vis de tre første radene
4) Vis bare kolonnene total_bill og tip
5) Vis bare den 100. raden
6) Vis bare kolonne sex og size for rad 10 og 11
7) Vis rader hvor total_bill er mindre en 8 dollar.
8) Vis de tre dyreste regningene.
9) Er det flest menn eller kvinner som har betalt regningene?
10) Hva er det meste som er betalt i tip?
11) Hva er den største andelen tip i forhold til regningen (total_bill)?
12) Regn ut den gjennomsnittlige % tip av regningen (total_bill) for menn og kvinner som har
betalt den. Hvilken av de to gruppene har gjennomsnittlig tipset mest?
13) Hvor mange gjester inngår totalt i datasettet?
14) Hvor mange personer (hvilken size) er mest vanlig (på én regning)?
15) ...