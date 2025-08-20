'''4. Calcolatrice Semplice con Metodi Statici

Crea una classe Calcolatrice con metodi statici per somma, sottrazione, moltiplicazione e divisione.
Ogni metodo prende due numeri e restituisce il risultato.
Gestisci la divisione per zero con una stampa di errore.

Difficoltà: 4
Focus: metodi statici, eccezioni base'''

class Calcolatrice:
    def addizione(self, n1: int | float, n2: int | float) -> float:
        self.somma = float(f"{n1 + n2:.2f}")
        return self.somma   
    
    def sottrazione(self, n1: int | float, n2: int | float) -> float:
        self.sott = float(f"{n1 - n2:.2f}")
        return self.sott
    
    def moltiplicazione(self, n1: int | float, n2: int | float) -> float:
        self.prodotto = float(f"{n1 * n2:.2f}")
        return self.prodotto
    
    def divisione(self, numeratore: int | float, denominatore: int | float) -> float | None:
        if denominatore == 0:
            print("Errore: divisione per zero!")
            self.risultato = None
            return None
        else:
            self.risultato = float(f"{numeratore / denominatore:.2f}")
            return self.risultato


# Test
c = Calcolatrice()

c.addizione(5,5)
print(c.somma)
c.addizione(3,5)
print(c.somma)
c.addizione(3.5,5)
print(c.somma)

c.sottrazione(8, 2)
print(c.sott)
c.sottrazione(4, 8)
print(c.sott)
c.sottrazione(8.3, 2)
print(c.sott)

c.moltiplicazione(2, 5)
print(c.prodotto)
c.moltiplicazione(0, 5)
print(c.prodotto)

c.divisione(6, 2)
print(c.risultato)
c.divisione(2, 8)
print(c.risultato)
c.divisione(6, 0)
print(c.risultato)
