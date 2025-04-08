'''Esercizio 3.

Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.'''


''' se n = 1 o a 0 ci fermiamo'''

''' 5! = 5 * 4 * 3 * 2 * 1 
    5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1! = 5 * 4 * 3 * 2 * 1 = 120'''

def recursive_factorial(n:int):
    if n < 0:
        print("Error! Inserire numero positivo")
    elif n == 0 or n == 1:
        return 1
    else:
        return int(n * recursive_factorial(n -1))
    
risultato = recursive_factorial(5)
print(risultato)

print(f"5! = {recursive_factorial(5)}")
