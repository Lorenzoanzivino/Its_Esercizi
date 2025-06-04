'''2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''

def positivo_negativo(lista: list[int|float]) -> dict:
    dizionario:dict = {
        "positivi": [],
        "negativi": []
    }

    for numero in lista:
        if numero >= 0:
            dizionario["positivi"].append(numero)
        else:
            dizionario["negativi"].append(numero)

    return dizionario

numeri = [5, -3, 0, 12, -7, 8, -1, -19.5, 3.2]
risultato = positivo_negativo(numeri)
print(risultato)


def positivo_negativo2(lista: list[int|float]) -> dict:
    dizionario1: dict[str, list] = {}

    for numero in lista:
        if numero >= 0:
            if "positivi" not in dizionario1:
                dizionario1["positivi"] = []
            dizionario1["positivi"].append(numero)
        else:
            if "negativi" not in dizionario1:
                dizionario1["negativi"] = []
            dizionario1["negativi"].append(numero)

    return dizionario1

numeri2 = [5, -3, 0, 12, -7, 8, -1, -19.5, 3.2]
risultato1 = positivo_negativo2(numeri2)
print(risultato1)
