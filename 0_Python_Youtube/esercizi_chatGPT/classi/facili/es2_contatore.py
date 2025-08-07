'''🔢 Esercizio 2 : Contatore

Crea una classe Contatore che:
    abbia un attributo valore inizializzato a 0
    abbia un metodo incrementa() che aumenta valore di 1
    abbia un metodo stampa() che mostra il valore corrente

Esempio:

c = Contatore()
c.incrementa()
c.incrementa()
c.stampa()  # Output: Valore attuale: 2'''

class Contatore:
    _valore : int

    def __init__(self, valore:int = 0) -> None:
        self._valore = valore

    def get_valore(self) -> int:
        return self._valore
    
    def incrementa(self) -> None:
        self._valore += 1
    
    def decrementa(self) -> None:
        self._valore -= 1

    def incrementa_Step(self, step:int) -> None:
        self._valore += step
    
    def stampa(self) -> str:
        return f"Valore attuale: {self.get_valore()}"
    
if __name__ == "__main__":
    c = Contatore()
    c.incrementa()
    c.incrementa_Step(3)
    c.decrementa()
    
    print(c.stampa())