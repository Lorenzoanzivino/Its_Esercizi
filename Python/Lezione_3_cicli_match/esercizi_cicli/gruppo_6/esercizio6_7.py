'''6-7. Persone: Inizia con il programma che hai scritto per l'esercizio 6-1. Crea due nuovi dizionari che rappresentano persone diverse e conserva tutti e tre i dizionari in una lista chiamata persone. Attraversa la tua lista di persone. Mentre in loop l'elenco, stampa tutto ciò che sai su ogni persona.'''

from typing import Any


lorenzo:dict[Any] = {"nome": "lorenzo", "cognome":"anzivino", "anni":30, "citta":"roma"}
marco:dict[Any] = {"nome": "marco", "cognome":"anzivino", "anni":49, "citta":"roma"}
stefano:dict[Any] = {"nome": "stefano", "cognome":"anzrealiivino", "anni":35, "citta":"roma"}

persone:list[str, int] = [lorenzo, stefano, marco]

for info in persone:
    print(info.values())