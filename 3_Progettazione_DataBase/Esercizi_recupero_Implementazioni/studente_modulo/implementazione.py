from __future__ import annotations
from typing import Any

class Studente:
    _nome: str # noto alla nascita
    _esami: set[esame] # da assoc. 'esame' [0..*], certamente non noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._esami = set()

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def esami(self) -> frozenset[esame] :
        return frozenset(self._esami)

    def add_esame(self, modulo: Modulo, voto: int) -> None:
        # Mi assicuro che lo studente self non abbia mai superato il modulo 'modulo'

        new_esame: esame = esame(studente=self, modulo=modulo, voto=voto)

        if new_esame in self._esami: # cerco un esame *equivalente* (stesso esame e stesso modulo) tra quelli già sostenuti dallo studente
            raise RuntimeError(f"Lo studente {self.nome()} "
                               f"ha già superato un esame di {modulo.codice()}")

        self._esami.add(new_esame)

    def remove_link_esame(self, esame: esame) -> None:
        self._esami.remove(esame)

    def remove_esame(self, modulo: Modulo) -> None:
        # TODO rendere questo metodo più efficiente
        for esame in self.esami():
            if esame.modulo() == modulo:
                self.remove_link_esame(esame)
                return

        raise ValueError(f"Impossibile rimuovere l'esame del modulo {modulo.codice()} "
                         f"perché {self.nome()} non l'ha sostenuto!")

    def esame(self, modulo: Modulo) -> esame:
        # TODO implementare in modo efficiente
        pass

    def media_voti(self) -> float:
        # TODO implementare
        pass


class Modulo:
    _codice: str # noto alla nascita

    def __init__(self, codice: str) -> None:
        self.set_codice(codice)

    def codice(self) -> str:
        return self._codice

    def set_codice(self, codice: str) -> None:
        self._codice = codice


class esame:
    # Gli oggetti di questa classe rappresentano link dell'associazione 'esame'
    _studente: Studente     # immutabile (ovviamente!)
    _modulo: Modulo         # immutabile (ovviamente!)
    _voto: int              # immutabile

    def __init__(self, studente: Studente, modulo: Modulo, voto: int) -> None:
        self._studente = studente
        self._modulo = modulo
        self._voto = voto

    def studente(self) -> Studente:
        return self._studente

    def modulo(self) -> Modulo:
        return self._modulo

    def voto(self) -> int:
        return self._voto

    def __hash__(self) -> int:
        return hash((self.studente(), self.modulo()))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) \
                or hash(self) != hash(other):
            return False
        return self.studente() == other.studente() \
            and self.modulo() == other.modulo()
        # ignora il voto, perché 'esame' è un'associazione e 'voto' è un attributo

    def __repr__(self) -> str:
        return f"Esame({self.studente().nome()}, {self.modulo().codice()}: {self.voto()})"