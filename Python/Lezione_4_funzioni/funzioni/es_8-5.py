'''8-5. Città: Scrivere una funzione chiamata des-city() che accetta il nome di una città e del suo paese. La funzione dovrebbe stampare una frase semplice, come Reykjavik è in Islanda. Dai al parametro per il paese un valore predefinito. Chiama la tua funzione per tre città diverse, almeno una delle quali non è nel paese predefinito.'''

def describe_city(citta:str, paese:str = "Italia"):
    print(f"Il {citta} sta in {paese}")

describe_city("Roma")
describe_city("Milano")
describe_city("Torino")