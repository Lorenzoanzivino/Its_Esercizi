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

import time

def bubblesort(lista: list[int]) -> list[int]:

    ordered: bool = True    
    
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
#            if lista[j] > lista[j + 1]:
#                # Scambio
#                lista[j], lista[j + 1] = lista[j + 1], lista[j]
#    return lista

            if lista[i] >= lista[j]:
                ordered = False

        if ordered:
        
            return lista

lista:list = [5, 2, 2, 5, 5, 6, 235, 634]


import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0

    def __enter__(self):
        self.start_time = time.time()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.8f} seconds")

        if exc_type is not None:
            print(f"Exception type : {exc_type}")
            print(f"An error occured : {exc_value}")
            print(f"Traceback : {traceback}")

        return True
    
with Stopwatch():
    print(bubblesort(lista=lista))