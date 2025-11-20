'''es 1.Radice Quadrata Sicura...

Scrivi una funzione safe_sqrt(number) che calcoli la radice quadrata di un numero usando math.sqrt(). Gestisci l'eccezione ValueError se l'input è negativo restituendo un messaggio informativo.'''

import math

def safe_sqrt(number: float) -> int:
    try:
        return math.sqrt(number)
    except ValueError as error:
        print(error)
    
# Esempi di utilizzo
print(safe_sqrt(9)) 
print(safe_sqrt(-9))  