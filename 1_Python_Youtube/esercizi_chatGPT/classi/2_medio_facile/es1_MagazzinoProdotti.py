'''📦 Esercizio 1 – Magazzino Prodotti

Crea una classe Prodotto con:

    attributi: nome, prezzo, quantità

    metodo valore_totale() che restituisce il valore: prezzo * quantità

    metodo aggiungi_scorta(n) che aumenta la quantità

    metodo vendi(n) che diminuisce la quantità (ma non va sotto zero)

Crea poi una lista di oggetti Prodotto e stampa il valore totale del magazzino.'''


class Prodotto:
    _nome:str
    _prezzo:float
    _quantita:int

    def __init__(self, nome: str, prezzo: float, quantita: int) -> None:
        if prezzo <= 0:
            raise ValueError("Prezzo deve essere positivo")
        if quantita < 0:
            raise ValueError("Quantità non può essere negativa")
        self._nome = nome          # Uso underscore e resto coerente
        self._prezzo = prezzo
        self._quantita = quantita
    
    def get_nome(self) -> str:
        return self._nome
    
    def get_prezzo(self) -> float:
        return self._prezzo 

    def get_quantita(self) -> int:
        return self._quantita   
    
    def set_prezzo(self, prezzo: float) -> None:
        if prezzo <= 0:
            raise ValueError("Prezzo deve essere positivo")
        self._prezzo = prezzo
    
    def set_quantita(self, quantita: int) -> None:
        if quantita < 0:
            raise ValueError("Quantità non può essere negativa")
        self._quantita = quantita

    def __str__(self) -> str:
        return f"Prodotto: {self.get_nome()}, quantità: {self.get_quantita()} prezzo: {self.get_prezzo()}"
    
    def prezzo_totale(self) -> float:
        return self._prezzo * self._quantita
    
    def aggiungi_scorta(self, n:int) -> int:
        if n < 0:
            raise ValueError("Non puoi aggiungere in negativo")
        self._quantita += n

    def vendi(self, n:int) -> int:
        if n < 0:
            raise ValueError("Non puoi vendere in negativo")
        if self._quantita < n:
            raise ValueError("Non puoi vendere il prodotto")
        self._quantita -= n



if __name__ == "__main__":

    magazzino_dati:list[tuple] = [
        ("martello", 9.99, 5),
        ("trapano", 9.99, 10),
        ("cacciavite", 5.99, 15)
    ]

    magazzino = []

    for item in magazzino_dati:
        nome, prezzo, quantita = item
        prodotto = Prodotto(nome, prezzo, quantita)
        magazzino.append(prodotto)
    
    valore_totale_magazzino = 0
    for prodotto in magazzino:
        valore_totale_magazzino += prodotto.prezzo_totale()
    
    print(magazzino_dati)
    print(f"Valore totale del magazzino: {valore_totale_magazzino:.2f}€")