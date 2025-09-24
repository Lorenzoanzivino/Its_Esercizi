'''
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
'''

from quadrato import Quadrato
from rettangolo import Rettangolo
from triangolo import Triangolo


q = Quadrato(4)
print("Nome:", q.nome)
print("Area:", q.getArea())
print("Render del quadrato: ")
q.render()

print()

r = Rettangolo(8, 4)
print("Nome:", r.nome)
print("Area:", r.getArea())
print("Render del rettangolo: ")
r.render()

print()

t = Triangolo(4)
print("Nome:", t.nome)
print("Area:", t.getArea())
print("Render del Triangolo: ")
t.render()