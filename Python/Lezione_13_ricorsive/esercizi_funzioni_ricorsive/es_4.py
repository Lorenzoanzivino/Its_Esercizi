'''Esercizio 4.

Scrivere una funzione ricorsiva recursiveDigitCounter che restituisca il numero di cifre di un numero intero n passato in input.
Sono permessi sia valori positivi che negativi per n.
Ad esempio, il numero -120 ha 3 cifre.
Non si tenga conto di eventuali zeri non significativi.

Suggerimento: per il calcolo delle cifre, fare un controllo se il valore assoluto di n sia minore di 10. In caso positivo, significa che il numero n ha una sola cifra. In caso negativo, significa che il numero n ha più cifre; dunque, dividere n per 10 per rimuovere l'ultima cifra e richiama ricorsivamente la funzione, fino a ottenere un numero con una sola cifra.'''


def recursiveDigitCounter(n:int) -> int:
    if abs(n) < 10: # abs = valore assoluto
        return 1
    
    else:
        return int(1 + recursiveDigitCounter(n/10))
    
print(f"Il numero 120 ha: {recursiveDigitCounter(-120)} cifre")
print(f"Il numero 2504 ha: {recursiveDigitCounter(2504)} cifre")