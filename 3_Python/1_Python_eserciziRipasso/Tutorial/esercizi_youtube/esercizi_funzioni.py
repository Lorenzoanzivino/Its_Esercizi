# Es 1 - Da una lista restituisco una lista di tuple con Elemento della lista e la sua posizione dell'indice
def daLista_aTupla(lista:list) -> list[tuple]:
    risultato = []
    for i in range(len(lista)):
        risultato.append((lista[i], i))
    return risultato
print(daLista_aTupla([4,5,6,7]))


# Es 2 - Inserisci le stringhe di una lista in un dizionario come chiave, e inserire come valore il numero di volte in cui si ripete la parola 
def daLista_aDizionario(lista2:list) -> dict:
    dizionario:dict = {}
    for elemento in lista2:
        if elemento not in dizionario:
            dizionario[elemento] = 1
        else:
            dizionario[elemento] += 1
    return dizionario
print(daLista_aDizionario(["ciao", "mondo", "ciao", "mondo", "mondo"]))


# Es 3 - restituire il numero di numeri pari in una lista
def quantiPari(lista3:list) -> int:
    count = 0
    for num in lista3:
        if num % 2 == 0:
            count += 1
    return count

print(quantiPari([1,2,3,4,5]))


# Es 4 - conta quanti caratteri a mia scelta ci sono in una stringa
def contaCaratteri(stringa:str, carattere:str) -> int:
    count = 0
    for char in stringa:
        if carattere == char:
            count +=1
    return count
print(contaCaratteri("ciao", "c"))


# Es 5 - Restituisci una lista con soli numeri divisibili per il divisore
def divisibiliPerTre(lista4:list[int], divisore:int) -> list:
    nuova_lista:list = []
    for num2 in lista4:
        if num2 % divisore == 0:
            nuova_lista.append(num2)
    return nuova_lista

print(divisibiliPerTre([1,2,3,4,5,6,7,8,9,10], 3))