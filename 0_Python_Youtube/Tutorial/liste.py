
# Ordinata, modificabile (mutable), permette duplicati

# Si usa quando ti serve una sequenza ordinata di elementi, anche uguali.

# Es: my_list = [1, 2, 3, 2]

x:list = ["milano", "roma", "napoli"]

y:list[str, int, bool] = ["ciao", 123, False]

z:list = list(("milano", "roma", "napoli"))     # Caso Particolare, utilizza Il COSTRUTTORE LIST

x.append("Pomezia")                             # Aggiungo Pomezia alla fine della lista
x.extend(y)                                     # Aggiunge alla fine della lista X tutta la lista Y
x.remove(False)                                 # Rimuove elemento scelto

print(x)                                        # Stampo l'intera lista
print(x[0])                                     # stampo il primo elemento "milano"
print(type(x))                                  # mi stampa il tipo - in questo caso LISTA    

# Riprendi gli elementi solo della lista Y
for element in y:
    # se sono presenti dentro X
    if element in x:
        # eliminali
        x.remove(element)

# Per ogni elemento di X
for citta in x:
    # Stampa gli elementi
    print(citta)

x.clear()                                       # Mantiene la lista x ma la svuota
print(x)

listaCitta:list = ["Pomezia", "Ardea", "roma"] 
[print(citta) for citta in listaCitta]          # List comprehension


listaCitta.sort()                               # Ordina elementi della lista in ordine alfabetico
listaCitta.sort(reverse=True)                   # Ordina elementi della lista in ordine inverso
print(listaCitta)

listaCopiata:list = listaCitta.copy()
print(f"\nLista originale: {listaCitta}")
print(f"lista copiata: {listaCopiata}")