'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.
Il programma deve:
• Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
• Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

#variabili inizializzate fuori dal ciclo
somma:float = 0
numeri_interi:int = 0
numero_max:float = float('-inf')  
numero_min:float = float('inf')   
media:float = 0

#ciclo While
while True:
    numeri:float = float(input('Inserisci numeri positivi (interi e decimali) oppure (inserisci un "numero negativo" per terminare): '))
    #se il numero è negativo allora termina
    if numeri < 0:
        break
    #se i numeri sono interi, aggiorna la somma e il numero di numeri inseriti
    if numeri.is_integer():  
        somma += numeri  
        numeri_interi += 1  
    #altrimenti se sono decimali, verifica il maggiore e il minore
    else:
        if numeri > numero_max:
            numero_max = numeri  
        if numeri < numero_min:
            numero_min = numeri  
#se sono interi stampa la media
if numeri_interi > 0:
    media = somma / numeri_interi  
    print(f"La media dei numeri interi inseriti è: {media:.2f}")
#se sono decimali stampa il maggiore e il minore
if numero_max != float('-inf') and numero_min != float('inf'):
    print(f"Il numero decimale più grande inserito è: {numero_max}")
    print(f"Il numero decimale più piccolo inserito è: {numero_min}")