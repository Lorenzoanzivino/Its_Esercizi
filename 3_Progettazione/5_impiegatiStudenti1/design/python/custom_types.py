from typing import Self, Any
import re


class CodiceVolo(str):
    # Gli oggetti di questa classe *sono* stringhe
    #  che rispettano il formato dei codici dei voli: XY1234
    def __new__(cls, cv: str) -> Self:
        cv: str = cv.upper().strip()  # rendo la stringa maiuscola e senza spazi iniziali e finali
        if re.fullmatch(r'^[A-Z0-9]{2}\d{4}$', cv):
            return super().__new__(cls, cv)

        raise ValueError(f"La stringa '{cv}' non è un codice valido per un volo!")


class CodiceIATA(str):
    def __new__(cls, c: str) -> Self:
        if re.fullmatch(r'^[A-Z]{3}$', c):
            return super().__new__(cls, c)
        raise ValueError(f"La stringa '{c}' non è un codice IATA valido per un aeroporto!")


class IntGE1900(int):
    # Tipo di dato specializzato Intero >= 1900
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n >= 1900:
            return n
        raise ValueError(f"Il valore {n} è minore di 1900!")


class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0 (Greater than or Equal to Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n >= 0:
            return n
        raise ValueError(f"Il valore {n} è minore di 0!")


class IntGZ(int):
    # Tipo di dato specializzato Intero > 0 (Greater than Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n > 0:
            return n
        raise ValueError(f"Il valore {n} non è positivo!")
    

class RealGEZ(float):
    # Tipo di dato specializzato float >= 0 (Greater than or Equal to Zero)
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        n: float = super().__new__(cls, v)  # prova a convertire v in un float
        if n >= 0:
            return n
        raise ValueError(f"Il valore {n} è minore di 0!")


# IMPORT E MODULI DI BASE
'''Importazione di moduli standard per gestione date, enumerazioni e validazione tramite espressioni regolari'''

from datetime import date
from enum import StrEnum
import re


# CLASSE STRINGA
'''Classe di utilità per validare che un valore sia una stringa non vuota'''

class Stringa:
    @staticmethod
    def valida(valore):
        if not isinstance(valore, str):
            raise ValueError("Il valore deve essere una stringa")
        if not valore.strip():
            raise ValueError("La stringa non può essere vuota o solo spazi")
        return valore


# CLASSE INDIRIZZO
'''Rappresenta un indirizzo con via, civico e CAP validato'''

class Indirizzo:
    _via: str
    _civico: int

    def __init__(self, via:str, civico:int, cap: str) -> None:
        self._via: str = Stringa.valida(via)
        self._civico: int = civico

        # Converti prima in stringa, poi fai i controlli:
        cap_str = str(cap)

        if len(cap_str) != 5 or not cap_str.isdigit():
            raise ValueError("Il CAP deve essere una stringa di 5 cifre numeriche")

        self._cap = cap_str

    def via(self) -> str:
        return self._via
    def civico(self) -> int:
        return self._civico
    def cap(self) -> str:
        return self._cap
    def __str__(self) -> str:
        return f"{self.via()}, {self.civico()}, CAP: {self.cap()}"
    def __eq__(self, other) -> bool:
        if not isinstance(other, Indirizzo):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())
    def __hash__(self)->int: 
        return hash((self.via(), self.civico(), self.cap()))


# CLASSE PARTITA IVA - TELEFONO - EMAIL - CF - RegEx
'''Valida e rappresenta una partita IVA (11 cifre numeriche)'''

class PartitaIVA:
    pattern = re.compile(r'^\d{11}$')
    
    def __init__(self, partitaiva: str):
        if not self.is_valid(partitaiva):
            raise ValueError(f"Partitaiva non valida: {partitaiva}")
        self.partitaiva = partitaiva

    @classmethod
    def is_valid(cls, partitaiva: str) -> bool:
        return bool(cls.pattern.fullmatch(partitaiva))

class Telefono:
    pattern = re.compile(r'^\+?\d{6,15}$')

    def __init__(self, telefono: str):
        if not self.is_valid(telefono):
            raise ValueError(f"telefono non valido: {telefono}")
        self.telefono = telefono

    @classmethod
    def is_valid(cls, telefono: str) -> bool:
        return bool(cls.pattern.fullmatch(telefono))

class Email:
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    def __init__(self, email: str):
        if not self.is_valid(email):
            raise ValueError(f"Email non valida: {email}")
        self.value = email

    @classmethod
    def is_valid(cls, email: str) -> bool:
        return bool(cls.pattern.match(email))

class CodiceFiscale:
    pattern = re.compile(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$')

    def __init__(self, cf: str):
        if not self.is_valid(cf):
            raise ValueError(f"Codice fiscale non valido: {cf}")
        self.cf = cf

    @classmethod
    def is_valid(cls, cf: str) -> bool:
        return bool(cls.pattern.fullmatch(cf))
    
    def __str__(self):
        return self.cf


# CLASSE STATO ORDINE - StrEnum
'''Stato dell’ordine: in preparazione, inviato, da saldare, saldato'''

class StatoOrdine(StrEnum):
    IN_PREPARAZIONE = "inPreparazione"
    INVIATO = "inviato"
    DA_SALDARE = "daSaldare"
    SALDATO = "saldato"
