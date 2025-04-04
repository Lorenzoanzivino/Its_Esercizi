'''es 13. Generatore di Alberi Frattali:

Crea una funzione che generi un albero frattale utilizzando la ricorsione.

    Specifica la lunghezza iniziale del tronco e l'angolo di ramificazione.

    Disegna il tronco e richiama ricorsivamente la funzione per disegnare due rami con un angolo specificato e una lunghezza ridotta.

    Ripeti il processo di ramificazione fino a raggiungere il livello di dettaglio desiderato'''

def disegna_albero(grid, x, y, lunghezza, angolo, livello):
    if livello == 0:
        return
    
    # Calcola le nuove coordinate dei rami
    dx = int(lunghezza * cos(angolo))
    dy = int(lunghezza * sin(angolo))
    
    # Modifica la griglia per disegnare il tronco
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        grid[y][x] = '|'
    
    # Calcola le nuove coordinate per i rami
    x2 = x + dx
    y2 = y - dy
    
    if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
        grid[y2][x2] = '/'
        
    x3 = x - dx
    y3 = y + dy
    
    if 0 <= x3 < len(grid[0]) and 0 <= y3 < len(grid):
        grid[y3][x3] = '\\'
    
    # Chiamata ricorsiva per i rami
    disegna_albero(grid, x2, y2, lunghezza * 0.7, angolo - 0.3, livello - 1)
    disegna_albero(grid, x3, y3, lunghezza * 0.7, angolo + 0.3, livello - 1)

def stampa_griglia(grid):
    for row in grid:
        print(''.join(row))

def albero_frattale(lunghezza_iniziale, angolo_iniziale, livelli):
    # Crea una griglia di dimensioni abbastanza grandi
    larghezza = 60
    altezza = 20
    grid = [[' ' for _ in range(larghezza)] for _ in range(altezza)]
    
    # Posizione di partenza per il tronco
    x_iniziale = larghezza // 2
    y_iniziale = altezza - 1
    
    # Disegna l'albero
    disegna_albero(grid, x_iniziale, y_iniziale, lunghezza_iniziale, angolo_iniziale, livelli)
    
    # Stampa la griglia
    stampa_griglia(grid)

# Esegui il disegno dell'albero frattale
from math import sin, cos, radians
albero_frattale(8, 90, 6)
