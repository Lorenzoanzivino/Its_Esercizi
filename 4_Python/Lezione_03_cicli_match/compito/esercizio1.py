'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

#ciclo While
while True:
    #l'utente può inserire una parola in input
    parola:str = str(input('inserisci una parola (inserisci "fine" per terminare): '))
    
    #inserendo la parola "fine" termina il programma
    if parola == "fine":
        break
    
    #verifico se il primo e l'ultimo carattere siano uguali oppure no
    if parola[0] == parola[-1]:
        print(f'La parola "{parola}" inizia e finisce con la stessa lettera')
    else:
        print(f'La parola "{parola}" inizia e finisce con lettere diverse')