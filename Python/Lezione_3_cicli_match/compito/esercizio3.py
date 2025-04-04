'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

#l'utente può inserire una parola o una frase in input
stringa:str = str(input("inserisci una parola o una frase: "))
#inizializzo una variabile reverse vuota
stringa_invertita:str = " "

#ciclo For: per ogni lettera della stringa stampo le stesse lettere invertendo la loro posizione (la prima diventa l'ultima)
for carattere in stringa:
    stringa_invertita = carattere + stringa_invertita
print(f"La frase invertita è: {stringa_invertita}")