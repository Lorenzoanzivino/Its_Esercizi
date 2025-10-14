'''ROT13 è un semplice cifrario di sostituzione delle lettere che sostituisce una lettera con le lettere 13 lettere dopo di essa nell'alfabeto. ROT13 è un esempio del cifrario di Cesare.

Creare una funzione che prende una stringa e restituisce la stringa cifrata con Rot13. Se ci sono numeri o caratteri speciali inclusi nella stringa, dovrebbero essere restituiti così come sono. Solo le lettere dell'alfabeto latino/inglese dovrebbero essere spostate, come nell'originale Rot13 "implementazione".

Si prega di notare che l'uso di codice di codifica è considerato un imbroglio.'''

def rot13(messaggio:str) -> str:
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    risultato = []

    for char in messaggio:
        # gestione minuscole
        if char in alfabeto:
            indice = alfabeto.index(char)
            indice_rot = (indice + 13) % 26
            risultato.append(alfabeto[indice_rot])
        # gestione maiuscole
        elif char.lower() in alfabeto:
            indice = alfabeto.index(char.lower())
            indice_rot = (indice + 13) % 26
            # ricostruisco maiuscola
            risultato.append(alfabeto[indice_rot].upper())
        else:
            # altri caratteri rimangono così
            risultato.append(char)

    return ''.join(risultato)

messaggio = "ciao come stai?"
print(rot13(messaggio))