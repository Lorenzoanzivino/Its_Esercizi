'''11. Risolutore di Puzzle di Parole (Word Search Puzzle Solver):

Crea una funzione che risolva un puzzle di parole.
Fornisci una griglia 2D che rappresenta il puzzle e un elenco di parole da trovare.
Implementa un algoritmo di backtracking per cercare le parole nella griglia, marcando le celle visitate per evitare ripetizioni.
Mostra le posizioni delle parole trovate all'interno della griglia.'''


# Griglia del puzzle
griglia = [
    ["c", "a", "n", "e", "g", "p"],
    ["m", "g", "a", "s", "a", "o"],
    ["o", "d", "s", "i", "t", "l"],
    ["t", "i", "n", "o", "t", "l"],
    ["o", "o", "u", "n", "o", "o"],
    ["g", "i", "a", "l", "l", "o"]
]

# Lista delle parole da trovare
parole_da_trovare = ["cane", "gatto", "fiore", "moto", "asino", "lupo", "tino", "gas", "torre", "giallo", "trattore"]

# Direzioni possibili (dx, dy)
direzioni = [
    (0, 1),   # Destra
    (0, -1),  # Sinistra
    (1, 0),   # Giù
    (-1, 0),  # Su
    (1, 1),   # Diagonale basso-destra
    (1, -1),  # Diagonale basso-sinistra
    (-1, 1),  # Diagonale alto-destra
    (-1, -1)  # Diagonale alto-sinistra
]

# Funzione per stampare la griglia in modo leggibile
def stampa_griglia(griglia):
    colonne = len(griglia[0])
    
    # Stampa i numeri delle colonne
    print("    " + "   ".join(str(i) for i in range(colonne)))
    print("  " + "-------------------------")  # Linea iniziale
    
    # Stampa la griglia con numeri di riga
    for i, riga in enumerate(griglia):
        print(f"{i} | " + " | ".join(riga) + " |")
        print("  " + "-------------------------")  # Linea di separazione

# Funzione per verificare se una parola esiste a partire da una posizione (x, y) in una direzione (dx, dy)
def cerca_parola(griglia, parola, x, y, dx, dy):
    righe, colonne = len(griglia), len(griglia[0])
    lunghezza = len(parola)
    
    # Calcola le coordinate finali basate sulla direzione e la lunghezza della parola
    x_finale = x + (lunghezza - 1) * dx
    y_finale = y + (lunghezza - 1) * dy

    # Controlla se la coordinata finale rientra nei limiti della griglia
    if x_finale < 0 or x_finale >= righe:
        return None  # La parola uscirebbe dai bordi verticali (righe)

    if y_finale < 0 or y_finale >= colonne:
        return None  # La parola uscirebbe dai bordi orizzontali (colonne)

    # Se siamo qui, significa che la parola può stare nei bordi
    
    # Verifica lettera per lettera
    posizioni = []
    for i in range(lunghezza):
        nx, ny = x + i * dx, y + i * dy
        if griglia[nx][ny] != parola[i]:  
            return None  # La parola non corrisponde
        posizioni.append((nx, ny))  # Salva le coordinate delle lettere

    return posizioni  # Restituisce le coordinate se la parola è trovata

# Funzione principale per cercare tutte le parole
def trova_parole(griglia, parole_da_trovare):
    righe, colonne = len(griglia), len(griglia[0])
    parole_trovate = []
    parole_non_trovate = []  # Lista per parole non trovate

    for parola in parole_da_trovare:
        parola_trovata = False  # Flag per sapere se la parola è trovata
        for x in range(righe):
            for y in range(colonne):
                for dx, dy in direzioni:
                    posizioni = cerca_parola(griglia, parola, x, y, dx, dy)
                    if posizioni:  # Se la parola è stata trovata
                        parole_trovate.append((parola, posizioni))
                        parola_trovata = True
                        break  # Esci dal ciclo appena trovi la parola
        
        if not parola_trovata:  # Se la parola non è stata trovata
            parole_non_trovate.append(parola)

    return parole_trovate, parole_non_trovate  # Restituisce entrambe le liste

# Funzione per stampare i risultati
def stampa_risultati(parole_trovate, parole_non_trovate):
    if parole_trovate:
        print("\n- Parole trovate:")
        for parola, posizioni in parole_trovate:
            print(f"· {parola.upper()} trovato in: {posizioni}")
    else:
        print("\n- Nessuna parola trovata!")

    if parole_non_trovate:
        print("\n- Parole non trovate:")
        for parola in parole_non_trovate:
            print(f"· {parola.upper()} non trovata!")

# Avvio del programma
print("\nGriglia Iniziale:\n")
stampa_griglia(griglia)

# Trova le parole
parole_trovate, parole_non_trovate = trova_parole(griglia, parole_da_trovare)

# Stampa i risultati
stampa_risultati(parole_trovate, parole_non_trovate)
