'''🔹 Esercizi su routing statico e dinamico
    Route dinamica per profilo utente
        Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.
        Testare con nomi diversi nell’URL.
    Route con parametri numerici
        Definire /square/<int:n> che ritorni il quadrato di n.
    Parametri multipli
        Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.
'''

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/') # avere solo il percorso e basta restituisce un get
def home() -> str:
    return "<h3>La mia Home</h3>"

@app.route('/user/<string:nome>')
def show_nome(nome:str) -> str:
    return f"Benvenuto, {nome}"

@app.route('/square/<int:n>')
def show_quadrato(n:int) -> int:
    quadrato = n**2
    return f"La radice di {n} è : {quadrato}"

@app.route('/sum/<int:a>/<int:b>')
def show_somma(a:int, b:int) -> int:
    somma = a+b
    return f"La somma di {a} e {b} è : {somma}"
    
    
app.run(debug=True, host='127.0.0.1', port=5000)