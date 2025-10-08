'''2. Conta parole

Scrivi una funzione che riceve una stringa e ritorna un dizionario con quante volte compare ogni parola.

# Input: "ciao mondo ciao"
# Output: {"ciao": 2, "mondo": 1}

Suggerimento: usa .split() + un dizionario per contare.'''

def contaParole(stringa:str)-> dict[str, int]:
    dizionario:dict[str, int] = {}

    for parola in stringa.split():
        if parola not in dizionario:
            dizionario[parola] = 1
        else:
            dizionario[parola] += 1
    
    return dizionario
            
# Test
stringa = "ciao mondo ciao"
print(contaParole(stringa))  # Output: {"ciao": 2, "mondo": 1}