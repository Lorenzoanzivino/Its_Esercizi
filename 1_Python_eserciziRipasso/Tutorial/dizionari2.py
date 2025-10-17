mio_dict:dict[str,int, list[int]] = {"mia_chiave" : "mio_valore", "age" : 29, 3.14 : "pi greco", "primi" : [2,3,5,7]}

# Aggiornare il valore di una chiave
mio_dict["mia_chiave"] = "mio_valore_aggiornato"

# stampare valore della chiave
print(mio_dict["mia_chiave"]) 

# Aggiungere chiave/valore nuovi
mio_dict["nuova_chiave"] = "nuovo valore"
print(mio_dict)

# verificare se una chiave è presente nel dizionario
print("chiave 99" in mio_dict)    # Flase
print("chiave 99" not in mio_dict)    # True
print("age" in mio_dict)    # True

'''-----------------------------------------------------------------------------------------'''

# metodi per i dizionari - 
    # .keys() = (Lista) di chiavi
        # list(.keys()) = Vera Lista di chiavi
    # .values() = (Lista) di valori
        # list(.values()) = Vera Lista di valori
    # .items() = (lista) chiavi/valori
        # list(.items()) = Vera Lista di chiavi/valori

ita_eng:dict = {"ciao" : "hello", "arrivederci" : "goodbye", "uova" : "eggs", "gatto" : "cat", "arancia" : "orange"}
print("\nChiavi: ")
print(ita_eng.keys())
print("\nValori: ")
print(ita_eng.values())
print("\nChiavi/Valori: ")
print(ita_eng.items())
print("\nListe: ")
print(list(ita_eng.keys()))
print(list(ita_eng.values()))
print(list(ita_eng.items()))

print()   # divisorio
# Ciclo For
for chiave in ita_eng.keys():
    print(chiave)