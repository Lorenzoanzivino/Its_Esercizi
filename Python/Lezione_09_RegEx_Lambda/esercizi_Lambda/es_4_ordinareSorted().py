'''Esercizio 4 – Ordinamento con sorted()

Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]. Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.'''

studenti: list[tuple[str, int]] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

print(list(sorted(studenti, key = lambda info: info[1])))