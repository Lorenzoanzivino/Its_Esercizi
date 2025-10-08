
# Non ordinato, modificabile, non permette duplicati

# Perfetto per collezioni uniche e operazioni insiemistiche (unione, intersezione, ecc.).

# Es: my_set = {1, 2, 3}


x:set = {"milano", "roma", "napoli"}

for citta in x:
    print(citta)


# Aggiungo in ordine casuale elementi con ADD 
x.add("venezia")
print(x)

# Aggiungo in ordine casuale tuytti gli elementi di y con UPDATE
y = ("pomezia", "ardea")
x.update(y)
print(x)

z = x.union(y)
print(z) # Crea un nuovo SET con entrambi i set


# UNION() e UPDATE() elimina i duplicati
