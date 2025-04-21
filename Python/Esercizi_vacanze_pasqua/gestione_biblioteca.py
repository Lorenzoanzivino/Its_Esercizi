'''
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

Codice Driver

    Aggiungi libri alla biblioteca.
    Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
    Mostra i libri disponibili in ogni fase.
    Visualizza lo stato finale di ogni libro.'''

class Libro:
    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito = "disponibile"

    def presta(self):
        if self.stato_prestito == "disponibile":
            self.stato_prestito = "prestato"
            return f"Il libro '{self.titolo}' è stato prestato."
        else:
            return f"Il libro '{self.titolo}' è già prestato."

    def restituisci(self):
        if self.stato_prestito == "prestato":
            self.stato_prestito = "disponibile"
            return f"Il libro '{self.titolo}' è stato restituito."
        else:
            return f"Il libro '{self.titolo}' non era stato prestato."


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro: Libro):
        for l in self.catalogo:
            if l.titolo == libro.titolo:
                return f"Il libro '{libro.titolo}' è già nel catalogo."
        self.catalogo.append(libro)
        return f"Libro '{libro.titolo}' aggiunto al catalogo."

    def presta_libro(self, titolo: str):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                return libro.presta()
        return f"Il libro '{titolo}' non è presente nel catalogo."

    def restituisci_libro(self, titolo: str):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                return libro.restituisci()
        return f"Il libro '{titolo}' non è presente nel catalogo."

    def mostra_libri_disponibili(self):
        disponibili = []
        for libro in self.catalogo:
            if libro.stato_prestito == "disponibile":
                disponibili.append(libro.titolo)
        if disponibili:
            return disponibili
        else:
            return "Nessun libro disponibile al momento."

    def stato_catalogo(self):
        if not self.catalogo:
            return "Catalogo vuoto."
        risultato = ""
        for libro in self.catalogo:
            risultato += f"- {libro.titolo} ({libro.autore}): {libro.stato_prestito}\n"
        return risultato


# Creazione istanze dei libri con autori diversi
libro1 = Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling")
libro2 = Libro("Piccoli Brividi - Il Fantasma Vampiro", "R.L. Stine")
libro3 = Libro("Dieci Piccoli Indiani", "Agatha Christie")
libro4 = Libro("Harry Potter e la Camera dei Segreti", "J.K. Rowling")

# Creazione dell'istanza della biblioteca
biblioteca = Biblioteca()

# Aggiunta dei libri al catalogo
print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.aggiungi_libro(libro3))
print(biblioteca.aggiungi_libro(libro4))

# Mostra i libri disponibili
print("\nLibri disponibili:")
disponibili = biblioteca.mostra_libri_disponibili()
if isinstance(disponibili, list):
    for titolo in disponibili:
        print(f"- {titolo}")
else:
    print(disponibili)

# Presta un libro
print("\nPrestito del libro 'Harry Potter e la Camera dei Segreti':")
print(biblioteca.presta_libro("Harry Potter e la Camera dei Segreti"))

# Mostra i libri disponibili dopo il prestito
print("\nLibri disponibili dopo il prestito:")
disponibili = biblioteca.mostra_libri_disponibili()
if isinstance(disponibili, list):
    for titolo in disponibili:
        print(f"- {titolo}")
else:
    print(disponibili)

# Restituisce un libro
print("\nRestituzione del libro 'Harry Potter e la Camera dei Segreti':")
print(biblioteca.restituisci_libro("Harry Potter e la Camera dei Segreti"))

# Mostra lo stato finale del catalogo
print("\nStato finale del catalogo:")
print(biblioteca.stato_catalogo())
