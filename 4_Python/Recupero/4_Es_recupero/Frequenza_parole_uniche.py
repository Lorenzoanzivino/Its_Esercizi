'''Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}
'''

def count_unique_words(text):
    # Elenco dei segni di punteggiatura da rimuovere
    punteggiatura = ".,;:!?()[]{}'\"-_/\\<>@#$%^&*+=~`|"

    parole = text.split()
    dizionario = {}

    for parola in parole:
        parola = parola.lower()
        # Rimuove i caratteri di punteggiatura solo ai bordi
        while parola and parola[0] in punteggiatura:
            parola = parola[1:]
        while parola and parola[-1] in punteggiatura:
            parola = parola[:-1]
        if parola != "":
            if parola in dizionario:
                dizionario[parola] += 1
            else:
                dizionario[parola] = 1
    return dizionario
