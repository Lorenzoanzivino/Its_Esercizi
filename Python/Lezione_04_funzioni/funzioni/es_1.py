'''Scrivere un check_value(), che prende un numero come argomento.
Usando if / else, la funzione dovrebbe stampare se il numero è più grande, più piccolo o uguale a 5'''

n1:int = int(input("Inserisci un numero: "))

def check_value(n1:int):
    if n1 < 5:
        print(f"il numero {n1} è più piccolo")
    elif n1 == 5:
        print(f"il numero {n1} è uguale")
    else:
        print(f"Il numero {n1} è più grande")

# Non metto il PRINT perche non ho il return
check_value(n1)