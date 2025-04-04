'''4-10.
Slice: usando uno dei programmi che hai scritto in questo capitolo, aggiungi diverse righe alla fine del programma che facciano quanto segue:
• Stampa il messaggio I primi tre elementi nell'elenco sono:. Quindi usa uno slice per stampare i primi tre elementi dall'elenco di quel programma.
• Stampa il messaggio Tre elementi dal centro dell'elenco sono:. Quindi usa uno slice per stampare tre elementi dal centro dell'elenco.
• Stampa il messaggio Gli ultimi tre elementi nell'elenco sono:. Quindi usa uno slice per stampare gli ultimi tre elementi nell'elenco.'''

numeri:list[int] = []

for numero in range(1, 21):
    numeri.append(numero)
print(numeri) 

centro = len(numeri)//2 
print(f"I primi 3 elementi sono: {numeri[:3]}")
print(f"3 elementi dal centro sono: {numeri[centro-1:centro+2]}")
print(f"Gli ultimi 3 elementi sono: {numeri[-3:]}")