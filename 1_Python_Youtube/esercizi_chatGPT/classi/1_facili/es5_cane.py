'''🐶 Esercizio 5 : Cane

Crea una classe Cane che abbia:
    attributi: nome, razza
    metodo abbaia() che stampa "Bau! Sono <nome>!"

Esempio:

c = Cane("Fido", "Labrador")
c.abbaia()  # Output: Bau! Sono Fido!'''


class Cane:
    _nome:str
    _razza:str

    def __init__(self, nome:str, razza:str) -> None:
        self._nome = nome
        self._razza = razza
    
    def get_nome(self) -> str:
        return self._nome
    
    def get_razza(self) -> str:
        return self._razza
    
    def abbaia(self) -> str:
        return f"Bau! Sono: {self.get_nome()}"
    
if __name__ == "__main__":
    cane = Cane("Astrid", "Pit-Bull")
    print(cane.abbaia())