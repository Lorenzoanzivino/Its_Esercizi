'''es 3.Gestione dei File con Context Manager

Utilizza l'istruzione with e i context manager per aprire e chiudere un file. Gestisci eventuali IOError all'interno del blocco with per garantire una gestione pulita delle risorse.'''

try:
    with open('file_di_testo.txt', 'r') as file:
        try:
            contenuto = file.read()
            print(contenuto)
        except IOError:
            print("Errore durante la lettura del file.")
except IOError:
    print("Errore nell'apertura del file.")