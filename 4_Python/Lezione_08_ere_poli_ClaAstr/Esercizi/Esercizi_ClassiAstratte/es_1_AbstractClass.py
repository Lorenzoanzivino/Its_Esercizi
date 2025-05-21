'''Esercizio 1: Creare una classe astratta con metodi astratti

Inizia definendo una classe di base astratta chiamata Shape. Questa classe dovrebbe includere due metodi astratti: uno chiamato area, che sarà responsabile del calcolo dell'area di una forma, e un altro perimetro, che calcolerà il perimetro. Poiché la forma è astratta, non fornirà implementazioni specifiche per questi metodi. Invece, imposta un modello per tutte le forme che erediteranno da esso.

Quindi, crea due sottoclassi in calcestruzzo, Cerchio e Rettangolo, che entrambi estendono la classe Shape. Ognuna di queste sottoclassi deve fornire la propria implementazione dell'area e dei metodi perimetrali, sulla base delle formule geometriche appropriate alle loro forme.

Infine, scrivi un semplice programma di driver (codice di prova) che crea istanze di Circle and Retangle, chiama la loro area e i metodi perimetrali e stampa i risultati. Questo aiuterà a verificare che la gerarchia delle classi funzioni come previsto.'''

from abc import ABC, abstractmethod
import math

# Classe astratta
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Sottoclasse concreta: Cerchio
class Cerchio(Shape):
    def __init__(self, raggio):
        self.r = raggio

    def area(self):
        return math.pi * self.r ** 2

    def perimetro(self):
        return 2 * math.pi * self.r

# Sottoclasse concreta: Rettangolo
class Rettangolo(Shape):
    def __init__(self, base, altezza):
        self.b = base
        self.h = altezza

    def area(self):
        return self.b * self.h

    def perimetro(self):
        return 2 * (self.b + self.h)

# Codice di test
if __name__ == "__main__":
    c = Cerchio(5)
    r = Rettangolo(4, 6)

    print(f"Cerchio -> Area: {c.area():.2f}, Perimetro: {c.perimetro():.2f}")
    print(f"Rettangolo -> Area: {r.area():.2f}, Perimetro: {r.perimetro():.2f}")
