'''Carrello della Spesa E-Commerce:
Crea una funzione che definisce un prodotto con un nome, un prezzo e una quantità.
Crea una funzione che gestisce il carrello della spesa, consentendo all'utente di aggiungere, rimuovere e visualizzare i prodotti nel carrello.
La funzione dovrebbe calcolare il totale del carrello e applicare eventuali sconti o tasse.
Implementa un ciclo for per iterare sugli articoli nel carrello e stampare informazioni dettagliate su ogni prodotto e il totale.'''


# Funzione che definisce un prodotto
def prodotto(nome: str, prezzo: float, quantita: int) -> dict:
    return {'nome': nome, 'prezzo': prezzo, 'quantita': quantita}

# Funzione per visualizzare il carrello
def visualizza_carrello(carrello):
    if not carrello:
        print("Il carrello è vuoto.")
    else:
        print("\nContenuto del carrello:")
        for prodotto in carrello:
            print(f"Nome: {prodotto['nome'].title()}, Prezzo: {prodotto['prezzo']:.2f}€, Quantità: {prodotto['quantita']}")
    print()

# Funzione per calcolare il totale con sconto e tasse
def calcola_totale(carrello, sconto_percentuale=0, tassa_percentuale=0):
    totale_senza_sconto = 0  # Inizializziamo il totale senza applicare lo sconto
    for prodotto in carrello:
        totale_senza_sconto += prodotto['prezzo'] * prodotto['quantita']  # Sommiamo il prezzo * quantità di ogni prodotto
    
    # Calcoliamo lo sconto sul totale
    totale_con_sconto = totale_senza_sconto * (1 - (sconto_percentuale / 100))  # Applichiamo lo sconto
    
    # Calcoliamo la tassa sul totale scontato
    totale_con_tassa = totale_con_sconto * (1 + (tassa_percentuale / 100))  # Aggiungiamo la tassa
    
    return totale_con_tassa

# Funzione per aggiungere un prodotto al carrello
def aggiungi_prodotto(carrello):
    nome_prodotto = str(input("Digita il nome del prodotto: "))
    prezzo_prodotto = float(input("Digita il prezzo del prodotto: "))
    quantita_prodotto = int(input("Digita le quantità del prodotto inserito: "))
    
    # Aggiungiamo il prodotto al carrello come dizionario
    carrello.append(prodotto(nome_prodotto, prezzo_prodotto, quantita_prodotto))

# Funzione per rimuovere un prodotto dal carrello
def rimuovi_prodotto(carrello):
    nome_rimuovere = input("Inserisci il nome del prodotto da rimuovere: ").lower()
    for prodotto in carrello:
        if prodotto['nome'].lower() == nome_rimuovere:
            carrello.remove(prodotto)
            print(f"Prodotto '{nome_rimuovere}' rimosso dal carrello.")
            return
    print(f"Prodotto '{nome_rimuovere}' non trovato nel carrello.")

# Funzione principale per gestire il carrello
def carrello_spesa():
    carrello = []  # Creazione del carrello vuoto
    while True:
        print("\n--- Gestione Carrello ---")
        print("1. Aggiungi prodotto")
        print("2. Rimuovi prodotto")
        print("3. Visualizza carrello")
        print("4. Calcola totale e esci")
        
        scelta = input("Scegli un'opzione (1/2/3/4): ")
        
        if scelta == '1':
            aggiungi_prodotto(carrello)
        elif scelta == '2':
            rimuovi_prodotto(carrello)
        elif scelta == '3':
            visualizza_carrello(carrello)
        elif scelta == '4':
            visualizza_carrello(carrello)
            sconto = float(input("Inserisci la percentuale di sconto: "))
            tassa = float(input("Inserisci la percentuale di tassa: "))
            totale = calcola_totale(carrello, sconto, tassa)
            print(f"Totale del carrello (con sconto e tassa): {totale:.2f}€")
            print("Grazie per aver usato il nostro carrello. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

# Avvio del carrello
carrello_spesa()
