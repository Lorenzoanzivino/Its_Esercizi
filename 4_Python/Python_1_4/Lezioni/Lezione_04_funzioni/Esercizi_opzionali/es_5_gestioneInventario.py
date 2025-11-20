''' Sistema di Gestione dell'Inventario:
    · Crea una funzione che definisca un articolo con un codice, un nome, una quantità e un prezzo.
    · Crea un database o un dizionario per memorizzare gli articoli nell'inventario.
    · Implementa funzioni per aggiungere, rimuovere, cercare e aggiornare gli articoli nell'inventario.
    · Utilizza cicli for e dichiarazioni condizionali per gestire le varie operazioni sull'inventario.

In pratica, dovrai creare una struttura dati (ad esempio un dizionario) che contenga gli articoli dell'inventario. Ogni articolo avrà un codice identificativo, un nome, una quantità disponibile e un prezzo. Poi dovrai implementare delle funzioni per:
    Aggiungere articoli: Inserire nuovi articoli o aggiornare quelli esistenti.
    Rimuovere articoli: Eliminare articoli dall'inventario.
    Cercare articoli: Trovare un articolo specifico in base al codice o al nome.
    Aggiornare articoli: Modificare i dettagli di un articolo, come quantità o prezzo.
Utilizzerai cicli for per iterare sull'inventario e istruzioni condizionali (if) per verificare le condizioni (ad esempio, se un articolo esiste già o se la quantità è sufficiente).'''

# Dizionario globale per memorizzare l'inventario
inventario:dict = {}

# Funzione per aggiungere o aggiornare un articolo
def aggiungi_articolo(codice:int, nome:str, quantita:int, prezzo:float) -> None:
    if codice in inventario:
        print(f"L'articolo: {nome} con codice: {codice} esiste già.")
    else:
        inventario[codice] = {'nome': nome, 'quantita': quantita, 'prezzo': prezzo}
        print(f"L'articolo: {nome} con codice: {codice} aggiunto con successo!")

# Funzione per rimuovere un articolo
def rimuovere_articolo(codice:int, nome:str) -> None:
    if codice in inventario:
        del inventario[codice]
        print(f"Articolo: {nome} con codice {codice} rimosso con successo!")
    else:
        print(f"Articolo: {nome} con codice {codice} non trovato nell'inventario.")

# Funzione per cercare un articolo per codice
def cerca_articolo_per_codice(codice:int) -> None:
    if codice in inventario:
        dettagli = inventario[codice]
        print(f"Codice: {codice}")
        print(f"Nome: {dettagli['nome']}")
        print(f"Quantità: {dettagli['quantita']}")
        print(f"Prezzo: {dettagli['prezzo']}")
    else:
        print(f"Articolo con codice {codice} non trovato nell'inventario.")

# Funzione per cercare un articolo per nome
def cerca_articolo_per_nome(nome:str) -> None:
    trovato = False
    for codice, dettagli in inventario.items():
        if dettagli['nome'].lower() == nome.lower():
            print(f"Codice: {codice}")
            print(f"Nome: {dettagli['nome']}")
            print(f"Quantità: {dettagli['quantita']}")
            print(f"Prezzo: {dettagli['prezzo']}")
            trovato = True
    if not trovato:
        print(f"Articolo con nome {nome} non trovato nell'inventario.")

# Funzione per aggiornare la quantità di un articolo
def aggiorna_quantita(codice:int, nome:str, quantita:int) -> None:
    if codice in inventario:
        inventario[codice]['quantita'] += quantita
        print(f"Quantità dell'articolo: {nome} con codice {codice} aggiornata a {inventario[codice]['quantita']}.")
    else:
        print(f"Articolo con codice {codice} non trovato nell'inventario.")

# Funzione per aggiornare il prezzo di un articolo
def aggiorna_prezzo(codice:int, nome:str, prezzo:float) -> None:
    if codice in inventario:
        inventario[codice]['prezzo'] = prezzo
        print(f"Prezzo dell'articolo: {nome} con codice {codice} aggiornato a {prezzo}.")
    else:
        print(f"Articolo con codice {codice} non trovato nell'inventario.")

# Funzione per visualizzare l'intero inventario
def visualizza_inventario() -> None:
    if inventario:
        print("\nInventario completo:")
        for codice, dettagli in inventario.items():
            print(f"Codice: {codice}")
            print(f"Nome: {dettagli['nome']}")
            print(f"Quantità: {dettagli['quantita']}")
            print(f"Prezzo: {dettagli['prezzo']}")
            print("-" * 20)  # Separatore tra gli articoli
    else:
        print("L'inventario è vuoto.")

# Funzione principale per interagire con l'utente
def gestisci_inventario():
    while True:
        print("\nScegli un'operazione:")
        print("1 - Aggiungi o aggiorna un articolo")
        print("2 - Rimuovi un articolo")
        print("3 - Cerca un articolo per codice")
        print("4 - Cerca un articolo per nome")
        print("5 - Aggiorna la quantità di un articolo")
        print("6 - Aggiorna il prezzo di un articolo")
        print("7 - Visualizza l'inventario")
        print("8 - Esci")

        scelta:str = input("\nInserisci il numero dell'operazione: ")

        if scelta == "1":
            codice:int = input("\nInserisci il codice dell'articolo: ")
            nome:str = input("\nInserisci il nome dell'articolo: ")
            quantita:int = input("\nInserisci la quantità dell'articolo: ")
            prezzo:float = input("\nInserisci il prezzo dell'articolo: ")
            aggiungi_articolo(codice, nome, quantita, prezzo)

        elif scelta == "2":
            codice = int(input("Inserisci il codice dell'articolo da rimuovere: "))
            rimuovere_articolo(codice)

        elif scelta == "3":
            codice = int(input("Inserisci il codice dell'articolo da cercare: "))
            cerca_articolo_per_codice(codice)

        elif scelta == "4":
            nome = input("Inserisci il nome dell'articolo da cercare: ")
            cerca_articolo_per_nome(nome)

        elif scelta == "5":
            codice = int(input("Inserisci il codice dell'articolo da aggiornare: "))
            quantita = int(input("Inserisci la nuova quantità dell'articolo: "))
            aggiorna_quantita(codice, quantita)

        elif scelta == "6":
            codice = int(input("Inserisci il codice dell'articolo da aggiornare: "))
            prezzo = float(input("Inserisci il nuovo prezzo dell'articolo: "))
            aggiorna_prezzo(codice, prezzo)

        elif scelta == "7":
            visualizza_inventario()

        elif scelta == "8":
            print("Uscendo dal programma.")
            break
        else:
            print("Operazione non valida. Riprova.")

# Esegui la funzione principale per gestire l'inventario
gestisci_inventario()