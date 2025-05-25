'''Segue le norme trovate online del codice IATA + 3 numeri -> 2 lettere maiuscole + 3 numeri, es. AA123'''

import re

class CodiceVolo:
    pattern = re.compile(r'^[A-Z]{2}[0-9]{3}$')  # 2 lettere maiuscole + 3 cifre

    def __init__(self, codice: str):
        codice = codice.strip().upper()
        if not self.is_valid(codice):
            raise ValueError(f"Codice volo non valido: {codice}")
        self.codice = codice

    @classmethod
    def is_valid(cls, codice: str) -> bool:
        return bool(cls.pattern.fullmatch(codice))

    def __str__(self):
        return self.codice

print(CodiceVolo("AA123"))   # valido
print(CodiceVolo("aa123"))   # valido (convertito in maiuscolo)

CodiceVolo("A1234")          # ValueError (solo 1 lettera iniziale)
CodiceVolo("AB12")           # ValueError (solo 2 cifre, serve esattamente 3)