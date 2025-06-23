from __future__ import annotations
from custom_types import *
from datetime import date
from abc import ABC, abstractmethod

class Persona:
    __nome: str
    __cognome: str
    __cf: CodiceFiscale
    __dataNascita: date
    __is_uomo: bool
    __is_donna: bool
    __maternita: IntGEZ

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, dataNascita: date, 
                 is_uomo: bool = False, is_donna: bool = False, maternita: IntGEZ = 0):
        
        # Validazione coerenza genere
        if is_uomo == is_donna:
            raise ValueError("Errore: deve essere selezionato solo uno tra is_uomo o is_donna")
        
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self.set_dataNascita(dataNascita)
        self.set_is_uomo(is_uomo)
        self.set_is_donna(is_donna)

        # Maternità solo per donna
        if is_donna:
            self.set_maternita(maternita)
        else:
            self.__maternita = IntGEZ(0)  # valore neutro se uomo

    def get_nome(self) -> str:
        return self.__nome

    def get_cognome(self) -> str:
        return self.__cognome

    def get_cf(self) -> CodiceFiscale:
        return self.__cf

    def get_dataNascita(self) -> date:
        return self.__dataNascita

    def get_is_uomo(self) -> bool:
        return self.__is_uomo

    def get_is_donna(self) -> bool:
        return self.__is_donna

    def get_maternita(self) -> IntGEZ:
        return self.__maternita

    def set_nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Errore: il nome deve essere una stringa")

    def set_cognome(self, cognome: str) -> None:
        if isinstance(cognome, str):
            self.__cognome = cognome
        else:
            raise ValueError("Errore: il cognome deve essere una stringa")

    def set_cf(self, cf: CodiceFiscale) -> None:
        if isinstance(cf, CodiceFiscale):
            self.__cf = cf
        else:
            raise ValueError("Errore: Codice Fiscale non valido")

    def set_dataNascita(self, dataNascita: date) -> None:
        if isinstance(dataNascita, date):
            self.__dataNascita = dataNascita
        else:
            raise ValueError("Errore: la data di nascita deve essere un oggetto date")

    def set_is_uomo(self, is_uomo: bool) -> None:
        if isinstance(is_uomo, bool):
            self.__is_uomo = is_uomo
        else:
            raise ValueError("Errore: is_uomo deve essere un booleano")

    def set_is_donna(self, is_donna: bool) -> None:
        if isinstance(is_donna, bool):
            self.__is_donna = is_donna
        else:
            raise ValueError("Errore: is_donna deve essere un booleano")

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not isinstance(maternita, IntGEZ):
            raise ValueError("Errore: maternità deve essere un oggetto IntGEZ")
        if not self.__is_donna:
            raise ValueError("Errore: solo una donna può avere un valore di maternità")
        self.__maternita = maternita

    def __str__(self):
        genere = "Uomo" if self.get_is_uomo() else "Donna"
        maternita_str = f", maternità: {self.get_maternita()}"
        return (
            f"Nome: {self.get_nome()}\n"
            f"Cognome: {self.get_cognome()}\n"
            f"Codice Fiscale: {self.get_cf()}\n"
            f"Data di nascita: {self.get_dataNascita()}\n"
            f"Genere: {genere}{maternita_str}"
    )
    

class Studente(Persona):
    __matricola: IntGEZ

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, dataNascita: date,
                 is_uomo: bool, is_donna: bool, maternita:IntGEZ, matricola: IntGEZ):
        super().__init__(nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita)
        self.set_matricola(matricola)
        self._studenti:dict = {}
    
    def aggiungi_studente(self, studente: Studente):
        matricola = studente.get_matricola()
        if matricola in self._studenti:
            raise ValueError("Matricola già presente")
        self._studenti[matricola] = studente

    def rimuovi_studente(self, matricola: IntGEZ):
        if matricola in self._studenti:
            del self._studenti[matricola]

    def get_matricola(self) -> IntGEZ:
        return self.__matricola

    def set_matricola(self, matricola: IntGEZ) -> None:
        if not isinstance(matricola, IntGEZ):
            raise ValueError("Errore: matricola deve essere un oggetto IntGEZ")
        self.__matricola = matricola

    def __str__(self):
        return f"{super().__str__()}\nMatricola: {self.get_matricola()}"


class Impiegato(Persona, ABC):
    __stipendio: RealGEZ

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, dataNascita: date,
                 is_uomo: bool, is_donna: bool, maternita: IntGEZ, stipendio: RealGEZ):
        super().__init__(nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita)
        self.set_stipendio(stipendio)

    def get_stipendio(self) -> RealGEZ:
        return self.__stipendio

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        if not isinstance(stipendio, RealGEZ):
            raise ValueError("Errore: stipendio deve essere un oggetto RealGEZ")
        self.__stipendio = stipendio

    def __str__(self):
        return f"{super().__str__()}\nStipendio: {self.get_stipendio()}"



class Direttore(Impiegato):
    def __init__(self, nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita, stipendio):
        super().__init__(nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita, stipendio)

    def __str__(self):
        return f"Direttore:\n{super().__str__()}"


class Segretario(Impiegato):
    def __init__(self, nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita, stipendio):
        super().__init__(nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita, stipendio)

    def __str__(self):
        return f"Segretario:\n{super().__str__()}"
    

class Progettista(Impiegato):
    def __init__(self, nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita, stipendio, progetto):
        super().__init__(nome, cognome, cf, dataNascita, is_uomo, is_donna, maternita, stipendio)
        self.set_progetto(progetto)

    def get_progetto(self) -> Progetto:
        return self.__progetto

    def set_progetto(self, progetto: Progetto) -> None:
        if not isinstance(progetto, Progetto):
            raise ValueError("Errore: progetto deve essere un oggetto Progetto")
        self.__progetto = progetto
        progetto.add_progettista(self)

    def __str__(self):
        progetto_nome = self.get_progetto().get_nome() if self.get_progetto() else "Nessun progetto"
        return f"Progettista:\n{super().__str__()}\nProgetto: {progetto_nome}"


class Progetto:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__progettisti = []

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def add_progettista(self, progettista: 'Progettista') -> None:
        if progettista not in self.__progettisti:
            self.__progettisti.append(progettista)

    def remove_progettista(self, progettista: 'Progettista') -> None:
        if progettista in self.__progettisti:
            self.__progettisti.remove(progettista)

    def get_progettisti(self) -> list:
        return self.__progettisti
    
    def __str__(self):
        progettisti_nomi = ", ".join([f"{p.get_nome()} {p.get_cognome()}" for p in self.get_progettisti()])
        return f"Progetto: {self.get_nome()}\nProgettisti: {progettisti_nomi if progettisti_nomi else 'Nessun progettista'}"
