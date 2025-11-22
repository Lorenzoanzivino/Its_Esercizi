vendite = {
    "gennaio": 1000,
    "febbraio": 1200,
    "marzo": 900
}

# Somma totale
somma = 0
for mese, prezzo in vendite.items():
    somma += prezzo
print("Somma totale vendite:", somma)

# Trova il mese con le vendite massime
mese_max = None
vendita_max = 0

for mese, prezzo in vendite.items():
    if prezzo > vendita_max:
        vendita_max = prezzo
        mese_max = mese

print("Mese con più vendite:", mese_max)
print("Valore massimo:", vendita_max)
