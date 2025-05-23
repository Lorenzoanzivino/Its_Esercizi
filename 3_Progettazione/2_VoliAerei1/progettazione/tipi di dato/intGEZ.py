from typing import Self

class IntGEZ(int):
    #Tipo dato specializzato intero >= 0
    def __new__(cls, v: float|int|str|bool|Self) -> Self:
        n : int = super().__new__(cls, v) #prova a convertire v in un int

        if n>= 0:
            return n
        raise ValueError(f"Il valore {n} è negativo!")