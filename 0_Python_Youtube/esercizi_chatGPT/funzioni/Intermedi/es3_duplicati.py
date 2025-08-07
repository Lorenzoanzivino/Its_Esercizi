'''6. Rimuovi duplicati

Scrivi una funzione che prende una lista e ritorna una nuova lista con tutti i duplicati rimossi, mantenendo l’ordine originale.

# Input: [1, 2, 2, 3, 1]
# Output: [1, 2, 3]'''

def duplicati(lista: list) -> list:
    lista_nuova = []
    for numero in lista:
        if numero not in lista_nuova:
            lista_nuova.append(numero)
    return lista_nuova

# Test
lista_input = [1, 2, 2, 3, 1, 3]
print(duplicati(lista_input))  # Output: [1, 2, 3]