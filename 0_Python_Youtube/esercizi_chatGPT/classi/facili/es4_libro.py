'''📚 Esercizio 4 : Libro

Crea una classe Libro che contenga:
    attributi: titolo, autore, pagine
    metodo descrizione() che stampa: "Titolo: <titolo>, Autore: <autore>, Pagine: <pagine>"

Esempio:
l = Libro("1984", "George Orwell", 328)
l.descrizione()'''


class Libro:
    _titolo:str
    _autore:str
    _pagine:int

    def __init__(self, titolo:str, autore:str, pagine:int) -> None:
        self._titolo = titolo
        self._autore = autore

        if pagine <= 0:
            raise ValueError("Numero di pagine erraro")
        self._pagine = pagine

    def get_titolo(self) -> str:
        return self._titolo

    def get_autore(self) -> str:
        return self._autore
    
    def get_pagine(self) -> int:
        return self._pagine
    
    def descrizione(self) -> str:
        return f"Titolo: {self.get_titolo()}, autore: {self.get_autore()}, pagine: {self.get_pagine()}"
    

if __name__ == "__main__":

    libro = Libro("1984", "George Orwell", 328)
    print(libro.descrizione())
