'''5. Gestione Base di una Playlist Musicale

Gestire una playlist musicale composta da brani di diversi artisti.

    Artista: dati personali e lista dei propri brani.

    Brano: titolo, durata (mm:ss), artista associato.

    Playlist: lista di brani, con funzioni per aggiungere, rimuovere, calcolare durata totale e stampare in ordine alfabetico.'''

from datetime import time 

class Artista:
    # classe per creare Artista
    _nome:str
    _cognome:str
    _nomeArte:str
    _braniArtista:list

    def __init__(self) -> None:
        pass

    def get_nome(self) -> str:
        pass
        
    def get_cognome(self) -> str:
        pass

    def get_nomeArte(self) -> str:
        pass

    def aggiungiBrano(self, brano) -> None:
        pass

    def get_brani(self) -> list:
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        pass
    

class Brano:
    # classe per creare il Brano
    _titolo:str
    _durata:time    # formato mm:ss
    _artista:Artista

    def __init__(self) -> None:
        pass

    def get_titolo(self) -> str:
        pass
        
    def get_durata(self) -> time:
        pass

    def set_durata(self, minuti:int, secondi:int) -> None:
        # controllo del tempo in minuti        
        pass

    def get_artista(self) -> Artista:
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, other) -> bool:
        pass

class Playlist:
    # classe per raccolta di brani
    _listaBrani:list

    def __init__(self) -> None:
        pass

    def get_listaBrani(self) -> str:
        pass

    def aggiungiBrano(self, brano:Brano) -> None:
        pass

    def rimuoviBrano(self, titolo:str) -> None:
        pass

    def durataPlaylist(self) -> time:
        pass

    def stampaLista(self) -> None:
        # stampa l'intera playlist in ordine alfabetico
        pass

    def __str__(self) -> str:
        pass

if __name__ == "__main__":
    pass