'''6. Generatore di password:
Crea una funzione che genera una password casuale con una lunghezza specificata e i tipi di caratteri desiderati (lettere minuscole, lettere maiuscole, numeri, simboli).
Permetti all'utente di specificare la lunghezza della password e i tipi di caratteri desiderati.
Genera e restituisci una password casuale che soddisfi i criteri dell'utente.'''

import random

# funzione per avere la lunghezza dei parametri dall'utente
def scegli_parametri():
    # Chiedi i parametri all'utente
    lunghezza = int(input("Scegli la lunghezza della password: "))
    maiuscole = int(input("Quante lettere maiuscole vuoi nella password? "))
    minuscole = int(input("Quante lettere minuscole vuoi nella password? "))
    simboli = int(input("Quanti simboli vuoi nella password? "))
    numeri = int(input("Quanti numeri vuoi nella password? "))

    # Controllo se la somma dei caratteri non supera la lunghezza della password
    while (maiuscole + minuscole + simboli + numeri) > lunghezza:
        print("Errore: La somma di maiuscole, minuscole, simboli e numeri deve essere minore o uguale alla lunghezza della password.")
        
        # Ritorna i parametri in caso di errore
        lunghezza = int(input("Scegli la lunghezza della password: "))
        maiuscole = int(input("Quante lettere maiuscole vuoi nella password? "))
        minuscole = int(input("Quante lettere minuscole vuoi nella password? "))
        simboli = int(input("Quanti simboli vuoi nella password? "))
        numeri = int(input("Quanti numeri vuoi nella password? "))

    return lunghezza, maiuscole, minuscole, simboli, numeri

# funzione per generare la password casualmente
def genera_password(lunghezza, maiuscole, minuscole, simboli, numeri):

    # Definisci i gruppi di caratteri
    maiuscole_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscole_str = "abcdefghijklmnopqrstuvwxyz"
    simboli_str = "!#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
    numeri_str = "0123456789"

    # Crea una lista con i caratteri richiesti dall'utente
    password:list = []

    # Aggiungi lettere maiuscole
    for i in range(maiuscole):
        indice_casuale:int = random.randint(0, len(maiuscole_str) - 1)
        password.append(maiuscole_str[indice_casuale])

    # Aggiungi lettere minuscole
    for i in range(minuscole):
        indice_casuale:int = random.randint(0, len(minuscole_str) - 1)
        password.append(minuscole_str[indice_casuale])

    # Aggiungi numeri
    for i in range(numeri):
        indice_casuale:int = random.randint(0, len(numeri_str) - 1)
        password.append(numeri_str[indice_casuale])

    # Aggiungi simboli
    for i in range(simboli):
        indice_casuale:int = random.randint(0, len(simboli_str) - 1)
        password.append(simboli_str[indice_casuale])

    # Aggiungi caratteri casuali per completare la lunghezza della password
    caratteri_disponibili = maiuscole_str + minuscole_str + numeri_str + simboli_str
    for i in range(lunghezza - len(password)):
        indice_casuale:int = random.randint(0, len(caratteri_disponibili) - 1)
        password.append(caratteri_disponibili[indice_casuale])

    # Mischia la password per garantire casualità
    random.shuffle(password)

    # Restituisci la password come stringa
    return ''.join(password)

# Ottieni i parametri dall'utente
lunghezza, maiuscole, minuscole, simboli, numeri = scegli_parametri()

# Genera la password
password = genera_password(lunghezza, maiuscole, minuscole, simboli, numeri)

# Mostra la password generata
print(f"La tua password generata è: {password}")

# Mostra asterischi corrispondenti alla lunghezza della password
print('*' * len(password))