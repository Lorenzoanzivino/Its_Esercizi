'''
Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
    cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
    anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
    getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. '''

from typing import Self

class Specie:

    def  __init__(self, popolazione: int, tasso_crescita: float):
        self.nome = ''
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita / 100))
        return self.popolazione

    def anni_per_superare(self, altra_specie: Self) -> int:
        anni: int = 0
        while self.popolazione < altra_specie.popolazione:
            self.cresci()
            altra_specie.cresci()
            anni += 1
            if anni == 1000:
                return anni
        return anni
    
    def getDensita(self, area_kmq: float) -> int:
        anni: int = 0
        while self.popolazione / area_kmq < 1:
            self.cresci()
            anni += 1
        return anni


class BufaloKlingon(Specie):
    
    def __init__(self, popolazione, tasso_crescita):
        super().__init__(popolazione, tasso_crescita)
        self.nome = 'Bufalo Klingon'


class Elefante(Specie):
    
    def ___init___(self, popolazione, tasso_crescita):
        super().__init__(popolazione, tasso_crescita)
        self.nome = 'Elefante'



if __name__ == '__main__':

    # Creazione delle istanze delle specie
    bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
    elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

    # Calcolo degli anni necessari per superare
    anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
    print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

    # Calcolo della densità di popolazione per i Bufali Klingon
    anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
    print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")

