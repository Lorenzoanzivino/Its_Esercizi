'''2. Gestore di Biblioteca con Ereditarietà e Eccezioni
Crea una classe Libro con titolo, autore, e stato (disponibile o no).
Crea una classe Biblioteca che gestisce libri, prestiti e restituzioni.
Implementa metodi per prestare libri, restituirli, e una custom exception se si prova a prendere un libro non disponibile o un libro raro senza autorizzazione.'''

class Libro:
    _titolo: str
    _autore: str
    _stato: str
    
    def __init__(self, titolo: str, autore: str, stato: str = "disponibile") -> None:
        self._titolo = titolo
        self._autore = autore
        self._stato = stato

    def get_titolo(self) -> str:
        return self._titolo
    
    def get_autore(self) -> str:
        return self._autore
    
    def get_stato(self) -> str:
        return self._stato
    
    def presta(self) -> str:
        if self._stato == "disponibile":
            self._stato = "prestato"
            return f"Il libro '{self.get_titolo()}' è stato prestato."
        else:
            return f"Il libro '{self.get_titolo()}' non è disponibile per il prestito."
        
    def restituzione(self) -> str:
        if self._stato == "prestato":
            self._stato = "disponibile"
            return f"Il libro '{self.get_titolo()}' è stato restituito."
        else:
            return f"Il libro '{self.get_titolo()}' non era stato prestato."
        
    def info(self) -> str:
        return f"Libro: {self.get_titolo()}, autore: {self.get_autore()}, stato: {self.get_stato()}"

class Biblioteca:
    def __init__(self):
        self._libri = []

    def aggiungi_libro(self, libro: Libro) -> None:
        self._libri.append(libro)

    def presta_libro(self, titolo: str, autorizzato: bool = False) -> str:
        libro = self._trova_libro(titolo)
        if libro is None:
            return f"Libro '{titolo}' non trovato in biblioteca."
        

    def restituisci_libro(self, titolo: str) -> str:
        libro = self._trova_libro(titolo)
        if libro is None:
            return f"Libro '{titolo}' non trovato in biblioteca."
        libro.restituzione()
        return f"Il libro '{titolo}' è stato restituito."

    def _trova_libro(self, titolo: str) -> Libro | None:
        for libro in self._libri:
            if libro.get_titolo() == titolo:
                return libro
        return None