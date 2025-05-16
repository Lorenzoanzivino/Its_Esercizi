'''
Esercizio 10.

Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".'''

def charDuplicator(s):
    # Caso base: se la stringa è vuota, ritorna stringa vuota
    if s == "":
        return ""
    else:
        # Duplica il primo carattere e chiama ricorsivamente sulla sottostringa rimanente
        return s[0]*2 + charDuplicator(s[1:])

# Esempio di utilizzo
input_str = "libro"
output_str = charDuplicator(input_str)
print(output_str)  # Stampa: lliibbrroo
