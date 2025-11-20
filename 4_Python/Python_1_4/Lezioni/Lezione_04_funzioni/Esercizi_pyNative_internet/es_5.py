'''Esercizio 5: Creare una funzione interiore per calcolare l'aggiunta nel modo seguente

    Creare una funzione esterna che accetti due parametri, a e così via b
    Creare una funzione interna all'interno di una funzione esterna che calcolerà l'aggiunta di a e così via b
    Infine, una funzione esterna aggiungerà 5 nell'addizione e la restituirà'''

def esterna(a, b):
    
    def interna(a, b):
        return a + b
    
    return interna(a, b) + 5

result = esterna(5, 10)
print(result)