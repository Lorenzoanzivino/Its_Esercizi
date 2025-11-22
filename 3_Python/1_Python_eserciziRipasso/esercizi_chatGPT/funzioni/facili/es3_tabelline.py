'''3. Tabellina

Chiedi all’utente un numero e stampa la tabellina di quel numero fino a 10.

# Input: 3
# Output: 3 6 9 12 15 18 21 24 27 30'''

numero:int = int(input("Scegli un numero: "))
risultato = 0

for i in range(1, 11):
    risultato = numero * i
    print(risultato)