'''Esercizio: Gestore di Prodotti
Descrizione:
Crea una classe Prodotto con attributi: nome (stringa), prezzo (float), quantità (intero).

Crea una classe Magazzino che contiene una lista di prodotti e permette di:
    aggiungere un prodotto (se il prodotto con quel nome esiste già, aggiorna la quantità),
    rimuovere un prodotto per nome,
    cercare un prodotto per nome e restituirlo,
    stampare la lista completa dei prodotti,
    aggiornare il prezzo di un prodotto dato il nome.

Obiettivi:
    Definire le classi con metodi base (__init__, getter/setter, __str__).
    Gestire una lista di oggetti Prodotto dentro Magazzino.
    Implementare metodi di ricerca e modifica.
    Gestire casi di prodotti duplicati e aggiornare quantità.'''

class Prodotto:
    _nome:str
    _prezzo:float
    _quantita:int
    
    def __init__(self, nome:str, prezzo:float, quantita:int)->None:
        self._nome = nome
        self.set_prezzo(prezzo)
        self.set_quantita(quantita)
    
    def get_nome(self)-> str:
        return self._nome
    
    def get_prezzo(self)-> float:
        return self._prezzo
    
    def get_quantita(self)-> int:
        return self._quantita
    
    def set_prezzo(self, nuovo_prezzo:float):
        if nuovo_prezzo < 0:
            raise ValueError("Il prezzo non può essere negativo")
        self._prezzo = nuovo_prezzo

    def set_quantita(self, nuova_quantita: int):
        if nuova_quantita < 0:
            raise ValueError("La quantità non può essere negativa")
        self._quantita = nuova_quantita

    def prezzoTotale(self, somma:float = 0):
        somma = self.get_prezzo() * self.get_quantita()
        return somma

    def __str__(self):
        return f"prodotto: {self.get_nome()}\nprezzo: {self.get_prezzo():.2f}\nquantita: {self.get_quantita()}\ntotale: {self.prezzoTotale():.2f}"


    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return False
        if self.get_nome() == other.get_nome():
            return True
        return False


class Magazzino:
    def __init__(self):
        self._listaProdotti = []

    def aggiungiProdotto(self, prodotto: Prodotto):
        for elemento in self._listaProdotti:
            if elemento.get_nome() == prodotto.get_nome():
                nuova_quantita = elemento.get_quantita() + prodotto.get_quantita()
                elemento.set_quantita(nuova_quantita)
                return f"Esistente: {prodotto.get_nome()}, quantità aggiornata"
        self._listaProdotti.append(prodotto)
        return f"Aggiunto: {prodotto.__str__()}"
    
    def rimuovi_prodotto(self, prodotto: Prodotto):
        for elemento in self._listaProdotti:
            if elemento.get_nome() == prodotto.get_nome():
                self._listaProdotti.remove(elemento)
                return f"Eliminato: {prodotto.get_nome()}"
        return f"Inesistente: {prodotto.get_nome()}"
    
    def cerca(self, nome: str):
        for elemento in self._listaProdotti:
            if elemento.get_nome() == nome:
                return f"\nRisultato ricerca: {elemento}"
        return None  # se non lo trovi
    
    def __str__(self):
        if not self._listaProdotti:
            return "Magazzino vuoto"
        return "\n".join(str(p) for p in self._listaProdotti)



magazzino = Magazzino()

p1 = Prodotto("Martello", 9.99, 10)
print(magazzino.aggiungiProdotto(p1))  # Prodotto aggiunto

p2 = Prodotto("Trapano", 11.99, 10)
print(magazzino.aggiungiProdotto(p2))  # Prodotto aggiunto

p3 = Prodotto("Cacciaviti", 5.99, 15)
print(magazzino.aggiungiProdotto(p3))  # Prodotto aggiunto

print(magazzino.rimuovi_prodotto(p3))  # Prodotto eliminato

p4 = Prodotto("Martello", 9.99, 10)
print(magazzino.aggiungiProdotto(p4))  # Prodotto esistente, quantità aggiornata

print(magazzino)

print(magazzino.cerca("Martello"))
