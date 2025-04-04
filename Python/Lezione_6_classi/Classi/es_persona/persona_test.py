'''
# 1 Dal file "persona.py" importo la classe "Persona"
from persona import Persona

# 2 creo una persona "la = lorenzo anzivino"
la:Persona = Persona("Lorenzo", "Anzivino", 28)


# 3 richiamo la variabile della classe persona
#print(la)
#print(la.name, la.lastname, la.age)

# 4 richiamo la funzione displayData della classe persona per mostrare in output i dati relativi alla persona L.A

la.displayData()
'''
print("-----------------")

# 5 dal file persona2 importa la classe persona
from persona2 import Persona

la:Persona = Persona()

# 6 richiamo la funzione displayData della classe persona per mostrare in output le informazioni relative all'oggetto L.A
la.displayData()

# 7 usare metodi "Set" e "Get" per manipolare e cambiare i valori degli attributi

# 8 Modificare il nome della persona L.a
la.setName("Lorenzo")

print("-----------------")

la.displayData()

# 9 Modificare il cognome della persona L.a
la.setLastname("Anzivino")

# 10 Modificare l'età della persona L.a
la.setAge(28)

print("-----------------")

la.displayData()

print("-----------------")

# Print dei Get
print(la.getName(), la.getLastname(), la.getAge())