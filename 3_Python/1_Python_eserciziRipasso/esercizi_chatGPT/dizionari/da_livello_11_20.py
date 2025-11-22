print("livello 11")
'''Livello 11 — Aggiornamento Condizionale
Hai un dizionario con prodotti e stock:
magazzino = {"pane": 10, "latte": 0, "uova": 12}
Se la quantità è 0, cambia il valore in "esaurito".
Altrimenti, aggiungi +5 alla quantità.
📘 Obiettivo: usare for, condizioni e aggiornamento valori.'''

magazzino:dict = {"pane": 10, "latte": 0, "uova": 12}
for key, value in magazzino.items():
    if value == 0:
        magazzino[key] = "esaurito"
    else:
        magazzino[key] += 5
print(magazzino)


print("\nLivello 12")
'''Livello 12 — Ricerca per Valore
Dato un dizionario di studenti e media:
voti = {"Luca": 18, "Anna": 30, "Marco": 22, "Sara": 25}
Scrivi una funzione che, dato un voto x, restituisce tutti gli studenti che hanno quel voto.
📘 Obiettivo: filtri su valori con liste di risultati.'''

def stessoVoto(x:int):
    voti:dict = {"Luca": 18, "Anna": 30, "Marco": 22, "Sara": 25}
    lista:list = []
    for key, value in voti.items():
        if value == x:
            lista.append(key)
    return lista 

print(stessoVoto(22))

print("\nLivello 13")
'''Livello 13 — Conteggio Frequenze
Hai una lista di parole:
parole = ["gatto", "cane", "gatto", "cane", "uccello"]
Crea un dizionario che conti quante volte appare ogni parola.
📘 Obiettivo: usare dict.get() o collections.defaultdict.'''

parole = ["gatto", "cane", "gatto", "cane", "uccello"]
dizionario:dict = {}

for parola in parole:
    if parola not in dizionario:
        dizionario[parola] = 1
    else:
        dizionario[parola] += 1
print(dizionario)




print("\nLivello 14")
'''Livello 14 — Dizionario di Dizionari
Crea un dizionario classi dove:
le chiavi sono i nomi delle classi: "1A", "2B", "3C"
i valori sono dizionari con "numero_studenti" e "insegnante"
Poi stampa:
il numero totale di studenti
la classe con più studenti
📘 Obiettivo: combinare dizionari annidati e aggregazioni.'''

classi:dict = {
    "1A" : {
        "studenti" : 30,
        "insegnanti" : 4
    },
    "2B" : {
        "studenti" : 22,
        "insegnanti" : 3
    },
    "3C" : {
        "studenti" : 17,
        "insegnanti" : 6
    }
}
somma = 0
classe_top = 0
classe_max = ""

for key, value in classi.items():
    somma += value["studenti"]
    if value["studenti"] > classe_top:
        classe_top = value["studenti"]
        classe_max = key  # <-- qui salvi il nome della classe

print(f"Il numero totale di studenti è: {somma}")
print(f"La classe con più studenti è: {classe_max} con: {classe_top} studenti")



print("\nLivello 15")
'''Livello 15 — Unione di Dizionari
Hai due dizionari:
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
Crea un nuovo dizionario che unisce i due:
se una chiave esiste in entrambi, somma i valori.
📘 Obiettivo: logica combinatoria con dizionari.'''

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3:dict = {}

for key, value in d1.items():
    d3[key] = value
for key,value in d2.items():
    if key in d3:
        d3[key] += value
    else:
        d3[key] = value
print(d3)


print("\nLivello 16")
'''Livello 16 — Ordinamento Dizionari
Dato:
voti = {"Luca": 18, "Anna": 30, "Marco": 22, "Sara": 25}
Stampa la lista degli studenti ordinati per media decrescente.
Poi crea un nuovo dizionario ordinato.
📘 Obiettivo: usare sorted() e lambda con dizionari.'''


print("\nLivello 17")
'''Livello 17 — Flatten Dizionario Annidato
Hai:
rubrica = {
    "Lorenzo": {"telefono": "123", "email": "l@x.com"},
    "Anna": {"telefono": "456", "email": "a@x.com"}
}
Crea un nuovo dizionario piatto con chiavi "Lorenzo_telefono", "Lorenzo_email" ecc.
📘 Obiettivo: manipolare dizionari annidati e concatenare chiavi.'''


print("\nLivello 18")
'''Livello 18 — Dizionario da Liste di Liste
Hai una lista di coppie:
coppie = [["Luca", 80], ["Anna", 90], ["Marco", 75]]
Trasformala in un dizionario.
📘 Obiettivo: comprendere la conversione lista → dizionario e comprehension.'''


print("\nLivello 19")
'''Livello 19 — Filtri Complessi
Dato:
studenti = {"Luca": 18, "Anna": 30, "Marco": 22, "Sara": 25}
crea un nuovo dizionario con solo gli studenti che hanno voti pari e maggiori di 20.
📘 Obiettivo: comprehension + condizioni multiple sui valori.'''


print("\nLivello 20")
'''Livello 20 — Funzioni con Dizionari Annidati
Crea un dizionario classe con studenti e materie (come nel tuo livello 10), ma ogni studente ha voti per materia:
classe = {
    "studenti": [
        {"nome": "Luca", "voti": {"matematica": 7, "storia": 8}},
        {"nome": "Anna", "voti": {"matematica": 9, "storia": 10}}
    ]
}
Scrivi una funzione che calcola la media totale di ogni studente e stampa chi ha la media più alta.
📘 Obiettivo: combinare liste, dizionari annidati e calcoli aggregati.'''