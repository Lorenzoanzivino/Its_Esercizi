'''Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
    - Film: Rappresenta un film con titolo e durata.
 
    - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

        Metodi:
        - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
        - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
    - Cinema: Gestisce le operazioni legate alla gestione delle sale.

        Metodi:
        - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
        - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:
    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.'''


from datetime import time

class Film:
    # Non ritorna nulla, Inizializza solo gli oggetti
    # Non serve il return alla fine, sto già creando l'oggetto film

    def __init__(self, titolo_film:str, durata: time): 
        self.titolo_film = titolo_film
        self.durata = durata

class Sala:
    # In argomento passo film di tipo Film che richiama la classe Film che crea l'oggetto
    # Posti_prenotati inizializzato internamente, nessun argomento necessario

    def __init__(self, numero_sala:int, film:Film, posti_totali:int):
        self.numero_sala: int = numero_sala
        self.film: Film = film
        self.posti_totali: int = posti_totali
        self.posti_prenotati: int = 0 
        pass

    def prenota_posti(self, num_posti: int) -> str:
        if num_posti <= self.posti_disponibili():
            self.posti_prenotati += num_posti
            return "· Prenotazione confermata"
        else:
            return "· Posti insufficienti per la prenotazione"

    def posti_disponibili(self) -> int:
        posti_liberi: int = self.posti_totali - self.posti_prenotati
        return posti_liberi
    
    def posti_occupati(self) -> int:
        return self.posti_prenotati
    
    
class Cinema:
    # Creo un dizionario vuoto per inserire key = numero_sala, value = attributi classe Sala
    def __init__(self):
        self.sale: dict = {}

    def aggiungi_sala(self, sala:Sala) -> str:
        if sala.numero_sala in self.sale:
            return f"· Sala: {sala.numero_sala} già esistente"
        else:
            self.sale[sala.numero_sala] = sala
            return f"· Sala: {sala.numero_sala} aggiunta con successo"
        
    
    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        # Cerca una sala in cui è proiettato il film

        for sala in self.sale.values(): # Scorre le sale presenti nel dizionario 'sale' del cinema
            if sala.film.titolo_film == titolo_film: # Controlla se il film nella sala ha il titolo richiesto
                return sala.prenota_posti(num_posti) # Se il film corrisponde, tenta la prenotazione dei posti
            
        return "· Errore! Film non trovato"


# --- Setup ---

film1 = Film("Matrix", time(hour=2, minute=16))
film2 = Film("Inception", time(hour=2, minute=28))

sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 2)  # Sala con pochi posti per test overflow

cinema = Cinema()
print(cinema.aggiungi_sala(sala1))
print(cinema.aggiungi_sala(sala2))

# --- Test: prenotazione normale ---
print("· Il cliente vuole prenotare 3 posti per il film 'Matrix'")
print(cinema.prenota_film("Matrix", 3))
print(f"· Posti occupati sala 1: {sala1.posti_occupati()}")
print(f"· Posti disponibili sala 1: {sala1.posti_disponibili()}")

# --- Test: film non esistente ---
print("\n· Il cliente vuole prenotare posti per il film 'Avatar' (non in programmazione)")
print(cinema.prenota_film("Avatar", 2))

# --- Test: posti insufficienti ---
print("\n· Il cliente vuole prenotare 3 posti per il film 'Inception' (solo 2 posti disponibili)")
print(cinema.prenota_film("Inception", 3))

# --- Test: prenotare esattamente i posti disponibili ---
print("\n· Il cliente vuole prenotare 2 posti per il film 'Inception'")
print(cinema.prenota_film("Inception", 2))
print(f"· Posti occupati sala 2: {sala2.posti_occupati()}")
print(f"· Posti disponibili sala 2: {sala2.posti_disponibili()}")

# --- Test: tentativo di prenotare posti in sala piena ---
print("\n· Il cliente vuole prenotare 1 posto per il film 'Inception' dopo che è piena")
print(cinema.prenota_film("Inception", 1))