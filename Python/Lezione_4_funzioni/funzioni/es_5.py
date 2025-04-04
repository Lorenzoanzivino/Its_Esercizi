'''Scrivi una funzione add-one(). Ci vuole un numero intero come argomento. La funzione aggiunge 1 all'intero e la restituisce.
Scrivi un'altra funzione add-one-to-list(). Ci vuole una lista di numeri interi come argomento.
Definire una variabile new-list in questa funzione.
Usando un ciclo for, iterare attraverso l'elenco degli argomenti.
Utilizzando add-one(), compilare new-list con interi dall'elenco degli argomenti incrementati'''


def add_one(numero:int):
    numero += 1

    return numero

list:list = [1, 2, 3, 4, 5, 6, 7, 8]

#per scrivere una sequenza di numeri da a 

#list2:list = [i for i in range(1, 11)]

def add_one_to_list(list):
    new_list = []
    for numero in list:
        new_list.append(add_one(numero))

    return new_list

# Metto il PRINT perche non ho il return
print(add_one_to_list(list))