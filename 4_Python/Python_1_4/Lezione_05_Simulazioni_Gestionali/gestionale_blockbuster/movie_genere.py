'''### CLASSI GENERE
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:

    getGenere(), che ritorna il genere di film
    getPenale(), che ritorna il valore della penale
    calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".'''

from film import Film

class Azione(Film):
    __genere:str
    __penale:float

    def __init__(self, id, title) -> None:
        super().__init__(id, title)
        self.__genere = 'Azione'
        self.__penale = 3.0

    def getGenere(self) -> str:
        return self.__genere

    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo:int) -> float:
        return self.__penale * giorniRitardo



class Commedia(Film):
    __genere:str
    __penale:float

    def __init__(self, id, title) -> None:
        super().__init__(id, title)
        self.__genere = 'Commedia'
        self.__penale = 2.50
    
    def getGenere(self) -> str:
        return self.__genere

    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self, giorniRitardo:int) -> float:
        return self.__penale * giorniRitardo



class Drama(Film):
    __genere:str
    __penale:float

    def __init__(self, id, title) -> None:
        super().__init__(id, title)
        self.__genere = 'Drama'
        self.__penale = 2.0

    def getGenere(self) -> str:
        return self.__genere

    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniRitardo:int) -> float:
        return self.__penale * giorniRitardo