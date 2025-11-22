'''# input serve per far interagire l'utente con il terminale ad esempio per scelte

x = input("cosa vuoi fare? ")

persona:dict = {
    "nome" : "Lorenzo",
    "cognome" : "Anzivino",
    "eta" : 28
}

operazioni:tuple = ("aggiungere", "modificare", "eliminare")

def start():
    operazione = input("Cosa vuoi fare? ")

    if operazione == operazioni[0]:    # aggiungere
        x = input("Aggiungi chiave:valore separati da virgola: ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:  # modificare
        pass 
    elif operazione == operazioni[2]:  # eliminare
        pass

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

while True:
    start()
'''
import json

dizionario:dict = {
    "nome" : "Simona",
    "cognome" : "Macchioni",
    "eta" : 25,
    "interessi" : ["Musica", "Cucina", "Droga"],
    "indirizzo" : {
        "via" : "Via PietroNenni",
        "civico" : 32,
        "CAP" : "00071"
    },
    "pensione" : False,
}

print(dizionario["nome"])

y = json.dumps(dizionario, indent=4, sort_keys=True)    # ordine alfabetico
print("--------------------------------------------------------------")
print(y)