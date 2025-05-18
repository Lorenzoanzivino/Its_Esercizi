''' 🚀 Guida Python Completa: Come Costruire Programmi Modulari e Organizzati 🐍 '''

# Importazione del modulo 'time' dalla libreria 'datetime'
from datetime import time

# Step 1: Definizione della classe Film
# -------------------------------------
# Scopo: rappresentare un film con due proprietà fondamentali: il titolo e la durata.
# Nota: la durata viene rappresentata con un oggetto 'time' (solo ore e minuti).
class Film:
    # Step 1.1: Metodo costruttore __init__
    # - Serve per creare un oggetto Film con titolo e durata specifici.
    # - Parametri:
    #    - titolo_film (str): nome del film
    #    - durata (time): durata del film in ore e minuti
    def __init__(self, titolo_film: str, durata: time):
        self.titolo_film = titolo_film  # Attributo stringa che memorizza il titolo del film
        self.durata = durata            # Attributo oggetto time che memorizza la durata

# Step 2: Definizione della classe Sala
# ------------------------------------
# Scopo: rappresentare una sala del cinema che proietta un film,
# e gestire la capacità dei posti (totali e prenotati).
class Sala:
    # Step 2.1: Metodo costruttore __init__
    # - Inizializza la sala con numero identificativo, film e numero di posti totali.
    # - Inizializza i posti prenotati a zero.
    # - Parametri:
    #    - numero_sala (int): identificativo univoco della sala
    #    - film (Film): istanza di Film che viene proiettata in questa sala
    #    - posti_totali (int): numero massimo di posti disponibili
    def __init__(self, numero_sala: int, film: Film, posti_totali: int):
        self.numero_sala: int = numero_sala      # Attributo identificativo della sala
        self.film: Film = film                    # Attributo Film proiettato in sala
        self.posti_totali: int = posti_totali    # Attributo numero totale posti disponibili
        self.posti_prenotati: int = 0            # Attributo posti prenotati inizialmente 0
    
    # Step 2.2: Metodo prenota_posti(num_posti)
    # - Prova a prenotare un certo numero di posti.
    # - Se i posti richiesti sono disponibili, aggiorna posti_prenotati.
    # - Altrimenti ritorna un messaggio di errore.
    # - Parametri:
    #    - num_posti (int): numero di posti che si vuole prenotare
    # - Ritorna:
    #    - stringa messaggio di conferma o errore
    def prenota_posti(self, num_posti: int) -> str:
        # Step 2.2.1: Controlla se ci sono abbastanza posti disponibili
        if num_posti <= self.posti_disponibili():
            # Step 2.2.2: Prenota i posti richiesti sommando a quelli già prenotati
            self.posti_prenotati += num_posti
            return "· Prenotazione confermata"
        else:
            # Step 2.2.3: Se non ci sono abbastanza posti, ritorna messaggio errore
            return "· Posti insufficienti per la prenotazione"

    # Step 2.3: Metodo posti_disponibili()
    # - Calcola e ritorna quanti posti sono ancora liberi in sala.
    # - Non ha parametri.
    # - Ritorna:
    #    - int: posti liberi (totali - prenotati)
    def posti_disponibili(self) -> int:
        posti_liberi: int = self.posti_totali - self.posti_prenotati
        return posti_liberi

    # Step 2.4: Metodo posti_occupati()
    # - Ritorna quanti posti sono già prenotati.
    # - Utile per controllare lo stato attuale della sala.
    # - Non ha parametri.
    # - Ritorna:
    #    - int: posti prenotati
    def posti_occupati(self) -> int:
        return self.posti_prenotati

# Step 3: Definizione della classe Cinema
# ---------------------------------------
# Scopo: gestire un insieme di sale cinematografiche,
# permettere di aggiungere sale e prenotare posti per film in programmazione.
class Cinema:
    # Step 3.1: Metodo costruttore __init__
    # - Inizializza un dizionario vuoto che conterrà tutte le sale.
    # - Chiave del dizionario: numero sala (int)
    # - Valore: oggetto Sala
    def __init__(self):
        self.sale: dict = {}  # Dizionario vuoto per contenere le sale

    # Step 3.2: Metodo aggiungi_sala(sala)
    # - Permette di aggiungere una nuova sala al cinema.
    # - Prima controlla che non esista già una sala con lo stesso numero.
    # - Parametri:
    #    - sala (Sala): oggetto Sala da aggiungere
    # - Ritorna:
    #    - messaggio stringa di conferma o errore se la sala esiste già
    def aggiungi_sala(self, sala: Sala) -> str:
        if sala.numero_sala in self.sale:
            return f"· Sala: {sala.numero_sala} già esistente"
        else:
            self.sale[sala.numero_sala] = sala
            return f"· Sala: {sala.numero_sala} aggiunta con successo"

    # Step 3.3: Metodo prenota_film(titolo_film, num_posti)
    # - Permette di prenotare posti per un film specifico.
    # - Cerca tra tutte le sale quella che proietta il film richiesto.
    # - Se lo trova, chiama il metodo prenota_posti della sala.
    # - Se nessuna sala proietta quel film, ritorna messaggio di errore.
    # - Parametri:
    #    - titolo_film (str): titolo del film per cui si vuole prenotare
    #    - num_posti (int): numero di posti da prenotare
    # - Ritorna:
    #    - messaggio stringa di conferma o errore
    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.sale.values():
            if sala.film.titolo_film == titolo_film:
                return sala.prenota_posti(num_posti)
        return "· Errore! Film non trovato"

# Step 4: Creazione delle istanze di Film
# ---------------------------------------
# - Si crea un film "Matrix" con durata 2 ore e 16 minuti.
film1 = Film("Matrix", time(hour=2, minute=16))

# - Si crea un film "Inception" con durata 2 ore e 28 minuti.
film2 = Film("Inception", time(hour=2, minute=28))

# Step 5: Creazione delle istanze di Sala
# ---------------------------------------
# - Si crea una sala numero 1 con il film "Matrix" e 100 posti totali.
sala1 = Sala(1, film1, 100)

# - Si crea una sala numero 2 con il film "Inception" e solo 2 posti totali (per testare casi limite).
sala2 = Sala(2, film2, 2)

# Step 6: Creazione dell'istanza Cinema
# -------------------------------------
# - Si crea un oggetto Cinema che conterrà tutte le sale.
cinema = Cinema()

# Step 7: Aggiunta delle sale al cinema
# -------------------------------------
print(cinema.aggiungi_sala(sala1))  # Aggiunge sala1 e stampa conferma
print(cinema.aggiungi_sala(sala2))  # Aggiunge sala2 e stampa conferma

# Step 8: Test prenotazioni
# -------------------------
# - Proviamo a prenotare 3 posti per il film "Matrix"
print("· Il cliente vuole prenotare 3 posti per il film 'Matrix'")
print(cinema.prenota_film("Matrix", 3))  # Prenota 3 posti per Matrix
print(f"· Posti occupati sala 1: {sala1.posti_occupati()}")  # Verifica posti occupati
print(f"· Posti disponibili sala 1: {sala1.posti_disponibili()}")  # Verifica posti liberi

# - Prova a prenotare posti per un film non in programmazione ("Avatar")
print("\n· Il cliente vuole prenotare posti per il film 'Avatar' (non in programmazione)")
print(cinema.prenota_film("Avatar", 2))  # Film non trovato

# - Prova a prenotare più posti di quelli disponibili nella sala 2
print("\n· Il cliente vuole prenotare 3 posti per il film 'Inception' (solo 2 posti disponibili)")
print(cinema.prenota_film("Inception", 3))  # Posti insufficienti

# - Prenota esattamente i posti disponibili nella sala 2
print("\n· Il cliente vuole prenotare 2 posti per il film 'Inception'")
print(cinema.prenota_film("Inception", 2))  # Prenotazione ok
print(f"· Posti occupati sala 2: {sala2.posti_occupati()}")
print(f"· Posti disponibili sala 2: {sala2.posti_disponibili()}")

# - Prova a prenotare dopo che la sala è piena
print("\n· Il cliente vuole prenotare 1 posto per il film 'Inception' dopo che è piena")
print(cinema.prenota_film("Inception", 1))  # Posti insufficienti

# ------------------------------------------
# Fine script
# ------------------------------------------