# Leggere json in python
# da Python a Json
# dati convertibili in Json
    # dict
    # list
    # tuple
    # string
    # int
    # float
    # True
    # False
    # None
# formattare il json
# ordinare il json

import json

file_json = '{"nome" : "Lorenzo", "cognome" : "Anzivino", "eta" : 25}'

x:dict = {
    "nome" : "Lorenzo", 
    "cognome" : "Anzivino", 
    "eta" : 25,
    "isOnline" : False,
    "interessi" : ["calcio", "musica"],
    "soldi" : 4.50,
    "fidanzata" : None
    }

y = json.loads(file_json)
y = json.dumps(x, indent=2, sort_keys=True)    # ordine alfabetico

print(file_json)
print(y)