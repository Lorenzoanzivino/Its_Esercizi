from __future__ import annotations
from custom_types import *

class Nazione:
    _nome: str  # mutabile, noto alla nascita
    _citta: set[Citta] # da assoc. 'citta_naz' [0..*], possibilmente non noti alla nascita

    def __init__(self, nome: str, citta: set[Citta]|None = None) -> None:
        self.set_nome(nome)
        if citta:
            for c in citta:
                c.set_nazione(self)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def citta(self) -> frozenset[Citta]:
        return frozenset(self._citta)

    def _add_citta(self, citta: Citta) -> None:
        self._citta.add(citta)

    def _remove_citta(self, citta: Citta) -> None:
        self._citta.remove(citta)



    def __str__(self) -> str:
        return f"Nazione '{self.nome()}'"


class Citta:
    _nome: str  # mutabile, noto alla nascita
    _abitanti: IntGEZ # noto alla nascita
    _nazione: Nazione # da assoc. 'citta_naz' [1..1], nota alla nascita

    def __init__(self, nome: str, abitanti: IntGEZ, nazione: Nazione) -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti)
        self.set_nazione(nazione)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def abitanti(self) -> IntGEZ:
        return self._abitanti

    def set_abitanti(self, abitanti: IntGEZ) -> None:
        self._abitanti = abitanti

    def nazione(self) -> Nazione:
        return self._nazione

    def set_nazione(self, nazione: Nazione) -> None:
        if nazione:
            self._nazione._remove_citta(self)
            nazione._add_citta(self)
            self._nazione = nazione
        


    def __str__(self) -> str:
        return f"Citta '{self.nome()}' con {self.abitanti()} abitanti"

class Compagnia:
    _nome: str # noto alla nascita
    _fondazione: IntGE1900 # immutabile, noto alla nascita
    _citta_direzione: Citta # da aggregazione 'citta_direzione', noto alla nascita
    _voli: set[Volo] # da assoc. 'volo_comp' [0..*], certamente non noti alla nascita

    def __init__(self, nome: str, fondazione: IntGE1900, citta: Citta) -> None:
        self.set_nome(nome)
        self._fondazione = fondazione
        self.set_citta_direzione(citta)
        self._voli = set()

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def fondazione(self) -> IntGE1900:
        return self._fondazione

    def set_citta_direzione(self, citta: Citta) -> None:
        self._citta_direzione = citta

    def citta_direzione(self) -> Citta:
        return self._citta_direzione

    def voli(self) -> frozenset[Volo]:
        return frozenset(self._voli)

    def _add_volo(self, volo: Volo) -> None:
        '''if volo.compagnia() != self:
            raise ValueError(f"Il volo è già della compagnia {volo.compagnia().nome()}!")'''
        self._voli.add(volo)

    def remove_volo(self, volo: Volo) -> None:
        self._voli.remove(volo)

    def __str__(self) -> str:
        return f"Compagnia '{self.nome()}' fondata nel {self.fondazione()}, con sede a {self.citta_direzione().nome()}"


class Aeroporto:
    _nome: str # noto alla nascita
    _codice: CodiceIATA # immutabile, noto alla nascita

    def __init__(self, nome: str, codice: CodiceIATA) -> None:
        self.set_nome(nome)
        self._codice = codice

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def codice(self) -> CodiceIATA:
        return self._codice

    def __str__(self) -> str:
        return f"Aeroporto '{self.nome()}' ({self.codice()})"


class Volo:
    _codice: CodiceVolo # immutabile, noto alla nascita
    _durata_minuti: IntGZ # noto alla nascita
    _compagnia: Compagnia # da assoc. volo_comp [1..1], immutabile, noto alla nascita
    _arrivo: Aeroporto # <<imm>>
    _partenza: Aeroporto # <<imm>>

    def __init__(self, codice: CodiceVolo, durata: IntGZ, compagnia: Compagnia, arrivo: Aeroporto, partenza: Aeroporto) -> None:
        self._codice = codice
        self.set_durata_minuti(durata)
        self._compagnia = compagnia
        compagnia._add_volo(self)
        self._arrivo = arrivo
        self._partenza = partenza

    def codice(self) -> CodiceVolo:
        return self._codice

    def durata_minuti(self) -> IntGZ:
        return self._durata_minuti

    def set_durata_minuti(self, durata_minuti: IntGZ) -> None:
        self._durata_minuti = durata_minuti

    def compagnia(self) -> Compagnia:
        return self._compagnia
    
    def arrivo(self) -> Aeroporto:
        return self._arrivo

    def partenza(self) -> Aeroporto:
        return self._partenza

    def __str__(self) -> str:
        return f"Volo '{self.codice()}' di '{self.compagnia().nome()} con durata {self.durata_minuti()} minuti"