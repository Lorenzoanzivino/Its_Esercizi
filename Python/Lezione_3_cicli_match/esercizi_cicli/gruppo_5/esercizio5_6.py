'''5-6. Fasi della vita: scrivi una catena if-elif-else che determini la fase della vita di una persona. Imposta un valore per la variabile età, quindi:
• Se la persona ha meno di 2 anni, stampa un messaggio che la persona è un neonato.
• Se la persona ha almeno 2 anni ma meno di 4, stampa un messaggio che la persona è un bambino.
• Se la persona ha almeno 4 anni ma meno di 13, stampa un messaggio che la persona è un bambino.
• Se la persona ha almeno 13 anni ma meno di 20, stampa un messaggio che la persona è un adolescente.
• Se la persona ha almeno 20 anni ma meno di 65, stampa un messaggio che la persona è un adulto.
• Se la persona ha 65 anni o più, stampa un messaggio che la persona è un anziano.'''

eta:int = int(input("Scrivi l'età della persona: da 1 a 100: "))

if eta < 2:
    print("La persona è un neonato.")
elif eta == 2 and eta < 4:
    print("La persona è un bambino.")
elif eta == 4 and eta < 13:
    print("La persona è un bambino.")
elif eta == 13 and eta < 20:
    print("La persona è un adolescente.")
elif eta == 20 and eta < 65:
    print("La persona è un adulto.")
else:
    print("La persona è un anziano")