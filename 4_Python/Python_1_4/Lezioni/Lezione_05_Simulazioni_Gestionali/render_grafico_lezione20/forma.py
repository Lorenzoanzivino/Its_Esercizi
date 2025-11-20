'''2. RENDERING GRAFICO
Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.'''

from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome:str):
        super().__init__()

        self.nome = nome
    
    @abstractmethod
    def getArea(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass