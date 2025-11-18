'''🔹 Esercizi su url_for()
    Generazione link interni
        Usare url_for per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).
    Navigazione dinamica
        Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.
    Mini blog
        Definire route /post/<int:id> che restituisca un articolo fittizio.
        Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.
'''

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def homepage():
    return f"""
    <h3>URL About: {url_for('show_about')}</h3>
    <h3>URL Profilo Lorenzo: {url_for('show_nome', nome='Lorenzo_Anzivino')}</h3>
    <h3>URL Quadrato: {url_for('show_quadrato', n=5)}</h3>
    <h3>URL Somma: {url_for('show_somma', a=5, b=6)}</h3>
    """

@app.route('/about')
def show_about() -> str:
    return "<p>Ciao mi chiamo Lorenzo e questa è la mia app</p>"

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


with app.test_request_context():
    print(url_for('homepage'))
    print(url_for('show_about'))
    print(url_for('show_nome', nome='Lorenzo_Anzivino'))
    print(url_for('show_quadrato', n=3))
    print(url_for('show_somma', a=5, b=6))
    
    
app.run(debug=True, host='127.0.0.1', port=5000)