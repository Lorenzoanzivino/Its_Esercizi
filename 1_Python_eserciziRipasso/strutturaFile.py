
"""Modulo di esempio che definisce la classe Prova con metodi base e supporto per confronto, stampa e hashing."""

# ===================================================== IMPORT librerire o elementi utili =====================================================


from __future__ import annotations
'''Permette di usare le "type hints" di classi non ancora definite (forward references) senza doverle mettere tra virgolette. Utile per annotazioni più leggibili.'''

from typing import *
'''Importa tutti gli strumenti per l’annotazione dei tipi, come List, Dict, Optional, ecc. Serve per scrivere codice più chiaro e aiutare con l’autocompletamento o il type checking statico.'''

from weakref import WeakValueDictionary
'''Importa un dizionario che tiene riferimenti deboli agli oggetti. Se l’oggetto non è più usato altrove, viene automaticamente rimosso dal dizionario. Utile per caching senza rischiare memory leak.'''

from abc import ABC, abstractmethod
'''Permette di creare classi astratte (ABC = Abstract Base Class). 'abstractmethod' indica che un metodo **deve** essere implementato nelle sottoclassi.'''

from datetime import datetime
'''Importa l'oggetto `datetime` per lavorare con date e orari in modo preciso e flessibile.'''

import random
'''Modulo standard per generare numeri casuali, scegliere elementi random da una lista, ecc.'''


# ===================================================== CLASSI + FUNZIONI + CONDIZIONI + CICLI =====================================================

class Prova:
    '''Classe di esempio per mostrare la struttura standard di una classe in Python.'''

    def __init__(self) -> None:
        '''Costruttore della classe: viene chiamato automaticamente alla creazione dell’oggetto.'''
        self.set_prova(None)  # Inizializza il valore _prova a None usando il setter

    def get_prova(self) -> int:
        '''Getter: restituisce il valore dell’attributo privato _prova.'''
        return self._prova

    def set_prova(self, value: int) -> None:
        '''Setter: imposta il valore dell’attributo privato _prova.'''
        if not isinstance(value, int):
            raise TypeError("Il valore deve essere un intero.")
        self._prova = value

    def __repr__(self) -> str:
        '''Rappresentazione ufficiale dell’oggetto, utile per debug e stampa tecnica.'''
        return f"Prova(prova={self._prova})"

    def __str__(self) -> str:
        '''Rappresentazione leggibile dell’oggetto, usata da print() e str().'''
        return str(self._prova)

    def __hash__(self) -> int:
        '''Rende l’oggetto hashabile (es. per usarlo come chiave in un dizionario o metterlo in un set).'''
        return hash(self._prova)

    def __eq__(self, value: object) -> bool:
        '''Confronto tra due oggetti Prova: ritorna True se hanno lo stesso valore _prova.'''
        if not isinstance(value, Prova):     # Se l’altro oggetto non è di tipo Prova, non ha senso confrontarli
            return NotImplemented            # Rispetta il comportamento previsto da Python
        return self._prova == value._prova   # Confronto del valore interno


# ===================================================== INGRESSO DEL PROGRAMMA =====================================================

# Punto di ingresso del programma, eseguito solo se il file è lanciato direttamente

if __name__ == "__main__":
    # Istanzia un oggetto della classe Prova
    p = Prova()
    
    # Imposta il valore dell’attributo _prova a 42 usando il setter
    p.set_prova(42)
    
    # Stampa il valore di _prova tramite il getter
    print(f"Valore: {p.get_prova()}")
