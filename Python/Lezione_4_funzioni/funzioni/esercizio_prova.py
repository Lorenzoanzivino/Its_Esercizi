'''Fare tre diverse somme, sotto indicate. Esempio per spiegare le Funzioni. Creo 3 somme con i cicli, ma per fare la stessa cosa posso usare 1 sola funzione e i pèarametri li cambio nei print()'''

# 1 Somma tra 1 e 10
sum:int = 0
for i in range(1, 11):
    sum += i
print("La somma tra 1 e 10 è:", sum)

# 2 Somma tra 20 e 37
sum:int = 0
for i in range(20, 38):
    sum += i
print("La somma tra 20 e 37 è:", sum)

# 3 Somma tra 35 e 49
sum:int = 0
for i in range(35, 50):
    sum += i
print("La somma tra 35 e 49 è:", sum)

'---------------------------------------------------------------------------------------------------------------'

# FUNZIONI: ripeto gli esercizi precedenti, usando le funzioni
def sumInRange(a:int, b:int):
# definire una somma
    result:int = 0
# calcolare la somma
    for i in range(a,b+1):
        result = result + i
# restituisce il valore di somma come output della funzione somma
    return result
# salvo la funzione in una variabile cosi da inserire nel print solo il nome della variabile
my_sum:int = sumInRange(1, 10)

# utilizzare la funzione sumInRange modificando direttamente solo i parametri
print(f"\nSum from 1 to 10 is {sumInRange(1, 10)}")
# oppure inserisco il nome della variabile dove ho salvato la funzione ma senza modificare i parametri
print(f"Sum from 1 to 10 is {my_sum}")

# utilizzare la funzione sumInRange per calcolare una somma di numeri da 20 to 37
print(f"Sum from 20 to 37 is {sumInRange(20, 37)}")
# utilizzare la funzione sumInRange per calcolare una somma di numeri da 35 to 49
print(f"Sum from 35 to 49 is {sumInRange(35, 49)}")

'---------------------------------------------------------------------------------------------------------------'

# Sottrazione con dati in input dati dall'utente
n1:int = int(input("\nInserisci un numero: "))
n2:int = int(input("Inserisci un numero: "))

def subtract(a:int, b:int) -> int: # -> int serve per far capire che il valore che ritorna è un intero
    # variabile che avrà l'operazione
    risultato:int = a - b
    # se il primo numero è minore, inverto i valori
    if a < b:
        risultato = b - a
    # ritorno della variabile come risultato
    return risultato
print(f"La sottrazione è: {subtract(n1, n2)}")

