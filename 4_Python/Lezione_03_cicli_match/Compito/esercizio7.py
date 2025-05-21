'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...
Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

#inizializzo lista a e b
lista_a:list[int] = [32, 76, 59, 94, 45]
lista_b:list[int] = [88, 36, 118, 67, 54]

#inizializzo lista c vuota
lista_c:list[int] = []

#variabile somma vuota
somma:int = 0

#ciclo for per scorrere le liste
for i in range(len(lista_a)):
    #somma dall'indice[0] + indice della lunghezza della lista -1 - indice per prendere l'ultimo.
    somma = lista_a[i] + lista_b[len(lista_a)-1 -i]
    #il risultato lo aggiungo (.append()) nella lista_c
    lista_c.append(somma)

print(f"I numeri della lista_a sono: {lista_a}")
print(f"I numeri della lista_b sono: {lista_b}")
print(f"I numeri della lista_c sono: {lista_c}")