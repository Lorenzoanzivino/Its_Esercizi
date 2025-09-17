'''8-15. Modelli di stampa: mettere le funzioni per l'esempio print-models.py in un file separato chiamato print-functions.py. Scrivi una dichiarazione di importazione nella parte superiore di print-models.py e modifica il file per utilizzare le funzioni importate.'''

# print-models.py
from print_functions import printing_asterischi, printing_trattini, printing_numeri, printing_punti, printing_somma

# Esempio di utilizzo delle funzioni importate
printing_asterischi(10)
printing_trattini(15)
printing_numeri(9)
printing_punti(18)
printing_somma(6, 8)
printing_somma(5, 5)