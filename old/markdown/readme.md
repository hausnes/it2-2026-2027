# Opplæring i Markdown

Markdown er eit enkelt språk for å skrive tekst med formatering. Det er lett å lære, og gjer god kontroll over korleis teksten blir presentert.

Denne guiden gjer ein kort innføring i dei mest brukte funksjonane i Markdown.

Du kan lese meir i dokumentasjonen til Markdown: [Markdown Guide](https://www.markdownguide.org/). Det står og noko hjå GitHub: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

## Overskrifter

Overskrifter blir skrive med `#`. Jo fleire `#`, jo mindre overskrift.

## Paragrafar

Paragrafar blir skrive utan nokre spesielle teikn. Det er linjeskift som avgjer kvar ein ny paragraf startar.

## Lister

### Punktliste

- Eit punkt
- Eit anna punkt
- Eit tredje punkt

### Nummerert liste

1. Eit punkt
2. Eit anna punkt
3. Eit tredje punkt

## Tekstformatering

### Kursiv

Kursiv tekst blir skrive med `*` eller `_`. Dette er *kursiv tekst*.

### Fet

Fet tekst blir skrive med `**` eller `__`. Dette er **fet tekst**.

### Kode

Kode blir skrive med backticks (\`). Dette er ei kodeblokk: `print("Hello, world!")`.

### Sitat

Sitat blir skrive med `>`. Dette er eit sitat.

## Lenker

Lenker blir skrive med `[tekst](url)`. Dette er ei [lenke til Google](https://www.google.com).

## Emojis

Emojis går an å bruke i markdown. 🎅 og ✅ og ❌ og ...

## Bileter

Bileter blir skrive med `![alternativ tekst](url)`.

![Bilete av ein solnedgang](https://images.unsplash.com/photo-1735506266367-d6941df3efdc?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## Tabellar

Tabellar blir skrive med `|`. Dette er ein tabell:

| Fornavn | Etternamn | Alder |
|---------|-----------|-------|
| Ola     | Nordmann  | 32    |
| Kari    | Nordkvinne| 28    |


## Kodeblokker

Kodeblokker blir skrive med tre backticks (\`\`\`). Dette er ei kodeblokk:

```python
def hello():
    print("Hello, world!")
```