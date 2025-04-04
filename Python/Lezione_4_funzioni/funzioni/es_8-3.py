'''8-3. T-Shirt: Scrivi una funzione chiamata make-shirt() che accetta una taglia e il testo di un messaggio che dovrebbe essere stampato sulla camicia. La funzione dovrebbe stampare una frase che riassuma la dimensione della camicia e il messaggio stampato su di essa. Chiamare la funzione una volta utilizzando argomenti posizionali per fare una camicia. Chiamare la funzione una seconda volta utilizzando argomenti di parole chiave.'''

taglia:int = input("Inserisci la taglia in numeri: ")
testo:str = input("Inserisci un testo: ")

def make_shirt(a:int, b:str):
    a == taglia and b == testo
    print(f" La taglia è: {taglia}, il testo è: {testo.upper()}")

make_shirt(taglia, testo)