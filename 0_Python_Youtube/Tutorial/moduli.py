# Moduli: libreria (un file contenente altre funzioni/variabili già esistenti)

import miomodulo as em    # em -> alias per chiamare il modulo in modo più veloce con poche lettere
import platform
import math


x = em.persona1["nome"]
y = em.persona1["cognome"]
em.saluta(x)
em.saluta(y)


# platform
x = platform.system()
print(x)


print(math.floor(2.90))
print(dir(math))
