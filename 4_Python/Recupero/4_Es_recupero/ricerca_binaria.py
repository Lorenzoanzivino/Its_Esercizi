'''Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.'''


def ricerca_binaria(lista: list[int], valore: int) -> bool:
    sinistra = 0
    destra = len(lista) - 1

    while sinistra <= destra:
        medio = (sinistra + destra) // 2
        if lista[medio] == valore:
            return True
        elif lista[medio] < valore:
            sinistra = medio + 1
        else:
            destra = medio - 1

    return False
