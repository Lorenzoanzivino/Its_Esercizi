'''Es 6 Scrivere un programma per creare una funzione ricorsiva per calcolare la somma dei numeri da 0 a 10. '''

# Senza Ciclo
def ricorsiva(a: int) -> int:
        return (a*(a+1))/2


result = ricorsiva(0)
print(result)


# Ciclo While
def somma_con_ciclo_while(a: int) -> int:
    somma = 0
    i = 0
    while i <= a:
        somma += i
        i += 1
    return somma

result = somma_con_ciclo_while(10)
print(result)


# Ciclo For
def sum(a:int):
    mysum=0
    for i in range(a+1):
        mysum+=i
        print(mysum)

    return mysum

print(sum(10))

