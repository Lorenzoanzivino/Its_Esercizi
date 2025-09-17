'''Esercizio 3: Sistema di Gestione di Biblioteca

Crea una classe Book (Libro) che contenga i seguenti attributi:

    title (titolo)

    author (autore)

    isbn (codice ISBN)

La classe Book deve contenere i seguenti metodi:

    __str__: un metodo che restituisce una rappresentazione testuale del libro.

    from_string: un metodo di classe che crea un'istanza di Book a partire da una stringa nel formato "titolo, autore, isbn". Significa che devi usare il riferimento cls per creare un nuovo oggetto della classe Book usando quella stringa.

Esempio:

book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)

In questo caso, divina_commedia sarà un’istanza della classe Book con:

    title = "La Divina Commedia"

    author = "D. Alighieri"

    isbn = "999000666"

Crea una classe Member (Membro) con i seguenti attributi:

    name (nome)

    member_id (ID del membro)

    borrowed_books (lista di libri presi in prestito)

La classe Member deve contenere i seguenti metodi:

    borrow_book: per aggiungere un libro alla lista dei libri presi in prestito.

    return_book: per rimuovere un libro dalla lista dei libri presi in prestito.

    __str__: un metodo che restituisce una rappresentazione testuale del membro.

    from_string: un metodo di classe che crea un'istanza di Member a partire da una stringa nel formato "nome, member_id".

Crea una classe Library (Biblioteca) con i seguenti attributi:

    books (lista di libri disponibili)

    members (lista dei membri registrati)

    total_books (attributo di classe che tiene traccia del numero totale di istanze di Book)

La classe Library deve contenere i seguenti metodi:

    add_book: per aggiungere un libro alla biblioteca e incrementare total_books.

    remove_book: per rimuovere un libro dalla biblioteca e decrementare total_books.

    register_member: per registrare un nuovo membro nella biblioteca.

    lend_book: per prestare un libro a un membro. Deve verificare se il libro è disponibile e se il membro è registrato.

    __str__: metodo che restituisce una rappresentazione testuale della biblioteca, mostrando l’elenco dei libri e dei membri.

    library_statistics: metodo di classe che stampa il numero totale di libri.

Infine, scrivi un semplice programma principale (driver program). Dopo aver creato una biblioteca, esegui le seguenti operazioni:

    Crea delle istanze delle classi Book e Member. Dove possibile, utilizza i metodi di classe from_string per creare oggetti da stringhe, in modo da rendere il codice più chiaro e modulare.

    Registra nuovi membri nella biblioteca (cioè, aggiungili alla collezione della biblioteca).

    Aggiungi dei libri alla collezione della biblioteca.

    Presta dei libri ai membri (cioè, segna il libro come preso in prestito e collegalo al membro corrispondente).

In ogni fase significativa, stampa lo stato della biblioteca per monitorare come cambia:

    Prima che venga prestato qualsiasi libro

    Dopo che i libri sono stati prestati'''


class Book:
    def __init__(self, titolo: str, autore: str, isbn: str):
        if not isbn.isdigit():
            raise ValueError("L'ISBN deve contenere solo numeri")
        self.titolo: str = titolo
        self.autore: str = autore
        self.isbn: str = isbn

    @classmethod
    def from_string(cls, stringa: str) -> "Book":
        parti = stringa.split(",")
        parti_pulite = [parte.strip() for parte in parti]
        titolo = parti_pulite[0]
        autore = parti_pulite[1]
        isbn = parti_pulite[2]
        return cls(titolo, autore, isbn)

    def __str__(self) -> str:
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"


class Member:
    def __init__(self, nome: str, member_id: str):
        self.nome = nome
        self.member_id = member_id
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self) -> str:
        if self.borrowed_books:
            libri = ", ".join(str(book) for book in self.borrowed_books)
        else:
            libri = "Nessun libro in prestito"
        return f"Membro: {self.nome}, ID: {self.member_id}, Libri in prestito: {libri}"

    @classmethod
    def from_string(cls, stringa: str) -> "Member":
        parti = stringa.split(",")
        parti_pulite = [parte.strip() for parte in parti]
        nome = parti_pulite[0]
        member_id = parti_pulite[1]
        return cls(nome, member_id)


class Library:
    total_books: int = 0  # Attributo di classe

    def __init__(self):
        self.books: list[Book] = []          # libri disponibili
        self.members: list[Member] = []

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)
            Library.total_books += 1

    def remove_book(self, book: Book) -> None:
        if book in self.books:
            self.books.remove(book)
            Library.total_books -= 1

    def register_member(self, member: Member) -> None:
        if member not in self.members:
            self.members.append(member)

    def lend_book(self, book: Book, member: Member) -> None:
        if member not in self.members:
            # Membro non registrato, non fare nulla
            return

        if book not in self.books:
            # Libro non disponibile
            return

        # Prestito: rimuovo il libro dai disponibili e lo assegno al membro
        self.books.remove(book)
        member.borrow_book(book)
        Library.total_books -= 1  # consideriamo il libro "non disponibile" nella biblioteca

    def __str__(self) -> str:
        libri_str = "\n".join(str(book) for book in self.books) if self.books else "Nessun libro disponibile"
        membri_str = "\n".join(str(member) for member in self.members) if self.members else "Nessun membro registrato"
        return f"LIBRI DISPONIBILI:\n{libri_str}\n\nMEMBRI REGISTRATI:\n{membri_str}"

    @classmethod
    def library_statistics(cls) -> str:
        return f"Totale libri nella biblioteca (disponibili): {cls.total_books}"


if __name__ == '__main__':
    # 1. Creazione della biblioteca
    biblioteca = Library()

    # 2. Creazione dei libri usando from_string
    book1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
    book2 = Book.from_string("Il Gattopardo, G. Tomasi di Lampedusa, 123456789")
    book3 = Book.from_string("I Promessi Sposi, A. Manzoni, 987654321")

    # 3. Creazione dei membri usando from_string
    member1 = Member.from_string("Mario Rossi, M001")
    member2 = Member.from_string("Luca Bianchi, M002")

    # 4. Registrazione dei membri nella biblioteca
    biblioteca.register_member(member1)
    biblioteca.register_member(member2)

    # 5. Aggiunta dei libri alla biblioteca
    biblioteca.add_book(book1)
    biblioteca.add_book(book2)
    biblioteca.add_book(book3)

    # 6. Stato iniziale della biblioteca (prima dei prestiti)
    print("STATO INIZIALE DELLA BIBLIOTECA (prima del prestito):\n")
    print(biblioteca)

    # 7. Prestito di libri ai membri
    biblioteca.lend_book(book1, member1)  # Mario Rossi prende La Divina Commedia
    biblioteca.lend_book(book2, member2)  # Luca Bianchi prende Il Gattopardo

    # 8. Stato della biblioteca dopo i prestiti
    print("\nSTATO DELLA BIBLIOTECA (dopo i prestiti):\n")
    print(biblioteca)

    # 9. Statistiche generali
    print("\nSTATISTICHE:")
    print(Library.library_statistics())
