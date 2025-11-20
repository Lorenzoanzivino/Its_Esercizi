''' 7. Conversione numerica romana:
    Crea una funzione che converte un dato intero alla sua rappresentazione numerica romana.
    Maneggiare i numeri da 1 a 3999.
    Utilizzare una combinazione di manipolazione delle stringhe e dichiarazioni condizionali per costruire il numero romano.'''

# Pseudocodice
'''
1) Chiedere all'utente un numero tra 1 e 3999
2) Controllare che il numero sia valido (se non lo è, mostrare un messaggio di errore e terminare)
3) Creare una tabella ordinata di conversione (associa numeri ai simboli romani)
4) Creare una stringa vuota per la conversione
5) Scorrere la tabella dalla cifra più grande alla più piccola:
    • Se il numero è maggiore o uguale al valore attuale:
    • Aggiungere il simbolo corrispondente alla stringa
    • Sottrarre il valore dal numero
    • Ripetere finché il numero è inferiore al valore attuale
6) Stampare il numero romano risultante'''

# Funzioni da utilizzare
'''
1) Funzione per generare un numero tra 1 e 3999 da input
    • Controllare che sia nell'intervallo corretto (1-3999).
    • Se non è valido, chiedere di inserirlo di nuovo.
    • Restituire il numero corretto.
    
2) Funzione che tiene traccia della conversione da numeri a numeri romani (esiste una tabella)
    • Definire una tabella di conversione con i numeri e i simboli corrispondenti.
    • Restituire questa tabella per poterla usare nella conversione.
3) Funzione che converte i numeri e li salva in una nuova lista
    • Creare una lista vuota per il risultato.
    • Prendere il numero e confrontarlo con la tabella di conversione.
    • Sottrarre i valori più grandi possibili e aggiungere i simboli corrispondenti alla lista.
    • Ripetere fino a ridurre il numero a zero.
    • Restituire la lista unita in una stringa.'''
    

# 1) Funzione per generare un numero tra 1 e 3999 da input   
def numero_da_convertire():
    while True:
        numero:int = int(input("Seleziona un numero compreso tra 1 e 3999 (oppure digita 0 per terminare): "))
        if numero == 0:
            return None
        elif numero < 1 or numero > 3999:
            print("Numero non valido, seleziona un altro numero: ")
        else:
            return numero
        
# 2) Funzione che tiene traccia della conversione da numeri a numeri romani    
def tabella():    
    tabella_conversione:dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    return tabella_conversione

# 3) Funzione che converte i numeri e li salva in una nuova lista
def conversione(numero, tabella_conversione):
    numeri_romani = []  # Lista per accumulare i simboli romani
    
    for key, value in tabella_conversione.items():  
        while numero >= key:  # Finché il numero è maggiore o uguale alla chiave
            numero -= key  # Sottrai il valore della chiave
            numeri_romani.append(value)  # Aggiungi il simbolo romano corrispondente
    
    return "".join(numeri_romani)  # Converte la lista in una stringa

# Ottieni il numero da convertire
while True:
    numero = numero_da_convertire()
    if numero is None:
        print("Termine del programma")
        break

    # Ottieni la tabella di conversione
    tabella_conversione = tabella()

    # Converte il numero e ottieni il risultato
    numero_romano = conversione(numero, tabella_conversione)

    # Stampa il risultato
    print(f"\nIl numero: {numero} in numeri romani è: {numero_romano}")