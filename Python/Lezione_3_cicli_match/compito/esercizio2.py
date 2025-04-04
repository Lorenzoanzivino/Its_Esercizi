'''Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''

#l'utente può inserire una parola o una frase in input
stringa:str = str(input("inserisci una parola o una frase: "))
#numeri spazi inizzializzati a 0
numero_spazi:int = 0

#ciclo For: per ogni carattere nella stringa conta gli spazi vuoti (" ")
for carattere in stringa:
    if carattere == " ":
        numero_spazi += 1
print(f"il numero di spazi è: {numero_spazi}")