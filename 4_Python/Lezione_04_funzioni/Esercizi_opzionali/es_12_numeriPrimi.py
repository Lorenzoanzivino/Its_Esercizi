'''es.12 Generatore di Numeri Primi con il Crivello di Eratostene:

Crea una funzione che generi un elenco di numeri primi fino a un limite specificato utilizzando l'algoritmo del Crivello di Eratostene.

    Inizializza un array con tutti i numeri fino al limite, marcandoli inizialmente come primi.

    Itera attraverso l'array a partire dal numero 2 e segna come non primi tutti i multipli del numero corrente.

    I numeri rimasti non segnati sono i numeri primi all'interno del limite.

    Restituisci l'elenco dei numeri primi.'''

def elenco_numeri_primi() -> str:
    while True:
        try:
            limite: int = int(input("Inserisci un numero come limite: "))
            if limite <= 0:
                print("Il numero selezionato non va bene, selezionare un altro.")
            else:
                break  # Esce dal loop se il numero è valido
        except ValueError:
            print("Inserisci un numero intero valido.")

    lista = list(range(2, limite + 1))  # Crea la lista con numeri da 2 a 'limite'
    print("Lista creata:", lista)

    for numero in lista:
        if numero != "x":  # Se il numero non è stato marcato
            for multiplo in range(numero * 2, limite + 1, numero):  # Inizia dal doppio del numero
                if multiplo in lista:  # Può essere ottimizzato
                    lista[lista.index(multiplo)] = "x"  # Segna il multiplo come non primo
    print(f"Eliminazione dei numeri multipli: {lista}")

    # Rimuovi tutti i "x" dalla lista (numeri non primi)
    numeri_primi = []  # Lista per i numeri primi
    for numero in lista:
        if numero != "x":
            numeri_primi.append(numero)

    print("Numeri primi:", numeri_primi)

elenco_numeri_primi()
