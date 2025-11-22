'''
### Test con codice driver
Scrivere un codice driver in cui si crea una lista di 10 film, di cui 5 sono film d'azione, 4 sono commedie e 1 è un film drammatico. Successivamente:

    Creare un oggetto Noleggio.
    Stampare: "Quale film vuoi nolleggiare?"
    Simulare il noleggio di un film di un primo cliente.
    Simulare il noleggio di un secondo film sempre da parte del primo cliente.
    Simulare il noleggio del film precedente da parte di un secondo cliente. (assicurarsi che il codice avvisi il secondo cliente che il film richiesto non è disponibile).
    Simulare il noleggio di un terzo film da parte del secondo cliente.
    Simulare il reso del secondo film noleggiato dal primo cliente.
    Stampare la lista dei film disponibili in negozio.

'''

from movie_genere import *
from noleggio import Noleggio

# Film d'azione
film1 = Azione(1, "Die Hard")
film2 = Azione(2, "Mad Max: Fury Road")
film3 = Azione(3, "John Wick")
film4 = Azione(4, "The Dark Knight")
film5 = Azione(5, "Gladiator")

# Commedie
film6 = Commedia(6, "The Hangover")
film7 = Commedia(7, "Superbad")
film8 = Commedia(8, "Step Brothers")
film9 = Commedia(9, "Anchorman")

# Drammatico
film10 = Drama(10, "The Shawshank Redemption")

lista_film = [film1, film2, film3, film4, film5, film6, film7, film8, film9, film10]

noleggio1: Noleggio = Noleggio(film_list=lista_film)

print('Quale film vuoi nolleggiare?')

noleggio1.rentAMovie(film=film1, clientID=1)
print('-' * 50)
noleggio1.rentAMovie(film=film2, clientID=1)
print('-' * 50)
noleggio1.rentAMovie(film=film2, clientID=2)
print('-' * 50)
noleggio1.rentAMovie(film=film3, clientID=2)
print('-' * 50)
noleggio1.giveBack(film=film2, clientID=1, giorniRitardo=8)
print('-' * 50)
noleggio1.printMovies()