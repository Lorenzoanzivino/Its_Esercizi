'''4. Calcolatrice Semplice con Metodi Statici

Crea una classe Calcolatrice con metodi statici per somma, sottrazione, moltiplicazione e divisione.
Ogni metodo prende due numeri e restituisce il risultato.
Gestisci la divisione per zero con una stampa di errore.

Difficoltà: 4
Focus: metodi statici, eccezioni base'''

class Calcolatrice:
    @staticmethod
    def addizione(n1: int | float, n2: int | float) -> int | float:
        return n1 + n2

    @staticmethod
    def sottrazione(n1: int | float, n2: int | float) -> int | float:
        return n1 - n2

    @staticmethod
    def moltiplicazione(n1: int | float, n2: int | float) -> int | float:
        return n1 * n2

    @staticmethod
    def divisione(n1: int | float, n2: int | float) -> int | float | None:
        if n2 == 0:
            print("Errore! Divisione per zero.")
            return None
        return n1 / n2


# Uso senza istanza (oppure con, ma non serve)
print(Calcolatrice.addizione(5, 5))
print(Calcolatrice.sottrazione(8, 2))
print(Calcolatrice.moltiplicazione(2, 5))
print(Calcolatrice.divisione(6, 2))
print(Calcolatrice.divisione(6, 0))  # None
