from datetime import date
from classi import *

# Crea impiegati
alice = Impiegato("Alice", "Rossi", date(1990, 5, 12), 30000.0)
bob = Impiegato("Bob", "Verdi", date(1988, 3, 22), 32000.0)

# Crea progetto
pegaso = Progetto("Pegaso", 100000.0)

# Aggiunge progetto ad Alice
alice.add_progetto(pegaso)

# Aggiunge progetto a Bob
bob.add_progetto(pegaso)

# Stampa risultati
print(alice)
print(bob)
print(pegaso)
