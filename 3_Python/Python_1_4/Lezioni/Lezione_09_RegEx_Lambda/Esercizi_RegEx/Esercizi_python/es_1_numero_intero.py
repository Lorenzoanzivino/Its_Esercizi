'''1. Verifica se una stringa è un numero intero

Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.

Esempio:

is_integer("123")      # True
is_integer("-456")     # True
is_integer("12.3")     # False'''

import re

def is_integer(s:int) -> bool:

    return True if re.fullmatch(r'-?\d+', s) else False
              
print(f'For 123 - Expected #True --> {is_integer("123")}')
print(f'For -456 - Expected #True --> {is_integer("-456")}')
print(f'For 12.3 - Expected #False --> {is_integer("12.3")}')