'''Esercizio 5 – Funzione lambda con if

Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".'''

from typing import Callable

def pari_dispari(x: int) -> str:
    if x % 2 == 0:
        return 'pari'
    else:
        return 'dispari'

# TEST
print(pari_dispari(4))  # Expected 'pari'
print(pari_dispari(5))  # Expected 'dispari'