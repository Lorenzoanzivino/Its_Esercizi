'''1.1 Converti una lista di tuple (prodotto, quantità) in un dizionario che sommi le quantità per ogni prodotto.'''

dati:list[tuple[str, int]] = [
    ('a', 1),
    ('b', 2),
    ('a', 3),
    ('c', 4),
    ('c', 3)
]

def tupla_dizionario(lista_tuple:list[tuple[str, int]]) -> dict[str, int] : 
    dizionario_somma: dict[str, int] = {}

    for elemento in lista_tuple:
        chiave, valore = elemento[0], elemento[1]
        if chiave in dizionario_somma:
            dizionario_somma[chiave] += valore
        else:
            dizionario_somma[chiave] = valore
            print(dizionario_somma)
        
    return dizionario_somma

print(tupla_dizionario(dati))