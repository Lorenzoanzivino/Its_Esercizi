'''1) Costruisci un algoritmo che permette di vincere sempre oppure pareggiare (nel caso peggiore) nel gioco tic-tac-toe.
L'algoritmo si chiama minimax: https://en.wikipedia.org/wiki/Minimax, Tic-tac-toe: https://en.wikipedia.org/wiki/Tic-tac-toe'''

# Pseudocodice
'''Fun minimax (nodo, profondità, massimizzazionePlayer) è
    Se la profondità 0 o il nodo è un nodo terminale, allora
        Restituire il valore euristico del nodo
    Se massimizza il giocone, allora
        Valore : ?
        Per ogni figlio di nododo
            Valore : max(valore, minimax(bambino, profondità 1, FALSE))
        Riportare il valore
    Altro (* minimizzando il giocatore *)
        Valore : +?
        Per ogni figlio di nododo
            Valore : min(valore, minimax(bambino, profondità 1, VERO))
        Riportare il valore

(* Chiamata iniziale *)
minimax(origine, profondità, VERO)'''

class Griglia:
    #Rappresenta la griglia di gioco del Tic-Tac-Toe e gestisce le operazioni sulla griglia.

    def __init__(self):
        # Inizializza la griglia di gioco 3x3 con celle vuote (' ').
        # Usiamo spazi singoli per una migliore coerenza con i simboli 'X' e 'O'.
        self.griglia: list[list[str]] = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        # Stampa la griglia iniziale vuota quando un oggetto Griglia viene creato.
        self.stampa_griglia()

    def stampa_griglia(self):
        """
        Stampa lo stato corrente della griglia di gioco sulla console.
        """
        print("\n   GRIGLIA \n")
        print("-------------")
        for i in range(len(self.griglia)):
            # Stampa il contenuto di ogni cella della riga con i bordi verticali.
            # Esempio: "| X |   | O |"
            print(f"| {self.griglia[i][0]} | {self.griglia[i][1]} | {self.griglia[i][2]} |")
            # Stampa un separatore orizzontale tra le righe, ma non dopo l'ultima riga.
            if i < len(self.griglia) - 1:
                print("-------------")
        print("-------------\n")

class Player:
    def __init__(self):
        pass

class Strategia:
    def __init__(self):
        pass

# Questo serve per far partire il gioco
if __name__ == "__main__":
    gioco = Griglia()
