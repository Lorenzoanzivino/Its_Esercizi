'''Esercizio 3: Sistema di gestione della biblioteca

Crea una classe di libro contenente i seguenti attributi: titolo, autore, isbn. La classe di libri deve contenere i seguenti metodi:

    ?st?, metodo per restituire una rappresentazione delle stringhe del libro.

    Dastring, un metodo di classe per creare un'istanza del Libro da una stringa nel formato "title, author, isbn". Significa che è necessario utilizzare i cl di riferimento di classe per creare un nuovo oggetto della classe Book utilizzando una stringa.

Un esempio:

book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)

In questo caso, divina-commedia dovrebbe essere un'istanza della classe del libro con:

    Titolo originale - "La Divina Commedia"

    Autore - "D. Gli Alighieri"

    I miliardi di miliardi di "999000666"

Creare una classe di membri con i seguenti attributi: nome, member-id, mutuato-books. La classe membro deve contenere i seguenti metodi:

    Prelievo-book, per aggiungere un libro alla lista dei libri presi in prestito.

    Return-book, per rimuovere un libro dall'elenco dei libri presi in prestito.

    ?str?, metodo per restituire una rappresentazione delle stringhe del membro.

    from-string, un metodo di classe per creare un'istanza del Membro da una stringa nel formato "name, member-id". Significa che è necessario utilizzare i riferimenti di classe cl per creare un nuovo oggetto della classe Membro utilizzando una stringa.

Creare una classe di Libreria con i seguenti attributi: libri, membri, total-book (cioè un attributo di classe per tenere traccia del numero totale di istanze di Libro). La classe della biblioteca deve contenere i seguenti metodi:

    Add-book, per aggiungere un libro alla libreria e incrementare total-books.

    Rimuovi-libro, per rimuovere un libro dalla libreria e decrementare total-books.

    Registra-membro, per aggiungere un membro alla biblioteca.

    prestazioni, per prestare un libro ad un membro. Dovrebbe controllare se il libro è disponibile e se il socio è registrato.

    -str, metodo per restituire una rappresentazione delle stringhe della biblioteca con l'elenco dei libri e dei membri.

    . library-statistiche, un metodo di classe per stampare il numero totale di libri.

Infine, scrivi un semplice programma di driver. Dopo aver creato un libra r y, dovresti iniziare creando istanze di Libro e Membro. Ove appropriato, utilizzare metodi di classe (come da "string) per istanziare gli oggetti dalle stringhe, migliorando la chiarezza e la modularità.

Una volta creati gli oggetti, simula alcune operazioni di base della libreria:

    Registra nuovi membri alla biblioteca. Ciò potrebbe comportare l'aggiunta di oggetti membri a una collezione gestita dalla biblioteca.

    Aggiungi libri alla collezione della biblioteca.

    Prestare libri ai membri. Ciò comporterà la marcatura di un libro come preso in prestito e l'associazione con un membro specifico.

    Ad ogni passo significativo, stampa lo stato della libreria per tracciare come cambia:
        prima di prestare qualsiasi libro,
        Dopo che i libri sono stati prestati.'''