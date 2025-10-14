# calcola il tempo di utilizzo di una funzione, calcola l'intervallo

from utility.timer import cronometro

# Metodo 1 per richiamare il decoratore
def ciao():
    print("Ciao")
def hello():
    print("Hello")
ciao = cronometro(ciao)
hello = cronometro(hello)

ciao()
hello()

# Metodo 2 per richiamare il decoratore
@cronometro
def lorenzo(nome, cognome):
    print("Lorenzo", "Anzivino")

lorenzo('nome', 'cognome')