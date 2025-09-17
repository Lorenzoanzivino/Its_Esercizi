''' 1-1.
    Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:
    Memorizzare un numero in virgola mobile nella variabile x.
    Calcolare 1.0/x memorizzare il risultato nella variabile y.
    Visualizzare il valore di x, y e il prodotto tra x e y.
    Sottrarre x dal prodotto tra x e y e mostrarne il risultato.'''

x: float = 2.3
y: float = 1.0/x
Prod: float = x*y

print(x, f"{y:.3f}")
print(Prod)
print(f"{Prod-x:.3f}")