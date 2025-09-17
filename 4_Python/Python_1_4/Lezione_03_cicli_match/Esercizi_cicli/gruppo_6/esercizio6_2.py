'''- 6-2. Numeri preferiti: utilizzare un dizionario per memorizzare i numeri preferiti delle persone. Pensa a cinque nomi e usali come chiavi nel tuo dizionario. Pensa a un numero preferito per ogni persona e memorizza ciascuno come un valore nel tuo dizionario. Stampa il nome di ogni persona e il suo numero preferito. Per ancora più divertimento, controlla alcuni amici e ottieni alcuni dati reali per il tuo programma.'''

numeri_preferiti:dict[str, int] = {"Stefano":23, "Marco":15, "Lorenzo":28, "Carlo":89, "Luca":2}

for nome, numero in numeri_preferiti.items():
    print(f"{nome}: {numero}")