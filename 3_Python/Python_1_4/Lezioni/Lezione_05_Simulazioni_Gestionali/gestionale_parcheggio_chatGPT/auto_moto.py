'''CLASSI DERIVATE

Crea due classi che derivano da Veicolo:

Auto

Moto

Ogni sottoclasse deve avere:

un attributo privato tipo (string) = "Auto" o "Moto"

un attributo privato tariffa (float):

Auto → 2.0 € all’ora

Moto → 1.0 € all’ora

Metodi richiesti:

getTipo()

getTariffa()

calcolaCosto(ore) → restituisce il costo del parcheggio.

Queste classi vanno in tipi_veicolo.py.'''

from veicolo import Veicolo

class Auto(Veicolo):

    __tipo:str
    __tariffa:float

    def __init__(self, id, modello) -> None:
        super().__init__(id, modello)

        self.__tipo = "Auto"
        self.__tariffa = 2.00

    def getTipo(self) -> str:
        return self.__tipo 

    def getTariffa(self) -> float:
        return self.__tariffa
    
    def calcolaCosto(self, ore:int) -> float:
        return self.__tariffa * ore
    
class Moto(Veicolo):

    __tipo:str
    __tariffa:float

    def __init__(self, id, modello) -> None:
        super().__init__(id, modello)

        self.__tipo = "Moto"
        self.__tariffa = 1.00

    def getTipo(self) -> str:
        return self.__tipo 

    def getTariffa(self) -> float:
        return self.__tariffa
    
    def calcolaCosto(self, ore:int) -> float:
        return self.__tariffa * ore