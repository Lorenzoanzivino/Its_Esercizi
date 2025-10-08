'''🔹 Esercizio di base
    Definire un route /about
        Definire una route /about che ritorni un breve testo HTML con descrizione dell’app o dell’autore.
'''

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/') # avere solo il percorso e basta restituisce un get
def home() -> str:
    return "<h3>La mia Home</h3>"

@app.route('/about')
def show_about() -> str:
    return "<p>Ciao mi chiamo Lorenzo e questa è la mia app</p>"


app.run(debug=True, host='127.0.0.1', port=5000)