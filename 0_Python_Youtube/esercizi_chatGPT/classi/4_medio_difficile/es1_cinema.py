'''1. Sistema di Prenotazioni per un Cinema

Crea una classe Film con attributi: titolo, durata, e una lista di orari di proiezione.
Crea una classe Sala con numero di posti e lista delle prenotazioni (posti occupati per ogni orario).
Crea una classe Prenotazione che lega utente, film, sala, orario e numero di posti prenotati.
Implementa metodi per prenotare posti, controllare disponibilità, cancellare prenotazioni e stampare il programma del cinema.'''

from datetime import datetime, timedelta, time

# Date = Date
# Datetime = Date e Orari
# Timedelta = Durata

class Film:
    _titolo:str
    _durata:timedelta
    _orari_proiezione:list[time]

    def __init__(self, titolo:str, durata:timedelta) -> None:
        self._titolo = titolo
        self._durata = durata
        self._orari_proiezione = []

    def get_titolo(self) -> str:
        return self._titolo
    
    def get_durata(self) -> str:
        totale_secondi = int(self._durata.total_seconds())
        ore = totale_secondi // 3600
        secondi_residui = totale_secondi % 3600
        minuti = secondi_residui // 60
        secondi = secondi_residui % 60

        return f"{ore}h {minuti}m {secondi}s"
    
    def get_orari_proiezione(self) -> str:
        orari_stringhe:list = []
        for orario in self._orari_proiezione:
            orari_stringhe.append(str(orario))

        return ", ".join(orari_stringhe)
    
    def aggiungi_orario(self, orario: time) -> None:
        self._orari_proiezione.append(orario)
    
    def __str__(self) -> str:
        return f"film: {self.get_titolo()}, durata: {self.get_durata()}, orari: {self.get_orari_proiezione()}"


class Sala:
    _numero_posti:int
    _prenotazioni:dict[time, int]

    def __init__(self, numero_posti:int = 50) -> None:
        self._numero_posti = numero_posti
        self._prenotazioni = {}

    def get_numero_posti(self) -> int:
        return self._numero_posti
    
    def posti_disponibili(self, orario: time) -> int:
        if orario in self._prenotazioni:
            occupati = self._prenotazioni[orario]
        else:
            occupati = 0
        return self._numero_posti - occupati
    
    def prenota(self, orario:time, posti:int) -> bool:
        disponibili = self.posti_disponibili(orario)
        if posti <= disponibili:
            if orario in self._prenotazioni:
                self._prenotazioni[orario] += posti
            else:
                self._prenotazioni[orario] = posti
            return True
        return False
    
    def cancella_prenotazione(self, orario: time, posti: int) -> None:
        if orario in self._prenotazioni:
            self._prenotazioni[orario] -= posti
            if self._prenotazioni[orario] <= 0:
                del self._prenotazioni[orario]


class Prenotazione:
    _utente:str
    _film:Film
    _sala:Sala
    _orario:datetime
    _posti:int
    
    def __init__(self, utente: str, film: Film, sala: Sala, orario: datetime, posti: int):
        self._utente = utente
        self._film = film
        self._sala = sala
        self._orario = orario
        self._posti = posti



if __name__ == "__main__":
    # Creo film
    film1 = Film("DragonBall", timedelta(hours=1, minutes=30))
    film1.aggiungi_orario(time(16, 30))
    film1.aggiungi_orario(time(18, 0))
    film1.aggiungi_orario(time(19, 30))

    film2 = Film("Matrix", timedelta(hours=2))
    film2.aggiungi_orario(time(17, 0))
    film2.aggiungi_orario(time(20, 0))

    # Creo sale
    sala1 = Sala(numero_posti=100)
    sala2 = Sala(numero_posti=50)

    # Lista prenotazioni (per tenerle in memoria)
    prenotazioni = []

    # Provo a prenotare su sala1
    if sala1.prenota(time(16, 30), 5):
        prenotazioni.append(Prenotazione("Lorenzo", film1, sala1, time(16, 30), 5))
        print("Prenotazione per Lorenzo confermata.")

    if sala1.prenota(time(18, 0), 10):
        prenotazioni.append(Prenotazione("Anna", film1, sala1, time(18, 0), 10))
        print("Prenotazione per Anna confermata.")

    if not sala1.prenota(time(16, 30), 97):  # Provo a prenotare più posti di quelli disponibili
        print("Prenotazione per Marco fallita: posti insufficienti.")

    # Prenotazione in sala2
    if sala2.prenota(time(17, 0), 30):
        prenotazioni.append(Prenotazione("Giulia", film2, sala2, time(17, 0), 30))
        print("Prenotazione per Giulia confermata.")

    # Stampa stato sala e disponibilità
    print("\nStato Sala 1:")
    for orario in film1._orari_proiezione:
        disp = sala1.posti_disponibili(orario)
        print(f"Orario {orario}: posti disponibili {disp} / {sala1.get_numero_posti()}")

    print("\nStato Sala 2:")
    for orario in film2._orari_proiezione:
        disp = sala2.posti_disponibili(orario)
        print(f"Orario {orario}: posti disponibili {disp} / {sala2.get_numero_posti()}")

    # Stampa prenotazioni
    print("\nPrenotazioni attive:")
    for p in prenotazioni:
        print(f"{p._utente} ha prenotato {p._posti} posti per '{p._film.get_titolo()}' alle {p._orario}")

    # Cancelliamo la prenotazione di Anna
    print("\nCancello prenotazione di Anna...")
    for p in prenotazioni:
        if p._utente == "Anna":
            p._sala.cancella_prenotazione(p._orario, p._posti)
            prenotazioni.remove(p)
            break

    # Stampa stato sala dopo cancellazione
    print("\nStato Sala 1 dopo cancellazione:")
    for orario in film1._orari_proiezione:
        disp = sala1.posti_disponibili(orario)
        print(f"Orario {orario}: posti disponibili {disp} / {sala1.get_numero_posti()}")

    # Stampa prenotazioni aggiornate
    print("\nPrenotazioni attive dopo cancellazione:")
    for p in prenotazioni:
        print(f"{p._utente} ha prenotato {p._posti} posti per '{p._film.get_titolo()}' alle {p._orario}")
