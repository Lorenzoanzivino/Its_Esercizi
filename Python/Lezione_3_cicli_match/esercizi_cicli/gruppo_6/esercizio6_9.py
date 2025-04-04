'''6-9. Posti preferiti: Fare un dizionario chiamato preferito-places. Pensa a tre nomi da usare come chiavi nel dizionario e memorizza uno o tre luoghi preferiti per ogni persona. Per rendere questo esercizio un po 'più interessante, chiedi ad alcuni amici di citare alcuni dei loro posti preferiti. Attraversa il dizionario e stampa il nome di ogni persona e i suoi luoghi preferiti.'''

favorite_places:dict[str, str] = {"Marcel": ("Japan", "America"), "Daniela": ("Japan", "America", "Paris"), "Patrisia": ("Japan", "Russia", "China")}

for people in favorite_places.keys():
    print(f"{people}: {favorite_places[people]}")