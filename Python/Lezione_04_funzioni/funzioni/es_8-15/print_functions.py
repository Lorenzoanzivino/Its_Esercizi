'''8-15. Modelli di stampa: mettere le funzioni per l'esempio print-models.py in un file separato chiamato print-functions.py. Scrivi una dichiarazione di importazione nella parte superiore di print-models.py e modifica il file per utilizzare le funzioni importate.'''

# printing_functions.py

def printing_asterischi(n:str):
    """ stampa una riga di asterischi """
    print('*' * n)

def printing_trattini(n:str):
    """ stampa una riga di trattini """
    print('-' * n)

def printing_numeri(n:str):
    """ stampa numeri da 1 a ... """
    for i in range(1, n + 1):
        print(i, end=' ')
    print()

def printing_punti(n:str):
    ''' stampa una riga di punti '''
    print("·" * n)

def printing_somma(a:int, b:int):
    ''' stampa la somma'''
    print(a + b)
    return a + b