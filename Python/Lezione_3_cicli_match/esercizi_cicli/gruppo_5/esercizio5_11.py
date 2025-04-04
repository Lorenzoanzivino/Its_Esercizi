'''5-11. Numeri ordinali: i numeri ordinali indicano la loro posizione in un elenco, ad esempio 1° o 2°. La maggior parte dei numeri ordinali termina in th, eccetto 1, 2 e 3.
• Memorizza i numeri da 1 a 9 in un elenco.
• Esegui un ciclo nell'elenco.
• Utilizza una catena if-elif-else all'interno del ciclo per stampare la corretta terminazione ordinale per ogni numero. Il tuo output dovrebbe essere "1st 2nd 3rd 4th 5th 6th 7th 8th 9th" e ogni risultato dovrebbe essere su una riga separata.'''

numeri:list[str] = []

for n in range (1, 10):
    if n == 1:
        numeri.append(f"{n}st")
    elif n == 2:
        numeri.append(f"{n}nd")
    elif n == 3:
        numeri.append(f"{n}rd")
    else:
        numeri.append(f"{n}th")
print(f'{", ".join(numeri)}')

