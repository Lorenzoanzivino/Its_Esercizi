'''6. Verifica un codice prodotto

Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

Esempio:

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False
'''

import re

def check_product_code(code:str) -> bool:

    pattern:str = r'^PROD-\d{4}-[A-Z]{2}$'

    if re.fullmatch(pattern, code):
        return True
    else:
        return False
    
print(check_product_code("PROD-9876-ZX"))
print(check_product_code("PROD-99-ZX")  )