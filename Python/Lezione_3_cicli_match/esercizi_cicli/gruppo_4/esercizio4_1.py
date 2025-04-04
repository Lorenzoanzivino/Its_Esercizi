'''Esercizio 4-1
Pensa ad almeno tre tipi di pizza preferita. Memorizza i nomi di queste pizze in un elenco, quindi usa un ciclo for per stampare il nome di ogni pizza.
• Modifica il ciclo for per stampare una frase usando il nome della pizza, invece di stampare solo il nome della pizza. Per ogni pizza, dovresti avere una riga di output contenente una semplice istruzione come I like pepperoni pizza.
• Aggiungi una riga alla fine del programma, al di fuori del ciclo for, che indichi quanto ti piace la pizza. L'output dovrebbe essere composto da tre o più righe sui tipi di pizza che ti piacciono e poi una frase aggiuntiva, come I really love pizza!'''

pizze_preferite:list[str] = ["Margherita", "Marinara", "Diavola"]
for pizza in pizze_preferite:
    print(pizza)
    print(f"La mia pizza preferita è {pizza}")

print("Mi piace veramente la pizza!")