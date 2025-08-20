'''10 Esercizi pratici

1 Scrivi un programma che prende in input un numero e stampa se è pari o dispari.

2 Data la lista [3, 7, 2, 9, 4], crea una nuova lista con solo i numeri maggiori di 4.

3 Scrivi una funzione fattoriale(n) che calcola il fattoriale di un numero usando un ciclo for.

4 Scrivi una classe Studente con attributi nome, cognome e voti (lista). Aggiungi un metodo media() che calcola la media dei voti.

5 Scrivi una funzione lambda che prende un numero e restituisce il suo cubo.

6 Crea un dizionario rubrica con 3 contatti, dove la chiave è il nome e il valore è il numero di telefono. Poi stampa tutti i contatti in formato Nome: Numero.

7 Scrivi un programma che legge un file numeri.txt (un numero per riga) e stampa la somma totale dei numeri.

8 Scrivi un programma che gestisce l’errore di divisione per zero usando try/except.

9 Usa il modulo random per creare una lista di 5 numeri casuali tra 1 e 50.

10 Scrivi un programma che stampa la data e l’ora corrente in formato dd-mm-yyyy hh:mm:ss.'''

#1
print("Esercizio 1")
#n:int = int(input("Inserisci un numero: ")) #commento per non inserire sempre un numero
n = 4
if n % 2 == 0:
    print(f"{n} è Pari")
else:
    print(f"{n} è Dispari")

#2
print("\nEsercizio 2")
lista:list = [3, 7, 2, 9, 4]
nuovaLista:list=[]
for n in lista:
    if n > 4:
        nuovaLista.append(n)
print(nuovaLista)

#3
print("\nEsercizio 3")
def fattoriale(n: int) -> int:
    if n < 0:
        raise ValueError("Errore: il numero deve essere >= 0")
    risultato = 1
    for i in range(1, n + 1):
        risultato *= i
    return risultato
print(fattoriale(5))

#4
#Scrivi una classe Studente con attributi nome, cognome e voti (lista). Aggiungi un metodo media() che calcola la media dei voti.
print("\nEsercizio 4")
class Studente:
    def __init__(self, nome: str, cognome: str, voti: list):
        self.nome = nome
        self.cognome = cognome
        self.voti = voti

    def mediaVoti(self) -> float:
        if not self.voti:  # se la lista è vuota
            return 0
        somma = 0
        cont = 0
        for voto in self.voti:
            somma += voto
            cont += 1
        media = somma / cont
        print(media)
        return media

if __name__ == "__main__":
    studente = Studente("Lorenzo", "Anzivino", [3, 4, 5, 3])
    studente.mediaVoti()

# 5
print("\nEsercizio 5")
'''5 Scrivi una funzione lambda che prende un numero e restituisce il suo cubo.'''
from typing import Callable

quadrato:Callable [[int], int] = lambda x: x ** 3
print(quadrato(4))

# 6
print("\nEsercizio 6")
'''6 Crea un dizionario rubrica con 3 contatti, dove la chiave è il nome e il valore è il numero di telefono. Poi stampa tutti i contatti in formato Nome: Numero.'''
dizionario:dict = {
    "Lorenzo":"3774738083",
    "Stefano":"3475622532",
    "Simona":"7584722334"
}

for nome, numero in dizionario.items():
    print(f"{nome}: {numero}")

# 7
print("\nEsercizio 7")
'''7 Scrivi un programma che legge un file numeri.txt (un numero per riga) e stampa la somma totale dei numeri.'''

# 8
print("\nEsercizio 8")
'''8 Scrivi un programma che gestisce l’errore di divisione per zero usando try/except.'''

# 9
print("\nEsercizio 9")
'''9 Usa il modulo random per creare una lista di 5 numeri casuali tra 1 e 50.'''
import random
lista = []
while len(lista) < 5:
    n = random.randint(1, 50)
    if n not in lista:
        lista.append(n)
print(lista)

# 10
print("\nEsercizio 10")
'''10 Scrivi un programma che stampa la data e l’ora corrente in formato dd-mm-yyyy hh:mm:ss.'''
from datetime import datetime

# ottieni data e ora corrente
adesso = datetime.now()

# stampa nel formato dd-mm-yyyy hh:mm:ss
print(adesso.strftime("%d-%m-%Y %H:%M:%S"))