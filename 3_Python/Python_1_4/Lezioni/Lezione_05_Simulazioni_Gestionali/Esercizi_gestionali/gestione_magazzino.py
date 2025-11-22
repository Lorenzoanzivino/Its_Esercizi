''' Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.
Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
Test case:
    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.'''


class Prodotto:
    def __init__(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità

    def __str__(self):
        return f"Prodotto: {self.nome}, Quantità: {self.quantità}"
        
class Magazzino:
    def  __init__(self):
        self.listaProdotti: dict[str, int] = {}
    
    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome not in self.listaProdotti:
            self.listaProdotti[prodotto.nome] = prodotto.quantità
            return f"· Prodotto: {prodotto.nome}, quantità: {prodotto.quantità} aggiunto con successo"
        else:
            return f"· Prodotto: {prodotto.nome} già esistente"
        
    def cerca_prodotto(self, nome: str) -> Prodotto:
        if nome in self.listaProdotti:
            quantità = self.listaProdotti[nome]
            return f"· {Prodotto(nome, quantità)}"
        else:
            return f"· Errore! il prodotto: {nome} non esiste" 
        
    def verifica_disponibilità(self, nome: str) -> str:
        if nome in self.listaProdotti:
            quantità = self.listaProdotti[nome]
            if quantità > 0:
                return f"· Il: {nome} è disponibile (quantità: {quantità})"
            else:
                return f"· Il: {nome} non è disponibile (esaurito)"
        else:
            return f"· Il: {nome} non è disponibile"


prodotto1 = Prodotto("Martello", 3)
prodotto2 = Prodotto("Cacciavite", 0)

magazzino = Magazzino()
print("\nAggiungi prodotto: ")
print(magazzino.aggiungi_prodotto(prodotto1))
print(magazzino.aggiungi_prodotto(prodotto2))

print("\nCerca prodotto: ")
print(magazzino.cerca_prodotto("Martello"))
print(magazzino.cerca_prodotto("Tavolo"))

print("\nVerifica disponibilità: ")
print(magazzino.verifica_disponibilità("Martello"))
print(magazzino.verifica_disponibilità("Cacciavite"))
print(magazzino.verifica_disponibilità("Tavolo"))
