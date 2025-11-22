
# Ordinata, immutabile, permette duplicati

# Utile per dati costanti o usati come chiavi in un dizionario.

# Es: my_tuple = (1, 2, 3)

x:tuple = ("roma", "napoli")

y:tuple = ("milano", True, 123)

z:tuple = ("milano",)                       # La tupla con un solo valore vuole la VIRGOLA (,)

tupla = tuple(("ciao", "costruttore"))      # Creo la tupla con il costruttore TUPLE

print(type(x))
print(type(z))
print(tupla)

if "milano" in x:
    print("milano")
else: 
    print("Non esiste milano")


lista:list = ["roma", "pomezia"]
print(lista)
print(type(lista))

tupla:tuple = tuple(lista)
print(tupla)
print(type(tupla))

for i in range(len(tupla)):
    print(tupla[0])


tuplaCitta:tuple = ("roma", "milano", "udine", "roma")

x = tuplaCitta.count("roma")                # Conta quante volte appare "roma"
print(x)
