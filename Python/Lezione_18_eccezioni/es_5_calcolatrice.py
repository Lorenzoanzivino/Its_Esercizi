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