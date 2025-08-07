'''2. Conta le vocali

Chiedi all’utente una stringa e stampa quante vocali ci sono (a, e, i, o, u).

# Input: "ciao mondo"
# Output: 5'''

stringa:str = "ciao mondo"
vocali:str = "aeiou"
i=0

for char in stringa:
    if char in vocali:
        i += 1
print(i)