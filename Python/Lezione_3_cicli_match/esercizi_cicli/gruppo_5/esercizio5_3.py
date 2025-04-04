'''5-3.
Colori alieni n. 1: immagina che un alieno sia stato appena abbattuto in un gioco. Crea una variabile chiamata alien_color e assegnale un valore di "verde", "giallo" o "rosso".
• Scrivi un'istruzione if per testare se il colore dell'alieno è verde. Se lo è, stampa un messaggio che il giocatore ha appena guadagnato 5 punti.
• Scrivi una versione di questo programma che superi il test if e un'altra che fallisca. (La versione che fallisce non avrà alcun output.)'''


#colore Input per casualità
alien_color:str = input("Inserisci un colore tra verde, giallo e rosso: ")

if alien_color == "verde":
    print("Il giocatore ha guadagnato 5 punti")
