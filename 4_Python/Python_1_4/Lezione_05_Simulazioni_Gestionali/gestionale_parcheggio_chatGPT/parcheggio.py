'''CLASSE: Parcheggio

In un file parcheggio.py, crea la classe Parcheggio.

Attributi:

posti: lista di veicoli attualmente parcheggiati

clienti: dizionario {id_cliente: lista di veicoli parcheggiati}

Metodi richiesti:

__init__() → inizializza posti vuota e clienti vuoto

entra(veicolo, id_cliente) → aggiunge un veicolo alla lista dei posti e lo associa all’utente in clienti. Stampa: "Cliente X ha parcheggiato Y".

esce(veicolo, id_cliente, ore) → rimuove il veicolo dal parcheggio e calcola il costo totale. Stampa: "Cliente X paga Z € per il veicolo Y".

stampaVeicoli() → stampa tutti i veicoli presenti nel parcheggio.

stampaVeicoliCliente(id_cliente) → stampa i veicoli parcheggiati da un certo cliente.'''

from veicolo import Veicolo
from auto_moto import Auto, Moto

class Parcheggio:

    __posti:list[Veicolo]
    __clienti: dict[int, list[Veicolo]]
    
    def __init__(self):
        self.__posti = []
        self.__clienti = {}

    def entra(self, veicolo:Veicolo, id_cliente:int):
        self.__posti.append(veicolo)

        if id_cliente in self.__clienti:
            self.__clienti[id_cliente].append(veicolo)
        else:
            self.__clienti[id_cliente] = [veicolo]

        print(f"Cliente {id_cliente} ha parcheggiato {veicolo.getModello()}")

    def esce(self, veicolo, id_cliente, ore):
        pass

    def stampaVeicoli(self):
        pass

    def stampaVeicoliCliente(self, id_cliente):
        pass

