# Ciclo WHILE -> Finchè la condizione è vera continua a ciclare, poi esci

i = 0
while i < 6:                    # è minore di 6? 
    print(i)                    # stampa i
    if i == 3:
        print("i è uguale a 3") # se i è uguale a 3 stampa anche i = 3
    i+=1                        # aumenta i di 1

else:
    print("finito")             # finito il ciclo stampa finito