# Undervisningsopplegg: Lage eit program som kontakter ChatGPT

## Mål
Elevane skal lære å lage eit program som kan kontakte ChatGPT og stille eigne spørsmål via terminalen.

## Forutsetningar
- Grunnleggjande kunnskap om programmering
- Installert Python på datamaskina
- API-nøkkel frå OpenAI:

## Steg-for-steg guide

### 1. Installere nødvendige bibliotek
Elevane må installere `openai` biblioteket. Dette kan gjerast ved å køyre følgjande kommando i terminalen:
```sh
pip install openai
```

### 2. Opprette ein Python-fil
Elevane skal opprette ein ny Python-fil, for eksempel `chatgpt_terminal.py`.

### 3. Skrive programmet
Her er eit eksempelprogram som elevane kan bruke som utgangspunkt:

```python
import openai

# Set din OpenAI API-nøkkel her
openai.api_key = 'DIN_API_NØKKEL'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Velkommen til ChatGPT-terminalen!")
    while True:
        user_input = input("Stille eit spørsmål (eller skriv 'exit' for å avslutte): ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT svarer: ", response)

if __name__ == "__main__":
    main()
```

### 4. Køyre programmet
Elevane kan køyre programmet ved å bruke følgjande kommando i terminalen:
```sh
python chatgpt_terminal.py
```

### 5. Utforske og stille spørsmål
Elevane kan no stille spørsmål til ChatGPT direkte frå terminalen og få svar.

## Oppsummering
Dette undervisningsopplegget gir elevane praktisk erfaring med å bruke API-er og lage interaktive program. Det gir også innsikt i korleis dei kan integrere kunstig intelligens i eigne prosjekt.