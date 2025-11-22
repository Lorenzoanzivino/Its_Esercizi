'''1) Costruisci un algoritmo che permette di vincere sempre oppure pareggiare (nel caso peggiore) nel gioco tic-tac-toe.
L'algoritmo si chiama minimax: https://en.wikipedia.org/wiki/Minimax
Tic-tac-toe: https://en.wikipedia.org/wiki/Tic-tac-toe'''

class Griglia:
# La tua griglia iniziale (i contenuti non sono importanti per questo output, ma la struttura sì)
    griglia:list[list[str]] = [
        ["  ", "  ", "  "],
        ["  ", "  ", "  "],
        ["  ", "  ", "  "]
    ]
    def stampa_griglia(griglia: list[list[str]]):
        for i in range(len(griglia)): 
            # Stampa la riga delle celle vuote con i bordi verticali
            print("|   |   |   |")
            # Stampa il separatore orizzontale, ma solo tra le righe (non dopo l'ultima)
            if i < len(griglia) - 1:
                print("-------------")

        # La tua griglia iniziale (i contenuti non sono importanti per questo output, ma la struttura sì)
        griglia:list[list[str]] = [
            ["  ", "  ", "  "],
            ["  ", "  ", "  "],
            ["  ", "  ", "  "]
        ]
    # Stampa la griglia vuota nel formato richiesto
    stampa_griglia(griglia)

    def valuta_stato(griglia: list[list[str]]) -> int:
        # Controlla righe, colonne e diagonali per la vittoria di 'X' o 'O'

        # Righe
        for riga in griglia:
            if riga[0] == riga[1] == riga[2] and riga[0] != " ":
                if riga[0] == "X":
                    return 10  # X vince
                elif riga[0] == "O":
                    return -10 # O vince
        # Colonne
        for col in range(3):
            if griglia[0][col] == griglia[1][col] == griglia[2][col] and griglia[0][col] != " ":
                if griglia[0][col] == "X":
                    return 10
                elif griglia[0][col] == "O":
                    return -10
        # Diagonali
        if (griglia[0][0] == griglia[1][1] == griglia[2][2] and griglia[0][0] != " "):
            if griglia[0][0] == "X":
                return 10
            elif griglia[0][0] == "O":
                return -10
        if (griglia[0][2] == griglia[1][1] == griglia[2][0] and griglia[0][2] != " "):
            if griglia[0][2] == "X":
                return 10
            elif griglia[0][2] == "O":
                return -10 
        # Controlla se ci sono ancora mosse disponibili (griglia non piena)
        for riga in griglia:
            for cella in riga:
                if cella == " ":
                    return 0 # Il gioco non è finito
        # Se non ci sono vincitori e la griglia è piena, è un pareggio
        return 0 # Pareggio


'''i= 0
player1 : Player = player()
player2 : Player = player()
while True:
    mossa_player1 = player1.move()
    mossa_player2 = player2.move()'''

class Strategia:

    @staticmethod
    def minimax(griglia:Griglia) -> int :
        pass