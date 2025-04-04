'''es.15 Editor di Testo con Funzionalità di Base:

Crea un semplice editor di testo che permetta all'utente di aprire, modificare e salvare file di testo.

    Implementa funzionalità di base come inserimento, eliminazione e copia del testo.

    Fornisci la funzionalità di annullamento/ripristino (undo/redo) per consentire agli utenti di invertire le azioni.

    Salva il testo modificato in un file quando l'utente sceglie di salvare.'''

editor:dict = {} # inventario vuoto che simuli una cartella

editor = {}  # Dizionario vuoto che simula una cartella

def aggiungi_file(nome: str, testo: str):
    if nome in editor:
        print(f"Il file {nome} esiste già")
    else:
        scelta = input("Vuoi salvare il file? (s/n): ")
        if scelta.lower() == 's':
            editor[nome] = testo  # Aggiunge un nuovo file al dizionario
            print(f"Il file {nome}: {testo} è salvato con successo")
        else:
            print("Il file non è stato salvato.")

def apri_file(nome: str):
    if nome in editor:
        print(f"Il file {nome} è aperto: {editor[nome]}")
    else:
        print(f"File {nome} non trovato")

def modifica_file(nome: str, nuovo_testo: str):
    if nome in editor:
        editor[nome] += nuovo_testo  # Modifica il file esistente
        print(f"Il file {nome} è stato modificato: {editor[nome]}")
    else:
        print(f"File {nome} non trovato")

def rimuovi_file(nome: str):
    if nome in editor:
        del editor[nome]
        print(f"File {nome} rimosso")
    else:
        print(f"File {nome} non trovato")

def copia_file(nome: str):
    if nome in editor:
        nome_copia = f"{nome}_copia"
        editor[nome_copia] = editor[nome]  # Aggiunge la copia direttamente all'editor
        print(f"Il file: {nome} è stato copiato come: {nome_copia}")
    else:
        print(f"File {nome} non trovato")

def visualizza_editor():
    if editor:
        print("\nEditor completo:")
        for nome, testo in editor.items():
            print(f"Nome: {nome} - Testo: {testo}")
            print("-" * 20)  # Separatore
    else:
        print("L'editor è vuoto.")

def gestisci_file():
    while True:
        print("\nScegli un'operazione:")
        print("1 - Aggiungi file")
        print("2 - Aprire un file")
        print("3 - Modifica un file")
        print("4 - Rimuovi un file")
        print("5 - Copia un file")
        print("6 - Visualizza l'editor")
        print("7 - Esci")
        
        scelta = input("\nInserisci il numero dell'operazione: ")

        if scelta == "1":
            nome = input("Scegli il nome: ")
            testo = input("Inserisci il testo: ")
            aggiungi_file(nome, testo)
        elif scelta == "2":
            nome = input("Inserisci il nome di un file: ")
            apri_file(nome)
        elif scelta == "3":
            nome = input("Inserisci il nome del file: ")
            nuovo_testo = input("Inserisci il nuovo testo: ")
            modifica_file(nome, nuovo_testo)
        elif scelta == "4":
            nome = input("Inserisci il nome di un file: ")
            rimuovi_file(nome)
        elif scelta == "5":
            nome = input("Inserisci il nome di un file: ")
            copia_file(nome)
        elif scelta == "6":
            visualizza_editor()
        elif scelta == "7":
            print("Programma terminato")
            break
        else:
            print("Operazione non valida")

gestisci_file()
