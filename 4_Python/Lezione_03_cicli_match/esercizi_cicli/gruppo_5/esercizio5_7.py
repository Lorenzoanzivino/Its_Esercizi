'''5-7. Frutto preferito: fai un elenco dei tuoi frutti preferiti, quindi scrivi una serie di istruzioni if ​​indipendenti che controllano determinati frutti nel tuo elenco. • Crea un elenco dei tuoi tre frutti preferiti e chiamalo frutta_preferita.

Scrivi cinque istruzioni if. Ognuna dovrebbe controllare se un certo tipo di frutto è presente nel tuo elenco. Se il frutto è presente nel tuo elenco, il blocco if dovrebbe stampare un'istruzione, come Ti piacciono molto le mele!'''

frutto_preferito:list[str] = ["mela", "banana", "arancia"]

if "mela" in frutto_preferito:
    print("Ti piacciono molto le mele")
if "banana" in frutto_preferito:
    print("Ti piacciono molto le banane")
if "arancia" in frutto_preferito:
    print("Ti piacciono molto le arance")
if "anguria" in frutto_preferito:
    print("Ti piacciono molto le angurie")
if "limone" in frutto_preferito:
    print("Ti piacciono molto i limoni")