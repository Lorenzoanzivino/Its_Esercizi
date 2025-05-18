'''Esercizio 7 – Filtra parole corte

Hai una lista di parole parole = ["cane", "gatto", "elefante", "ratto", "orso"] Estrai solo le parole con più di 4 lettere usando filter() e lambda.'''

parole:list = ["cane", "gatto", "elefante", "ratto", "orso"]
paroleLunghe : list = []

paroleLunghe = list(filter(lambda parola: len(parola) > 4, parole))

print(paroleLunghe)  # Output: ['gatto', 'elefante', 'ratto']