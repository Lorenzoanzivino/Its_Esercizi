''' Esercizio di base
    Definire un route /about
        Definire una route /about che ritorni un breve testo HTML con descrizione dell’app o dell’autore.
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello, world!</h3>"