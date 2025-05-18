'''8. Trova parole con lettere maiuscole e numeri

Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e/o numeri.

Esempio:

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678', 'XYZZYZZZ']'''

import re

def find_codes(text:str) -> list[str]:

    pattern:str = r'[A-Z0-9]{8}'

    code:str = re.findall(pattern, text)
    print(code)

find_codes("I codici sono AB12CD34 e 12345678 e XYZZYZZZ")