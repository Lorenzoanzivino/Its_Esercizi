'''1.2 Dato un elenco di tuple (nome_studente, punteggio), crea un dizionario che somma i punteggi per ogni studente.
'''

dati:list[tuple[str, int]] = [
    ("Lorenzo", 25),
    ("Francesco", 28),
    ("Stefano", 30),
    ("Lorenzo", 18),
    ("Francesco", 22),
    ("Stefano", 25),
]

def somma_punteggi(lista_tuple:list[tuple[str, int]]) -> dict[str, int]:
    dizionario:dict[str, int] = {}
    media = 0
    for elementi in lista_tuple:
        key, value = elementi[0], elementi[1]
        if key in dizionario:
            dizionario[key] += value
        else:
            dizionario[key] = value

    return dizionario, media

print(somma_punteggi(dati))