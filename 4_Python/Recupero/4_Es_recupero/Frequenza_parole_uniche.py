'''Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il numero di occorrenze.
Requisiti:
    ● Suddividi l’input sugli spazi bianchi per ottenere i token.
    ● Normalizza ogni token:
        1. Converti in minuscolo.
        2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip() con un insieme di caratteri di punteggiatura).
    ● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della punteggiatura.
    ● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi interi.
        Esempio:
            text = "Hello, world! Hello... PYTHON? world."
            output = count_unique_words(text)
    ● # output == {'hello': 2, 'world': 2, 'python': 1}'''

def conta_parole_uniche(testo: str) -> dict[str, int]:
    punteggiatura:str = ".,;:!?()[]{}'\"-_/\\<>@#$%^&*+=~`|"
    parole:str = testo.split()
    frequenze: dict[str, int] = {}

    for parola in parole:
        parola = parola.lower()

        # Rimuovo punteggiatura iniziale
        while parola and parola[0] in punteggiatura:
            parola = parola[1:]

        # Rimuovo punteggiatura finale
        while parola and parola[-1] in punteggiatura:
            parola = parola[:-1]

        if parola != "":
            if parola in frequenze:
                frequenze[parola] += 1
            else:
                frequenze[parola] = 1

    return frequenze

# soluzione del Professore
'''Esempio: 
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}'''

# 1) rendere l'intera stringa una stringa minuscola
# 2) eliminare tutti i caratteri che non sono lettere e numeri
# 3) se la parola esiste faccio una cosa
# 4) se la parola non esiste ne faccio un'altra

from string import punctuation

def count_unique_words(text: str) -> dict[str, int] :

    words_frequencies: dict[str, int] = {}

    # 1) tutta la stringa diventerà minuscola
    text:str = text.lower()
    text_cleaned: str = ""

    # 1.2) verificare e creare una stringa nuova fatta solo di caratteri escludendo i c. speciali
    for carattere in text:
        if carattere.isalpha() or carattere.isdigit():
            text_cleaned += carattere

    # 2) ho splittato l'intera stringa ogni volta che incontro uno spazio in singoli token
    token_lists:list[str] = text_cleaned.split(" ")

    # 3) voglio pulire i singoli token dai caratteri
    for token in token_lists:

        if token in words_frequencies:
            words_frequencies[token] += 1
        else:
            words_frequencies[token] = 1

    return words_frequencies

text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
print(output)