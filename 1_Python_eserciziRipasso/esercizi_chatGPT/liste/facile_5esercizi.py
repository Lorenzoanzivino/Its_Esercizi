'''Somma elementi
Scrivi una funzione somma_lista(lista) che prende una lista di numeri e restituisce la somma di tutti gli elementi.
Esempio: [1, 2, 3] → 6.'''
def somma_lista(lista1:list) -> int:
    somma = 0
    for i in lista1:
        somma += i
    return somma
print(somma_lista([1,2,3,4,5]))

'''Trova il massimo
Scrivi una funzione massimo(lista) che prende una lista di numeri e restituisce l’elemento più grande.
Non usare max() per allenarti a fare il confronto manualmente.'''
def massimo(lista2:list) -> int:
    max_num = lista2[0]
    for num in lista2:
        if num > max_num:
            max_num = num
    return max_num
print(massimo([8, 89, 4, 2, 39, 5, 110, 83]))

'''Aggiungi elemento
Scrivi una funzione aggiungi_elemento(lista, elemento) che aggiunge l’elemento alla lista e restituisce la lista aggiornata.'''
def add_elemento(lista3:list, elemento:str) -> list:
    if elemento not in lista3:
        lista3.append(elemento)
        return lista3
    return "Elemento già presente"
print(add_elemento(["cane","gatto", "pesce"], "cane"))

'''Conta elementi
Scrivi una funzione conta_elementi(lista, x) che prende una lista e un elemento x e restituisce quante volte x compare nella lista.'''
def conta_elemento(lista4:list, x:int) -> int:
    count = 0
    for i in lista4:
        if i == x:
            count += 1
    return f"elemento {x} compare {count} volte"
print(conta_elemento([1,2,3,4,5,3,3,2], 3))

'''Inverti lista
Scrivi una funzione inverti_lista(lista) che restituisce la lista con gli elementi in ordine inverso.
Esempio: [1, 2, 3] → [3, 2, 1].'''
def inverti(lista5: list) -> list:
    lista_invertita = []

    # Scorri la lista al contrario
    for i in range(len(lista5) - 1, -1, -1):
        lista_invertita.append(lista5[i])

    return lista_invertita
print(inverti([1,2,3,4]))