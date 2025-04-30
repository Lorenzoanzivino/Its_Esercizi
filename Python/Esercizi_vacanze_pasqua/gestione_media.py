class Media:
    def __init__(self, name: str, y: int) -> None:
        self.title : str = name
        self.years : int = y

    def get_info(self) -> str:
        return f"{self.title} ({self.years})"
    

class Movie(Media):
    def __init__(self, name: str, y: int, duration: int) -> None:
        super().__init(name, y)
        self.duration : int = duration

    def get_info(self) -> str:
        return f"[FILM] {super().get_info} - Durata: {self.duration}"
    

class SerieTV(Media):
    def __init__(self, name: str, y: int, seasons: int) -> None:
        super().__init(name, y)
        self.seasons : int = seasons

    def get_info(self):
        return f"[SERIETV] {super().get_info} - Stagioni: {self.seasons}" 
    
    
class MovieCatalog:
# Seguire questo schema per i progetti di Progettazione
catalogo: dict[str, list[str]]

def __init__(self) -> None:
    # Dizionario per memorizzare i registi e i loro film
    self.catalogo = {} # Inizializzata

def add_movie(self, director_name: str, movies: list[Movie] | list[SerieTV]) -> None:
    # Aggiunge uno o più film al regista specificato
    if director_name not in self.catalogo:
        self.catalogo[director_name] = movies
    else:
        for movie in movies:
            if movie not in self.catalogo[director_name]:
                self.catalogo[director_name].append(movie)
            
    print(f"Film aggiunti al regista {director_name}: {', '.join(movies)}")

def remove_movie(self, director_name, movie_name) -> None:
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

def list_directors(self) -> list[str]:
    # Elenco dei registi presenti nel catalogo
    if self.catalogo:
        print("Registi nel catalogo:")
        for director in self.catalogo:
            print(director)
    else:
        print("Nessun regista nel catalogo.")

def get_movies_by_director(self, director_name) -> list[str]:
    # Restituisce tutti i film di un regista specifico
    if director_name in self.catalogo:
        return self.catalogo[director_name]

def search_movies_by_title(self, title) -> dict[str, list[str]] | str:
    # Cerca film che contengono una certa parola nel titolo
    result : dict[str, list[str]] = {}

    for director, movies in self.catalogo.items():
        matching_movies: list[str] = []

        for movie in movies:
            if title.lower() in movie.lower():
                matching_movies.append(movie)
        

        if matching_movies:
            result[director] = matching_movies

    if result:
        return result
    else:
        return "non è stato trovato nulla"