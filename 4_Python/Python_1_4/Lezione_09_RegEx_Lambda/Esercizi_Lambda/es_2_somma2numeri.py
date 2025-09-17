'''Esercizio 2 – Somma di due numeri

Crea una funzione lambda che accetti due numeri e restituisca la loro somma.'''

from typing import Callable

somma : Callable[[int], int] = lambda x, y: x + y

# TEST x = 4, y = 5 Expected 9
print(somma(2, 3))

# TEST x = 6, y = 20  Expected 26
print(somma(6, 20))