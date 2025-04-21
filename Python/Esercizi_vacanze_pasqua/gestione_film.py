'''Sistema di Gestione Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
 
Codice driver

    Crea un’istanza della classe MovieCatalog.
    Aggiungi nuovi film e registi.
    Aggiungi film a registi già presenti nel catalogo.
    Rimuovi film dal catalogo.
    Elenca i registi presenti nel catalogo.
    Visualizza film di uno specifico regista.
    Cerca film per parola chiave nel titolo, gestendo il caso con risultati che senza.'''

class MovieCatalog:
    def __init__(self):
        # Dizionario per memorizzare i registi e i loro film
        self.catalogo: dict = {}

    def add_movie(self, director_name: str, movies: list):
        # Aggiunge uno o più film al regista specificato
        if director_name not in self.catalogo:
            self.catalogo[director_name] = []

        for movie in movies:
            if movie not in self.catalogo[director_name]:
                self.catalogo[director_name].append(movie)

        print(f"Film aggiunti al regista {director_name}: {', '.join(movies)}")

    def remove_movie(self, director_name, movie_name):
        # Controllo se il regista esiste nel catalogo
        if director_name in self.catalogo:
            # Controllo se il film è presente nella lista del regista
            if movie_name in self.catalogo[director_name]:
                self.catalogo[director_name].remove(movie_name)
                print(f"Il film '{movie_name}' è stato eliminato da {director_name}.")

                # Se la lista del regista è vuota, chiediamo se rimuovere anche il regista dal catalogo
                if not self.catalogo[director_name]:
                    while True:
                        scelta = input(f"La lista dei film di {director_name} è vuota. Vuoi rimuovere il regista dal catalogo? [s/n]: ")
                        if scelta.lower() == 's':
                            del self.catalogo[director_name]
                            print(f"{director_name} è stato rimosso dal catalogo.")
                            break
                        elif scelta.lower() == 'n':
                            print(f"{director_name} non è stato rimosso dal catalogo.")
                            break
                        else:
                            print("Risposta non valida, per favore scegli 's' o 'n'.")
            else:
                print(f"Il film '{movie_name}' non è presente per il regista {director_name}.")
        else:
            print(f"Il regista '{director_name}' non è presente nel catalogo.")

    def list_directors(self):
        # Elenco dei registi presenti nel catalogo
        if self.catalogo:
            print("Registi nel catalogo:")
            for director in self.catalogo:
                print(director)
        else:
            print("Nessun regista nel catalogo.")

    def get_movies_by_director(self, director_name):
        # Restituisce tutti i film di un regista specifico
        if director_name in self.catalogo:
            print(f"Film di {director_name}: {', '.join(self.catalogo[director_name])}")
        else:
            print(f"Il regista '{director_name}' non è presente nel catalogo.")

    def search_movies_by_title(self, title):
        # Cerca film che contengono una certa parola nel titolo
        risultati = []
        for director, movies in self.catalogo.items():
            for movie in movies:
                if title.lower() in movie.lower():
                    risultati.append(f"{director}: {movie}")

        if risultati:
            print("Film trovati:")
            for risultato in risultati:
                print(risultato)
        else:
            print(f"Nessun film trovato con il titolo '{title}'.")


# Creo istanze diverse della classe MovieCatalog
catalogo1 = MovieCatalog()
catalogo2 = MovieCatalog()

# Aggiungo alcuni film al catalogo1
catalogo1.add_movie("Martin Scorsese", ["Goodfellas", "Taxi Driver", "The Irishman"])
catalogo1.add_movie("Steven Spielberg", ["Schindler's List", "Jurassic Park", "E.T."])

# Aggiungo alcuni film al catalogo2
catalogo2.add_movie("Ridley Scott", ["Gladiator", "Alien", "The Martian"])
catalogo2.add_movie("James Cameron", ["Titanic", "Avatar", "Terminator"])

# Elenco tutti i registi nel catalogo1
catalogo1.list_directors()

# Ottengo tutti i film di un regista nel catalogo2
catalogo2.get_movies_by_director("Ridley Scott")

# Cerco film per parola chiave nel titolo nel catalogo1
catalogo1.search_movies_by_title("irish")  # Dovrebbe trovare "The Irishman"
catalogo1.search_movies_by_title("park")  # Dovrebbe trovare "Jurassic Park"
catalogo1.search_movies_by_title("star")  # Nessun film trovato

# Elenco i registi nel catalogo2
catalogo2.list_directors()

# Ottengo i film di un regista nel catalogo1
catalogo1.get_movies_by_director("Steven Spielberg")

# Rimuovo un film dal catalogo2
catalogo2.remove_movie("James Cameron", "Avatar")

# Rimuovo un film che non esiste nel catalogo1
catalogo1.remove_movie("Martin Scorsese", "The Godfather")  # Film non presente
