'''4-11.
Le mie pizze, le tue pizze: inizia con il tuo programma dall'esercizio 4-1. Crea una copia dell'elenco delle pizze e chiamalo friend_pizzas. Quindi, fai quanto segue:
• Aggiungi una nuova pizza all'elenco originale.
• Aggiungi una pizza diversa all'elenco friend_pizzas.
• Dimostra di avere due elenchi separati. Stampa il messaggio Le mie pizze preferite sono:, quindi usa un ciclo for per stampare il primo elenco. Stampa il messaggio Le pizze preferite del mio amico sono:, quindi usa un ciclo for per stampare il secondo elenco. Assicurati che ogni nuova pizza sia archiviata nell'elenco appropriato.
'''
pizze_preferite:list[str] = ["Margherita", "Marinara", "Diavola", "Boscaiola"]
friend_pizzas:list[str] = ["Margherita", "Marinara", "Diavola", "Ortolana"]

print("Le mie pizze preferite sono: ")
for pizza in pizze_preferite:
    print(pizza)
    
print("Le pizze preferite del mio amico sono: ")
for pizza in pizze_preferite:
    print(pizza)

