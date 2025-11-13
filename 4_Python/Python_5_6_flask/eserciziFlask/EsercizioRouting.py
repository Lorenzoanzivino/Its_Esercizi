# Esercizi su routing statico e dinamico

from flask import Flask
app = Flask(__name__)

'''Route dinamica per profilo utente:
    Creare un percorso /users/<nome> che restituisca “Benvenuto, <nome>!”.
    Testare con nomi diversi nell’URL.'''
@app.route('/')
def home() -> str:
    return 'Ciao'

@app.route('/users/<string:nome>') 
def utente(nome: str) -> str:
    return f"Benvenuto! {nome}"

'''Route con parametri numerici:
    Definire /square/<int:n> che ritorni una stringa contenente n e il suo quadrato.
    Parametri multipli'''

@app.route('/numbers/<int:n>') 
def mostra_multiplo(n:int) -> str:
    multiplo = n ** 2
    return f"La radice di {n} è : {multiplo}"


'''Creare /sum/<int:a>/<int:b> che restituisca una stringa contenente a, b, e la somma dei due numeri.'''

@app.route('/sums/<int:a>/<int:b>')
def mostra_somma(a:int, b:int) -> str:
    somma = a+b
    return f"La somma di {a} e {b} è : {somma}"

app.run(debug=True)