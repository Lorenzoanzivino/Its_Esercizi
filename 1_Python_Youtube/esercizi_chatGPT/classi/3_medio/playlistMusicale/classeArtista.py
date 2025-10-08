

class Artista:
    # classe per creare Artista
    _nome:str
    _cognome:str
    _nomeArte:str

    def __init__(self, nome:str, cognome:str, nomeArte:str) -> None:
        self._nome = nome
        self._cognome = cognome
        self._nomeArte = nomeArte

    def get_nome(self) -> str:
        return self._nome
        
    def get_cognome(self) -> str:
        return self._cognome

    def get_nomeArte(self) -> str:
        return self._nomeArte

    def get_brani(self) -> list:
        print("Lista brani")
        return self._braniArtista

    def __str__(self) -> str:
        return f"{self._nome} {self._cognome} aka {self._nomeArte}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Artista):
            return False
        if self.get_nomeArte() == other.get_nomeArte():
            return True
        return False
    
    def __hash__(self) -> int:
        return hash(self._nomeArte)