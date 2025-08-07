
# Non ordinato (fino a Python 3.6), modificabile, mappa chiavi uniche a valori

# Si usa per rappresentare strutture a coppie chiave-valore.

# Es: my_dict = {'a': 1, 'b': 2}


persona:dict = {
    "nome" : "Lorenzo",
    "cognome" : "Anzivino",
    "età" : 28
}
print(persona)
print(persona.get("nome"))

# stampo le chiavi
x = persona.keys()
print(x)

# stampo i valori
y = persona.values()
print(y)

#stampo tutto chiave e valore
z = persona.items()
print(z)

# modifico la chiave nome con un altro nome
persona["nome"] = "Marco"
print(persona)

# modifico la chiave con un altro nome
persona.update({"nome":"Anna"})
print(persona)

# Aggiungo chiave valore nuovo che non esiste
persona["colore"] = "blue"
print(persona)


persona_nuova:dict = {
    "nome" : "Lorenzo",
    "cognome" : "Anzivino",
    "età" : 28,
    "indirizzo" : {
        "citta" : "pomezia",
        "cap" : "00071",
        "civico" : 45
    }
}


for x in persona_nuova.items():
    print(f"\nDati: {persona}")