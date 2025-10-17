'''Livello 1 — Creazione e Accesso Base
Crea un dizionario persona con le chiavi "nome", "cognome", "eta".
Poi:
stampa il nome;
aggiorna l’età;
aggiungi una nuova chiave "città".
📘 Obiettivo: prendere confidenza con sintassi base e accesso a valori.'''

persona:dict[str, int] = {"nome" : "Lorenzo", "cognome" : "Anzivino", "eta" : 28}
print(persona["nome"])
persona["eta"] = 30
persona["citta"] = "Pomezia"
print(persona)