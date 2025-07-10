from abc import ABC, abstractmethod
from datetime import datetime

class Utente(ABC):
    def __init__(self, username:str) -> None:
        self.set_username(username)
        self._registrazione = datetime.now() # imposta l'orario di registrazione al momento della creazione dell’istanza.

    def get_username(self) -> str:
        return self._username
    
    def set_username(self, nuovo_username:str) -> None:
        if not isinstance(nuovo_username, str):
            raise ValueError("L'username deve essere una stringa")
        self._username = nuovo_username

    def get_registrazione(self) -> datetime: # non serve il set perche la data non può cambiare
        return self._registrazione
    
class VenditoreProfessionale(Utente):
    def __init__(self, username, vetrina: str):
        super().__init__(username)
        self.set_vetrina(vetrina)

    def get_vetrina(self) -> str:
        return self._vetrina
    
    def set_vetrina(self, nuova_vetrina:str) -> None:
        if not isinstance(nuova_vetrina, str):
            raise ValueError("La vetrina deve essere una stringa")
        self._vetrina = nuova_vetrina

    def __str__(self):
        return f"VenditoreProfessionale(username={self.get_username()}, vetrina={self.get_vetrina()}, registrazione={self.get_registrazione()})"
    
    def popolarita(self) -> str:
        return 

class Privato(Utente):
    def __init__(self, username):
        super().__init__(username)

    def __str__(self) -> str:
        return f"Privato = {self.get_username()}, registrazione = {self.get_registrazione()}"