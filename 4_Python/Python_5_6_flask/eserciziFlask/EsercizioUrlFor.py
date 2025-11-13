# Esercizi su url_for()
from flask import Flask, url_for
app = Flask(__name__)


'''Generazione link interni
Usare url_for() per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /users/..., ecc.).'''

@app.route('/')
def homepage():
    return f"""
    <a href= "URL About: {url_for('show_about')}" </a>
    <h3>URL Profilo Lorenzo: {url_for('mostra_nome', nome='Lorenzo_Anzivino')}</h3>
    <h3>URL Quadrato: {url_for('mostra_quadrato', n=5)}</h3>
    <h3>URL Somma: {url_for('mostra_somma', a=5, b=6)}</h3>
    """

@app.route('/')
def show_about() -> str:
    return f"<p>Ciao mi chiamo {mostra_nome()} e questa è la mia app</p>"

@app.route('/users/<string:nome>')
def mostra_nome(nome:str) -> str:
    return f"Benvenuto, {nome}"

@app.route('/squares/<int:n>')
def mostra_quadrato(n:int) -> str:
    quadrato = n**2
    return f"La radice di {n} è : {quadrato}"

@app.route('/sums/<int:a>/<int:b>')
def mostra_somma(a:int, b:int) -> str:
    somma = a+b
    return f"La somma di {a} e {b} è : {somma}"


with app.test_request_context():
    print(url_for('homepage'))
    print(url_for('show_about'))
    print(url_for('mostra_nome', nome='Lorenzo_Anzivino'))
    print(url_for('mostra_quadrato', n=3))
    print(url_for('mostra_somma', a=5, b=6))
    
app.run(debug=True)

'''Navigazione dinamica
Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for().'''

'''Mini blog
Definire route /posts/<int:id> che restituisca un articolo fittizio.
Creare una pagina /posts con un elenco di post e i relativi link agli articoli generati tramite url_for().
'''