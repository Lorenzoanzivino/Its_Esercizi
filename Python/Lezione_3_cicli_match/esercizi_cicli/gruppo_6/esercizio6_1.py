'''- 6-1. Persona: Utilizzare un dizionario per memorizzare informazioni su una persona che conosci. Conservare il loro nome, cognome, età e la città in cui vivono. Dovresti avere chiavi come nome, cognome, età e città. Stampa ogni informazione memorizzata nel tuo dizionario.'''

from typing import Any

persone:dict[Any] = {"nome": "lorenzo", "cognome":"anzivino", "anni":30, "citta":"roma"}
print(persone.values())

