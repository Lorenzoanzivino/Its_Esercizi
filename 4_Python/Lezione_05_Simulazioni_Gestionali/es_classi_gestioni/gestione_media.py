class Media:
    def __init__(self, name: str, y: int) -> None:
        self.title: str = name
        self.years: int = y

    def get_info(self) -> str:
        return f"{self.title} ({self.years})"


class Movie(Media):
    def __init__(self, name: str, y: int, duration: int) -> None:
        super().__init__(name, y)
        self.duration: int = duration

    def get_info(self) -> str:
        return f"[FILM] {super().get_info()} - Durata: {self.duration} min"


class SerieTV(Media):
    def __init__(self, name: str, y: int, seasons: int) -> None:
        super().__init__(name, y)
        self.seasons: int = seasons

    def get_info(self) -> str:
        return f"[SERIETV] {super().get_info()} - Stagioni: {self.seasons}"


class MovieCatalog:
    def __init__(self) -> None:
        self.catalogo: dict[str, list[Media]] = {}

    def add_movie(self, director_name: str, movies: list[Media]) -> None:
        if director_name not in self.catalogo:
            self.catalogo[director_name] = movies
        else:
            for movie in movies:
                if movie not in self.catalogo[director_name]:
                    self.catalogo[director_name].append(movie)
        print(f"Film aggiunti al regista {director_name}: {', '.join(m.get_info() for m in movies)}")

    def remove_movie(self, director_name: str, movie_name: str) -> None:
        if director_name in self.catalogo:
            for movie in self.catalogo[director_name]:
                if movie.title == movie_name:
                    self.catalogo[director_name].remove(movie)
                    print(f"Il film '{movie_name}' è stato eliminato da {director_name}.")
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
                    return
            print(f"Il film '{movie_name}' non è presente per il regista {director_name}.")
        else:
            print(f"Il regista '{director_name}' non è presente nel catalogo.")

    def list_directors(self) -> None:
        if self.catalogo:
            print("Registi nel catalogo:")
            for director in self.catalogo:
                print(director)
        else:
            print("Nessun regista nel catalogo.")

    def get_movies_by_director(self, director_name: str) -> list[str] | None:
        if director_name in self.catalogo:
            return [movie.get_info() for movie in self.catalogo[director_name]]
        return None

    def search_movies_by_title(self, title: str) -> dict[str, list[str]] | str:
        result: dict[str, list[str]] = {}

        for director, movies in self.catalogo.items():
            matching_movies: list[str] = []
            for movie in movies:
                if title.lower() in movie.title.lower():
                    matching_movies.append(movie.get_info())
            if matching_movies:
                result[director] = matching_movies

        if result:
            return result
        else:
            return "Non è stato trovato nulla."