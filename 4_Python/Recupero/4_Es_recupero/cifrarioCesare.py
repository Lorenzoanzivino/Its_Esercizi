'''Cifrario di Cesare
Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste
a chi non possiede la chiave per decifrarle.
Immagina l’alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere
dell’alfabeto minuscole scrivendo from string import ascii_lowercase
Ogni lettera ha una posizione in questa lista:
● a è 1
● b è 2
● j è 10
● e così via…
Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero
positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
alla posizione della lettera cifrata.
● a con key = 2 diventa c
Se la chiave porta oltre la fine dell’alfabeto, si ricomincia dal principio:
● a con key = 28 diventa c
Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
all’indietro nell’alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:
● s è una stringa (lettera, parola, frase, ecc.).
● key è un numero intero positivo, la chiave del cifrario di Cesare.
La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.
Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o
decifrata.'''

# Spiegazione del % 26
# z ha indice 25
# 25 + 2 = 27 → dobbiamo tornare indietro all'inizio
# 27 % 26 = 1 → che corrisponde a 'b'

def caesar_cypher_encrypt(s: str, key: int) -> str:
    alphabet_lower: str = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result: str = ""

    for char in s:
        if char in alphabet_lower:
            pos: int = alphabet_lower.index(char)
            new_pos: int = (pos + key) % 26
            result += alphabet_lower[new_pos]
        elif char in alphabet_upper:
            pos: int = alphabet_upper.index(char)
            new_pos: int = (pos + key) % 26
            result += alphabet_upper[new_pos]
        else:
            result += char
    return result

def caesar_cypher_decrypt(s: str, key: int) -> str:
    alphabet_lower: str = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result: str = ""

    for char in s:
        if char in alphabet_lower:
            pos: int = alphabet_lower.index(char)
            new_pos: int = (pos - key) % 26
            result += alphabet_lower[new_pos]
        elif char in alphabet_upper:
            pos: int = alphabet_upper.index(char)
            new_pos: int = (pos - key) % 26
            result += alphabet_upper[new_pos]
        else:
            result += char
    return result
