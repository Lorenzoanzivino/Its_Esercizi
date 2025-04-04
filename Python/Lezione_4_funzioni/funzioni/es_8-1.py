'''- 8-1. Messaggio: Scrivi una funzione chiamata display-message() che stampa una frase che dice a tutti ciò che stai imparando in questo capitolo. Chiamare la funzione e assicurarsi che il messaggio venga visualizzato correttamente.'''


frase:str = (input("Cosa stai imparando in questo capitolo: "))

def display_message(frase:str):
    print(frase)

display_message(frase)