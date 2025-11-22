'''Esercizio 3C-1.
Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:
- 10 → "Eccellente"
- 8-9 → "Molto buono"
- 6-7 → "Sufficiente"
- 4-5 → "Insufficiente"
- 1-3 → "Gravemente insufficiente"
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto: 5
Output: Insufficiente
- - - - - - - - - - -
Inserisci il voto: 11
Output: Voto non valido'''

#metodo 1
voto:int = int(input("Inserisci un voto: "))

match voto:
    case 10:
        print("Eccellente")
    case voto if voto >7 and voto < 10:
        print("Molto buono")
    case voto if voto >5 and voto < 8:
        print("Sufficiente")
    case voto if voto >3 and voto < 6:
        print("Insufficiente")
    case voto if voto >0 and voto < 4:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")
        
#metodo 2
voto:int = int(input("Inserisci un voto: "))

match voto:
    case 10:
        print("Eccellente")
    case (8|9):
        print("Molto buono")
    case (6|7):
        print("Sufficiente")
    case (4|5):
        print("Insufficiente")
    case (1|3):
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")