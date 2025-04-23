'''Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.
Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:
*****
********
***
************
*******
'''

#inizializzo una lista vuota
numeri:list[int] = []

#faccio inserire all'utente 5 numeri
for i in range(5):
    numero:int = int(input("inserisci compreso tra 1 e 30: "))
    
    #se i numeri sono compresi tra 1 e 30 allora aggiungi il numero alla lista
    if 1 <= numero <= 30:
        numeri.append(numero)
    #altrimenti errore e quel numero viene eliminato e non viene considerato
    else:
        print("Numero non compreso tra 1 e 30, inserisci un altro numero")
        i -=1
#per ogni numero nella lista numeri, scambia il numero con il caratte "*"
for numero in numeri:
    print('*' * numero)