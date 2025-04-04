'''
Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:
- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.
Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.
Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

Expected Output:
Digita il nome di un animale: cane
Output: cane appartiene alla categoria dei Mammiferi!
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
Digita il nome di un animale: coccodrillo
Output: coccodrillo appartiene alla categoria dei Rettili!
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
Digita il nome di un animale: pappagallo
Output: pappagallo appartiene alla categoria degli Uccelli!
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
Digita il nome di un animale: squalo
Output: squalo appartiene alla categoria dei Pesci!
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
Digita il nome di un animale: giraffa
Output: Non so dire in quale categoria classificare l'animale giraffa!
'''

animale:str = input("Digita il nome di un animale: ")

match animale:
    case ("cane"|"gatto"|"cavallo"|"elefante"|"leone"):
        print(f"{animale} appartiene alla categoria dei Mammiferi")
    case ("serpente"|"lucertola"|"tartaruga"|"coccodrillo"):
        print(f"{animale} appartiene alla categoria dei Rettili")
    case ("aquila"|"pappagallo"|"gufo"|"falco"):
        print(f"{animale} appartiene alla categoria degli Uccelli")
    case ("squalo"|"trota"|"salmone"|"carpa"):
        print(f"{animale} appartiene alla categoria dei Pesci")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}")