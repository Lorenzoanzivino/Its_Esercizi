'''Esercizio: Parcheggio Auto 🚗
CLASSE: Veicolo

In un file chiamato veicolo.py, definisci la classe Veicolo che rappresenta un veicolo.
La classe deve avere:

un id (int)

un modello (string)

Entrambi gli attributi devono essere privati.

Metodi richiesti:

__init__(id, modello)

getID()

getModello()

isEqual(otherVeicolo) → ritorna True se due veicoli hanno lo stesso id.'''

class Veicolo:

    __id:int
    __modello:str

    def __init__(self, id:int, modello:str) -> None:
        self.__id = id
        self.__modello = modello

    def getID(self) -> int:
        return self.__id

    def getModello(self) -> str:
        return self.__modello

    def isEqual(self, otherVeicolo: 'Veicolo') -> bool:
        if not isinstance (otherVeicolo, Veicolo):
            return False
        return self.__id == otherVeicolo.getID()