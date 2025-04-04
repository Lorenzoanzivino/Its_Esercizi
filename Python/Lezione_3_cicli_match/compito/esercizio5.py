'''Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.
Scrivere un programma che:
• Acquisisca in input un valore N (numero di euro disponibili).
• Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
• Mostri quanti buoni sconto avanzano al termine dell'acquisto.

Esempio:
Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati.'''

#variabili inizializzate a 0 fuori dal ciclo
barrette = 0
buono_sconto = 0
#cliclo While
while True:
    euro_disponibili:int = int(input("Quanti soldi hai a disposizione? "))
    #se i soldi scendono a 0 termina
    if euro_disponibili == 0:
        print("Hai terminato i soldi")
        break
    #variabili inizializzate nel ciclo che si aggiornano
    barrette = euro_disponibili
    buono_sconto = euro_disponibili
    #per ogni 6 buoni sconto ho una barretta in più e aggiorno il numero di barrette
    while buono_sconto >= 6:
        barrette_aggiuntiva = buono_sconto // 6
        barrette += barrette_aggiuntiva
        buono_sconto %= 6 
    #stampo il numero di barrette e il numero di buoni rimasti
    print(f"Il numero totale di barrette prese è: {barrette}")
    print(f"Buoni sconto avanzanti sono: {buono_sconto}")