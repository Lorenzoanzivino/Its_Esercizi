'''Segue le norme trovate online del codice IATA, codice di 3 o di 4 cifre numeriche'''

from typing import Self

class CodiceAeroporto(str) :
    def __new__(cls, value: str|Self) -> Self:
        val = str(value).strip().upper()

        if len(val) != 3 or not val.isalpha() or not val.isupper():
            raise ValueError(f"codice IATA non valido: '{value}' Deve essere una stringa di 3 lettere maiuscole.")
        return super().__new__(cls, val)

aeroporto = CodiceAeroporto("fco")
print(aeroporto)  # → FCO

print(CodiceAeroporto("fco"))   # → FCO
print(CodiceAeroporto("JFK"))   # → JFK

CodiceAeroporto("A@C") # → ValueError