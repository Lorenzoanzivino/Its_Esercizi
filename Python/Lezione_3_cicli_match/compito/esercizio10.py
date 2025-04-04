'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.
Il programma deve:
• acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
• calcolare e visualizzare la somma di tutti i numeri pari inseriti;
• calcolare e visualizzare la media di tutti i numeri dispari inseriti;
• determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
• se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0

Output:
Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''

sommaP:int = 0
sommaD:float = 0
media:float = 0
cont_numeri:int = 0
numeri:list = []

while True:
    numero:int = int(input("Inserisci un numero intero (0 per terminare): "))
    if numero == 0:
        break
    elif numero < 0:
        print("Errore, devi inserire un numero intero")
    else:
        numeri.append(numero)
        if numero > 0 and numero % 2 == 0:
            sommaP += numero
        else:
            cont_numeri += 1
            sommaD += numero
            media = sommaD / cont_numeri
            
# Stampa dei risultati output
print(f"I numeri scelti sono: {numeri}")
print(f"La somma dei numeri pari: {sommaP}")
print(f"La media dei numeri dispari: {media:.2f}")

#Trova il numero più frequente
frequenze:dict[int] = {}  

#Calcolare la frequenza di ogni numero della lista
for num in numeri:
    if num in frequenze:
        frequenze[num] += 1
    else:
        frequenze[num] = 1

#trovo i numeri con la frequenza più alta
max_frequenza = max(frequenze.values())
numeri_frequenti = [num for num, freq in frequenze.items() if freq == max_frequenza]

#a parità di ripetizioni, prendo il numero più grande
numero_piu_frequente = max(numeri_frequenti)
print(f"Il numero più frequente è: {numero_piu_frequente} ({max_frequenza} volte)")