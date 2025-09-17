'''Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

n1 = int(input("Inserisci un numero intero n1: "))
n2 = int(input("Inserisci un numero intero n2: "))
#n1 deve essere minore di n2
if n1 > n2:
    n1, n2 = n2, n1
#Calcolo il prodotto tra i numeri compresi tra n1 e n2
prod = 1
for i in range(n1, n2):
    prod *= i

print(f"Il prodotto dei numeri tra {n1} e {n2} è: {prod}")