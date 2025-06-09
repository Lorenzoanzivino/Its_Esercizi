'''Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.'''


def binary_search(lista, numero):
    inizio = 0
    fine = len(lista) - 1

    while inizio <= fine:
        centro = (inizio + fine) // 2
        if lista[centro] == numero:
            return True
        elif lista[centro] < numero:
            inizio = centro + 1
        else:
            fine = centro - 1
    return False
