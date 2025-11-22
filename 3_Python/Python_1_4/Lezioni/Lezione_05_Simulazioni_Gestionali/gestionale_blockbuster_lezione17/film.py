'''### CLASSE: Film
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
'''

class Film:
    
    __id:int
    __title:str

    def __init__(self, id:int, title:str) -> None:
        self.__id = id
        self.__title = title

    def getId(self) -> int:
        return self.__id
    
    def setId(self, new_id) -> None:
        if isinstance(new_id, int):
            self.__id = new_id
        else:
            print("Il codice deve essere un intero")

    def getTitle(self) -> str:
        return self.__title
    
    def setTitle(self, new_title) -> None:
        if isinstance(new_title, str):
            self.__title = new_title
        else:
            print("Il titolo deve essere una stringa")

    def isEqual(self, otherFilm: 'Film') -> bool:
        if not isinstance (otherFilm, Film):
            return False
        return self.__id == otherFilm.getId()

