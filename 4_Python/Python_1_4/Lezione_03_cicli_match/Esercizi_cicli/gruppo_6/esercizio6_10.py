'''6-10. Numeri preferiti: Modifica il tuo programma dall'esercizio 6-2 in modo che ogni persona possa avere più di un numero preferito. Quindi stampa il nome di ogni persona insieme ai suoi numeri preferiti.'''

numeri:list[str, int] = {"Marcel": (73, 21), "Stefano": (6, 9), "Lorenzo": (23, 32), "Leandro": (11, 99), "Valentina": (16, 61)}

for name, number in numeri.items():
    print(f"{name}: {number}")