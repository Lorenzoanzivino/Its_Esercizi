# Classe Book
# Attributi
# book_id: str
# title: str
# is_borrowed: bool
# Metodi
# borrow() -> None
# Se is_borrowed è False, lo imposta a True.
# Altrimenti stampa "Il libro '{self.title}' è già in prestito."
# return_book() -> None
# Se is_borrowed è True, lo imposta a False.
# Altrimenti stampa "Il libro '{self.title}' non risulta in prestito."

class Book:
    def __init__(self, book_id:str, title:str) -> None:
        self.book_id = book_id
        self.title = title
        self.is_borrowed = False
    
    def borrow(self) -> None:
        if self.is_borrowed == False:
            self.is_borrowed = True
        else:
            print(f"Il Libro '{self.title}' è già in prestito")
    
    def return_book(self) -> None:
        if self.is_borrowed == True:
            self.is_borrowed = False
        else:
            print(f"Il Libro '{self.title}' non risulta in prestito")

# classe Member
# Attributi
# member_id: str
# name: str
# borrowed_books: list[Book]
# Metodi
# borrow_book(book: Book) -> None
# Se book.is_borrowed è False, lo aggiunge a borrowed_books e chiama book.borrow().
# Altrimenti stampa "Il libro '{book.title}' non è disponibile."
# return_book(book: Book) -> None
# Se book è in borrowed_books, lo rimuove e chiama book.return_book().
# Altrimenti stampa "Il libro '{book.title}' non è stato preso in prestito da questo utente.

class Member:
    def __init__(self, member_id:str, name:str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book:Book) -> None:
        if book.is_borrowed == False:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print(f"Il Libro '{book.title}' non è disponibile")

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"Il libro '{book.title}' non è stato preso in prestito da questo utente")

# Classe Library
# Attributi
# books: dict[str, Book]
# members: dict[str, Member]

# Metodi
# add_book(book_id: str, title: str) -> None
# Se book_id esiste, stampa "Il libro con ID '{book_id}' esiste già."
# Altrimenti aggiunge un nuovo Book.

# register_member(member_id: str, name: str) -> None
# Se member_id esiste, stampa "L'utente con ID '{member_id}' è già registrato."
# Altrimenti aggiunge un nuovo Member.

# borrow_book(member_id: str, book_id: str) -> None
# Se entrambi esistono, invoca member.borrow_book(book); 
# altrimenti stampa "Utente o libro non trovato."

# return_book(member_id: str, book_id: str) -> None
# Se entrambi esistono, invoca member.return_book(book); 
# altrimenti stampa "Utente o libro non trovato."

# list_available_books() -> list[str]
# Restituisce la lista degli ID dei libri con is_borrowed == False.

# list_member_loans(member_id: str) -> list[str] | str
# Se l’utente esiste, restituisce la lista dei book_id presi in prestito.
# Altrimenti restituisce "Errore: utente non trovato."

class Library:
    def __init__(self):
        self.books:dict[str, Book] = {}
        self.members:dict[str, Member] = {}
    
    def add_book(self, book:Book) -> None:
        if book.book_id in self.books:
            print(f"Il libro con ID '{book.book_id}' esiste già.")
        else:
            self.books[book.book_id] = book
            print(f"Libro '{book.title}' aggiunto con successo.")

    def register_member(self, member:Member) -> None:
        if member.member_id in self.members:
            print(f"L'utente con ID '{member.member_id}' è già registrato.")
        else:
            self.members[member.member_id] = member
            print(f"Utente con ID '{member.member_id}' aggiunto con successo.")

    def borrow_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)
        else:
            print("Utente o libro non trovato.")


    def return_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)
        else:
            print("Utente o libro non trovato.")

    def list_available_books(self) -> list[str]:
        disponibili = []
        for book_id, book in self.books.items():
            if not book.is_borrowed:  # se il libro non è preso in prestito
                disponibili.append(book_id)
        return disponibili

    def list_member_loans(self, member_id: str) -> list[str] | str:
        if member_id not in self.members:
            return "Errore: utente non trovato."
        member = self.members[member_id]
        loans = [book.book_id for book in member.borrowed_books]
        return loans
    

# Creo la libreria
lib = Library()

# Creo libri
b1 = Book("B01", "1984")
b2 = Book("B02", "Il Signore degli Anelli")
b3 = Book("B03", "Harry Potter")

# Aggiungo libri alla libreria
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b1)  # test duplicato

print("\n--- Registrazione membri ---")
# Creo membri
m1 = Member("M01", "Lorenzo")
m2 = Member("M02", "Alice")

# Registro membri
lib.register_member(m1)
lib.register_member(m2)
lib.register_member(m1)  # test duplicato

print("\n--- Prestiti libri ---")
# Prestito libri
lib.borrow_book("M01", "B01")  # Lorenzo prende 1984
lib.borrow_book("M02", "B01")  # Alice prova a prendere 1984 (non disponibile)
lib.borrow_book("M02", "B02")  # Alice prende Il Signore degli Anelli

print("\n--- Libri disponibili ---")
print(lib.list_available_books())  # dovrebbe mostrare solo B03

print("\n--- Prestiti membri ---")
print("Lorenzo:", lib.list_member_loans("M01"))  # ['B01']
print("Alice:", lib.list_member_loans("M02"))    # ['B02']

print("\n--- Restituzioni ---")
lib.return_book("M01", "B01")  # Lorenzo restituisce 1984
lib.return_book("M02", "B03")  # Alice prova a restituire un libro che non ha

print("\n--- Libri disponibili dopo restituzioni ---")
print(lib.list_available_books())  # dovrebbe mostrare B01 e B03

print("\n--- Prestiti membri dopo restituzioni ---")
print("Lorenzo:", lib.list_member_loans("M01"))  # []
print("Alice:", lib.list_member_loans("M02"))    # ['B02']
