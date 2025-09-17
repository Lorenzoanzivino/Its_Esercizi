'''es 14. Risolutore di Sudoku:

Crea una funzione che risolva un puzzle di Sudoku utilizzando il backtracking.
    Fornisci una griglia 9x9 che rappresenti il puzzle con alcuni numeri già inseriti e altri vuoti.
    Implementa un algoritmo di backtracking per verificare le posizioni valide nei riquadri vuoti, assicurandoti che nessuna riga, colonna o sottogriglia 3x3 contenga duplicati.
    Risolvi il puzzle riempiendo le celle vuote con numeri validi.'''


# Griglia
griglia:list = [
    [5, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 0, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 0]
]

def stampa_griglia(griglia: list):
    # Inizializza un contatore per le righe
    i = 0
    # Ciclo attraverso ogni riga nella griglia
    for riga in griglia:
        # Inizializza una lista vuota che conterrà i gruppi di 3 numeri
        gruppi = []
        # Dividere la riga in 3 gruppi di 3 numeri
        for j in range(0, 9, 3):
            gruppo = riga[j:j+3]
            gruppi.append(gruppo)
        # Inizializza una lista vuota che conterrà le rappresentazioni dei gruppi
        gruppi_stampa = []
        # Per ogni gruppo, trasformo i numeri in stringhe, sostituendo gli zeri con un punto
        for gruppo in gruppi:
            gruppo_str = []
            for x in gruppo:
                if x == 0:
                    gruppo_str.append('.')
                else:
                    gruppo_str.append(str(x))
            gruppi_stampa.append(" ".join(gruppo_str))  # Unisco gli elementi del gruppo con uno spazio
        # Ora unisco i gruppi con " | "
        riga_stampa = " | ".join(gruppi_stampa)
        # Stampa la riga formattata
        print(riga_stampa)
        # Se siamo alla fine di ogni terzo riga, stampa una linea separatrice
        if (i + 1) % 3 == 0 and i != 8:  # Non mettere una linea dopo l'ultima riga
            print("---------------------")
        # Incrementa il contatore delle righe
        i += 1


# Funzione per verificare se un numero è valido in una data posizione
def is_valido(griglia, riga, colonna, numero):
    # Verifica nella riga
    for c in range(9):
        if griglia[riga][c] == numero:
            return False

    # Verifica nella colonna
    for r in range(9):
        if griglia[r][colonna] == numero:
            return False

    # Verifica nella sottogriglia 3x3
    start_riga = (riga // 3) * 3
    start_colonna = (colonna // 3) * 3
    for i in range(3):
        for j in range(3):
            if griglia[start_riga + i][start_colonna + j] == numero:
                return False

    return True

# Funzione di risoluzione del Sudoku con backtracking
def risolvi_sudoku(griglia):
    for riga in range(9):
        for colonna in range(9):
            if griglia[riga][colonna] == 0:  # Trova una cella vuota
                for numero in range(1, 10):  # Prova numeri da 1 a 9
                    if is_valido(griglia, riga, colonna, numero):
                        griglia[riga][colonna] = numero
                        if risolvi_sudoku(griglia):  # Ricorsione
                            return True
                        griglia[riga][colonna] = 0  # Backtrack
                return False  # Se nessun numero è valido, torna indietro
    return True  # Se la griglia è completa

# Stampa la griglia iniziale
print("\nGriglia iniziale:")
stampa_griglia(griglia)
print()

# Risolvi il puzzle di Sudoku
if risolvi_sudoku(griglia):
    print("Griglia risolta:")
    stampa_griglia(griglia)
else:
    print("Impossibile risolvere il Sudoku.")