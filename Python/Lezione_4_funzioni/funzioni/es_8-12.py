'''8-12. Panini: scrivi una funzione che accetta un elenco di oggetti che una persona desidera su un panino. La funzione dovrebbe avere un parametro che raccoglie tutti gli elementi forniti dalla chiamata di funzione e dovrebbe stampare un riepilogo del sandwich che viene ordinato. Chiamare la funzione tre volte, utilizzando ogni volta un numero diverso di argomenti.'''

# funzione senza parametri, la uso solo per raccolta di dati
def sandwich(*ingredienti) -> None:
    print(f"Gli ingredienti sono : {', '.join(ingredienti).title()}")

sandwich("pane", "carne")
sandwich("pane", "carne", "pomodoro")
sandwich("pane", "carne", "pomodoro", "formaggio")

