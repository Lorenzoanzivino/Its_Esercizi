'''5. Fattoriale ricorsivo

Scrivi una funzione ricorsiva che calcola il fattoriale di un numero intero positivo n.

# Es: factorial(5) → 120'''

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