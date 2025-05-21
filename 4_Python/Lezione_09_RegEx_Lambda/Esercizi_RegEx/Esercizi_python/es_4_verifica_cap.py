'''4. Verifica un CAP

Scrivi una funzione is_valid_cap(cap) che restituisce True se il CAP è valido (5 cifre), False altrimenti.

Esempio:

is_valid_cap("70124")   # True
is_valid_cap("A0123")   # False'''

import re

def is_valid_cap(cap:str) -> bool:

    pattern:str[int] = r'^\d{5}$'
    if re.fullmatch(pattern, cap) :
        return True
    else:
        return False
    
print(f'For 70124 - Expected #True --> {is_valid_cap("70124")}')
print(f'For A0123 - Expected #False --> {is_valid_cap("A0123")}')

print(f'For 00071 --> {is_valid_cap("00071")}')
print(f'For 988 --> {is_valid_cap("988")}')