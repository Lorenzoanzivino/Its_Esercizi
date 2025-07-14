from __future__ import annotations
import weakref
from typing import Any, Self
from tipi_dati import RealGZ, RealGEZ, IntGEZ
from index import Index
from datetime import datetime
from abc import ABC, abstractmethod

class Utente(ABC):
    _id_usernames: Index[str, Self] = Index("Lista Username")
    _username: str  # <<imm>> {id}
    _registrazione: datetime  # <<imm>>

    @abstractmethod
    def __init__(self, username: str, registrazione: datetime):
        if username:
            self._id_usernames.add(username, self)
            self._username = username
        else:
            raise AttributeError("Value for attribute '_username' cannot be None or empty")
        self._registrazione = registrazione

    def get_username(self) -> str:
        return self._username

    def get_registrazione(self) -> datetime:
        return self._registrazione

    @classmethod
    def all(cls):
        return cls._id_usernames.all()

    @classmethod
    def get(cls, username: str):
        return cls._id_usernames.get(username)

    def __str__(self) -> str:
        return f"{self.get_username()} --- {self.get_registrazione()}"

class Privato(Utente):
    _done_bids: dict[Bid, bid_ut._link]

    def __init__(self, username, registrazione):
        super().__init__(username, registrazione)
        self._done_bids = dict()

    def bids(self) -> frozenset[weakref[bid_ut._link]]:
        return frozenset(weakref.ref(l) for l in self._done_bids.values())

    def _add_bid(self, link_with_bid: bid_ut._link) -> None:
        if link_with_bid.privato() is not self:
            raise ValueError("Link does not involve me!")
        if link_with_bid.bid() in self._done_bids:
            raise KeyError(f"Duplicate link ({self}, {link_with_bid.bid()}) not allowed")
        self._done_bids[link_with_bid.bid()] = link_with_bid

class Bid:
    _istante: datetime
    _privato: Privato
    _asta: Asta

    def __init__(self, istante_bid: datetime, privato: Privato, asta: Asta):
        self._istante = istante_bid
        self._privato = None
        self._asta = None
        bid_ut._add(self, privato)
        asta_bid._add(self, asta)

    def privato(self) -> weakref[Privato] | None:
        return weakref.ref(self._privato) if self._privato else None
    
    def asta(self) -> weakref[Asta] | None:
        return weakref.ref(self._asta) if self._asta else None

    def _set_privato(self, link_priv: bid_ut._link) -> None:
        if self.privato() is not None:
            raise ValueError("This bid is already in a link with another Privato")
        
        if link_priv.bid() is not self:
            raise ValueError("Link does not involve me!")

        self._privato = link_priv.privato()
    
    def _set_asta(self, link_asta: asta_bid._link) -> None:
        if self.asta() is not None:
            raise ValueError("This bid is already in a link with another Asta")
        
        if link_asta.bid() is not self:
            raise ValueError("Link does not involve me!")

        self._asta = link_asta.asta()

class bid_ut:
    class _link:
        def __init__(self, bid: Bid, privato: Privato):
            self._bid = bid
            self._privato = privato

        def bid(self) -> Bid:
            return self._bid

        def privato(self) -> Privato:
            return self._privato

    @classmethod
    def _add(cls, bid: Bid, privato: Privato) -> None:
        link = cls._link(bid, privato)
        bid._set_privato(link)
        privato._add_bid(link)

    # Link non rimuovibili

class PostOggetto(ABC):
    _descrizione: str
    _prezzo: RealGEZ
    _anni_garanzia: IntGEZ

    @abstractmethod
    def __init__(self, descrizione: str, anni_garanzia: IntGEZ, prezzo: RealGEZ):
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._prezzo = prezzo
    
    def descrizione(self) -> str:
        return self._descrizione
    
    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def prezzo(self) -> RealGEZ:
        return self._prezzo
    
    def set_descrizione(self, new_descrizione: str) -> None:
        self._descrizione = new_descrizione

    def set_anni_garanzia(self, new_garanzia: IntGEZ) -> None:
        self._anni_garanzia = new_garanzia

    @abstractmethod
    def __str__(self) -> str:
        pass

class Asta(PostOggetto):
    _prezzo_bid: RealGZ
    _scadenza: datetime
    _bids: dict[Bid, asta_bid._link]

    def __init__(self, descrizione: str, anni_garanzia: IntGEZ, prezzo_iniziale: RealGEZ, prezzo_rialzi: RealGZ, scadenza: datetime):
        # Does not use set method to bypass any checks - You can create an already expired asta (made mostly for testing)
        self._scadenza = scadenza
        self._prezzo = prezzo_iniziale
        self._prezzo_bid = prezzo_rialzi
        self._bids = dict()
        
        super().__init__(descrizione, anni_garanzia, prezzo_iniziale)

    def prezzo_bid(self) -> RealGZ:
        return self._prezzo_bid

    def scadenza(self) -> datetime:
        return self._scadenza
    
    def bids(self) -> frozenset[weakref[asta_bid._link]]:
        return frozenset(weakref.ref(l) for l in self._bids.values())
    
    def set_prezzo_bid(self, prezzo: RealGZ) -> None:
        if not self.scaduto():
            self._prezzo_bid = prezzo
        else:
            raise AttributeError("Can't set attribute 'prezzo_bid' of an Asta that has already ended.")
        
    def set_prezzo(self, new_prezzo):
        if not self.scaduto():
            self._prezzo = new_prezzo
            print("Ho eseguito questo")
        else:
            raise AttributeError("Can't set attribute 'prezzo' of an Asta that has already ended.")
    
    def set_scadenza(self, new_scadenza: datetime) -> None:
        if self.scaduto():
            raise AttributeError("Can't set attribute 'scadenza' of an Asta that has already ended.")
        elif new_scadenza < datetime.now():
            raise AttributeError("Can't set attribute 'scadenza' of Asta to a date that is before today")
        else:
            self._scadenza = new_scadenza

    def _add_bid(self, link_bid: asta_bid._link) -> None:
        if link_bid.asta() is not self:
            raise ValueError("Link does not involve me!")
        
        if link_bid.bid() in self._bids:
            raise KeyError(f"Duplicate link ({self}, {link_bid.bid()}) not allowed")
        
        self._bids[link_bid.bid()] = link_bid

    def scaduto(self) -> bool:
        return self.scadenza() < datetime.now()
    
    def __str__(self) -> str:
        return (f"{self._descrizione}\n\t- Prezzo iniziale: {self._prezzo:.2f}€\n\t- Rialzo minimo: {self.prezzo_bid():.2f}€\n"
        f"\t- Scadenza: {self.scadenza()}\n\t- Garanzia: {self.anni_garanzia()} ann{'o' if self.anni_garanzia() == 1 else 'i'}\n"
        f"\t- Stato: {'attivo' if self.scaduto() else 'scaduto'}"
    )

class asta_bid:
    class _link:
        def __init__(self, bid: Bid, asta: Asta):
            self._bid = bid
            self._asta = asta
        
        def bid(self) -> Bid:
            return self._bid
        
        def asta(self) -> Asta:
            return self._asta
    
    @classmethod
    def _add(cls, bid: Bid, asta: Asta) -> None:
        link = cls._link(bid, asta)
        bid._set_asta(link)
        asta._add_bid(link)