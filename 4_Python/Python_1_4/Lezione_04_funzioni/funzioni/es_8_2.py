'''8-2. Libro preferito: scrivi una funzione chiamata preferito-book() che accetta un parametro, titolo. La funzione dovrebbe stampare un messaggio, come "Uno dei miei libri preferiti è Alice nel paese delle meraviglie". Chiamare la funzione, assicurarsi di includere un titolo di libro come argomento nella chiamata di funzione.'''

titolo:str = input("Qual'è il tuo libro preferito?: ")
def favorite_book(titolo:str):
    print(f"Il mio libro preferito è: {titolo}")

favorite_book(titolo)