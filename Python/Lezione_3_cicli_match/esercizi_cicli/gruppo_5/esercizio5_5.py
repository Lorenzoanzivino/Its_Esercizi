'''5-5. Colori alieni n. 3: trasforma la tua catena if-else dell'esercizio 5-4 in una catena if-elif-else.
• Se l'alieno è verde, stampa un messaggio che il giocatore ha guadagnato 5 punti.
• Se l'alieno è giallo, stampa un messaggio che il giocatore ha guadagnato 10 punti.
• Se l'alieno è rosso, stampa un messaggio che il giocatore ha guadagnato 15 punti.
• Scrivi tre versioni di questo programma, assicurandoti che ogni messaggio sia stampato per l'alieno del colore appropriato.'''

#colore Input per casualità
alien_color:str = input("Inserisci un colore tra verde, giallo e rosso: ")

if alien_color == "verde":
    print("Il giocatore ha guadagnato 5 punti")
elif alien_color == "giallo":
    print("Il giocatore ha guadagnato 10 punti")
elif alien_color == "rosso":
    print("il giocatore ha guadagnato 15 punti")
else:
    print()

