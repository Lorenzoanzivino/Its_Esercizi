'''3. Gestione Base di un Negozio

Crea una classe Prodotto con nome, prezzo e quantità disponibile.
Crea una classe Negozio che tiene una lista di prodotti e permette di:

    aggiungere nuovi prodotti

    vendere un prodotto (riducendo la quantità)

    mostrare i prodotti esauriti

    mostrare il valore totale dell’inventario (prezzo * quantità)

Difficoltà: 5
Focus: oggetti, gestione stato (quantità), metodi più articolati
'''

class Prodotto:
    _nome: str
    _prezzo: float
    _quantita: int

    def __init__(self, nome: str, prezzo: float, quantita: int) -> None:
        self._nome = nome
        if prezzo <= 0:
            raise ValueError("Il prezzo non può essere negativo o zero")
        self._prezzo = prezzo
        if quantita <= 0:
            raise ValueError("Prodotto esaurito")
        self._quantita = quantita

    def get_nome(self) -> str:
        return self._nome

    def get_prezzo(self) -> float:
        return self._prezzo

    def get_quantita(self) -> int:
        return self._quantita

    def __str__(self) -> str:
        return f"Prodotto: {self.get_nome()} - Prezzo: {self.get_prezzo():.2f}€ - Quantità: {self.get_quantita()}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Prodotto):
            return False
        return self.get_nome() == other.get_nome()


class Negozio:
    _listaProdotti: list

    def __init__(self) -> None:
        self._listaProdotti = []

    def aggiungiProdotto(self, prodotto: Prodotto) -> None:
        for p in self._listaProdotti:
            if p.get_nome() == prodotto.get_nome():
                p._quantita += prodotto.get_quantita()
                print(f"Aggiunta quantità: {p.get_quantita()} unità di {p.get_nome()}")
                return
        self._listaProdotti.append(prodotto)
        print(f"Aggiunto nuovo prodotto: {prodotto}")

    def vendiProdotto(self, prodotto: Prodotto, numero: int) -> bool:
        for p in self._listaProdotti:
            if p.get_nome() == prodotto.get_nome():
                if numero > p.get_quantita():
                    print(f"Quantità insufficiente per vendere {numero} unità di {p.get_nome()}")
                    return False
                p._quantita -= numero
                print(f"\nVendute {numero} unità di {p.get_nome()} - Rimanenti: {p.get_quantita()}")
                return True
        print(f"Prodotto {prodotto.get_nome()} non trovato")
        return False

    def prodottiEsauriti(self) -> list[str]:
        esauriti: list[str] = []
        for p in self._listaProdotti:
            if p.get_quantita() == 0:
                esauriti.append(p.get_nome())
        return esauriti

    def totaleProdotto(self, prodotto: Prodotto) -> float:
        for p in self._listaProdotti:
            if p.get_nome() == prodotto.get_nome():
                return p.get_prezzo() * p.get_quantita()
        return 0.0

    def infoNegozio(self) -> list[Prodotto]:
        return self._listaProdotti


# Esempio di utilizzo
negozio = Negozio()

p1 = Prodotto("Trapano", 5.99, 10)
p2 = Prodotto("Cacciavite", 5.99, 10)
p3 = Prodotto("Viti", 0.99, 50)

negozio.aggiungiProdotto(p1)
negozio.aggiungiProdotto(p2)
negozio.aggiungiProdotto(p3)

negozio.vendiProdotto(p3, 40)
negozio.vendiProdotto(p3, 15)  # Non sufficiente
negozio.vendiProdotto(p3, 10)
negozio.vendiProdotto(p1, 10)

print("\nProdotti esauriti:")
for nome in negozio.prodottiEsauriti():
    print(f"- {nome}")

print("\nTotale per prodotto:")
for prodotto in negozio.infoNegozio():
    print(f"{prodotto.get_nome()}: {negozio.totaleProdotto(prodotto):.2f}€")
