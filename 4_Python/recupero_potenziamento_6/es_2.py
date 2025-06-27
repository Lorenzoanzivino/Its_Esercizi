'''Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe). L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza, oppure sono stati inseriti 30 nomi distinti. Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.'''

def serie_nomi():
    lista_nomi = []

    while len(lista_nomi) <= 30:
        nome = input("Inserisci un nome: ").strip().title()

        # Controllo nome vuoto
        if nome == "":
            print("Il nome non può essere vuoto. Riprova.")
            continue
        
        # Controllo lunghezza
        if len(nome) >= 20:
            print("Il nome deve contenere meno di 20 caratteri. Riprova.")
            continue

        # Controllo duplicato
        if nome in lista_nomi:
            print(f"Hai inserito un nome già presente: {nome}")
            break

        lista_nomi.append(nome)

    # Risultati finali
    print(f"\nHai inserito {len(lista_nomi)} nomi distinti.")
    
    
    nome_piu_lungo = ""
    lunghezza_massima = 0

    for nome in lista_nomi:
        if len(nome) > lunghezza_massima:
            nome_piu_lungo = nome
            lunghezza_massima = len(nome)

    print(f"Il più lungo è {nome_piu_lungo} con {lunghezza_massima} caratteri.")

serie_nomi()