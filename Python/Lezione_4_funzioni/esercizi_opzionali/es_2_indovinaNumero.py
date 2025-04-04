'''Gioco Indovina il Numero:
Crea una funzione che genera un numero casuale all'interno di un intervallo specificato dall'utente.
Chiedi all'utente di indovinare il numero entro un numero massimo di tentativi specificato.
Fornisci un feedback all'utente dopo ogni tentativo, indicando se il suo tentativo è troppo alto, troppo basso o corretto.
Termina il ciclo quando l'utente indovina il numero correttamente o raggiunge il numero massimo di tentativi.'''

import random

def indovina_il_numero():
    # Chiedi all'utente l'intervallo e il numero massimo di tentativi
    valore_minimo = int(input("Inserisci il valore minimo dell'intervallo: "))
    valore_massimo = int(input("Inserisci il valore massimo dell'intervallo: "))
    tentativi = int(input("Inserisci il numero massimo di tentativi: "))
    
    # Genera un numero casuale nell'intervallo specificato
    numero_da_indovinare = random.randint(valore_minimo, valore_massimo)
    
    print(f"Ho scelto un numero tra: {valore_minimo} e: {valore_massimo}. Hai: {tentativi} tentativi per indovinarlo.")
    

    for tentativo in range(1, tentativi + 1):
        # Chiedi all'utente di fare un tentativo
        indovina_numero = int(input(f"Tentativo {tentativo}/{tentativi}: Indovina il numero: "))
        # Verifica se l'utente ha indovinato il numero
        if indovina_numero == numero_da_indovinare:
            print(f"Congratulazioni! Hai indovinato il numero {numero_da_indovinare} al tentativo {tentativo}.")
            break
        elif indovina_numero < numero_da_indovinare:
            print("Troppo basso! Riprova.")
        else:
            print("Troppo alto! Riprova.")
    
    # Se l'utente non ha indovinato, stampa un messaggio di fine gioco
    if indovina_numero != numero_da_indovinare:
        print(f"Mi dispiace! Non hai indovinato il numero. Il numero corretto era {numero_da_indovinare}.")

# Chiamata alla funzione per iniziare il gioco
indovina_il_numero()