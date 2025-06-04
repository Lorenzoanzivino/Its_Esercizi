'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali'''


def prodotti(dizionario_1: dict[str, float]) -> dict[str, float]:
    dizionario_2: dict[str, float] = {}

    for prodotto, prezzo in dizionario_1.items():
        if prezzo < 50:
            dizionario_2[prodotto] = round(prezzo * 1.10, 2)
        else:
            dizionario_2[prodotto] = prezzo

    return dizionario_2

# Test
prodotti_input = {
    "penna": 20.0,
    "quaderno": 55.0,
    "matita": 10.5,
    "zaino": 100.0,
    "gomma": 3.25
}

print(prodotti(prodotti_input))
