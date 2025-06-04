'''1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.'''

'''def lista_tuple(lista: list[tuple]) -> dict:
    dizionario = {}

    for chiave, valore in lista:
        if chiave in dizionario:
            dizionario[chiave] += valore  # Somma il valore se la chiave esiste già
        else:
            dizionario[chiave] = valore  # Altrimenti, crea una nuova chiave

    return dizionario

# Esempio di utilizzo
tupla = [
    ('a', 1),
    ('b', 2),
    ('a', 3),
    ('c', 4),
    ('c', 3)
]

print(lista_tuple(tupla))'''

def lista_tuple(lista: list[tuple]) -> dict:
    dizionario_1:dict = {}

    for tupla in lista:
        key, value = tupla[0], tupla[1]
        if key in dizionario_1:
            dizionario_1[key] += value # Somma il valore se la chiave esiste già
        else:
            dizionario_1[key] = value # Altrimenti, crea una nuova chiave

    return dizionario_1

tupla = [
    ('a', 1),
    ('b', 2),
    ('a', 3),
    ('c', 4),
    ('c', 3)
]
print(lista_tuple(tupla))