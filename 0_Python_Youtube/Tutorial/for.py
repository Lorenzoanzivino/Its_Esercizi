
lista_citta:list = ["roma", "milano", "napoli"]
stringa:str = "ciao"

for citta in lista_citta: # per ogmni elemento nella lista, stampa gli elementi
    print(citta)

for lettera in stringa: # per ogni lettera nella stringa, stampa le lettere
    print(lettera)

for x in range(6):
    print(x)
else:
    print("Ho finito")

print("Esco dai cicli")


for riga in range(3):
    for colonna in range(3):
        print(f"({riga} : {colonna})")