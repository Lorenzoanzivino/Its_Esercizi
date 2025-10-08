'''1. Somma dei numeri pari

Scrivi un programma che prende una lista di numeri interi e stampa la somma di tutti i numeri pari presenti nella lista.

# Esempio input: [1, 2, 3, 4, 5, 6]
# Output: 12'''

lista_numeri:list = [1, 2, 3, 4, 5, 6]
somma = 0

for numeri in lista_numeri:
    if numeri % 2 == 0:
        somma += numeri

print(somma)