'''Data una serie di parole, devi trovare la parola con il punteggio più alto.

Ogni lettera di una parola segna in base alla sua posizione nell'alfabeto: a = 1, b = 2, c = 3- ecc.

Ad esempio, il punteggio di abadSi è 8(1 + 2 + 1 + 4).

È necessario restituire la parola con il punteggio più alto come una stringa.

Se due parole segnano lo stesso, restituisci la parola che appare prima nella stringa originale.

Tutte le lettere saranno minuscole e tutti gli input saranno validi.
'''

def high(parola):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    parola_nuova = parola.split()  # lista di parole dalla stringa

    max_valore = 0
    parola_max = ""

    for p in parola_nuova:
        valore = 0
        for lettera in p:
            valore += alfabeto.index(lettera) + 1

        if valore > max_valore:
            max_valore = valore
            parola_max = p

    return parola_max

# esempio
print(high("abadSi taxi volcano semynak aa b bb d aaa".lower()))