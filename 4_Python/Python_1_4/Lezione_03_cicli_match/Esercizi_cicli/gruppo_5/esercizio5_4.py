'''5-4. Colori alieni n. 2: scegli un colore per un alieno come hai fatto nell'esercizio 5-3 e scrivi una catena if-else.
• Se il colore dell'alieno è verde, stampa un'affermazione che il giocatore ha appena guadagnato 5 punti per aver sparato all'alieno.
• Se il colore dell'alieno non è verde, stampa un'affermazione che il giocatore ha appena guadagnato 10 punti.
• Scrivi una versione di questo programma che esegue il blocco if e un'altra che esegue il blocco else.'''

#colore Input per casualità
alien_color:str = input("Inserisci un colore tra verde, giallo e rosso: ")

if alien_color == "verde":
    print("Il giocatore ha guadagnato 5 punti per aver sparato all'alieno")
else:
    print("Il giocatore ha guadagnato 10 punti")



