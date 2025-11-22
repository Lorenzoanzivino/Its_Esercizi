'''es 5.Calcolatrice Interattiva

Devi sviluppare una calcolatrice interattiva con almeno 10 casi di test usando UnitTest, cercando di coprire tutti i possibili percorsi di esecuzione.

L'input dell'utente è una formula composta da:

    Un numero

    Un operatore (+ o -)

    Un altro numero

L'input è separato da spazi bianchi (esempio: 1 + 1).
Gestione degli errori:

    Se l'input non è composto da 3 elementi, solleva un'eccezione personalizzata FormulaError.

    Prova a convertire il primo e il terzo input in un numero decimale (float). Se si verifica un errore (ValueError), solleva FormulaError.

    Se il secondo elemento non è '+' o '-', solleva FormulaError.

    Se l'input è valido, esegui il calcolo e stampa il risultato.

    Il programma continua a chiedere nuovi input fino a quando l'utente scrive "quit".'''


class FormulaError(Exception):
    pass

def calcola(formula):
    parti = formula.strip().split()
    if len(parti) != 3:
        raise FormulaError("La formula deve contenere 3 elementi.")
    
    num1_str, operatore, num2_str = parti
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        raise FormulaError("I numeri devono essere validi numeri decimali.")
    
    if operatore not in ('+', '-'):
        raise FormulaError("Operatore non valido. Usa '+' o '-'.")
    
    if operatore == '+':
        return num1 + num2
    else:
        return num1 - num2

def calcolatrice_interattiva():
    while True:
        formula = input("Inserisci formula (es. 1 + 1) o 'quit' per uscire: ")
        if formula.lower() == 'quit':
            print("Calcolatrice terminata.")
            break
        try:
            risultato = calcola(formula)
            print("Risultato:", risultato)
        except FormulaError as e:
            print("Errore:", e)


# Se vuoi far partire la calcolatrice, decommenta la riga qui sotto
# calcolatrice_interattiva()


# Test con unittest

import unittest

class TestCalcolatrice(unittest.TestCase):
    def test_somma_base(self):
        self.assertEqual(calcola("1 + 1"), 2)

    def test_sottrazione_base(self):
        self.assertEqual(calcola("5 - 3"), 2)

    def test_spazi_extra(self):
        self.assertEqual(calcola("  10   +   20 "), 30)

    def test_float(self):
        self.assertAlmostEqual(calcola("2.5 + 3.1"), 5.6)

    def test_negativi(self):
        self.assertEqual(calcola("-1 + -2"), -3)

    def test_operatore_non_valido(self):
        with self.assertRaises(FormulaError):
            calcola("1 * 2")

    def test_input_meno_di_3_elementi(self):
        with self.assertRaises(FormulaError):
            calcola("1 +")

    def test_input_piu_di_3_elementi(self):
        with self.assertRaises(FormulaError):
            calcola("1 + 2 + 3")

    def test_numero_non_valido(self):
        with self.assertRaises(FormulaError):
            calcola("a + 2")

    def test_numero_non_valido_secondo_numero(self):
        with self.assertRaises(FormulaError):
            calcola("2 + b")

if __name__ == '__main__':
    unittest.main()