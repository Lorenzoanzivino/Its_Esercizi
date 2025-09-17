'''10. Controllo degli Anagrammi:

    Crea una funzione che verifichi se due stringhe date sono anagrammi l'una dell'altra.
    Converte entrambe le stringhe in minuscolo e rimuove eventuali caratteri non alfabetici.
    Ordina i caratteri di ciascuna stringa e confronta le stringhe ordinate per verificarne l'uguaglianza.
    Indica se le stringhe sono anagrammi o meno.'''

def processa_parola1() -> str:
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    parola1_lista = []
    stringa1 = input("Inserisci la prima parola: ").lower()  # Converte la parola in minuscolo
    parola1_originale = stringa1  # Salva la parola originale per il risultato finale
    
    # Aggiungi solo le lettere (ignora numeri e caratteri speciali)
    for char in stringa1:
        if char in alfabeto:  # Aggiungi solo le lettere
            parola1_lista.append(char)
    
    parola1_lista = sorted(parola1_lista)  # Ordina la lista
    return "".join(parola1_lista), parola1_originale  # Restituisce la lista ordinata e la parola originale

def processa_parola2() -> str:
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    parola2_lista = []
    stringa2 = input("Inserisci la seconda parola: ").lower()  # Converte la parola in minuscolo
    parola2_originale = stringa2  # Salva la parola originale per il risultato finale
    
    # Aggiungi solo le lettere (ignora numeri e caratteri speciali)
    for char in stringa2:
        if char in alfabeto:  # Aggiungi solo le lettere
            parola2_lista.append(char)
    
    parola2_lista = sorted(parola2_lista)  # Ordina la lista
    return "".join(parola2_lista), parola2_originale  # Restituisce la lista ordinata e la parola originale

def anagrammi():
    parola1, parola1_originale = processa_parola1()  # Ottieni la prima parola
    parola2, parola2_originale = processa_parola2()  # Ottieni la seconda parola

    # Verifica se le parole sono anagrammi
    if parola1 == parola2:
        print(f"\nLe parole '{parola1_originale}' e '{parola2_originale}' sono anagrammi!")
        print(f"Risultato ordinato: '{parola1}' = '{parola2}'\n")
    else:
        print(f"\nLe parole '{parola1_originale}' e '{parola2_originale}' non sono anagrammi.")
        print(f"Risultato ordinato: '{parola1}' ≠ '{parola2}'\n")

# Chiama la funzione anagrammi
anagrammi()

