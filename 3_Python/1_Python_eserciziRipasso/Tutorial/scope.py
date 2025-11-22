# La disponibilità della variabile nel codice
# Variabili dentro e fuori le funzioni
# le variabili dentro le funzioni non possono essere richiamate fuori solo dal print perchè vive dentro la funzione.

# RETURN permette di portare fuori le variabili

# SCOPE LOCALE
def funzione():
    x = 400
    def sottofunzione():
        print(x)
    return sottofunzione()

funzione()