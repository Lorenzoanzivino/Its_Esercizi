'''Scrivere una funzione check-each(), che prende come argomento un elenco di numeri.
Usando un loop for, iterare attraverso l'elenco.
Per ogni numero, stampa "più grande" se è più grande di 5, "più piccolo" se è più piccolo di 5 e "uguale" se è uguale a 5.'''

numeri:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_numbers(numeri):
    for i in numeri:
        if i < 5:
            print(f"{i} è più piccolo di 5")
        elif i == 5:
            print(f"{i} è uguale a 5")
        else:
            print(f"{i} è più grande di 5")

# Non metto il PRINT perche non ho il return
(print_numbers(numeri))