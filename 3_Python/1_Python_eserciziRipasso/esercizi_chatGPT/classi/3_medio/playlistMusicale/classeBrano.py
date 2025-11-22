
from classeArtista import Artista

class Brano:
    # classe per creare il Brano
    _titolo:str
    _durata:str    # formato oo:mm:ss

    def __init__(self, titolo:str, durata:str) -> None:
        self._titolo = titolo
        self._durata = durata

    def get_titolo(self) -> str:
        return self._titolo
        
    def get_durata(self) -> str:
        return self._durata

    def __str__(self) -> str:
        return f"{self._titolo} ({self._durata})"
    
    def __repr__(self) -> str:
        return f"{self._titolo} ({self._durata})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Brano):
            return False
        if self.get_titolo() == other.get_titolo() and self.get_durata() == other.get_durata():
            return True
        return False