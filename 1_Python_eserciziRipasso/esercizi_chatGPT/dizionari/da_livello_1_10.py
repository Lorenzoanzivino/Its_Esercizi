print("Livello 1")
'''Livello 1 — Creazione e Accesso Base
Crea un dizionario persona con le chiavi "nome", "cognome", "eta".
Poi:
stampa il nome;
aggiorna l’età;
aggiungi una nuova chiave "città".
📘 Obiettivo: prendere confidenza con sintassi base e accesso a valori.'''

persona:dict = {"nome" : "Lorenzo", "cognome" : "Anzivino", "eta" : 28}
print(persona["nome"])
persona["eta"] = 30
persona["citta"] = "Pomezia"
print(persona)

print("\nLivello 2")
'''Livello 2 — Verifica Chiavi
Dato il dizionario:
auto = {"marca": "Fiat", "modello": "Panda", "anno": 2012}
Scrivi un programma che:
controlla se "colore" è presente come chiave;
se non lo è, la aggiunge con valore "bianco".
📘 Obiettivo: usare in, not in e aggiunta condizionale.'''

auto:dict = {"marca" : "Fiat", "modello" : "Panda", "anno" : 2012}
if "colore" not in auto.keys():
    auto["colore"] = "bianco"
    print("Aggiunto il colore bianco")
else:
    print("il colore è gia presente")
print(auto)


print("\nLivello 3")
'''Livello 3 — Ciclo su Chiavi e Valori
Dato:
studenti = {"Anna": 28, "Luca": 22, "Marco": 25, "Giulia": 30}
Stampa tutte le coppie chiave/valore nel formato:
Anna → 28 anni
Luca → 22 anni
📘 Obiettivo: iterare con for chiave, valore in dizionario.items().'''

studenti:dict = {"Anna": 28, "Luca": 22, "Marco": 25, "Giulia": 30}
for nome, eta in studenti.items():
    print(f"{nome} → {eta} anni")


print("\nLivello 4")
'''Livello 4 — Conversione in Liste
Partendo da:
prezzi = {"mela": 0.99, "banana": 0.79, "pera": 1.20}
Crea due liste: una con i nomi della frutta e una con i prezzi.
Poi stampa il prezzo medio.
📘 Obiettivo: usare list(d.keys()) e list(d.values()).'''

prezzi:dict = {"mela": 0.99, "banana": 0.79, "pera": 1.20}
lista_chiavi:list = []
lista_valori:list = []
for chiavi, valori in prezzi.items():
    if chiavi not in lista_chiavi or valori not in lista_valori:
        lista_chiavi.append(chiavi)
        lista_valori.append(valori)
    else:
        print(f"Gli elementi {chiavi} o {valori} sono gia presenti")

print(lista_chiavi)
print(lista_valori)

# Oppure conversione diretta in liste
lista_chiavi: list = list(prezzi.keys())
lista_valori: list = list(prezzi.values())
print("Chiavi:", lista_chiavi)
print("Valori:", lista_valori)


print("\nLivello 5")
'''Livello 5 — Dizionari Annidati
Crea un dizionario rubrica con almeno 3 persone, dove ogni persona ha come valore un altro dizionario con:
"telefono", "email", "città"
Stampa il numero di telefono di una persona specifica.
📘 Obiettivo: capire bene l’accesso multiplo tipo rubrica["Anna"]["telefono"].'''

rubrica:dict = {
    "Lorenzo" : {"telefono" : "3774738083",
                 "email" : "lorenzo@gmail.ciao",
                 "citta" : "Pomezia"},
    "Simona" : {"telefono" : "3206311900",
                 "email" : "simona@gmail.ciao",
                 "citta" : "Pomezia"},
    "Stefano" : {"telefono" : "3404055123",
                 "email" : "stefano@gmail.ciao",
                 "citta" : "Pomezia"}
}
# Stampo un numero di telefono specifico
print({rubrica["Simona"]["telefono"]})
# Aggiungo un nuovo campo solo ad una persona
rubrica["Lorenzo"]["sesso"] = "maschio"
print(rubrica["Lorenzo"])
# Aggiungo nuovo campo a tutti con For
for key, value in rubrica.items():
    value["auto"] = True
print(rubrica)


print("\nLivello 6")
'''Livello 6 — Somme e Filtri
Hai il dizionario:
voti = {"Luca": 18, "Giulia": 27, "Marco": 22, "Anna": 30, "Sara": 25}
Calcola la media dei voti solo degli studenti che hanno preso più di 24.
📘 Obiettivo: combinare for, condizioni e operazioni numeriche sui valori.'''

voti:dict = {"Luca": 18, "Giulia": 27, "Marco": 22, "Anna": 30, "Sara": 25}
somma = 0
count = 0
for voto in voti.values():
    if voto > 24:
        somma += voto
        count += 1
        media = somma // count
if count > 0:
    media = somma / count
    print(f"La media dei voti sopra 24 è: {media:.2f}")
else:
    print("Nessuno ha preso più di 24.")


print("\nLivello 7")
'''Livello 7 — Invertire Chiavi e Valori
Dato:
ita_eng = {"gatto": "cat", "cane": "dog", "casa": "house"}
Crea un nuovo dizionario eng_ita invertendo chiavi e valori:
{"cat": "gatto", "dog": "cane", "house": "casa"}
📘 Obiettivo: comprendere come costruire nuovi dizionari da esistenti con comprensioni o cicli.'''

ita_eng:dict = {"gatto": "cat", "cane": "dog", "casa": "house"}

eng_ita:dict = {}

for key, value in ita_eng.items():
    eng_ita[value] = key
print(eng_ita)


print("\nLivello 8")
'''Livello 8 — Dizionario da Liste
Hai due liste:
nomi = ["Luca", "Anna", "Marco"]
punteggi = [80, 90, 75]
Crea un dizionario che mappa ogni nome al suo punteggio.
📘 Suggerimento: usa zip() o una dictionary comprehension.'''

nomi:list[str] = ["Luca", "Anna", "Marco"]
punteggi:list[int] = [80, 90, 75]
nomi_punteggi:dict = {}

for i in range(len(nomi)):    # genera gli indici da 0 a len(nomi)-1.
    nome = nomi[i]    # prende il nome corrispondente.
    punto = punteggi[i]    # prende il punteggio corrispondente.

    nomi_punteggi[nome] = punto
print(nomi_punteggi)


print("\nLivello 9")
'''Livello 9 — Rimuovere e Aggiornare
Dato:
magazzino = {"pane": 10, "latte": 5, "uova": 12, "burro": 0}
Rimuovi le voci con quantità 0.
Aggiorna tutte le altre quantità aggiungendo +2.
📘 Suggerimento: crea un nuovo dizionario con comprensione.'''

magazzino:dict = {"pane": 10, "latte": 5, "uova": 12, "burro": 0}
magazzino_2:dict = {}
for key, value in magazzino.items():
    if value > 0:
        magazzino_2[key] = value
        magazzino_2[key] += 2
print(magazzino_2)


print("\nLivello 10")
'''Livello 10 — Dati Complessi e Ricerca
Crea una struttura dati che rappresenti una classe scolastica:
classe = {
    "studenti": [
        {"nome": "Luca", "eta": 17, "media": 7.8},
        {"nome": "Anna", "eta": 18, "media": 9.1},
        {"nome": "Marco", "eta": 17, "media": 6.4}
    ],
    "materie": ["matematica", "storia", "inglese"]
}
Scrivi una funzione che:
trova lo studente con la media più alta;
stampa il suo nome e la media.
📘 Obiettivo: combinare dizionari annidati, liste e funzioni — livello “pro”.'''


classe:dict[str, dict] = {
    "studenti": [
        {"nome": "Luca", "eta": 17, "media": 7.8},
        {"nome": "Anna", "eta": 18, "media": 9.1},
        {"nome": "Marco", "eta": 17, "media": 6.4}
    ],
    "materie": ["matematica", "storia", "inglese"]
}

def mediaPiuAlta(classe:dict):
    studente_top = None
    media_max = 0

    for studente in classe["studenti"]:
        if studente["media"] > media_max:
            media_max = studente["media"]
            studente_top = studente
    
    print(f"Lo studente con la media più alta è: {studente_top['nome']} con una media di: {studente_top['media']}")

# chiamata alla funzione
mediaPiuAlta(classe)