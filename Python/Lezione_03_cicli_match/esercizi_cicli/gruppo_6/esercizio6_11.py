'''6-11. Città: Fare un dizionario chiamato città. Usa i nomi di tre città come chiavi nel tuo dizionario. Crea un dizionario di informazioni su ogni città e includi il paese in cui si trova la città, la sua popolazione approssimativa e un fatto su quella città. Le chiavi del dizionario di ogni città dovrebbero essere qualcosa come paese, popolazione e fatto. Stampa il nome di ogni città e tutte le informazioni che hai memorizzato su di essa.'''

from typing import Any
citta:dict[Any] =  {"Rome":{"Country": "Italy", "Population": "2.76 million", "Fact": "Has 280 fountains and more than 900 churches"},"Okinawa":{"Country": "Japan", "Population": "1.47 million", "Fact": "It's 2,271 square km big"},"Hollywood":{"Country": "America", "Population": "70,915", "Fact": "It's the center of the American film industry"}}
for key, value in citta.items():
    for key1, value1 in value.items():
        print(f"{key}: {key1} - {value1}")