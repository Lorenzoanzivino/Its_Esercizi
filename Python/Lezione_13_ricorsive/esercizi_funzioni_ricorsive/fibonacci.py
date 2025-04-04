def fibonacci(n:int) -> int:

    # se n è negativo o uguale a 0
    if n <= 0:
        return 0
    
    # se n è uguale a 1
    elif n == 1:
        return 1
    
    # altrimenti usare la formula di fibonacci
    else:
        return int(fibonacci(n-1) + fibonacci(n-2)) 
    
    # possiamo anche creare una variabile: 
    # fibonacci = (fibonacci(n-1) + fibonacci(n-2)) direttamente dopo else e poi richiamare solo fibonacci nel return
    # else:
    #     fibonacci = int(fibonacci(n-1) + fibonacci(n-2))
    #     return fibonacci


    
print(fibonacci(6))