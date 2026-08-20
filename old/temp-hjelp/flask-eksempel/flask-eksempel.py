# Konfigurer Flash-meldinger: Bruk flash-funksjonen til å legge til meldinger, og get_flashed_messages til å hente og vise dem i HTML-sidene dine.

from flask import Flask, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Nødvendig for å bruke flash-meldinger

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash')
def flash_message():
    flash('Dette er en flash-melding!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# Opprett en HTML-mal: Lag en HTML-mal (for eksempel templates/index.html) som viser flash-meldingene.
# Se filen flask-index.html for et eksempel på hvordan du kan vise flash-meldinger i en HTML-side.