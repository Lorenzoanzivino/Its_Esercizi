from __future__ import annotations  # va sempre al primo posto
from datetime import date

class Impiegato:
    _nome: str
    _cognome: str
    _dataNascita: date
    _stipendio: float
    _progetti_partecipa: set[Partecipa]  

    def __init__(self, *, nome: str, cognome: str, dataNascita: date, stipendio: float) -> None:
        self._nome = nome
        self._cognome = cognome
        self._dataNascita = dataNascita
        self._stipendio = stipendio
        self._progetti_partecipa = set()

    def __str__(self):
        return (f"Impiegato: {self._nome} {self._cognome}, Nato il: {self._dataNascita}, "
                f"Stipendio: {self._stipendio}, Progetti: {self._progetti_partecipa}")

    @staticmethod
    def valida_dataNascita(dataNascita: date):
        if dataNascita > date.today():
            raise ValueError("La data di nascita non può essere futura.")

    def add_progetto(self, progetto):  # progetto è un oggetto Progetto
        partecipazione = Partecipa(self, progetto)
        if partecipazione in self._progetti_partecipa:
            raise RuntimeError(f"Errore: progetto già presente per l'impiegato {self._nome}")
        self._progetti_partecipa.add(partecipazione)
        progetto.add_impiegati(self)


class Progetto:
    _nome: str # noto alla nascita
    _budget: float # noto alla nascita
    _impiegati_partecipano: set[Partecipa]

    def __init__(self, *, nome: str, budget: float) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati_partecipano = set()

    def set_nome(self, nome):
        self._nome = nome

    def set_budget(self, budget):
        self._budget = budget

    def add_impiegati(self, impiegato):  # impiegato è un oggetto Impiegato
        partecipazione = Partecipa(impiegato, self)
        if partecipazione in self._impiegati_partecipano:
            raise RuntimeError(f"Errore: impiegato già presente per il progetto {self._nome}")
        self._impiegati_partecipano.add(partecipazione)
        impiegato.add_progetto(self)


class Partecipa:
    _impiegato: 'Impiegato'
    _progetto: 'Progetto'
    _data_inizio: date

    def __init__(self, impiegato, progetto) -> None:
        self._impiegato = impiegato
        self._progetto = progetto
        self._data_inizio = date.today()

    def __eq__(self, other):
        if not isinstance(other, Partecipa):
            return NotImplemented
        return self._impiegato == other._impiegato and self._progetto == other._progetto

    def __hash__(self):
        return hash((self._impiegato, self._progetto))

    def __str__(self):
        return f"{self._impiegato._nome} in {self._progetto._nome} dal {self._data_inizio}"
