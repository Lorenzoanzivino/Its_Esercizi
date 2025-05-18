'''Scrivi una funzione print-numbers(), che prende come argomento un elenco di numeri.
Usando un loop, stampa ogni numero uno per uno.'''

numeri:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_numbers(numeri):
    for i in numeri:
        print(i)

# Non metto il PRINT perche non ho il return
print(numeri)