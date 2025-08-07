'''🚗 Esercizio 3: Auto

Crea una classe Auto con:
    attributi: marca, modello, velocità
    metodo accelera() che aumenta la velocità di 10
    metodo frena() che diminuisce la velocità di 10 (ma non va sotto 0)
    metodo stato() che stampa marca, modello e velocità attuale'''

class Auto:
    _marca:str    # dico che _marca sarà una stringa (tipo hint)
    _modello:str
    _velocita:int

    def __init__(self, marca:str, modello:str, velocita:int = 0) -> None:
        self._marca = marca    # qui assegno il valore vero e proprio
        self._modello = modello
        self._velocita = velocita

    def get_marca(self) -> str:
        return self._marca
    
    def get_modello(self) -> str:
        return self._modello
    
    def get_velocita(self) -> int:
        return self._velocita

    def accellera(self, incremento:int = 10) -> None:
            self._velocita += incremento

    def frena(self, decremento: int = 10) -> None:
        if self._velocita < decremento:
            self._velocita = 0
        else:
            self._velocita -= decremento

    def stato(self) -> str:
        return f"Marca: {self.get_marca()}, modello: {self.get_modello()}, velocità attuale: {self.get_velocita()}"
    

if __name__ == "__main__":
    auto = Auto("Renault", "Duster", 8)
    auto.accellera()
    auto.accellera()
    auto.frena()

    print(auto.stato())