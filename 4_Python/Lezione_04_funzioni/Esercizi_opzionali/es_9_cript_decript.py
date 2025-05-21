'''9. Cifratura di Cesare - Cifratura/Decifratura

    Crea funzioni per cifrare e decifrare un messaggio utilizzando la cifratura di Cesare.
    Permetti all'utente di specificare il valore di spostamento (numero di posizioni da spostare ogni lettera).
    Gestisci sia la cifratura che la decifratura utilizzando la stessa funzione con gli opportuni aggiustamenti.
    Cifra e decifra il messaggio dato utilizzando il valore di spostamento specificato.'''

def scegli_operazione() -> str:
    # Chiede all'utente se vuole cifrare o decifrare
    scelta = input("Vuoi criptare il codice? (si/no): ").lower()
    return scelta

def crittografia():
    alfabeto: str = "abcdefghijklmnopqrstuvwxyz"
    codice_criptato: list[str] = []
    codice_decriptato: list[str] = []

    while True:
        scelta = scegli_operazione()

        if scelta == "si":  # Se l'utente sceglie di criptare
            stringa: str = input("Inserisci una frase da cifrare: ")
            numero: int = int(input("Scegli il numero di codifica: "))
            codice_criptato = []  # Resetta la lista per ogni nuova cifratura
            
            # Cifra il messaggio
            for char in stringa:
                if char in alfabeto:
                    nuovo_indice = (alfabeto.index(char) + numero) % 26
                    codice_criptato.append(alfabeto[nuovo_indice])
                else:
                    codice_criptato.append(char)  # Non cifrare spazi o simboli

            print("Testo cifrato:", "".join(codice_criptato))

            # Dopo la cifratura, chiede se l'utente vuole anche decifrare
            scelta_decifra = input("Vuoi decifrare anche il codice? (si/no): ").lower()

            if scelta_decifra == "si":  # Se l'utente vuole decifrare
                codice_decriptato = []  # Resetta la lista per la decifratura
                
                # Decifra il messaggio usando lo stesso numero di codifica
                for char in codice_criptato:
                    if char in alfabeto:
                        nuovo_indice = (alfabeto.index(char) - numero) % 26
                        codice_decriptato.append(alfabeto[nuovo_indice])
                    else:
                        codice_decriptato.append(char)  # Non decifrare spazi o simboli

                print("Testo decifrato:", "".join(codice_decriptato))
        
        elif scelta == "no":  # Se l'utente non vuole criptare
            print("Operazione terminata.")
            break  # Esce dal ciclo

        else:
            print("Operazione non valida. Riprova.")
            continue  # Chiede di nuovo la scelta se l'input non è valido

        # Alla fine chiede se l'utente vuole continuare
        esci = input("Vuoi fare un'altra operazione? (si/no): ").lower()
        if esci == "no":
            break  # Esci dal ciclo principale

    return "".join(codice_criptato), "".join(codice_decriptato)

crittografia()
