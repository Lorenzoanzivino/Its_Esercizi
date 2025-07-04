'''Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.'''

# difficoltà computazionale = O (log2 n) = 32

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


# Test della funzione ricerca_binaria

lista = [1, 3, 5, 7, 9, 11, 13]
valore_da_cercare = 7
valore_non_presente = 4

print(ricerca_binaria(lista, valore_da_cercare))  # Output atteso: True
print(ricerca_binaria(lista, valore_non_presente))  # Output atteso: False


def bin_search(lista, numero) -> None:

    mid:int = len(lista) // 2

    if lista[mid] == numero:
        print("Il numero è stato trovato")
        # return None
    
    elif len(lista) == 1:
        print("Il numero non c'è!")
    
    elif lista[mid] > numero: #il numero che sto cercando è a sinistra
        bin_search(lista[:mid], numero)

    elif lista[mid] < numero: #il numero che sto cercando è a destra
        bin_search(lista[mid + 1:], numero)

    
