# metafora per le funzioni

# pseudocodice
'''fatti_la_pasta:
    prendi la pentola
    metti l'aqua
    metti la pasta
    prepara il sugo
    impiatta
'''

def fai_la_pasta(tipo_pasta:str = "fettuccine", metti_sugo:bool = False):
    print("\nMetti l'acqua")
    print("Fai bollire")
    print(f"metti: {tipo_pasta}")
    if metti_sugo:
        print("prepara il sugo")
    else:
        print("Pasta in bianco")

fai_la_pasta("fusilli", True)
fai_la_pasta("spaghetti")
fai_la_pasta(metti_sugo=True)
fai_la_pasta()


def fai_somma(n1, n2):
    somma = n1 + n2
    return somma

x = fai_somma(2, 3)
print(x)

print(fai_somma(2, 3))