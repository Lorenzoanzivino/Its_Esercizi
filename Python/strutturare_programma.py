# Lezione Flavio Giorgi
#'''step per scrivere bene un codice'''
#
#def prime(n: int) -> bool :
#    
#    if (str(n)[-1] == "0" or str(n)[-1] == 5) and n != 5:
#        return False
#    
#    for i in range(2, (n//2) + 1):
#
#        if n % i == 0:
#
#            print(f"Il divisore trovato è : {i}")
#            return False
#    
#    return True

''' scrivere una funzione che prende una lista di elementi non ordinati e restituisca una lista ordinata '''

def bubblesort(lista: list[int]) -> list[int]:
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                # Scambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista:list = [5, 2, 2, 5, 5, 6, 235, 634]

print(bubblesort(lista=lista))