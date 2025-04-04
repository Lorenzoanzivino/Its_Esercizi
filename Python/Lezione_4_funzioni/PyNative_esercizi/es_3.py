'''Es 3 Scrivere un programma per creare funzione calculation()In modo tale da poter accettare due variabili e calcolare l'addizione e la sottrazione. Inoltre, deve restituire sia l'addizione che la sottrazione in una singola chiamata di ritorno.'''

def calculation(a:int, b:int):
    result = (a+b), (a-b)
    return result

result = calculation(40, 10)
print(result)