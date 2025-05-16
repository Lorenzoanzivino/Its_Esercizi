'''Esercizio 6 – Uso con reduce()

Usa reduce() (dal modulo functools) e una lambda per calcolare il prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].'''

from typing import Callable
from functools import reduce

lista:list = [2, 3, 4]
risultato = reduce(lambda x, y: x * y, lista)

# TEST = Expected 24
print(risultato)