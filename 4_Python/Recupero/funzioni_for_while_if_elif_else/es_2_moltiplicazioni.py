'''2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold'''

def moltiplicazione(lista:list[int], threshold:int = 5) -> int:
    prodotto = 1

    for numero in lista:
        if numero < threshold:
            prodotto *= numero
    
    return prodotto

numeri:list = [1, 4, 8, 2, 3, 6, 5, 9]
print(moltiplicazione(numeri, 7))