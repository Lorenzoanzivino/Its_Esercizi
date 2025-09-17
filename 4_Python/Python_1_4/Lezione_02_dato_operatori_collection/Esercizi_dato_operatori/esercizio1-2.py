''' 1-2
    Si scriva un programma che dimostri le funzionalità dell'operatore % effettuando le seguenti attività:
    - Memorizzare un numero in virgola mobile nella variabile x.
    - Calcolare x%2.0 e memorizzare il risultato nella variabile y.
    - Visualizzare in maniera distinta x e y.
    Si esegua il programma con valori positivi e negativi di x. Che cosa cambia nel comportamento dell’applicazione
    quando i valori di x sono positivi o negativi?'''

x: float = 3.2
y: float = x%2.0

print (f"{x:.3f}")
print (f"{y:.3f}")

x: float = -3.2
y: float = x%2.0

print (f"{x:.3f}")
print (f"{y:.3f}")
