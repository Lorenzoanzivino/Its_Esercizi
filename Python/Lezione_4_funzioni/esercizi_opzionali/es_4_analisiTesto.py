'''4. Analisi del testo:

Crea una funzione che prenda un paragrafo e conti il numero di occorrenze di ogni parola.
La funzione dovrebbe stampare un report che mostra le parole più frequenti e il loro numero di occorrenze.
Puoi usare un ciclo for per scorrere le parole nel testo e un dizionario per memorizzare le occorrenze.
Implementa la gestione degli errori per gestire file mancanti o altri problemi di input.'''

def paragrafo(testo: str) -> None:
    # Rimuovere la punteggiatura e suddividere in parole
    testo = testo.lower()  # Rendere tutto il testo in minuscolo
    parole = []
    parola = ""
    
    for char in testo:
        if char.isalnum() or char == "'":  # Considera solo lettere, numeri e apostrofi
            parola += char
        else:
            if parola:  # Se trovi una parola, aggiungila alla lista
                parole.append(parola)
                parola = ""  # Reset della parola
    
    if parola:  # Aggiungi l'ultima parola
        parole.append(parola)
    
    # Conta le occorrenze delle parole
    frequenza = {}
    for parola in parole:
        if parola in frequenza:
            frequenza[parola] += 1
        else:
            frequenza[parola] = 1
    
    # Stampa le parole che si ripetono
    print("Le parole che si ripetono nel testo sono:")
    for parola, count in frequenza.items():
        if count > 1:
            print(f"'{parola}': {count} occorrenze")

# Testa la funzione con un testo
testo = "Il cielo è azzurro, il cielo è sereno. Il vento soffia leggero. Ogni giorno è un nuovo giorno, ogni giorno porta nuove opportunità"
paragrafo(testo)
