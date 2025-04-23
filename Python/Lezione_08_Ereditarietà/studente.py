from persona import Persona
from typing import Any

class Studente(Persona):
    '''def inheritanceTest(self):
        #verificare che la classe studente erediti tutti gli attributi della classe Persona
        self.nome
        self.cognome
        self.eta
        #verificare che la classe Studente erediti tutti i metodi della classe Persona
        self.getName
        self.getCognome
        self.getEta'''
    
    #inizializzare l'oggeto della classe studente
    def __init__(self, nome:str, cognome:str, eta:int,matricola:str):

        super().__init__(nome, cognome, eta) 
        #super ci consente di richiamare i metodi della classe Persona soprattutto il metodo costruttore

    
        self.setMatricola(matricola)


        #definire un metodo setter che ci consente di impostare il valore dell'attributo matricola

    def setMatricola(self,matricola)->None:
        if matricola:
            self.matricola = matricola
        else:
            print("Errore! La matricola non può essere una stringa vuota")


    def getMatricola(self)->str:
        return self.matricola

    #definisco il metodo che consente di visualizzare informazioni dell'oggetto della classe studente
    def __str__(self):
        return f"Nome: {self.getName()}\nCognome: {self.getCognome()}\nMatricola:{self.getMatricola()}"
    #modificando il metodo str della classe studente abbiamo effettuato un override
    
    #metodo che consente di calcolare la media dei voti sostenuti dallo studente
    def defGetMediaEsami(self,voti_esami:list[int])->float:
        #se la lista non è vuota
        if voti_esami:
            #calcolare la somma dei voti
            somma:int = 0
            for voto in voti_esami:
                somma+= voto
                #ritorna la media
            return round(somma/len(voti_esami),)
        #se la lista è vuota
        else:
            return 0.00
        

    #definire un metodo che consenta di confrontare se due oggetti della classe studente sono uguale
    #due studenti sono uguali se hanno la stessa matricola

    def __eq__(self, other:Any)->bool:
        #se other è None oppure se è other non è un istanza della classe Studente dovrà tornare False
        if other is None or not isinstance(other,type(self)):
            return False
        #altrimenti valuta la seguente ugualianza
        else:
            return self.getMatricola() == other.getMatricola()


        

    

    
    