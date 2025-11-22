'''Esercizio 1
Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.'''

def lista_numeri(lista:list = []) -> int:
    somma = 0

    for n in lista:
        somma += n
    return somma

print(f"somma: {lista_numeri([1, 2, 3, 4, 5])}")

'''Esercizio 2
Scrivi una funzione che prende una stringa e restituisce la stringa invertita.'''

def inverti_stringa(stringa:str) -> str:
    stringa_nuova:str = " "

    for char in stringa:
        stringa_nuova = char + stringa_nuova    # Prima char per poter invertire
    return stringa_nuova

print(inverti_stringa("ciao"))

'''Esercizio 3
Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.'''

def lista_parole(lista:list, lettera:str = "p") -> list :
    lista_nuova:list = []

    for parole in lista:
        if parole[0] == lettera:
            lista_nuova.append(parole)
        else:
            pass

    return lista_nuova

print(lista_parole(["ciao", "paolo", "pentola", "gatto"]))

'''Esercizio 4
Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.
'''

def lista_numeri_pari(lista:list) -> list:
    lista_pari:list = []

    for numero in lista:
        if numero % 2 == 0:
            lista_pari.append(numero)
        else:
            pass

    return lista_pari

print(lista_numeri_pari([1, 2, 3, 4, 5, 6, 8]))

'''Esercizio 5
Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.'''

'''Esercizio 6
Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.'''

'''Esercizio 7
Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.'''