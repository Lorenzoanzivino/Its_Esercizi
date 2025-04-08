'''Scrivere in Python una funzione recursivePower che calcola la potenza di un numero 
utilizzando la ricorsione. La funzione deve ricevere due parametri in input:

    base: il numero da elevare a potenza.
    exponent: l’esponente a cui elevare la base.

Utilizzare, poi, la funzione per calcolare:

    3⁴, ovvero 3 elevato alla potenza di 4. 
    43 , ovvero 4 elevato alla potenza di 3.
    25, ovvero 2 elevato alla potenza di 5. 
    52, ovvero 5 elevato alla potenza di 2.
'''

def recursivePower(base:int,esponente:int):
    if esponente==0:
        return 1
    else:
        return base*recursivePower(base,esponente - 1)
    
# 3⁴, ovvero 3 elevato alla potenza di 4.
risultato=recursivePower(3,4)
print(risultato)
# 4 elevato alla potenza di 3
risultato1=recursivePower(4,3)
print(risultato1)
# 2 elevato alla potenza di 5.
risultato2= recursivePower(2,5)
print(risultato2)
# 5 elevato alla potenza di 2.
risultato3= recursivePower(5,2)
print(risultato3)

print("------------------------------------------")


# CAPIRE COSA DECREMENTA -> in questo caso decrementa l'esponente
'''
3^4 = 3 * 3^3 =
    = 3 * (3 * 3^2) =
    = 3* (3 * (3 * 3^1)) =
    = 3 * (3 * (3 * (3 * 3^0)) =

    cosa rimane fisso?
    cosa cambia?
    dove e quando mi devo fermare?
'''

def potenza_ricorsiva(base:int, esponente:int) -> int:

    if esponente == 0:
        return 1
    
    elif base == 0:
        return 0
    
    else:
        return int(base * potenza_ricorsiva(base, esponente - 1))
    
# 3⁴, ovvero 3 elevato alla potenza di 4.
risultato=potenza_ricorsiva(3,4)
print(f"3^4: {risultato}")
# 4 elevato alla potenza di 3
risultato1=potenza_ricorsiva(4,3)
print(f"4^3: {risultato1}")
# 2 elevato alla potenza di 5.
risultato2= potenza_ricorsiva(2,5)
print(f"2^5: {risultato2}")
# 5 elevato alla potenza di 2.
risultato3= potenza_ricorsiva(5,2)
print(f"5^2: {risultato3}")
    
